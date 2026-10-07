import json, sys
from fetch_core import *
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = os.path.join(HERE, "submissions.json")
if not os.path.exists(p):
    open(p, "w").write(get("https://data.sec.gov/submissions/CIK0001393818.json"))
s = json.load(open(p))
print(s["name"], s.get("formerNames"), s.get("sicDescription"), s.get("fiscalYearEnd"))
rows = []
def add(r):
    for i in range(len(r["form"])):
        rows.append((r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r.get("items", [""]*len(r["form"]))[i], r["reportDate"][i]))
add(s["filings"]["recent"])
for f in s["filings"].get("files", []):
    add(json.loads(get("https://data.sec.gov/submissions/" + f["name"])))
rows.sort()
with open(os.path.join(HERE, "filings_list.txt"), "w", encoding="utf-8") as fh:
    for r in rows: fh.write(" | ".join(r) + "\n")
print(len(rows))
