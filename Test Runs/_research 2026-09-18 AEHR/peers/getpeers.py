import sys, json, os
sys.path.insert(0, "..")
from fetch_core import get, strip, time
sys.stdout.reconfigure(encoding="utf-8")
peers = {"FORM":1039399, "COHU":21535, "TER":97210}
for t, cik in peers.items():
    s = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    r = s["filings"]["recent"]
    ks = [(r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["reportDate"][i]) for i in range(len(r["form"])) if r["form"][i]=="10-K"][:2]
    print(t, s["name"], ks)
    for fd, acc, doc, rd in ks[:1]:
        path = f"{t}_10K_{rd}.txt"
        if not os.path.exists(path):
            raw = get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}")
            open(path, "w", encoding="utf-8").write(strip(raw)); time.sleep(0.5)
    cf = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json")
    open(f"{t}_companyfacts.json","w",encoding="utf-8").write(cf)
