import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import get as G
HERE = os.path.dirname(os.path.abspath(__file__))
rows = [l.rstrip("\n").split("\t") for l in open(os.path.join(HERE, "filings_list.txt"))]
for fd, form, acc, doc, desc, rd in rows:
    if form in ("20-F",):
        out = f"20F_FY{rd[:4]}"
    elif form in ("6-K",):
        out = f"k/6K_{fd}_{acc[-6:]}_{os.path.splitext(doc)[0][:40]}"
    elif form in ("424B4", "424B7", "F-3ASR"):
        out = f"k/{form}_{fd}_{acc[-6:]}"
    else:
        continue
    p = os.path.join(HERE, out + ".txt")
    if os.path.exists(p):
        continue
    url = f"https://www.sec.gov/Archives/edgar/data/{G.CIK}/{acc.replace('-', '')}/{doc}"
    raw = G.get(url)
    txt = G.strip_html(raw.decode("utf-8", "replace"))
    open(p, "w", encoding="utf-8").write(txt)
    print(out, len(txt))
