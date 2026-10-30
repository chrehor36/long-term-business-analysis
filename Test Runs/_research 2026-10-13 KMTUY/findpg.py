"""List PDF page indexes containing a phrase (navigation aid)."""
import sys, pymupdf
doc = pymupdf.open(sys.argv[1])
for i, p in enumerate(doc):
    t = p.get_text()
    if sys.argv[2].lower() in t.lower():
        print(i, t.strip().split("\n")[0][:80])
