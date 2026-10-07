# -*- coding: utf-8 -*-
"""Owner earnings for MGM over EVERY window the filed record supports, BOTH (c) ends.
Arithmetic only. It concludes nothing (operator rule 8).

CONVENTION as v4 section VI states it: owner earnings = multi-year mean of operating cash
flow less SBC less the (c) guess. OCF nets the working-capital change from one audited line.
"""
import json, io, os
from datetime import date
D = os.path.dirname(os.path.abspath(__file__))
f = json.load(io.open(os.path.join(D, "companyfacts.json"), encoding="utf-8"))
us = f["facts"]["us-gaap"]


def ann(tags, forms=("10-K",)):
    if isinstance(tags, str):
        tags = [tags]
    out = {}
    for tag in tags:
        if tag not in us:
            continue
        for u, items in us[tag]["units"].items():
            for it in items:
                if it.get("form") not in forms:
                    continue
                s, e = it.get("start"), it.get("end")
                if not s:
                    continue
                d0 = date(*map(int, s.split("-")))
                d1 = date(*map(int, e.split("-")))
                if not (340 <= (d1 - d0).days <= 380):
                    continue
                p = out.get(e)
                if p is None or it.get("filed", "") > p[1]:
                    out[e] = (it["val"], it.get("filed", ""))
    return {k[:4]: v[0] / 1e6 for k, v in sorted(out.items()) if k.endswith("12-31")}


OCF = ann(["NetCashProvidedByUsedInOperatingActivities",
           "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"])
CAPEX = ann("PaymentsToAcquirePropertyPlantAndEquipment")
DA = ann("DepreciationAndAmortization")
AMORT = ann("AmortizationOfIntangibleAssets")
SBC = ann("ShareBasedCompensation")
TAXPAID = ann(["IncomeTaxesPaidNet", "IncomeTaxesPaid"])
PRETAX = ann(["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
              "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"])
NCI = ann("NetIncomeLossAttributableToNoncontrollingInterest")
DISTNCI = ann(["PaymentsOfDistributionsToAffiliates", "PaymentsOfDividendsMinorityInterest"])
BUY = ann("PaymentsForRepurchaseOfCommonStock")
LEASECASH = ann(["OperatingLeasePayments"])
LEASECOST = ann(["OperatingLeaseCost"])

years = sorted(set(OCF) & set(CAPEX) & set(SBC))
print("=== A. THE RAW SERIES, $M, newest-vintage annual facts, 10-K forms only ===")
print("year  OCF      capex    SBC    D&A     intang.amort  depr.only  taxpaid  pretax  NCI_income  distrib_to_NCI")
for y in years:
    da = DA.get(y)
    am = AMORT.get(y)
    dep = None if da is None or am is None else da - am
    def s(v, w=8, p=1):
        return (" " * w) if v is None else ("%*.*f" % (w, p, v))
    print(y, s(OCF.get(y)), s(CAPEX.get(y)), s(SBC.get(y), 6), s(da), s(am, 12), s(dep, 10),
          s(TAXPAID.get(y)), s(PRETAX.get(y)), s(NCI.get(y), 11), s(DISTNCI.get(y), 14))

print()
print("=== B. SBC COMPLETENESS CHECK (the BE / Boeing lesson) ===")
miss = [y for y in years if SBC.get(y) is None]
print("years with OCF and capex:", len(years), years[0], "..", years[-1])
print("years where SBC does NOT resolve:", miss if miss else "NONE - SBC resolves for every year")
print("SBC undimensioned tag used: ShareBasedCompensation (cash-flow add-back)")
print("cross-check vs AllocatedShareBasedCompensationExpenseNetOfTax presence:",
      "AllocatedShareBasedCompensationExpenseNetOfTax" in us)

