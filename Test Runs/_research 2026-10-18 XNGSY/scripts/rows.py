# Reconstruct table rows from a PDF page by word y-position (PyMuPDF via fitz).
# usage: python -I rows.py file.pdf page1 [page2 ...]   (1-based pages)
import sys, warnings
warnings.filterwarnings("ignore")
import fitz
d = fitz.open(sys.argv[1])
for a in sys.argv[2:]:
    pn = int(a) - 1
    p = d[pn]
    words = p.get_text("words")
    rows = {}
    for w in words:
        y = round((w[1] + w[3]) / 2 / 4)
        rows.setdefault(y, []).append(w)
    print("===== PAGE", a)
    for y in sorted(rows):
        ws = sorted(rows[y], key=lambda w: w[0])
        print(" ".join(w[4] for w in ws))
