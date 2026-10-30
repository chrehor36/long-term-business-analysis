import json, sys
from fetch import get
cik = sys.argv[1].zfill(10); out = sys.argv[2]
d = json.loads(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"))
json.dump(d, open(out,"w"))
print(d["entityName"], len(d["facts"].get("us-gaap",{})))
