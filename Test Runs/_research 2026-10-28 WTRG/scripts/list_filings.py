import json, sys
sys.path.insert(0, sys.argv[1])
from fetch import get
cik = sys.argv[2]
forms = set(sys.argv[3].split(","))
d = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik}.json"))
r = d["filings"]["recent"]
for i in range(len(r["form"])):
    if r["form"][i] in forms:
        print(r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["reportDate"][i])
