import json, sys
R = "Test Runs/_research 2026-09-20 CALM"
cf = json.load(open(R + "/companyfacts.json"))
us = cf["facts"]["us-gaap"]

def annual(tag, lo=340, hi=380):
    """newest vintage per fiscal period end; annual 10-K durations only"""
    if tag not in us: return {}
    out = {}
    for u in us[tag]["units"]["USD"]:
        if "start" not in u: continue
        if u.get("form") not in ("10-K", "10-K/A"): continue
        from datetime import date
        s = date.fromisoformat(u["start"]); e = date.fromisoformat(u["end"])
        d = (e - s).days
        if not (lo <= d <= hi): continue
        key = u["end"]
        prev = out.get(key)
        # newest vintage = latest 'filed'
        if prev is None or u["filed"] > prev[1]:
            out[key] = (u["val"], u["filed"], u.get("accn"))
    return {k: v for k, v in sorted(out.items())}

tags = {
 "OCF": "NetCashProvidedByUsedInOperatingActivities",
 "OCF_CONT": "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations",
 "DA": "DepreciationDepletionAndAmortization",
 "DA2": "DepreciationAmortizationAndAccretionNet",
 "CAPEX": "PaymentsToAcquirePropertyPlantAndEquipment",
 "SBC": "ShareBasedCompensation",
 "NI": "ProfitLoss",
 "NIP": "NetIncomeLoss",
 "ACQ": "PaymentsToAcquireBusinessesNetOfCashAcquired",
}
res = {k: annual(v) for k, v in tags.items()}
years = sorted(set().union(*[set(v) for v in res.values()]))
print(f"{'end':12} " + " ".join(f"{k:>10}" for k in tags))
for y in years:
    row = []
    for k in tags:
        v = res[k].get(y)
        row.append(f"{v[0]/1e3:10.1f}" if v else f"{'-':>10}")
    print(f"{y:12} " + " ".join(row))
