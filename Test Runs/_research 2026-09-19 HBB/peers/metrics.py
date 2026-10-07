import json, sys, os
sys.stdout.reconfigure(encoding="utf-8")
here=os.path.dirname(os.path.abspath(__file__))
TAGS = {"rev":["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet"],
        "gp":["GrossProfit"], "oi":["OperatingIncomeLoss"],
        "ocf":["NetCashProvidedByUsedInOperatingActivities"],
        "capex":["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"],
        "sbc":["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"],
        "da":["DepreciationDepletionAndAmortization","DepreciationAmortizationAndAccretionNet","DepreciationAndAmortization"]}
def annual(g, tags):
    out={}
    for t in tags:
        for x in g.get(t,{}).get("units",{}).get("USD",[]):
            if x.get("form") not in ("10-K","20-F","10-K/A","20-F/A"): continue
            s,e=x.get("start"),x.get("end")
            if not s: continue
            from datetime import date
            d=(date.fromisoformat(e)-date.fromisoformat(s)).days
            if d<350 or d>380: continue
            fy=e[:4]
            # newest filed wins
            if fy not in out or x["filed"]>out[fy][1]: out[fy]=(x["val"],x["filed"])
        if out: pass
    return {k:v[0] for k,v in out.items()}
files={"HBB":os.path.join(here,"..","companyfacts.json")}
for t in ["SN","SPB","NWL","HELE","LCUT","WHR"]: files[t]=os.path.join(here,f"{t}_companyfacts.json")
for t,fn in files.items():
    g=json.load(open(fn))["facts"]; g={**g.get("ifrs-full",{}),**g.get("us-gaap",{})}
    print("=====",t)
    for k,tags in TAGS.items():
        a={}
        for tg in tags:
            for fy,v in annual(g,[tg]).items(): a.setdefault(fy,v)
        print(k, {fy:round(v/1e6,1) for fy,v in sorted(a.items()) if fy>="2019"})
