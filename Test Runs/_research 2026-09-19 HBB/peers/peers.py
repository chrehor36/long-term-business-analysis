import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fetch_core import get
sys.stdout.reconfigure(encoding="utf-8")
P = {"SN":1957132,"SPB":109177,"NWL":814453,"HELE":916789,"LCUT":874396,"WHR":106640}
here = os.path.dirname(os.path.abspath(__file__))
for t,c in P.items():
    fn = os.path.join(here, f"{t}_companyfacts.json")
    if not os.path.exists(fn):
        open(fn,"w").write(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json")); time.sleep(0.3)
    s = json.loads(get(f"https://data.sec.gov/submissions/CIK{c:010d}.json")); time.sleep(0.3)
    r = s["filings"]["recent"]
    ann = [(r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i]) for i in range(len(r["form"])) if r["form"][i] in ("10-K","20-F")][:4]
    print(t, s["name"], s.get("fiscalYearEnd"), ann)
