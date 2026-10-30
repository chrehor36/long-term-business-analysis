import json, sys, datetime as dt
def annual(f, tags):
    out = {}
    for tag in tags:
        for ns in ("us-gaap",):
            if tag not in f[ns]: continue
            u = f[ns][tag]["units"]["USD"]
            for x in u:
                if not x.get("form","").startswith("10-K") or "start" not in x: continue
                d = (dt.date.fromisoformat(x["end"]) - dt.date.fromisoformat(x["start"])).days
                if d < 350 or d > 380: continue
                out.setdefault(x["end"], {}).setdefault(tag, x["val"])
    return out
for t in sys.argv[1:]:
    f = json.load(open(f"cache/peers/{t}.json"))["facts"]
    rev = annual(f, ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet","SalesRevenueGoodsNet","RevenueFromContractWithCustomerIncludingAssessedTax"])
    oi = annual(f, ["OperatingIncomeLoss"])
    ni = annual(f, ["NetIncomeLoss"])
    ocf = annual(f, ["NetCashProvidedByUsedInOperatingActivities"])
    cap = annual(f, ["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"])
    print("==", t)
    for e in sorted(rev):
        if e < "2015-01-01": continue
        r = max(rev[e].values())
        o = oi.get(e,{}).get("OperatingIncomeLoss")
        n = ni.get(e,{}).get("NetIncomeLoss")
        oc = ocf.get(e,{}).get("NetCashProvidedByUsedInOperatingActivities")
        cp = list(cap.get(e,{}).values())
        print(e, f"rev {r/1e6:,.0f}", f"opinc {o/1e6:,.0f} ({o/r*100:.1f}%)" if o is not None else "opinc -", f"ni {n/1e6:,.0f}" if n is not None else "", f"ocf {oc/1e6:,.0f}" if oc else "", f"capex {cp[0]/1e6:,.0f}" if cp else "")
