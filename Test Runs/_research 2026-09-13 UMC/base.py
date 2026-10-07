import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from get import get, HERE
CIK = "0001033767"
open(os.path.join(HERE, "submissions.json"), "wb").write(get(f"https://data.sec.gov/submissions/CIK{CIK}.json"))
open(os.path.join(HERE, "companyfacts.json"), "wb").write(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK}.json"))
sub = json.load(open(os.path.join(HERE, "submissions.json")))
r = sub["filings"]["recent"]
with open(os.path.join(HERE, "filings_list.txt"), "w") as f:
    for i in range(len(r["form"])):
        f.write("\t".join([r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["reportDate"][i], r.get("primaryDocDescription", [""]*9999)[i]]) + "\n")
print(sub.get("filings", {}).get("files"))
print(sub.get("name"), sub.get("fiscalYearEnd"))
