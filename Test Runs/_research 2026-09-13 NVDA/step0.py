import sys, os, json
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.join(ROOT, "Screens"))
import sources as S
HERE = os.path.dirname(os.path.abspath(__file__))
CIK = "0001045810"

print("SOVEREIGN", S.sovereign("USD"))
print("PRICE", S.price("NVDA"))
print("DEAL_NOTE", S.deal_note(CIK))
hard, soft, since = S.deal_filings(CIK)
print("HARD", hard); print("SOFT", soft); print("SINCE", since)

import urllib.request
def sec(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=S.SEC_UA), timeout=60).read()
sub = json.loads(sec(f"https://data.sec.gov/submissions/CIK{CIK}.json"))
open(os.path.join(HERE, "submissions.json"), "w").write(json.dumps(sub))
r = sub["filings"]["recent"]
for i, f in enumerate(r["form"]):
    if f in ("10-K", "10-Q", "8-K", "DEF 14A", "10-K/A", "10-Q/A", "SC 13D", "S-4", "425") and r["filingDate"][i] >= "2020-01-01":
        print(f, r["filingDate"][i], r["reportDate"][i], r["accessionNumber"][i], r["primaryDocument"][i], r.get("items", [""]*len(r["form"]))[i])
facts = S.sec_facts(CIK)
open(os.path.join(HERE, "companyfacts.json"), "w").write(json.dumps(facts))
print("facts saved")
