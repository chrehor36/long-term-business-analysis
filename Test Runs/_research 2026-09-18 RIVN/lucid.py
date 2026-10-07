from fetch_core import *
import json
CIKL = 1811210
s = json.loads(get(f"https://data.sec.gov/submissions/CIK{CIKL:010d}.json"))
r = s["filings"]["recent"]
ks = [(r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["reportDate"][i]) for i in range(len(r["form"])) if r["form"][i]=="10-K"]
print(s["name"], ks[:5])
for fd, acc, doc, rd in ks[:5]:
    if rd[:4] in ("2025","2023","2021"):
        grab(acc, doc, os.path.join("peers", f"LCID_tenk_{rd}"), cik=CIKL)
