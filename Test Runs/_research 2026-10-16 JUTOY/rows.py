import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import fitz
f, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
d = fitz.open(f)
for pn in range(a - 1, b):
    words = d[pn].get_text("words")
    rows = {}
    for w in words:
        x0, y0, x1, y1, txt = w[:5]
        key = round((y0 + y1) / 2 / 3.0)
        rows.setdefault(key, []).append((x0, txt))
    print(f"--- page {pn+1}")
    for k in sorted(rows):
        r = sorted(rows[k])
        line = ""
        lastx = 0
        for x, t in r:
            gap = int((x - lastx) / 5)
            line += (" " * max(1, gap) if line else "") + t
            lastx = x + len(t) * 4.5
        print(line)
