import json
from datetime import date
def load(t):
    x=json.load(open(f"{t}_companyfacts.json"))
    if isinstance(x,str): x=json.loads(x)
    return x["facts"].get("us-gaap",{})
def ann(g,tags):
    out={}
    for tag in tags:
        if tag not in g: continue
        for u,arr in g[tag]["units"].items():
            if u!="USD": continue
            for x in arr:
                if x.get("form") not in ("10-K","10-K/A") or "start" not in x: continue
                d=(date.fromisoformat(x["end"])-date.fromisoformat(x["start"])).days
                if 350<d<380:
                    k=x["end"][:7]
                    if k not in out or x["filed"]>out[k][0]: 
                        if k in out and out[k][2]!=tag and tags.index(out[k][2])<tags.index(tag): continue
                        out[k]=(x["filed"],x["val"],tag)
    return {k:v[1] for k,v in sorted(out.items())}
REV=["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet","RevenueFromContractWithCustomerIncludingAssessedTax"]
OCF=["NetCashProvidedByUsedInOperatingActivities","NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"]
SBC=["ShareBasedCompensation"]
CAPX=["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"]
SW=["PaymentsForSoftware","PaymentsToDevelopSoftware"]
OPI=["OperatingIncomeLoss"]
rows={}
for t in ["ACVA","OPLN","CPRT","RBA","CVNA","KMX","CARG"]:
    g=load(t)
    rev,ocf,sbc,cx,sw,op=[ann(g,x) for x in (REV,OCF,SBC,CAPX,SW,OPI)]
    yrs=sorted(ocf)[-6:]
    print("==",t)
    tot={"rev":0,"oe":0}
    for y in yrs:
        r=rev.get(y); o=ocf.get(y); s=sbc.get(y,0); c=cx.get(y,0); w=sw.get(y,0); p=op.get(y)
        oe=None if o is None else o-s-c-w
        m=None if (oe is None or not r) else oe/r
        print(y, "rev",r and round(r/1e6,1),"ocf",o and round(o/1e6,1),"sbc",round(s/1e6,1),"capex",round(c/1e6,1),"sw",round(w/1e6,1),"opinc",p and round(p/1e6,1),
              "OE",oe and round(oe/1e6,1),"OEm", m and f"{m:.1%}", "opm", (p and r) and f"{p/r:.1%}")
    last5=yrs[-5:]
    R=sum(rev.get(y,0) for y in last5); O=sum(ocf.get(y,0)-sbc.get(y,0)-cx.get(y,0)-sw.get(y,0) for y in last5)
    print("5y cum", last5[0], last5[-1], f"{O/R:.1%}" if R else None)
