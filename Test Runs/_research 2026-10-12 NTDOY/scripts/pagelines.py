# Print PDF pages matching a phrase, words grouped into lines by y-coordinate (layout repair).
import sys, warnings
warnings.filterwarnings("ignore")
import fitz as pymupdf
pdf, phrase = sys.argv[1], sys.argv[2]
maxpages = int(sys.argv[3]) if len(sys.argv) > 3 else 2
doc = pymupdf.open(pdf)
hits = [i for i, p in enumerate(doc) if phrase.lower() in p.get_text().lower()]
start = int(sys.argv[4]) if len(sys.argv) > 4 else 0
for i in hits[start:start+maxpages]:
    p = doc[i]
    words = p.get_text("words")
    rows = {}
    for w in words:
        y = round(w[1] / 3)
        rows.setdefault(y, []).append(w)
    print(f"===== page {i+1}")
    for y in sorted(rows):
        ws = sorted(rows[y], key=lambda w: w[0])
        line = ""
        for w in ws:
            col = int(w[0] / 4.5)
            if len(line) < col: line += " " * (col - len(line))
            else: line += " "
            line += w[4]
        print(line.rstrip())
