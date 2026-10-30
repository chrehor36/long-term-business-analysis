import json, sys
from datetime import date
def annual(d, tags):
    out = {}
    for t in tags:
        if t not in d: continue
        for u, rows in d[t]["units"].items():
            for r in rows:
                if r.get("form") not in ("10-K","10-K/A"): continue
                if "start" not in r: continue
                s=date.fromisoformat(r["start"]); e=date.fromisoformat(r["end"])
                if not 350<= (e-s).days <=380: continue
                y = r["end"]
                if y not in out or r["filed"] < out[y][1]:
                    out[y] = (r["val"], r["filed"], r["accn"], t)
    return out
f = json.load(open(sys.argv[1]))["facts"]["us-gaap"]
rev = annual(f, ["Revenues","SalesRevenueNet","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueGoodsNet","RevenueFromContractWithCustomerIncludingAssessedTax"])
oi = annual(f, ["OperatingIncomeLoss"])
gi = annual(f, ["GoodwillImpairmentLoss","GoodwillAndIntangibleAssetImpairment","AssetImpairmentCharges","ImpairmentOfIntangibleAssetsExcludingGoodwill"])
ocf = annual(f, ["NetCashProvidedByUsedInOperatingActivities"])
cap = annual(f, ["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"])
print(sys.argv[1])
for y in sorted(oi):
    r = rev.get(y,(None,))[0]; o = oi[y][0]
    if not r: continue
    g = gi.get(y,(0,))[0]
    oc = ocf.get(y,(None,))[0]; cp = cap.get(y,(None,))[0]
    fcf = (oc-cp)/1e6 if oc is not None and cp is not None else None
    fs = str(round(fcf)) if fcf is not None else "na"
    print(f"  {y} sales {r/1e6:8.0f} opinc {o/1e6:7.0f} margin {100*o/r:5.1f}%  impair {g/1e6 if g else 0:6.0f}  OCF-capex {fs:>6}  {oi[y][2]}")
