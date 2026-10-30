import json, os
from fetch_core import *
p = os.path.join(HERE, "submissions.json")
if not os.path.exists(p):
    open(p, "w").write(get(f"https://data.sec.gov/submissions/CIK{CIK:010d}.json"))
s = json.load(open(p))
r = s["filings"]["recent"]
out = []
for i in range(len(r["form"])):
    out.append(f'{r["filingDate"][i]} {r["form"][i]:10s} {r["accessionNumber"][i]} {r["primaryDocument"][i]} {r.get("items",[""]*9999)[i]} {r["reportDate"][i]}')
open(os.path.join(HERE, "filings_list.txt"), "w").write("\n".join(out))
print(s["name"], s["sic"], s["fiscalYearEnd"], len(out), s["filings"].get("files"))
