# print one page of a PDF as text lines rebuilt from words (y-sorted), optional x-range
import sys, pymupdf
f, p = sys.argv[1], int(sys.argv[2])
x0 = float(sys.argv[3]) if len(sys.argv) > 3 else 0
x1 = float(sys.argv[4]) if len(sys.argv) > 4 else 1e9
doc = pymupdf.open(f); pg = doc[p-1]
words = [w for w in pg.get_text("words") if x0 <= w[0] < x1]
lines = {}
for w in words:
    key = round(w[1]/3)
    lines.setdefault(key, []).append(w)
for k in sorted(lines):
    ws = sorted(lines[k], key=lambda w: w[0])
    out = ""; 
    for w in ws:
        col = int(w[0]/4.5)
        if len(out) < col: out += " "*(col-len(out))
        else: out += " "
        out += w[4]
    print(out.rstrip())
