import sys, os, json, time
sys.stdout.reconfigure(encoding="utf-8")
from fetch_core import get, strip, HERE
P = os.path.join(HERE, "peers")
for t, cik in [("MDB", 1441816), ("TDC", 816761), ("DDOG", 1561550), ("ESTC", 1707753), ("PLTR", 1321655)]:
    s = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    r = s["filings"]["recent"]
    for i in range(len(r["form"])):
        if r["form"][i] == "10-K":
            acc, doc, fd, rd = r["accessionNumber"][i], r["primaryDocument"][i], r["filingDate"][i], r["reportDate"][i]
            break
    path = os.path.join(P, f"{t}_10K_{rd}.txt")
    if not os.path.exists(path):
        raw = get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}")
        open(path, "w", encoding="utf-8").write(strip(raw))
    print(t, acc, fd, rd, doc, os.path.getsize(path))
    time.sleep(0.5)
