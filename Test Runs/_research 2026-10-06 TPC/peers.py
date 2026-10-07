import json, sys
from datetime import date
def annual(g, tag):
    out={}
    if tag not in g: return out
    for unit, rows in g[tag]["units"].items():
        if unit!="USD": continue
        for r in rows:
            if r.get("form") not in ("10-K","10-K/A") or "start" not in r: continue
            s=date.fromisoformat(r["start"]); e=date.fromisoformat(r["end"])
            if not (350<=(e-s).days<=380): continue
            fy = e.year if e.month>6 else e.year-1
            if fy not in out or r["filed"]<out[fy][1]: out[fy]=(r["val"],r["filed"])
    return {k:v[0] for k,v in out.items()}
for tk in sys.argv[1:]:
    g=json.load(open(f"peers/{tk}_facts.json"))["facts"]["us-gaap"]
    rev={}
    for t in ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet","ContractsRevenue","SalesRevenueServicesNet","RevenueFromContractWithCustomerIncludingAssessedTax"]:
        for k,v in annual(g,t).items(): rev.setdefault(k,v)
    oi=annual(g,"OperatingIncomeLoss")
    gp=annual(g,"GrossProfit")
    ocf=annual(g,"NetCashProvidedByUsedInOperatingActivities")
    for k,v in annual(g,"NetCashProvidedByUsedInOperatingActivitiesContinuingOperations").items(): ocf.setdefault(k,v)
    cap=annual(g,"PaymentsToAcquirePropertyPlantAndEquipment")
    ys=[y for y in range(2010,2026) if y in rev]
    print("=====",tk)
    tr=to=0; n=0
    for y in ys:
        r=rev[y]/1e6; o=oi.get(y); g2=gp.get(y)
        print(y, f"rev {r:9.1f}", f"OI {o/1e6:8.1f} ({100*o/rev[y]:5.1f}%)" if o is not None else "OI -", f"GP {100*g2/rev[y]:5.1f}%" if g2 else "", f"OCF {ocf[y]/1e6:7.1f}" if y in ocf else "", f"capex {cap[y]/1e6:6.1f}" if y in cap else "")
        if o is not None and y>=2013: tr+=rev[y]; to+=o; n+=1
    if tr: print(f"cumulative OI/revenue {min([y for y in ys if y>=2013])}-{max(ys)} ({n} yrs with OI): {100*to/tr:.1f}%")
