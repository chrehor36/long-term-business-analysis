import sys
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
from sources import fts_count

CIKS = {"EQH": "0001333986", "LNC": "0000059558", "JXN": "0001822993", "KKR": "0001404912"}
PHRASES = ["net investment spread", "cost of funds", "base net investment spread", "net investment earned rate"]
for t, c in CIKS.items():
    for p in PHRASES:
        for forms in ("10-K", "8-K"):
            try:
                n, u = fts_count(p, cik=c, forms=forms)
            except Exception as e:
                n, u = "ERR " + str(e)[:80], ""
            print(t, forms, repr(p), n)
