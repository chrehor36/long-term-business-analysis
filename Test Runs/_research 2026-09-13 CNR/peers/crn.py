import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pf
cik = "0001770561"
j = json.loads(pf.get(f"https://data.sec.gov/submissions/CIK{cik}.json"))
r = j["filings"]["recent"]
for i, f in enumerate(r["form"]):
    if f in ("10-K", "10-K/A") or (f == "10-Q" and r["reportDate"][i] == "2026-06-30"):
        print(f, r["filingDate"][i], r["reportDate"][i], r["accessionNumber"][i], r["primaryDocument"][i])
        if r["reportDate"][i] >= "2021-12-31":
            fp = pf.fetch("CRN", cik, r["accessionNumber"][i], r["primaryDocument"][i]); print("   ", os.path.getsize(fp))
