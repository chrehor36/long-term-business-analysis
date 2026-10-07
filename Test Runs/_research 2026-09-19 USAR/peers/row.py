# -*- coding: utf-8 -*-
import json, sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def annuals(d, tag, taxo="us-gaap"):
    node = d["facts"].get(taxo, {}).get(tag)
    if not node:
        return {}
    out = {}
    for unit, arr in node["units"].items():
        if unit not in ("USD", "shares"):
            continue
        for f in arr:
            st, en = f.get("start"), f.get("end")
            if not st:
                continue
            m = (int(en[:4]) * 12 + int(en[5:7])) - (int(st[:4]) * 12 + int(st[5:7]))
            if m < 11 or m > 13:
                continue
            if f.get("form") not in ("10-K", "10-K/A", "20-F", "40-F"):
                continue
            key = en
            prev = out.get(key)
            if prev is None or f["filed"] > prev[1]:
                out[key] = (f["val"], f["filed"])
    return {k: v[0] for k, v in out.items()}

def instants(d, tag, taxo="us-gaap"):
    node = d["facts"].get(taxo, {}).get(tag)
    if not node:
        return {}
    out = {}
    for unit, arr in node["units"].items():
        for f in arr:
            if f.get("start"):
                continue
            key = f["end"]
            prev = out.get(key)
            if prev is None or f["filed"] > prev[1]:
                out[key] = (f["val"], f["filed"])
    return {k: v[0] for k, v in out.items()}

TAGS = {
    "revenue": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
                "RevenueFromContractWithCustomerIncludingAssessedTax"],
    "cogs": ["CostOfRevenue", "CostOfGoodsAndServicesSold"],
    "gross": ["GrossProfit"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities",
            "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"],
    "sbc": ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"],
    "dna": ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet",
            "DepreciationAndAmortization", "Depreciation"],
    "ni": ["NetIncomeLoss", "ProfitLoss"],
    "equity": ["StockholdersEquity"],
}

def pick(d, names):
    for n in names:
        a = annuals(d, n)
        if a:
            return n, a
    return None, {}

for t in sys.argv[1:]:
    d = json.load(open(f"{t}_companyfacts.json"))
    print("=" * 70)
    print(t, d.get("entityName"))
    for label, names in TAGS.items():
        used, a = pick(d, names)
        if not a:
            print(f"  {label:9s} ABSENT ({names[0]} etc.)")
            continue
        ks = sorted(a)[-7:]
        print(f"  {label:9s} [{used}]")
        for k in ks:
            print(f"      {k}  {a[k]:>18,}")
