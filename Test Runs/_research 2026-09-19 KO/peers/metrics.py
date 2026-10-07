import json, sys, os
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
TAGS = {"rev":["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet","SalesRevenueGoodsNet"],
        "gp":["GrossProfit"], "oi":["OperatingIncomeLoss"],
        "ocf":["NetCashProvidedByUsedInOperatingActivities"],
        "capex":["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"],
        "sbc":["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"],
        "da":["DepreciationDepletionAndAmortization","DepreciationAmortizationAndAccretionNet","DepreciationAndAmortization"]}
def annual(g, tag):
    out={}
    for x in g.get(tag,{}).get("units",{}).get("USD",[]):
        if x.get("form") not in ("10-K","10-K/A"): continue
        s,e=x.get("start"),x.get("end")
        if not s: continue
        d=(date.fromisoformat(e)-date.fromisoformat(s)).days
        if d<350 or d>380: continue
        if "segment" in x: continue
        fy=str(date.fromisoformat(e).year if date.fromisoformat(e).month>6 else date.fromisoformat(e).year-1)
        if fy not in out or x["filed"]>out[fy][1]: out[fy]=(x["val"],x["filed"])
    return {k:v[0] for k,v in out.items()}
res={}
for t in ["KO","PEP","KDP","MNST","CELH","COKE"]:
    g=json.load(open(f"{t}_companyfacts.json"))["facts"]["us-gaap"]
    print("=====",t); res[t]={}
    for k,tags in TAGS.items():
        a={}
        for tg in tags:
            for fy,v in annual(g,tg).items(): a.setdefault(fy,v)
        res[t][k]=a
        print(k, {fy:round(v/1e6,1) for fy,v in sorted(a.items()) if fy>="2019"})
json.dump(res,open("metrics.json","w"))
