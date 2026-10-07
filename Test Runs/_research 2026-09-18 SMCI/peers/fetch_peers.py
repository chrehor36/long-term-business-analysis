import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fetch_core
from fetch_core import get, strip
HERE = os.path.dirname(os.path.abspath(__file__))
for name, cik in [("HPE", 1645590), ("CLS", 1030894), ("SGH", 1616533)]:
    s = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    r = s["filings"]["recent"]
    ks = [(r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["reportDate"][i]) for i, f in enumerate(r["form"]) if f in ("10-K", "40-F", "20-F")]
    print(name, s["name"], ks[:3])
    d, acc, doc, rep = ks[0]
    p = os.path.join(HERE, f"{name}_10K_{rep}.txt")
    if not os.path.exists(p):
        raw = get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}")
        open(p, "w", encoding="utf-8").write(strip(raw)); print("wrote", p, acc)
