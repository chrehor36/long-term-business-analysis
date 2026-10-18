"""Print PDF pages as rows reconstructed by y-coordinate (PyMuPDF words).
usage: python -I pagerows.py file.pdf "search phrase" [maxpages]
       python -I pagerows.py file.pdf --pages 165,166"""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.append(r"C:\Users\chreh\AppData\Roaming\Python\Python311\site-packages")
import warnings
warnings.filterwarnings("ignore")
import fitz as pymupdf

f = sys.argv[1]
doc = pymupdf.open(f)


def rows(p):
    words = doc[p].get_text("words")
    lines = {}
    for w in words:
        y = round((w[1] + w[3]) / 2 / 3)  # bucket of 3pt
        lines.setdefault(y, []).append(w)
    out = []
    for y in sorted(lines):
        ws = sorted(lines[y], key=lambda w: w[0])
        out.append(" ".join(w[4] for w in ws))
    return out


if sys.argv[2] == "--pages":
    pages = [int(x) - 1 for x in sys.argv[3].split(",")]
else:
    phrase = sys.argv[2].lower()
    mx = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    pages = [i for i in range(len(doc)) if phrase in doc[i].get_text().lower()][:mx]
for p in pages:
    print(f"=== page {p+1}")
    print("\n".join(rows(p)))
