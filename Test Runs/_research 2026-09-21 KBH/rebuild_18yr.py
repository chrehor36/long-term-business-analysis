#!/usr/bin/env python3
"""KBH -- the eighteen-year rebuild the five-year screen window could not see.

Fetch and arithmetic only. It concludes nothing (operator rule 8).
All figures from SEC XBRL company-facts, cross-checked against the filed
CONSOLIDATED STATEMENTS OF CASH FLOWS in the FY2025 10-K (accession
0000795266-26-000017) for FY2023-FY2025.
"""
import json, os, datetime, statistics

D = os.path.dirname(os.path.abspath(__file__))


def series(us, tag, duration=True):
    out = {}
    if tag not in us:
        return out
    for unit, items in us[tag]["units"].items():
        for it in items:
            if it.get("form") not in ("10-K", "10-K/A"):
                continue
            if duration:
                if it.get("fp") != "FY":
                    continue
                d = (datetime.date.fromisoformat(it["end"])
                     - datetime.date.fromisoformat(it["start"])).days
                if not (330 < d < 400):
                    continue
            out[it["end"]] = it["val"] / 1e6
    return out


us = json.load(open(os.path.join(D, "companyfacts.json"), encoding="utf-8"))["facts"]["us-gaap"]
ocf = series(us, "NetCashProvidedByUsedInOperatingActivities")
sbc = series(us, "ShareBasedCompensation")
dep = series(us, "DepreciationAndAmortization")
ppe = series(us, "PaymentsToAcquirePropertyPlantAndEquipment")
inv = series(us, "InventoryOperativeBuilders", duration=False)
inv2 = series(us, "InventoryRealEstate", duration=False)
for k, v in inv2.items():
    inv.setdefault(k, v)

years = sorted(y for y in ocf if y.endswith("-11-30"))
print("FY end      OCF      SBC      D&A   PP&Ecapex   inventory   d(inv)")
prev = None
for y in years:
    di = (inv[y] - inv[prev]) if (prev and y in inv and prev in inv) else None
    print("%s %8.1f %8.1f %8.1f %8s %11s %8s" % (
        y, ocf[y], sbc.get(y, float("nan")), dep.get(y, float("nan")),
        ("%.1f" % ppe[y]) if y in ppe else "-",
        ("%.1f" % inv[y]) if y in inv else "-",
        ("%+.1f" % di) if di is not None else "-"))
    prev = y


def window(ys, label):
    o = [ocf[y] for y in ys]
    s = [sbc.get(y, 0.0) for y in ys]
    c_dep = [dep.get(y, 0.0) for y in ys]
    c_ppe = [ppe.get(y, 0.0) for y in ys]
    print("\n%s  (n=%d, %s..%s)" % (label, len(ys), ys[0], ys[-1]))
    print("  mean OCF            %9.1f   (min %.1f  max %.1f)" % (
        statistics.mean(o), min(o), max(o)))
    print("  mean SBC            %9.1f" % statistics.mean(s))
    print("  mean D&A            %9.1f" % statistics.mean(c_dep))
    print("  mean PP&E capex     %9.1f" % statistics.mean(c_ppe))
    print("  OCF - SBC - D&A     %9.1f" % (statistics.mean(o) - statistics.mean(s) - statistics.mean(c_dep)))
    print("  OCF - SBC - capex   %9.1f" % (statistics.mean(o) - statistics.mean(s) - statistics.mean(c_ppe)))
    neg = [y for y in ys if ocf[y] < 0]
    print("  years with NEGATIVE operating cash flow: %d of %d  %s" % (len(neg), len(ys), neg))


window(years, "FULL FILED WINDOW")
window([y for y in years if y >= "2021-11-30"], "FIVE-YEAR WINDOW (the screen's)")
window([y for y in years if "2011-11-30" <= y <= "2020-11-30"], "THE DECADE THE SCREEN CANNOT SEE")
