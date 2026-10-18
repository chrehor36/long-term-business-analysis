# Print PDF pages as rows rebuilt from word coordinates.
# usage: python -I pages.py file.pdf first last [find-printed]
import sys
import fitz as pymupdf
sys.stdout.reconfigure(encoding="utf-8")
pdf, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
doc = pymupdf.open(pdf)
for pno in range(a-1, min(b, doc.page_count)):
    page = doc[pno]
    words = page.get_text("words")
    rows = {}
    for w in words:
        x0,y0,x1,y1,t = w[:5]
        key = round((y0+y1)/2/3)
        rows.setdefault(key, []).append((x0,x1,t))
    print(f"===== PDF PAGE {pno+1} =====")
    for k in sorted(rows):
        ws = sorted(rows[k])
        out=""; lastx=None
        for x0,x1,t in ws:
            if lastx is None: out=t
            elif x0-lastx>8: out+=" | "+t
            else: out+=" "+t
            lastx=x1
        print(out)
