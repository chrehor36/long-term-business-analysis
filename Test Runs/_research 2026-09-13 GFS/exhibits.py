import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import get as G
HERE = os.path.dirname(os.path.abspath(__file__))
rows = [l.rstrip("\n").split("\t") for l in open(os.path.join(HERE, "filings_list.txt"))]
for fd, form, acc, doc, desc, rd in rows:
    if form != "6-K":
        continue
    base = f"https://www.sec.gov/Archives/edgar/data/{G.CIK}/{acc.replace('-', '')}/"
    try:
        d = json.loads(G.get(base + "index.json"))
    except SystemExit as e:
        print("ERR", acc, e); continue
    for it in d["directory"]["item"]:
        n = it["name"]
        if n == doc or not n.lower().endswith((".htm", ".html")) or "index" in n.lower():
            continue
        out = os.path.join(HERE, "k", f"EX_{fd}_{acc[-6:]}_{os.path.splitext(n)[0][:50]}.txt")
        if os.path.exists(out):
            continue
        raw = G.get(base + n)
        txt = G.strip_html(raw.decode("utf-8", "replace"))
        open(out, "w", encoding="utf-8").write(txt)
        print(os.path.basename(out), len(txt))
