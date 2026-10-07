# usage: python pdfpages.py file.pdf "regex" [maxhits]  -> lists page numbers whose text matches;
#        python pdfpages.py file.pdf --page N [--blocks]  -> prints page N text (1-based), sorted by position
import sys, re
import pymupdf
sys.stdout.reconfigure(encoding="utf-8")
doc = pymupdf.open(sys.argv[1])
if sys.argv[2] == "--page":
    for n in sys.argv[3].split(","):
        p = doc[int(n) - 1]
        print("=== page", n)
        if "--words" in sys.argv:
            # rebuild lines by y coordinate
            words = p.get_text("words")
            rows = {}
            for w in words:
                key = round(w[1] / 3)
                rows.setdefault(key, []).append(w)
            for k in sorted(rows):
                ws = sorted(rows[k], key=lambda w: w[0])
                print(" ".join(w[4] for w in ws))
        else:
            print(p.get_text("text", sort=True))
else:
    pat = re.compile(sys.argv[2], re.I)
    mx = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    hits = 0
    for i, p in enumerate(doc):
        t = p.get_text()
        if pat.search(t):
            m = pat.search(t)
            print(i + 1, "|", t[max(0, m.start() - 80):m.end() + 80].replace("\n", " "))
            hits += 1
            if hits >= mx:
                break
