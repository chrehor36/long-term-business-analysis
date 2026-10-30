# Print PDF pages as rows (words grouped by y), for reading tables. Usage: rows.py file.pdf "search text" [npages] | rows.py file.pdf -p 199
import sys, warnings; warnings.filterwarnings("ignore"); import fitz as pymupdf
f = sys.argv[1]; doc = pymupdf.open(f)
def dump(pno):
    pg = doc[pno]; words = pg.get_text("words")
    rows = {}
    for w in words:
        key = round((w[1]+w[3])/2/3)
        rows.setdefault(key, []).append(w)
    print(f"---- page {pno+1}")
    for k in sorted(rows):
        ws = sorted(rows[k], key=lambda w: w[0]); line=""; last=0
        for w in ws:
            gap = int((w[0]-last)/5)
            line += (" "*max(1,min(gap,30)) if line else "") + w[4]; last = w[2]
        print(line)
if sys.argv[2] == "-p":
    for p in sys.argv[3].split(","): dump(int(p)-1)
else:
    n = int(sys.argv[3]) if len(sys.argv)>3 else 1
    hits=[i for i in range(len(doc)) if sys.argv[2].lower() in doc[i].get_text().lower()]
    print("hits", [h+1 for h in hits])
