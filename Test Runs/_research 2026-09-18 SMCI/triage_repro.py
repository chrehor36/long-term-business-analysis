# Reproduce what the 2026-09-01 triage (floor_screen at a8bc84f) saw, on facts filed by then.
import json, sys, os
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r"C:/Users/chreh/OneDrive/Documents/BRK/Backtests/scripts"); sys.path.insert(0, r"C:/Users/chreh/OneDrive/Documents/BRK/Screens")
import floor_screen_a8bc84f as O
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\Screens")
import floor_screen as N
f = json.load(open("companyfacts.json"))
def cut(facts, before):
    import copy
    g = copy.deepcopy(facts)
    for ns in g["facts"].values():
        for t in ns.values():
            for u, L in t["units"].items():
                t["units"][u] = [x for x in L if x.get("filed", "9999") <= before]
    return g
f0 = cut(f, "2026-09-01")
O.TODAY = date(2026, 9, 1)
print("a8bc84f share_count_shift", O.share_count_shift(f0))
print("a8bc84f scale_shift", O.scale_shift(f0))
print("a8bc84f restatement_shift", O.restatement_shift(f0))
print("a8bc84f owner_earnings", O.owner_earnings(f0))
print("current share_count_shift with ticker", N.share_count_shift(f, "SMCI"))
print("current share_count_shift no ticker", N.share_count_shift(f))
dei = f["facts"]["dei"]["EntityCommonStockSharesOutstanding"]["units"]["shares"]
for x in dei[-12:]: print(x["end"], x["val"], x["form"], x["filed"])
rev = N.annual(f, N.REV_TAGS)
for k in sorted(rev)[-8:]: print(k, rev[k])
