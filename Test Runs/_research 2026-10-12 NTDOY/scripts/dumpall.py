# Dump every page of a PDF with words grouped into lines (layout repair); output path = arg2.
import sys, warnings
warnings.filterwarnings("ignore")
import fitz
doc = fitz.open(sys.argv[1]); out = open(sys.argv[2], "w", encoding="utf-8")
for i, p in enumerate(doc):
    rows = {}
    for w in p.get_text("words"):
        rows.setdefault(round(w[1] / 3), []).append(w)
    out.write(f"===== page {i+1}\n")
    for y in sorted(rows):
        line = ""
        for w in sorted(rows[y], key=lambda w: w[0]):
            col = int(w[0] / 4.5)
            line += (" " * (col - len(line))) if len(line) < col else " "
            line += w[4]
        out.write(line.rstrip() + "\n")
