"""List recent filings from a cached EDGAR submissions JSON.
Usage: python -I list_filings.py cache/submissions.json SINCE [FORM ...]"""
import sys, json

d = json.load(open(sys.argv[1]))
r = d["filings"]["recent"]
since = sys.argv[2]
forms = set(sys.argv[3:]) or None
for i in range(len(r["form"])):
    if r["filingDate"][i] < since:
        continue
    if forms and r["form"][i] not in forms:
        continue
    print(r["form"][i], r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i], r.get("items", [""] * 9999)[i])
