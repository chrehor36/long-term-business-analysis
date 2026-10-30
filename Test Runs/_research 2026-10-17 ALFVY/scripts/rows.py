# Print a PDF page's words grouped into rows by y coordinate (for tables).
import sys, site; sys.path.append(site.getusersitepackages())
sys.stdout.reconfigure(encoding="utf-8")
# usage: python -I rows.py file.pdf page_from page_to [xmin xmax]
import sys, fitz as pymupdf
f, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
xmin = float(sys.argv[4]) if len(sys.argv) > 4 else -1
xmax = float(sys.argv[5]) if len(sys.argv) > 5 else 1e9
doc = pymupdf.open(f)
for p in range(a, b + 1):
    pg = doc[p - 1]
    print(f"===== page {p} (w={pg.rect.width:.0f})")
    words = [w for w in pg.get_text("words") if xmin <= w[0] <= xmax]
    rows = {}
    for w in words:
        y = round((w[1] + w[3]) / 2 / 2.5)
        rows.setdefault(y, []).append(w)
    for y in sorted(rows):
        ws = sorted(rows[y], key=lambda w: w[0])
        print(" | ".join(w[4] for w in ws))
