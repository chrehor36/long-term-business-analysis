import sys, json, os
sys.path.insert(0, "..")
from fetch_core import get, strip, time
peers = {"FORM":1039399, "COHU":21535, "TER":97210}
for t, cik in peers.items():
    s = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    r = s["filings"]["recent"]
    for i in range(len(r["form"])):
        if r["form"][i]=="10-K" and r["reportDate"][i][:4]=="2022":
            acc, doc, rd = r["accessionNumber"][i], r["primaryDocument"][i], r["reportDate"][i]
            path = f"{t}_10K_{rd}.txt"
            raw = get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}")
            open(path, "w", encoding="utf-8").write(strip(raw)); print(t, acc, rd); time.sleep(0.5)
