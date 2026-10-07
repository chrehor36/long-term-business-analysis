import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pf
for cik in ["0000886986", "0000811809", "0001770561", "0001524684"]:
    j = json.loads(pf.get(f"https://data.sec.gov/submissions/CIK{cik}.json"))
    r = j["filings"]["recent"]
    forms = {}
    for i, f in enumerate(r["form"]):
        if f in ("40-F", "20-F", "10-K", "10-Q", "6-K"):
            forms.setdefault(f, []).append((r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i]))
    print(cik, j["name"], {k: v[:2] for k, v in forms.items()})
