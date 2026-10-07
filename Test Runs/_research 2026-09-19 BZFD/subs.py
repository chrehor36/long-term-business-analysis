from fetch_core import *
import sys
sys.stdout.reconfigure(encoding="utf-8")
s = json.loads(get("https://data.sec.gov/submissions/CIK0001828972.json"))
json.dump(s, open("submissions.json","w"))
print(s["name"], s.get("sic"), s.get("sicDescription"), s.get("stateOfIncorporation"), s.get("fiscalYearEnd"), s.get("formerNames"), s.get("tickers"), s.get("exchanges"))
r = s["filings"]["recent"]
rows=[]
for i in range(len(r["form"])):
    rows.append(f'{r["filingDate"][i]} {r["form"][i].replace(" ","_")} {r["accessionNumber"][i]} {r["primaryDocument"][i] or "-"} {r["items"][i] or "-"}')
for fx in s["filings"].get("files", []):
    o = json.loads(get("https://data.sec.gov/submissions/" + fx["name"]))
    for i in range(len(o["form"])):
        rows.append(f'{o["filingDate"][i]} {o["form"][i].replace(" ","_")} {o["accessionNumber"][i]} {o["primaryDocument"][i] or "-"} {o["items"][i] or "-"}')
with open("filings_list.txt","w") as f:
    f.write("\n".join(rows)+"\n")
print("n", len(rows), "files", s["filings"].get("files"))
