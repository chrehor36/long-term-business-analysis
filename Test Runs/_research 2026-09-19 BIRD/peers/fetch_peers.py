import sys, os, json, time
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, ".."))
from fetch_core import get
P = {"CRWV": 1769628, "NBIS": 1513845, "APLD": 1144879, "IREN": 1878848, "QMLS": 2084026}
for t, c in P.items():
    try:
        j = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json")
        open(os.path.join(here, f"{t}_companyfacts.json"), "w").write(j); print(t, "facts", len(j))
    except Exception as e: print(t, "facts ERR", e)
    time.sleep(0.3)
s = json.loads(get("https://data.sec.gov/submissions/CIK0002084026.json"))
json.dump(s, open(os.path.join(here, "QMLS_submissions.json"), "w"))
r = s["filings"]["recent"]
print(s["name"], s.get("sicDescription"), s.get("stateOfIncorporation"), s.get("formerNames"))
for i in range(min(40, len(r["form"]))):
    print(r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["items"][i])
