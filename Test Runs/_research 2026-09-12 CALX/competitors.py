"""Competitor companyfacts pull for the [E3-28] row. Transcription only."""
import json, urllib.request, os, time
from datetime import date
HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
def get(url):
    for i in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read().decode("utf-8","replace")
        except Exception as e:
            print("retry", i, e); time.sleep(3)
    raise RuntimeError(url)
tick = json.loads(get("https://www.sec.gov/files/company_tickers.json"))
tmap = {v["ticker"]: v["cik_str"] for v in tick.values()}
PEERS = ["COMM"]
out = {}
for t in PEERS:
    cik = tmap.get(t)
    if not cik:
        print(t, "NO CIK"); continue
    cf = json.loads(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json"))
    out[t] = {"cik": cik, "name": cf.get("entityName"), "facts": {}}
    for ns in ("us-gaap","ifrs-full"):
        for tag in ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet",
                    "GrossProfit","CostOfRevenue","CostOfGoodsAndServicesSold","OperatingIncomeLoss","NetIncomeLoss",
                    "ResearchAndDevelopmentExpense","ShareBasedCompensation",
                    "NetCashProvidedByUsedInOperatingActivities","PaymentsToAcquirePropertyPlantAndEquipment",
                    "StockholdersEquity","Assets","Liabilities","Goodwill","IntangibleAssetsNetExcludingGoodwill",
                    "Revenue","ProfitLossFromOperatingActivities","ProfitLoss","GrossProfit"]:
            d = cf.get("facts",{}).get(ns,{}).get(tag)
            if not d: continue
            unit = "USD" if "USD" in d["units"] else ("EUR" if "EUR" in d["units"] else list(d["units"])[0])
            rows = {}
            for r in d["units"][unit]:
                if "start" in r:
                    s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                    if not (330 <= (e-s).days <= 380): continue
                k = r["end"]
                if k not in rows or r["filed"] > rows[k]["filed"]:
                    rows[k] = {"val": r["val"], "filed": r["filed"], "form": r["form"], "unit": unit}
            out[t]["facts"][f"{ns}:{tag}"] = rows
    print(t, cik, cf.get("entityName"), len(out[t]["facts"]))
    time.sleep(0.3)
json.dump(out, open(os.path.join(HERE,"competitor_xbrl_comm.json"),"w"), indent=0)
