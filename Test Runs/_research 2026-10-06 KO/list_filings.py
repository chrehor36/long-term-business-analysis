"""List KO filings from the cached EDGAR submissions file. Usage: python list_filings.py [since] [forms comma-separated]"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
since = sys.argv[1] if len(sys.argv) > 1 else "2025-01-01"
forms = sys.argv[2].split(",") if len(sys.argv) > 2 else ["10-K", "10-Q", "DEF 14A", "8-K"]
d = json.load(open(os.path.join(HERE, "cache", "submissions_KO.json")))
r = d["filings"]["recent"]
for i in range(len(r["form"])):
    if r["form"][i] in forms and r["filingDate"][i] >= since:
        print(r["form"][i], r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i], r.get("items", [""] * len(r["form"]))[i])
