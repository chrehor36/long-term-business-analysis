import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import fitz as pymupdf
# usage: half.py file.pdf pageno(1-based) L|R|A [find-text]
f, pn, side = sys.argv[1], int(sys.argv[2]), sys.argv[3]
doc = pymupdf.open(f)
pg = doc[pn-1]
W = pg.rect.width
x0, x1 = {'L': (0, W/2), 'R': (W/2, W), 'A': (0, W)}[side]
words = [w for w in pg.get_text("words") if w[0] >= x0 - 1 and w[2] <= x1 + 1]
rows = {}
for w in words:
    key = round((w[1] + w[3]) / 2 / 3)  # 3pt buckets
    rows.setdefault(key, []).append(w)
for k in sorted(rows):
    ws = sorted(rows[k], key=lambda w: w[0])
    line = ""
    for w in ws:
        col = int((w[0] - x0) / 4)
        if len(line) < col: line += " " * (col - len(line))
        else: line += " "
        line += w[4]
    print(line.rstrip())
