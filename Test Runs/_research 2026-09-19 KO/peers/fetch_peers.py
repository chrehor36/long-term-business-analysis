import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from fetch_core import get
import time
C = {"KO":21344, "PEP":77476, "KDP":1418135, "MNST":865752, "CELH":1341766, "COKE":317540}
for t,c in C.items():
    fn = f"{t}_companyfacts.json"
    if os.path.exists(fn): continue
    j = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json")
    open(fn,"w").write(j); print(t, len(j)); time.sleep(0.5)
for t in ("MNST","CELH","PEP","KDP"):
    s = json.loads(get(f"https://data.sec.gov/submissions/CIK{C[t]:010d}.json"))
    r = s["filings"]["recent"]
    for i in range(len(r["form"])):
        if r["form"][i] in ("10-K",) :
            print(t, r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i]); break
    for i in range(len(r["form"])):
        if r["form"][i] in ("10-Q",) :
            print(t, "10-Q", r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i]); break
