"""Wrapper: tools/run.py with the ticker resolved to CIK 1720990 (Fisker Inc.), because the SEC
ticker list no longer carries FSRDQ. Arithmetic only; nothing it prints as a rule is used."""
import sys, os
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "tools")); sys.path.insert(0, os.path.join(ROOT, "Screens"))
import sources as S
S.cik_for = lambda t: ("0001720990", "Fisker Inc.")
_price = S.price
def price(t):
    try:
        return _price(t)
    except Exception as e:
        print(f"[wrapper] no price for {t}: {e!r}; using 0.01 placeholder (NOT A QUOTE)")
        return 0.01, "n/a", "USD"
S.price = price
import run
sys.argv = ["run.py", "FSRDQ"] + sys.argv[1:]
run.main()
