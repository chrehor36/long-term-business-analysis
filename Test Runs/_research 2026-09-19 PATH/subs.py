from fetch_core import *
import sys
sys.stdout.reconfigure(encoding="utf-8")
s = json.loads(get("https://data.sec.gov/submissions/CIK0001734722.json"))
json.dump(s, open("submissions.json","w"))
print(s["name"], s.get("sic"), s.get("sicDescription"), s.get("stateOfIncorporation"), s.get("fiscalYearEnd"), s.get("formerNames"), s.get("tickers"), s.get("exchanges"))
r = s["filings"]["recent"]
with open("filings_list.txt","w") as f:
    for i in range(len(r["form"])):
        f.write(f'{r["filingDate"][i]} {r["form"][i].replace(" ","_")} {r["accessionNumber"][i]} {r["primaryDocument"][i]} {r["items"][i] or "-"}\n')
print("n", len(r["form"]), "files", s["filings"].get("files"))
