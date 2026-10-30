# Print PDF pages with words grouped into visual lines (by y), to fix pdftotext column drift.
# usage: python -I pages.py file.pdf "search text" [maxpages]   or   python -I pages.py file.pdf -p 90-92
import sys, warnings
warnings.filterwarnings("ignore")
import fitz as pymupdf
f = sys.argv[1]
doc = pymupdf.open(f)
def dump(i):
    words = doc[i].get_text("words")
    lines = {}
    for w in words:
        y = round((w[1] + w[3]) / 2 / 3)  # 3pt buckets
        lines.setdefault(y, []).append(w)
    out = []
    for y in sorted(lines):
        ws = sorted(lines[y], key=lambda w: w[0])
        out.append(" ".join(w[4] for w in ws))
    return "\n".join(out)
if sys.argv[2] == "-p":
    a, b = sys.argv[3].split("-")
    for i in range(int(a) - 1, int(b)):
        print(f"===== page {i+1} =====")
        print(dump(i))
else:
    q = sys.argv[2].lower(); mx = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    n = 0
    for i in range(len(doc)):
        if q in doc[i].get_text().lower():
            print(f"===== page {i+1} =====")
            print(dump(i)); n += 1
            if n >= mx: break
