import json, sys
from fetch_core import *
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
raw = get("https://data.sec.gov/submissions/CIK0001326801.json")
open("submissions.json","w",encoding="utf-8").write(raw)
d = json.loads(raw)
print(d["name"], "|", d["sicDescription"], "|", d["fiscalYearEnd"], "|", d.get("formerNames"), "|", d.get("tickers"))
r = d["filings"]["recent"]
rows = list(zip(r["filingDate"], r["form"], r["accessionNumber"], r["primaryDocument"], r["reportDate"], r["items"]))
with open("filings_list.txt","w",encoding="utf-8") as f:
    for x in rows: f.write(" | ".join(map(str,x))+"\n")
for x in rows:
    if x[1] not in ("4","3","5","144","SC 13G/A","SC 13G","4/A","S-8","S-8 POS","FWP","424B2","11-K","SD","PX14A6G","DEFA14A","ARS"): print(*x)
print("files", d["filings"].get("files"))
tm = json.loads(get("https://www.sec.gov/files/company_tickers.json"))
for v in tm.values():
    if v["ticker"] in ("META",): print("company_tickers:", v)
