"""Dump PDF page text as rows (grouped by y), words ordered by x. Usage: dumprows.py file.pdf keyword [maxpages]"""
import sys, fitz
from collections import defaultdict
f, kw = sys.argv[1], sys.argv[2]
maxp = int(sys.argv[3]) if len(sys.argv) > 3 else 3
doc = fitz.open(f)
n = 0
for i, p in enumerate(doc):
    if kw not in p.get_text():
        continue
    n += 1
    print(f"===== page {i}")
    rows = defaultdict(list)
    for w in p.get_text("words"):
        rows[round((w[1] + w[3]) / 2 / 4)].append(w)
    for k in sorted(rows):
        r = sorted(rows[k], key=lambda w: w[0])
        out, last = "", None
        for w in r:
            if last is not None and w[0] - last > 15:
                out += " | "
            elif last is not None:
                out += " "
            out += w[4]
            last = w[2]
        print(out)
    if n >= maxp:
        break
