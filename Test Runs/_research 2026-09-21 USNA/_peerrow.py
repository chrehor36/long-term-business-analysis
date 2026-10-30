import json,os
from datetime import date
D="Test Runs/_research 2026-09-21 USNA/peers"
REV=["RevenueFromContractWithCustomerExcludingAssessedTax","Revenues","SalesRevenueNet","SalesRevenueGoodsNet"]
OPI=["OperatingIncomeLoss"]
def series(f,tags,dur=True):
    out={}
    for t in tags:
        d=f["facts"].get("us-gaap",{}).get(t)
        if not d: continue
        for u in d["units"].get("USD",[]):
            if u.get("form") not in ("10-K","10-K/A"): continue
            s,e=u.get("start"),u["end"]
            if dur:
                if not s: continue
                n=(date.fromisoformat(e)-date.fromisoformat(s)).days
                if not (340<=n<=380): continue
            else:
                if s: continue
            p=out.get(e)
            if p is None or u["filed"]>p[1]: out[e]=(u["val"],u["filed"])
    return out
names={"HLF":"Herbalife","NUS":"Nu Skin","MED":"Medifast","NHTC":"Natural Health Trends",
       "MTEX":"Mannatech","LFVN":"LifeVantage","BODI":"BODi (Beachbody)"}
for t in ["HLF","NUS","MED","NHTC","MTEX","LFVN","BODI"]:
    p=os.path.join(D,f"{t}_companyfacts.json")
    if not os.path.exists(p): continue
    f=json.load(open(p))
    R=series(f,REV); O=series(f,OPI)
    ks=sorted(R)
    print(f"\n=== {t} {names[t]} ===")
    for k in ks:
        if k < "2018": continue
        o=O.get(k)
        print(f"  {k}  rev {R[k][0]/1e6:9.1f}   opinc {(o[0]/1e6 if o else float('nan')):9.1f}  "
              f"{(100*o[0]/R[k][0] if o else float('nan')):6.1f}%")
