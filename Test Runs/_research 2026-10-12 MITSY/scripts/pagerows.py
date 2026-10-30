"""Print a PDF page's words grouped into rows by vertical position (for tables whose text layer is out of order).
usage: python -I pagerows.py file.pdf page_index [page_index...]  |  python -I pagerows.py file.pdf find "text" """
import sys, warnings
warnings.filterwarnings("ignore")
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import fitz as pymupdf
doc = pymupdf.open(sys.argv[1])
if sys.argv[2] == "find":
    for i, p in enumerate(doc):
        if sys.argv[3] in p.get_text():
            print(i, end=" ")
    print(); sys.exit()
for a in sys.argv[2:]:
    p = doc[int(a)]
    words = p.get_text("words")
    rows = {}
    for w in words:
        x0, y0, x1, y1, t = w[:5]
        key = round((y0 + y1) / 2 / 3)
        rows.setdefault(key, []).append((x0, t))
    print(f"==== page {a}")
    for k in sorted(rows):
        print(" ".join(t for x, t in sorted(rows[k])))
