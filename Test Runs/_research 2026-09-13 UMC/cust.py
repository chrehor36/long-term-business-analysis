import json, os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__))
os.environ["OUTDIR"] = os.path.join(HERE, "peers")
sys.path.insert(0, HERE)
import get as G
G.HERE = os.environ["OUTDIR"]
P = {"LSCC": 855658, "HIMX": 1342338, "ALGM": 866291, "SIMO": 1329394, "SITM": 1451809, "NXPI": 1413447, "TSEM": 928876, "GFS": 1709048}
for tk in sys.argv[1:] or P:
    cik = P[tk]
    sub = json.loads(G.get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    r = sub["filings"]["recent"]
    i = [k for k, fm in enumerate(r["form"]) if fm in ("10-K", "20-F")][0]
    acc, doc = r["accessionNumber"][i], r["primaryDocument"][i]
    name = f"{tk}_{r['form'][i]}_{r['reportDate'][i]}_{acc}.txt"
    fn = os.path.join(G.HERE, name)
    if not os.path.exists(fn):
        raw = G.get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}")
        open(fn, "w", encoding="utf-8").write(G.strip_html(raw.decode("utf-8", "replace")))
    t = re.sub(r"\s+", " ", open(fn, encoding="utf-8").read())
    print("=====", tk, r["form"][i], r["filingDate"][i], acc)
    for m in re.finditer(r"United Microelectronics|\bUMC\b", t):
        print("  ..", t[max(0, m.start()-350):m.start()+350])
