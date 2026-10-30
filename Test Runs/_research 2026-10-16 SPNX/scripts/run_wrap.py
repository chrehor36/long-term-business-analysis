# Wrapper: tools/run.py with the ticker map bypassed (SPNX is not in the SEC ticker map
# after the Form 15). Same arithmetic, CIK supplied by hand: 0000886835.
import sys, os
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "tools"))
import sources as S
S.cik_for = lambda t: ("0000886835", "SUPERIOR ENERGY SERVICES INC")
_price = S.price
def price(t):
    try:
        return _price(t)
    except Exception as e:
        print("price fetch failed:", e)
        return (80.0, "placeholder-2025-01-29-cashout", "USD")
S.price = price
import run
sys.argv = ["run.py", "SPNX"] + sys.argv[1:]
run.main()
