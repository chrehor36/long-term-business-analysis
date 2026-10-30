import json, os, sys, time, urllib.request
from datetime import date
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
here=os.path.dirname(os.path.abspath(__file__))
peers={"GWW":"0000277135","MSM":"0001003078","AIT":"0000109563"}
tags=["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet","OperatingIncomeLoss","StockholdersEquity","NetCashProvidedByUsedInOperatingActivities","PaymentsToAcquirePropertyPlantAndEquipment","GrossProfit","Goodwill"]
for tk,cik in peers.items():
    p=os.path.join(here,"cache",f"{tk}_facts.json")
    if not os.path.exists(p):
        open(p,"wb").write(urllib.request.urlopen(urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json",headers=UA),timeout=90).read()); time.sleep(0.5)
    d=json.load(open(p))["facts"]["us-gaap"]
    print("=====",tk)
    table={}
    for t in tags:
        if t not in d: continue
        for r in list(d[t]["units"].values())[0]:
            if r.get("form")!="10-K": continue
            if "start" in r and (date.fromisoformat(r["end"])-date.fromisoformat(r["start"])).days<350: continue
            e=r["end"]
            if e<"2014": continue
            k=(e,t)
            if k not in table or r["filed"]<table[k][1]: table[k]=(r["val"],r["filed"],r["accn"])
    ends=sorted({e for e,_ in table})
    for e in ends:
        row={t:table.get((e,t)) for t in tags}
        rev=next((row[t][0] for t in ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet"] if row.get(t)),None)
        oi=row["OperatingIncomeLoss"][0] if row.get("OperatingIncomeLoss") else None
        gp=row["GrossProfit"][0] if row.get("GrossProfit") else None
        f=lambda x: f"{x/1e6:,.0f}" if x is not None else "-"
        m=f"{oi/rev*100:.1f}%" if rev and oi else "-"
        g=f"{gp/rev*100:.1f}%" if rev and gp else "-"
        acc=(row.get("OperatingIncomeLoss") or (None,None,"-"))[2]
        print(e,"rev",f(rev),"GM",g,"OI",f(oi),"OM",m,"eq",f(row["StockholdersEquity"][0] if row.get("StockholdersEquity") else None),"OCF",f(row["NetCashProvidedByUsedInOperatingActivities"][0] if row.get("NetCashProvidedByUsedInOperatingActivities") else None),"capex",f(row["PaymentsToAcquirePropertyPlantAndEquipment"][0] if row.get("PaymentsToAcquirePropertyPlantAndEquipment") else None),"GW",f(row["Goodwill"][0] if row.get("Goodwill") else None),acc)
