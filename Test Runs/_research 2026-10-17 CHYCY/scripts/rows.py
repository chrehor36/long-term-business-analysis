# Print PDF page text grouped into rows by y-coordinate (words sorted by x).
import sys, warnings; warnings.filterwarnings("ignore"); import fitz as pymupdf
path = sys.argv[1]; pages = [int(p) for p in sys.argv[2].split(",")] if len(sys.argv) > 2 else None
doc = pymupdf.open(path)
for pno in (pages or range(len(doc))):
    pg = doc[pno - 1] if pages else doc[pno]
    words = pg.get_text("words")
    rows = {}
    for w in words:
        y = round((w[1] + w[3]) / 2 / 3)  # 3pt bins
        rows.setdefault(y, []).append(w)
    print(f"===== page {pno}")
    for y in sorted(rows):
        ws = sorted(rows[y], key=lambda w: w[0])
        print(" ".join(w[4] for w in ws))
