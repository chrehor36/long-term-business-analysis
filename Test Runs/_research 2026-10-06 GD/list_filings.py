"""List filings of a CIK from the EDGAR submissions file. Usage: python list_filings.py CIK10 SINCE [FORMS,..]"""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get
cik = sys.argv[1]
since = sys.argv[2]
forms = sys.argv[3].split(",") if len(sys.argv) > 3 else ["10-K", "10-Q", "DEF 14A", "8-K"]
p = get(f"https://data.sec.gov/submissions/CIK{cik}.json", f"subs_{cik}.json")
r = json.load(open(p))["filings"]["recent"]
for i in range(len(r["form"])):
    if r["form"][i] in forms and r["filingDate"][i] >= since:
        print(r["form"][i], r["filingDate"][i], r["reportDate"][i], r["accessionNumber"][i],
              r["primaryDocument"][i], r.get("items", [""] * len(r["form"]))[i])
