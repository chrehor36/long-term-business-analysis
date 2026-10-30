# Print a PDF page as rows rebuilt from word positions: python pagerows.py file.pdf "search text" [nth] [pages]
import site, sys as _s; _s.path.append(site.getusersitepackages())
import sys, warnings; warnings.filterwarnings("ignore"); import fitz as pymupdf
f, key = sys.argv[1], sys.argv[2]
nth = int(sys.argv[3]) if len(sys.argv) > 3 else 1
npages = int(sys.argv[4]) if len(sys.argv) > 4 else 1
doc = pymupdf.open(f)
hits = [i for i, p in enumerate(doc) if key in p.get_text()]
if len(hits) < nth:
    print("hits", hits); sys.exit()
for pi in range(hits[nth-1], min(hits[nth-1]+npages, len(doc))):
    words = doc[pi].get_text("words")
    rows = {}
    for w in words:
        y = round((w[1]+w[3])/2/3)
        rows.setdefault(y, []).append(w)
    print(f"===== page {pi+1}")
    for y in sorted(rows):
        ws = sorted(rows[y], key=lambda w: w[0])
        line = ""
        for w in ws:
            col = int(w[0]/4.5)
            if len(line) < col: line += " "*(col-len(line))
            else: line += " "
            line += w[4]
        print(line.encode("ascii","replace").decode())
