import sys
import fitz as pymupdf
for f in sys.argv[1:]:
    d = pymupdf.open(f)
    hits = {}
    for i, p in enumerate(d):
        t = p.get_text().upper()
        for key in ("CONSOLIDATED STATEMENT OF PROFIT OR LOSS", "CONSOLIDATED STATEMENT OF FINANCIAL POSITION", "CONSOLIDATED STATEMENT OF CASH FLOWS", "CONSOLIDATED STATEMENT OF COMPREHENSIVE INCOME", "CONSOLIDATED INCOME STATEMENT", "CONSOLIDATED BALANCE SHEET"):
            if key in t[:400]:
                hits.setdefault(key, []).append(i + 1)
    print(f, {k: v[:3] for k, v in hits.items()})
