"""Print a PDF page as rows of words grouped by y position (arithmetic aid, no judgment)."""
import sys
import pymupdf
doc = pymupdf.open(sys.argv[1])
pages = [int(p) for p in sys.argv[2].split(",")] if len(sys.argv) > 2 else range(len(doc))
tol = float(sys.argv[3]) if len(sys.argv) > 3 else 3.0
for pn in pages:
    words = doc[pn].get_text("words")
    words.sort(key=lambda w: (round(w[1]), w[0]))
    rows = []
    for w in words:
        yc = (w[1] + w[3]) / 2
        for r in rows:
            if abs(r[0] - yc) <= tol:
                r[1].append(w); break
        else:
            rows.append([yc, [w]])
    rows.sort(key=lambda r: r[0])
    print(f"=== page {pn}")
    for yc, ws in rows:
        ws.sort(key=lambda w: w[0])
        print(" | ".join(w[4] for w in ws))
