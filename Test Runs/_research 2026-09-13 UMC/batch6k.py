import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
os.environ["OUTDIR"] = os.path.join(HERE, "k")
sys.path.insert(0, HERE)
import get as G
G.HERE = os.environ["OUTDIR"]
import json
rows = [l.rstrip("\n").split("\t") for l in open(os.path.join(HERE, "filings_list.txt"))]
for fd, form, acc, doc, rd, desc in rows:
    if form != "6-K" or fd < "2023-01-01":
        continue
    base = f"https://www.sec.gov/Archives/edgar/data/1033767/{acc.replace('-', '')}/"
    prefix = fd + "_" + acc[-6:]
    if any(f.startswith(prefix) for f in os.listdir(G.HERE)):
        continue
    try:
        d = json.loads(G.get(base + "index.json"))
    except SystemExit:
        continue
    for it in d["directory"]["item"]:
        n = it["name"]
        if n.lower().endswith((".htm", ".html", ".txt")) and "index" not in n and not n.startswith(acc):
            G.save_txt(f"{prefix}__{os.path.splitext(n)[0]}.txt", G.get(base + n))
