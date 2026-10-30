import json, sys
from fetch_core import *
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
raw = get("https://data.sec.gov/submissions/CIK0001326801-submissions-001.json")
open("submissions_001.json","w",encoding="utf-8").write(raw)
r = json.loads(raw)
rows = list(zip(r["filingDate"], r["form"], r["accessionNumber"], r["primaryDocument"], r["reportDate"], r["items"]))
with open("filings_list_001.txt","w",encoding="utf-8") as f:
    for x in rows: f.write(" | ".join(map(str,x))+"\n")
for x in rows:
    if x[1] in ("10-K","10-K/A","10-Q/A","8-K") and x[0] >= "2019": print(*x)
