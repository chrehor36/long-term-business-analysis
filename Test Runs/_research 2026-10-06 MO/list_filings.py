"""List MO filings from the cached EDGAR submissions JSON. Usage: python list_filings.py cache/submissions.json SINCE"""
import json, sys

d = json.load(open(sys.argv[1]))
r = d["filings"]["recent"]
for i in range(len(r["form"])):
    if r["form"][i] in ("10-K", "10-Q", "DEF 14A", "8-K") and r["filingDate"][i] >= sys.argv[2]:
        print(r["form"][i], r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["items"][i])
