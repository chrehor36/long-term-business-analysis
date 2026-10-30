# Locate the consolidated primary statements in an annual report and dump them as rows.
import sys, warnings
warnings.filterwarnings("ignore")
import fitz
f = sys.argv[1]
d = fitz.open(f)
keys = ["CONSOLIDATED STATEMENT OF PROFIT OR LOSS", "CONSOLIDATED STATEMENT OF FINANCIAL POSITION", "CONSOLIDATED STATEMENT OF CASH FLOWS"]
def rows(p):
    words = p.get_text("words"); r = {}
    for w in words:
        y = round((w[1] + w[3]) / 2 / 4); r.setdefault(y, []).append(w)
    return [" ".join(w[4] for w in sorted(r[y], key=lambda w: w[0])) for y in sorted(r)]
for i in range(60, d.page_count):
    t = d[i].get_text()
    head = " ".join(t.split()[:40]).upper()
    if any(k in head for k in keys) and "NOTES TO" not in head[:60]:
        print("===== PAGE", i + 1)
        print("\n".join(rows(d[i])))
