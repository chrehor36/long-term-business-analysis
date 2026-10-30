# Dump the consolidated cash-flow statement pages (first page found plus the next two) as rows.
import sys, warnings
warnings.filterwarnings("ignore")
import fitz
d = fitz.open(sys.argv[1])
def rows(p):
    words = p.get_text("words"); r = {}
    for w in words:
        y = round((w[1] + w[3]) / 2 / 4); r.setdefault(y, []).append(w)
    return [" ".join(w[4] for w in sorted(r[y], key=lambda w: w[0])) for y in sorted(r)]
for i in range(60, d.page_count):
    t = " ".join(d[i].get_text().split()[:40]).upper()
    if "CONSOLIDATED STATEMENT OF CASH FLOWS" in t:
        for j in range(i, i + 3):
            print("===== PAGE", j + 1); print("\n".join(rows(d[j])))
        break
