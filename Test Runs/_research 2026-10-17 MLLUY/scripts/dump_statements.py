"""Dump the consolidated balance sheet, income statement and cash flow statement pages of each
annual report as y-reconstructed rows, into cache/stmts_<year>.txt. Arithmetic aid only.
usage: python -I dump_statements.py <cache_dir>"""
import sys, os, re
sys.path.append(r"C:\Users\chreh\AppData\Roaming\Python\Python311\site-packages")
import warnings
warnings.filterwarnings("ignore")
import fitz

cache = sys.argv[1]
HEADS = ["consolidated balance sheet", "consolidated income statement",
         "consolidated cash flow statement"]


def rows(page):
    lines = {}
    for w in page.get_text("words"):
        y = round((w[1] + w[3]) / 2 / 3)
        lines.setdefault(y, []).append(w)
    return [" ".join(w[4] for w in sorted(lines[y], key=lambda w: w[0])) for y in sorted(lines)]


for fn in sorted(os.listdir(cache)):
    m = re.match(r"AR(\d{4})\.pdf$", fn)
    if not m:
        continue
    doc = fitz.open(os.path.join(cache, fn))
    out = []
    for i in range(len(doc)):
        r = rows(doc[i])
        head = " ".join(r[:8]).lower()
        if any(h in head for h in HEADS) and "rmb" in head and i > 100:
            out.append(f"=== page {i+1}")
            out.extend(r)
    with open(os.path.join(cache, f"stmts_{m.group(1)}.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    print(fn, sum(1 for x in out if x.startswith("=== page")), "pages")
