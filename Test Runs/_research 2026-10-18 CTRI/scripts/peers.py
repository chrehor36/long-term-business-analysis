import json, sys
sys.path.insert(0, sys.argv[0].rsplit("/",1)[0])
from fetch import get
peers = {"PWR":"0001050915","MYRG":"0000700923","PRIM":"0001361538","MTZ":"0000015615"}
tags = ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","OperatingIncomeLoss","Assets","Goodwill",
        "IntangibleAssetsNetExcludingGoodwill","StockholdersEquity","NetCashProvidedByUsedInOperatingActivities",
        "PaymentsToAcquirePropertyPlantAndEquipment","ShareBasedCompensation","GoodwillImpairmentLoss","InterestExpense","InterestExpenseNonoperating","NetIncomeLoss"]
for t,cik in peers.items():
    d = json.loads(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"))
    g = d["facts"].get("us-gaap",{})
    print("=====",t,d["entityName"])
    for tag in tags:
        if tag not in g: continue
        rows = {}
        for u,vals in g[tag]["units"].items():
            for v in vals:
                if v.get("form") not in ("10-K","10-K/A"): continue
                fy_end = v["end"]
                if "start" in v:
                    from datetime import date
                    s=date.fromisoformat(v["start"]); e=date.fromisoformat(v["end"])
                    if (e-s).days<350: continue
                yr = int(fy_end[:4]) if fy_end[5:7]!="01" else int(fy_end[:4])-1
                if yr<2015: continue
                rows.setdefault(yr,(v["val"],v["accn"]))  # first filed
        if rows:
            print(f"{tag:45s}", " ".join(f"{y}:{rows[y][0]/1e6:.0f}" for y in sorted(rows)))
