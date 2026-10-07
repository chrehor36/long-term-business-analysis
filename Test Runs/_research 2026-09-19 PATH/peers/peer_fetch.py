import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fetch_core import get, strip
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
for tk, cik in [("APPN",1441683),("PEGA",1013857),("NOW",1373715),("SSNC",1402436)]:
    p = os.path.join(H, f"{tk}_companyfacts.json")
    if not os.path.exists(p):
        open(p,"w").write(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json")); time.sleep(0.5)
    s = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json")); r = s["filings"]["recent"]
    for i in range(len(r["form"])):
        if r["form"][i] == "10-K":
            acc, doc = r["accessionNumber"][i], r["primaryDocument"][i]
            print(tk, r["filingDate"][i], acc, doc)
            out = os.path.join(H, f"peer_{tk}_tenk_{r['reportDate'][i]}.txt")
            if not os.path.exists(out):
                open(out,"w",encoding="utf-8").write(strip(get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}")))
            break
    time.sleep(0.5)
