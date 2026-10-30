import json, sys, datetime as dt
def annual(f, tags, inst=False):
    out = {}
    for tag in tags:
        if tag not in f["us-gaap"]: continue
        u = f["us-gaap"][tag]["units"]["USD"]
        for x in u:
            if not x.get("form","").startswith("10-K"): continue
            if not inst:
                if "start" not in x: continue
                d = (dt.date.fromisoformat(x["end"]) - dt.date.fromisoformat(x["start"])).days
                if d < 350 or d > 380: continue
            out.setdefault(x["end"][:7], {}).setdefault(tag, x["val"])
    return out
def pick(d, e):
    v = d.get(e, {}); return max(v.values()) if v else None
print("ticker  rev FY15  rev FY25  CAGR   sumNI/sumRev  sum(OCF-capex)/sumRev  avg NI/avg assets   years")
for t in sys.argv[1:]:
    f = json.load(open(f"cache/peers/{t}.json"))["facts"]
    rev = annual(f, ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet","SalesRevenueGoodsNet"])
    ni = annual(f, ["NetIncomeLoss"]); ocf = annual(f, ["NetCashProvidedByUsedInOperatingActivities"])
    cap = annual(f, ["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"])
    at = annual(f, ["Assets"], inst=True)
    ends = sorted(e for e in rev if "2016-01" <= e <= "2026-02")
    first = [e for e in sorted(rev) if e.startswith("2016-01")]
    yrs = [e for e in ends if e >= "2017-01"]  # FY2016..FY2025 (10 yrs)
    R = sum(pick(rev,e) for e in yrs); N = sum(pick(ni,e) or 0 for e in yrs)
    oc = [ (pick(ocf,e), pick(cap,e)) for e in yrs]
    OC = sum(a-b for a,b in oc if a is not None and b is not None); Rc = sum(pick(rev,e) for e,(a,b) in zip(yrs,oc) if a is not None and b is not None)
    A = [pick(at,e) for e in yrs if pick(at,e)]
    r0 = pick(rev, first[0]) if first else None; r1 = pick(rev, yrs[-1])
    cagr = (r1/r0)**(1/10)-1 if r0 else float('nan')
    print(f"{t:6} {r0/1e6:9,.0f} {r1/1e6:9,.0f} {cagr*100:6.1f}%   {N/R*100:6.1f}%        {OC/Rc*100:6.1f}% (n={len(oc)})         {N/len(yrs)/(sum(A)/len(A))*100:6.1f}%   {yrs[0]}..{yrs[-1]}")
