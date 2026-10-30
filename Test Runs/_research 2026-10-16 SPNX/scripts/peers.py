import json, urllib.request, os, time
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
P={"RES":"0000742278","OIS":"0001121484","WFRD":"0001603923","SPN":"0000886835"}
TAGS={"rev":["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet"],
      "opinc":["OperatingIncomeLoss"],"assets":["Assets"],
      "ocf":["NetCashProvidedByUsedInOperatingActivities"],"capex":["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"],
      "ni":["NetIncomeLoss"]}
for t,cik in P.items():
    f=f"cache/peers/{t}_facts.json"
    if not os.path.exists(f):
        b=urllib.request.urlopen(urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json",headers=UA)).read()
        open(f,"wb").write(b); time.sleep(0.3)
    d=json.load(open(f))["facts"].get("us-gaap",{})
    out={}
    for k,tags in TAGS.items():
        for tg in tags:
            if tg not in d: continue
            for u in d[tg]["units"].get("USD",[]):
                if u.get("form")!="10-K": continue
                end=u["end"]; y=int(end[:4])
                if k=="assets":
                    if not end.endswith("12-31"): continue
                else:
                    if "start" not in u: continue
                    from datetime import date
                    s=date.fromisoformat(u["start"]); e=date.fromisoformat(end)
                    if not 340<(e-s).days<380: continue
                # newest filing wins
                key=(k,y)
                if key not in out or u["filed"]>out[key][1]:
                    if k in [kk for (kk,yy) in out if yy==y and kk==k] and tg!=out.get((k,y),(None,None,tg))[2]: pass
                    out[key]=(u["val"],u["filed"],tg)
    print("==",t)
    for y in range(2014,2026):
        row=[out.get((k,y),(None,))[0] for k in TAGS]
        if any(v is not None for v in row):
            print(y," ".join(f"{k}={v/1e6:,.0f}" if v is not None else f"{k}=n/f" for k,v in zip(TAGS,row)))
