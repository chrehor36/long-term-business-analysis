import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fetch_core import get
sys.stdout.reconfigure(encoding="utf-8")
P = {"GOOGL":1652044,"SNAP":1564408,"PINS":1506293,"RDDT":1713445,"AMZN":1018724,"META":1326801}
for t,c in P.items():
    fn = f"{t}_companyfacts.json"
    if not os.path.exists(fn):
        open(fn,"w",encoding="utf-8").write(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json"))
    s = json.loads(get(f"https://data.sec.gov/submissions/CIK{c:010d}.json"))
    r = s["filings"]["recent"]
    ks = [(d,a,p,rp) for d,f,a,p,rp in zip(r["filingDate"],r["form"],r["accessionNumber"],r["primaryDocument"],r["reportDate"]) if f=="10-K"][:2]
    print(t, s["name"], ks)
