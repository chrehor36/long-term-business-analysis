"""Print a PDF page's words regrouped into rows by vertical position (for reading filed tables).
Usage: python -I pagerows.py PDF "search text" [occurrence] [xsplit]
Finds the page containing the search text (the nth occurrence, default last), prints each row,
optionally splitting the page into a left and a right column at xsplit points. Arithmetic aid only."""
import sys
import pymupdf

pdf, needle = sys.argv[1], sys.argv[2]
occ = int(sys.argv[3]) if len(sys.argv) > 3 else -1
xsplit = float(sys.argv[4]) if len(sys.argv) > 4 else None
doc = pymupdf.open(pdf)
hits = ([int(needle[1:])] if needle.startswith("#") else
        [i for i, p in enumerate(doc) if needle in p.get_text()])
if not hits:
    sys.exit("not found")
pno = hits[occ]
page = doc[pno]
print(f"# page index {pno} (printed page {pno + 1}); hits {hits}")
words = page.get_text("words")
cols = [("ALL", words)] if xsplit is None else [
    ("LEFT", [w for w in words if w[0] < xsplit]), ("RIGHT", [w for w in words if w[0] >= xsplit])]
for name, ws in cols:
    print(f"## {name}")
    rows = {}
    for w in ws:
        key = round(w[1] / 3)
        rows.setdefault(key, []).append(w)
    for key in sorted(rows):
        r = sorted(rows[key], key=lambda w: w[0])
        print(" ".join(w[4].replace("–", "-").replace("−", "-") for w in r))
