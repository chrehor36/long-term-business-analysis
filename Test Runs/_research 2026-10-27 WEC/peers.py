import json
from datetime import date
def ann(f,tags,dur=True):
    out={}
    for t in tags:
        if t not in f["us-gaap"]: continue
        for u,vals in f["us-gaap"][t]["units"].items():
            if u!="USD": continue
            for v in vals:
                if v.get("form")!="10-K": continue
                if dur:
                    if "start" not in v: continue
                    d=(date.fromisoformat(v["end"])-date.fromisoformat(v["start"])).days
                    if not 350<d<380: continue
                else:
                    if "start" in v or v["end"][5:]!="12-31": continue
                y=int(v["end"][:4])
                if y not in out or v["filed"]>out[y][1]: out[y]=(v["val"]/1e6,v["filed"],t)
    return {k:v[0] for k,v in out.items()}
for tk in ["WEC","LNT","XEL","CMS"]:
    f=json.load(open(f"cache/facts_{tk}.json"))["facts"]
    ni=ann(f,["NetIncomeLossAvailableToCommonStockholdersBasic","NetIncomeLoss"])
    eq=ann(f,["StockholdersEquity"],dur=False)
    ocf=ann(f,["NetCashProvidedByUsedInOperatingActivities"])
    cap=ann(f,["PaymentsToAcquireProductiveAssets","PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireOtherPropertyPlantAndEquipment"])
    da=ann(f,["DepreciationDepletionAndAmortization","DepreciationAndAmortization","DepreciationAmortizationAndAccretionNet"])
    print(tk)
    roes=[]
    for y in range(2016,2026):
        if y in ni and y in eq and y-1 in eq:
            r=ni[y]/((eq[y]+eq[y-1])/2); roes.append(r)
        else: r=None
        print(" ",y,"NI",round(ni.get(y,0)),"Eq",round(eq.get(y,0)),"ROE",None if r is None else round(100*r,1),"OCF",round(ocf.get(y,0)),"capex",round(cap.get(y,0)),"D&A",round(da.get(y,0)),"OCF-capex",round(ocf.get(y,0)-cap.get(y,0)))
    if roes: print("  avg ROE",round(100*sum(roes)/len(roes),1),"n",len(roes))
