"""List filings of a CIK from the cached EDGAR submissions JSON. Usage: python listfilings.py <json> <since> [forms...]"""
import json, sys
d = json.load(open(sys.argv[1]))
since = sys.argv[2]
forms = set(sys.argv[3:]) or {"10-K", "10-Q", "DEF 14A", "8-K"}
r = d["filings"]["recent"]
for i, f in enumerate(r["form"]):
    if f in forms and r["filingDate"][i] >= since:
        print(f, r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i], r.get("items", [""] * len(r["form"]))[i])
