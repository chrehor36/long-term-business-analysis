"""Fetch the latest annual report (10-K or 20-F) of TSMC customers and foundry competitors, stripped to text,
into peers/. Also saves companyfacts for the foundry peers. Transcription only."""
import json, os, sys, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.environ["OUTDIR"] = os.path.join(HERE, "peers")
os.makedirs(os.environ["OUTDIR"], exist_ok=True)
import importlib, get as G
importlib.reload(G)
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
PEERS = {"NVDA": 1045810, "QCOM": 804328, "AVGO": 1730168, "AAPL": 320193, "UMC": 1033767, "GFS": 1709048,
         "INTC": 50863, "AMD": 2488}
which = sys.argv[1:] or list(PEERS)
for tk in which:
    cik = PEERS[tk]
    sub = json.loads(G.get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    r = sub["filings"]["recent"]
    hits = [i for i, fm in enumerate(r["form"]) if fm in ("10-K", "20-F")]
    for n, i in enumerate(hits[:2]):
        acc = r["accessionNumber"][i]; doc = r["primaryDocument"][i]
        url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{doc}"
        name = f"{tk}_{r['form'][i]}_{r['reportDate'][i]}_{acc}"
        out = os.path.join(os.environ["OUTDIR"], name + ".txt")
        if not os.path.exists(out):
            raw = G.get(url)
            txt = G.strip_html(raw.decode("utf-8", "replace"))
            open(out, "w", encoding="utf-8").write(txt)
        print(tk, r["form"][i], r["filingDate"][i], r["reportDate"][i], acc, doc)
    if tk in ("UMC", "GFS", "INTC"):
        cf = os.path.join(os.environ["OUTDIR"], f"{tk}_companyfacts.json")
        if not os.path.exists(cf):
            open(cf, "wb").write(G.get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"))
