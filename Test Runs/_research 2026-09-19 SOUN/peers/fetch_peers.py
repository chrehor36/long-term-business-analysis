import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fetch_core import get
sys.stdout.reconfigure(encoding="utf-8")
here = os.path.dirname(os.path.abspath(__file__))
t = json.loads(get("https://www.sec.gov/files/company_tickers.json"))
want = ["CRNC","LPSN","FIVN","NICE","VRNT","CXAI","BBAI","AI","RNG","SPT","NUAN"]
m = {v["ticker"]: (v["cik_str"], v["title"]) for v in t.values()}
for w in want:
    print(w, m.get(w))
    if w in m:
        cik = m[w][0]
        try:
            f = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json")
            open(os.path.join(here, f"{w}_companyfacts.json"), "w").write(f)
        except Exception as e: print("ERR", w, e)
