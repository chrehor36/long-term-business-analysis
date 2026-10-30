import json
from datetime import date
def annual(facts, tags, instant=False):
    out={}
    for ns in ("us-gaap",):
        for t in tags:
            if t not in facts["facts"].get(ns,{}): continue
            for u,vals in facts["facts"][ns][t]["units"].items():
                if u!="USD": continue
                for v in vals:
                    if not v.get("form","").startswith("10-K"): continue
                    if instant:
                        if v.get("start"): continue
                        if not v["end"].endswith("12-31"): continue
                    else:
                        s=v.get("start")
                        if not s: continue
                        span=(date.fromisoformat(v["end"])-date.fromisoformat(s)).days
                        if span<350 or span>380: continue
                    y=int(v["end"][:4])
                    if y not in out or v["filed"]<out[y][1]:
                        out[y]=(v["val"]/1e6,v["filed"],t)
            if out: pass
    return {y:v[0] for y,v in out.items()}
peers={"BTU":"facts.json","ARCH":"peers/facts_1037676.json","CNR(CEIX)":"peers/facts_1710366.json","ARLP":"peers/facts_1086600.json","HCC":"peers/facts_1691303.json"}
for name,fn in peers.items():
    f=json.load(open(fn))
    ni=annual(f,["NetIncomeLossAvailableToCommonStockholdersBasic","NetIncomeLoss","ProfitLoss"])
    eq=annual(f,["StockholdersEquity","PartnersCapital","PartnersCapitalIncludingPortionAttributableToNoncontrollingInterest","StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],instant=True)
    ocf=annual(f,["NetCashProvidedByUsedInOperatingActivities"])
    cap=annual(f,["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"])
    rev=annual(f,["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet"])
    print("==",name)
    print(" yr     rev     NI     equity   OCF   capex   ROE")
    for y in range(2011,2026):
        if y in ni or y in eq:
            e=eq.get(y); e0=eq.get(y-1)
            roe = ni.get(y)/((e+e0)/2)*100 if (ni.get(y) is not None and e and e0) else None
            print(f" {y} {rev.get(y,float('nan')):8.0f} {ni.get(y,float('nan')):7.0f} {eq.get(y,float('nan')):8.0f} {ocf.get(y,float('nan')):6.0f} {cap.get(y,float('nan')):6.0f}  {'' if roe is None else f'{roe:5.1f}%'}")
