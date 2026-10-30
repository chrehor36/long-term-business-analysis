import json,sys
from datetime import date
def series(f,keys):
    d=json.load(open(f));g=d["facts"]["us-gaap"];out={}
    for k in keys:
        if k not in g: continue
        for u,vals in g[k]["units"].items():
            if u!="USD" and u!="USD/shares": continue
            for v in vals:
                if v.get("form")!="10-K": continue
                if "start" in v and (date.fromisoformat(v["end"])-date.fromisoformat(v["start"])).days<350: continue
                y=v["end"][:4]
                if y not in out or v["filed"]>out[y][1]: out[y]=(v["val"],v["filed"],v["accn"])
        if out: break
    return d.get("entityName"),out
names={"0001711269":"EVRG","0000004904":"AEP","0001021635":"OGE","0001002910":"AEE"}
for c,t in names.items():
    f="cache/facts.json" if t=="EVRG" else f"cache/facts_{c}.json"
    rows={}
    for lab,keys in [("NI",["NetIncomeLossAvailableToCommonStockholdersBasic","NetIncomeLoss","ProfitLoss"]),("EQ",["StockholdersEquity"]),("OCF",["NetCashProvidedByUsedInOperatingActivities"]),("CAPEX",["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"]),("DA",["DepreciationDepletionAndAmortization","DepreciationAndAmortization","DepreciationAmortizationAndAccretionNet"]),("EPS",["EarningsPerShareDiluted"]),("REV",["Revenues","RevenueFromContractWithCustomerIncludingAssessedTax"])]:
        n,s=series(f,keys); rows[lab]=s
    print(t,n)
    for y in range(2016,2026):
        y=str(y); r=[rows[l].get(y,(None,))[0] for l in ["NI","EQ","OCF","CAPEX","DA","EPS","REV"]]
        roe = (r[0]/r[1]*100) if r[0] and r[1] else None
        print(" ",y," ".join("%9.1f"%(x/1e6) if isinstance(x,(int,float)) and abs(x)>1000 else ("%9.2f"%x if isinstance(x,(int,float)) else "        -") for x in r), " ROE %.1f%%"%roe if roe else "")
    accs=set(v[2] for l in rows for v in rows[l].values() if v)
    print("  accessions(latest):", sorted(accs)[-3:])
