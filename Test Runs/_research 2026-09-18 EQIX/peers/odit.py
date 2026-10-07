import json
from fetch_core import get, grab
for c in (2069692,1679688):
    d=json.loads(get(f"https://data.sec.gov/submissions/CIK{c:010d}.json")); r=d["filings"]["recent"]
    print(d["name"])
    for i,f in enumerate(r["form"]):
        if f=="10-K": print("  ",r["filingDate"][i],r["accessionNumber"][i],r["primaryDocument"][i])
