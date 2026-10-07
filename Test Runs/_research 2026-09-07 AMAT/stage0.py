"""AMAT Stage 0: margins, windows, yields. Arithmetic only. Originally-filed values."""
import json, os, collections
from datetime import date

OUT = os.path.dirname(os.path.abspath(__file__))
F = json.load(open(os.path.join(OUT, "companyfacts_AMAT.json"), encoding="utf-8"))["facts"]
US = F["us-gaap"]

def series(tag, ns=US, first=True):
    """originally-filed (earliest filed) value per fiscal-year end, 10-K FY only"""
    if tag not in ns: return {}
    by_end = collections.defaultdict(list)
    for unit, rows in ns[tag]["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A") or r.get("fp") != "FY": continue
            if "start" in r:
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                if not (330 <= (e - s).days <= 400): continue
            by_end[r["end"]].append((r["filed"], r["val"]))
    return {e: (sorted(v)[0][1] if first else sorted(v)[-1][1]) for e, v in by_end.items()}

def restatements(tag):
    out = {}
    if tag not in US: return out
    by_end = collections.defaultdict(set)
    for unit, rows in US[tag]["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A") or r.get("fp") != "FY": continue
            if "start" in r:
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                if not (330 <= (e - s).days <= 400): continue
            by_end[r["end"]].add(r["val"])
    for e, v in by_end.items():
        if len(v) > 1: out[e] = sorted(v)
    return out

rev = {}
for t in ("SalesRevenueNet", "RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues"):
    for e, v in series(t).items():
        rev.setdefault(e, v)
cogs = {}
for t in ("CostOfGoodsAndServicesSold", "CostOfRevenue", "CostOfGoodsSold"):
    for e, v in series(t).items():
        cogs.setdefault(e, v)
gp    = series("GrossProfit")
rd    = series("ResearchAndDevelopmentExpense")
opinc = series("OperatingIncomeLoss")
ocf   = series("NetCashProvidedByUsedInOperatingActivities")
sbc   = series("ShareBasedCompensation")
da    = {}
for t in ("DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet",
          "DepreciationAndAmortization"):
    for e, v in series(t).items():
        if e not in da or abs(v) > abs(da[e]): da[e] = v
amort = series("AmortizationOfIntangibleAssets")
cap   = {}
for t in ("PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"):
    for e, v in series(t).items():
        cap.setdefault(e, v)
ni    = series("NetIncomeLoss")
assets= series("Assets"); gw = series("Goodwill")
intan = series("IntangibleAssetsNetExcludingGoodwill")
cl    = series("LiabilitiesCurrent"); cd = series("LongTermDebtCurrent")
eq    = series("StockholdersEquity")
taxpd = series("IncomeTaxesPaidNet")
pretax= series("IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest")
if not pretax:
    pretax = series("IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments")
bb    = series("PaymentsForRepurchaseOfCommonStock")
div   = series("PaymentsOfDividendsCommonStock")

M = 1e6
ends = sorted(e for e in ocf if e >= "2007-01-01")
print("AMAT  FY(Oct)   rev     GM%   opinc  opm%  R&D%    OCF    SBC    D&A  amort tangD&A  capex cap/tD&A  OE(capex) OE(D&A)     NI   opinc/NTOA%")
rows = []
for e in ends:
    R = rev.get(e); C = cogs.get(e); D = rd.get(e)
    o = ocf[e]; b = sbc.get(e, 0); dd = da.get(e, 0); am = amort.get(e, 0); cx = cap.get(e, 0)
    oi = opinc.get(e)
    g = gp.get(e)
    gm = (g / R * 100) if (g is not None and R) else ((R - C) / R * 100 if (R and C) else None)
    tang = dd - am if dd else None
    oe_c = o - b - cx
    oe_d = o - b - dd
    ntoa = None
    if e in assets:
        nibcl = cl.get(e, 0) - cd.get(e, 0)
        ntoa = assets[e] - gw.get(e, 0) - intan.get(e, 0) - nibcl
    rows.append((e, oe_c, oe_d, R, oi))
    def f(x): return f"{x/M:8.1f}" if x is not None else "     n/a"
    def p(x): return f"{x:6.1f}" if x is not None else "   n/a"
    print(f"{e[:7]} {f(R)} {p(gm)} {f(oi)} {p(oi/R*100 if oi and R else None)} "
          f"{p(D/R*100 if D and R else None)} {f(o)} {f(b)} {f(dd)} {f(am)} {f(tang)} {f(cx)} "
          f"{p(cx/tang if tang else None)} {f(oe_c)} {f(oe_d)} {f(ni.get(e))} "
          f"{p(oi/ntoa*100 if oi and ntoa else None)}")

print("\n=== RESTATEMENTS across vintages (originally-filed vs later) ===")
for t in ("NetCashProvidedByUsedInOperatingActivities", "ShareBasedCompensation",
          "PaymentsToAcquirePropertyPlantAndEquipment", "SalesRevenueNet",
          "RevenueFromContractWithCustomerExcludingAssessedTax", "OperatingIncomeLoss",
          "DepreciationDepletionAndAmortization"):
    r = restatements(t)
    if r:
        for e, v in sorted(r.items()):
            print(f"  {t[:44]:44s} {e}  {[round(x/1e6,1) for x in v]}")

print("\n=== CASH TAX vs PRETAX [E4-30] ===")
for e in ends:
    if e in taxpd and e in pretax and pretax[e]:
        print(f"  {e[:7]}  cash tax {taxpd[e]/M:8.1f}  pretax {pretax[e]/M:9.1f}  = {taxpd[e]/pretax[e]*100:5.1f}%")

print("\n=== BUYBACK / DIVIDEND ===")
for e in ends:
    print(f"  {e[:7]}  buyback {bb.get(e,0)/M:8.1f}  dividends {div.get(e,0)/M:8.1f}")
