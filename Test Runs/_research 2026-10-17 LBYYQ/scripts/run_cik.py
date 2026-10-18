"""Drive tools/run.py with CIK 902274 (Libbey Inc.), since LBYYQ is gone from the SEC ticker map.
Arithmetic lines only are read from its output (Part VII)."""
import sys, os
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "tools")); sys.path.insert(0, os.path.join(ROOT, "Screens"))
os.chdir(ROOT)
import sources as S
import run as R
S.cik_for = lambda t: ("0000902274", "LIBBEY INC")
_price = S.price
def price(t):
    try:
        return _price(t)
    except Exception as e:
        print("price fetch failed:", e, "-> PLACEHOLDER price 1.00 so the filed-figure arithmetic prints; every price-based line below is void"); return (1.0, "PLACEHOLDER", "USD")
S.price = price
sys.argv = ["run.py"] + sys.argv[1:]
sys.exit(R.main())