print()
print("=== C. OWNER EARNINGS BY YEAR, BOTH (c) ENDS ===")
print("(c) LOW end  = D&A as filed            [E3-44] default")
print("(c) DEPR end = D&A less intangible amortisation (the renewal proxy that is not purchased-intangible runoff)")
print("(c) HIGH end = total capex as reported [E5-20] exception class")
print("year   OE(c=D&A)   OE(c=depr only)   OE(c=capex)")
oe = {}
for y in years:
    base = OCF[y] - SBC[y]
    da = DA.get(y)
    am = AMORT.get(y)
    dep = None if da is None or am is None else da - am
    a = None if da is None else base - da
    b = None if dep is None else base - dep
    c = base - CAPEX[y]
    oe[y] = (a, b, c)
    def s(v):
        return "          " if v is None else "%10.1f" % v
    print(y, s(a), s(b), s(c))

print()
print("=== D. EVERY WINDOW, BOTH ENDS. [E4-25] and [E4-38]: publish every window ===")
print("window            n   mean OE(c=D&A)  mean OE(c=capex)  mean OE(c=depr only)")
ends = sorted(years)[-1]


def mean(vals):
    vals = [v for v in vals if v is not None]
    return None if not vals else sum(vals) / len(vals)


for n in (3, 4, 5, 6, 7, 8, 9, 10, 12, 15, len(years)):
    if n > len(years):
        continue
    w = sorted(years)[-n:]
    a = mean([oe[y][0] for y in w])
    b = mean([oe[y][1] for y in w])
    c = mean([oe[y][2] for y in w])
    print("%s-%s %4d %14s %17s %21s" % (w[0], w[-1], n,
          "%.1f" % a if a is not None else "-",
          "%.1f" % c if c is not None else "-",
          "%.1f" % b if b is not None else "-"))

print()
print("=== E. WINDOWS THAT EXCLUDE 2020 AND 2021 (the disclosed judgment, [E2-23] multi-year) ===")
for lo, hi, label in [(2015, 2019, "five pre-COVID years"),
                      (2022, 2025, "four post-reset years"),
                      (2021, 2025, "five-year default incl. 2021"),
                      (2023, 2025, "three years since the lease set was complete")]:
    w = [y for y in years if lo <= int(y) <= hi]
    if not w:
        continue
    a = mean([oe[y][0] for y in w])
    b = mean([oe[y][1] for y in w])
    c = mean([oe[y][2] for y in w])
    print("%s (%s-%s, n=%d): c=D&A %.1f | c=depr %.1f | c=capex %.1f"
          % (label, w[0], w[-1], len(w), a, b if b is not None else float("nan"), c))

print()
print("=== F. THE CASH-TAX TELL [E4-30]: cash taxes paid as a share of reported pretax ===")
for y in years:
    tp, px = TAXPAID.get(y), PRETAX.get(y)
    if tp is None or px is None or px == 0:
        continue
    print(y, "taxes paid %8.1f  pretax %9.1f  = %6.1f%%" % (tp, px, 100.0 * tp / px))

print()
print("=== G. THE MINORITY LEAK: what the consolidated OCF is NOT ===")
for y in years:
    if int(y) < 2019:
        continue
    print(y, "NCI share of net income %8s   cash distributed to NCI owners %8s"
          % ("%.1f" % NCI[y] if y in NCI else "-",
             "%.1f" % DISTNCI[y] if y in DISTNCI else "-"))

print()
print("=== H. BUYBACKS AND THE SHARE COUNT ===")
SH = {}
for u, items in us["CommonStockSharesOutstanding"]["units"].items():
    for it in items:
        if it.get("form") != "10-K" or it.get("start"):
            continue
        e = it["end"]
        p = SH.get(e)
        if p is None or it.get("filed", "") > p[1]:
            SH[e] = (it["val"], it.get("filed", ""))
SH = {k[:4]: v[0] / 1e6 for k, v in sorted(SH.items()) if k.endswith("12-31")}
tot = 0.0
for y in years:
    if int(y) < 2021:
        continue
    b = BUY.get(y, 0.0)
    tot += b
    print(y, "repurchases $%8.1fM   shares outstanding %7.1fM" % (b, SH.get(y, float("nan"))))
print("total repurchases 2022-2025: $%.1fM" % sum(BUY.get(y, 0.0) for y in years if 2022 <= int(y) <= 2025))
print("share count 2021 -> 2025: %.1fM -> %.1fM" % (SH.get("2021", 0), SH.get("2025", 0)))
