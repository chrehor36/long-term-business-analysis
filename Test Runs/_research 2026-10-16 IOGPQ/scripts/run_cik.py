# Wrapper: tools/run.py cannot resolve the delisted ticker IOGPQ; route it to CIK 866609.
import sys, os
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources as S
_orig = S.cik_for
def cik_for(t):
    if t.upper() == "IOGPQ":
        return "0000866609", "ION Geophysical Corp"
    return _orig(t)
S.cik_for = cik_for
# no quote resolves for IOGPQ (Yahoo 404); price set to NaN so only the filed arithmetic prints
_op = S.price
def price(t):
    try:
        return _op(t)
    except Exception:
        return float("nan"), "NO QUOTE", "USD"
S.price = price
import run
sys.argv = ["run.py", "IOGPQ"] + sys.argv[1:]
run.main() if hasattr(run, "main") else None
