# Reconstruct table rows from a PDF page by grouping words on the same y coordinate.
import sys, warnings; warnings.filterwarnings("ignore"); import fitz as pymupdf
pdf, pat = sys.argv[1], sys.argv[2]
doc = pymupdf.open(pdf)
pages = [int(p) for p in sys.argv[3].split(',')] if len(sys.argv) > 3 else None
for i, page in enumerate(doc):
    if pages is not None and (i+1) not in pages: continue
    txt = page.get_text()
    if pages is None and pat.lower() not in txt.lower(): continue
    print(f"===== page {i+1}")
    words = page.get_text("words")
    # split page into halves if two-column? keep full width
    rows = {}
    for x0,y0,x1,y1,w,b,l,n in words:
        key = round(y1/2.5)
        rows.setdefault(key, []).append((x0,w))
    for k in sorted(rows):
        print(" ".join(w for x,w in sorted(rows[k])))
