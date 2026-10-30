import json, sys
from fetch_core import *
s = get("https://data.sec.gov/submissions/CIK0001874178.json")
open(os.path.join(HERE, "submissions.json"), "w", encoding="utf-8").write(s)
d = json.loads(s)
print(d["name"], d.get("tickers"), d.get("exchanges"))
r = d["filings"]["recent"]
out = []
for i in range(len(r["form"])):
    out.append(f'{r["filingDate"][i]} {r["form"][i]:10s} {r["accessionNumber"][i]} {r["primaryDocument"][i]} {r["items"][i]} {r["reportDate"][i]}')
open(os.path.join(HERE, "filings_list.txt"), "w", encoding="utf-8").write("\n".join(out))
print(len(out), "filings; files", d["filings"].get("files"))
