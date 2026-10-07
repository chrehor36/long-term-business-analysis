"""Competitor row: same metric, latest full fiscal year, SEC XBRL companyfacts. Transcription only."""
import json, os, time, urllib.request
from datetime import date
HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
PEERS = {
    "INOD": 903651, "G (Genpact)": 1398659, "CNXC (Concentrix)": 1803599,
    "WNS": 1356570, "TASK (TaskUs)": 1829864, "TIXT (TELUS Digital)": 1825155,
    "EXLS (ExlService)": 1297989, "CTSH (Cognizant)": 1058290,
}
TAGS = ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","OperatingIncomeLoss",
        "GrossProfit","CostOfRevenue","CostOfServices","NetIncomeLoss",
        "NetCashProvidedByUsedInOperatingActivities","ShareBasedCompensation",
        "PaymentsToAcquirePropertyPlantAndEquipment","DepreciationDepletionAndAmortization",
        "StockholdersEquity","Goodwill","IntangibleAssetsNetExcludingGoodwill","Assets"]
def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8","replace")
def latest_fy(facts, tag):
    for ns in ("us-gaap","ifrs-full"):
        d = facts.get(ns,{}).get(tag)
        if not d: continue
        rows = d["units"].get("USD") or next(iter(d["units"].values()))
        best = {}
        for r in rows:
            if r.get("form") not in ("10-K","20-F","40-F","10-K/A"): continue
            if "start" in r:
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                if not (330 <= (e-s).days <= 380): continue
            k = r["end"]
            if k not in best or r["filed"] > best[k]["filed"]:
                best[k] = r
        if best:
            k = max(best); return k, best[k]["val"], best[k]["form"], best[k]["accn"]
    return None
out = {}
for name, cik in PEERS.items():
    try:
        cf = json.loads(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"))
    except Exception as e:
        print(name, "FAILED", e); out[name] = {"error": str(e)}; continue
    facts = cf["facts"]
    row = {}
    for t in TAGS:
        row[t] = latest_fy(facts, t)
    out[name] = row
    print("==", name, cf.get("entityName"))
    for t, v in row.items():
        if v: print(f"   {t:60s} {v[0]}  {v[1]/1e6 if isinstance(v[1],(int,float)) and abs(v[1])>1e4 else v[1]:>12}  {v[2]} {v[3]}")
    time.sleep(0.3)
json.dump(out, open(os.path.join(HERE,"competitor_xbrl.json"),"w"), indent=1, default=str)
