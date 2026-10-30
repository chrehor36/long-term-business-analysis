# BIRD run 2026-09-19: reading (d) - does companyfacts carry more than one vintage of any annual cash-flow fact,
# and does the earliest vintage (what the a8bc84f and current screens read) differ from the latest?
import json, os
from collections import defaultdict
here = os.path.dirname(os.path.abspath(__file__))
f = json.load(open(os.path.join(here, "companyfacts.json")))
g = f["facts"]["us-gaap"]
tags = ["NetCashProvidedByUsedInOperatingActivities", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations",
        "CashProvidedByUsedInOperatingActivitiesDiscontinuedOperations", "ShareBasedCompensation", "AllocatedShareBasedCompensationExpense",
        "PaymentsToAcquirePropertyPlantAndEquipment", "DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet",
        "Depreciation", "Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "NetIncomeLoss"]
for t in tags:
    L = g.get(t, {}).get("units", {}).get("USD", [])
    by = defaultdict(list)
    for x in L:
        s, e = x.get("start"), x.get("end")
        if not s: continue
        d = (int(e[:4]) - int(s[:4])) * 12 + int(e[5:7]) - int(s[5:7])
        if d in (11, 12) or (x["fp"] in ("FY",) and d >= 11):
            by[e].append((x["filed"], x["val"], x["form"], x["accn"]))
    if not L: print("==", t, "absent"); continue
    print("==", t)
    for e in sorted(by):
        v = sorted(set(by[e]))
        vals = sorted(set(z[1] for z in v))
        mark = "  <-- VINTAGES DIFFER" if len(vals) > 1 else ""
        print("  ", e, "; ".join(f"{z[0]} {z[1]:,.0f} {z[2]}" for z in v), mark)
# the six-month continuing/discontinued split the 10-Q introduced
for t in ["NetCashProvidedByUsedInOperatingActivitiesContinuingOperations", "CashProvidedByUsedInOperatingActivitiesDiscontinuedOperations"]:
    for x in g.get(t, {}).get("units", {}).get("USD", []):
        print(t, x.get("start"), x["end"], f'{x["val"]:,}', x["form"], x["filed"])
