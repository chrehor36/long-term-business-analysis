# Reproduce the 2026-09-01 watchlist triage guard ORDER (Screens/new_candidates.py at ce98258/a8bc84f:
# share_count_shift 0.75-1.50 -> scale_shift > 2.0 -> filed_years < 5 -> CAPEX_UNRESOLVED) with the
# floor_screen functions as they stood at a8bc84f, on facts filed by 2026-09-01.
import json, sys, os, copy
from datetime import date
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, r"C:/Users/chreh/OneDrive/Documents/BRK/Backtests/scripts"); sys.path.insert(0, r"C:/Users/chreh/OneDrive/Documents/BRK/Screens")
import floor_screen_a8bc84f as O
f = json.load(open(os.path.join(HERE, "companyfacts.json")))
def cut(facts, before):
    g = copy.deepcopy(facts)
    for ns in g["facts"].values():
        for t in ns.values():
            for u, L in t["units"].items():
                t["units"][u] = [x for x in L if x.get("filed", "9999") <= before]
    return g
f0 = cut(f, "2026-09-01")
O.TODAY = date(2026, 9, 1)
r = O.share_count_shift(f0); print("1 share_count_shift", r, "-> fires" if r is not None and not (0.75 <= r <= 1.50) else "-> passes (0.75-1.50)")
s = O.scale_shift(f0); print("2 scale_shift", s, "-> FIRES (> 2.0): 'perimeter by revenue step'" if s and s > 2.0 else "-> passes")
rev = O.annual(f0, O.REV_TAGS); ends = sorted(rev)[-6:]
for a, b in zip(ends, ends[1:]): print("   ", a, rev[a]/1e6, "->", b, rev[b]/1e6, round(rev[b]/rev[a], 4))
print("3 filed_years", O.filed_years(f0))
print("4 owner_earnings", O.owner_earnings(f0))
print("  restatement_shift (not a guard in that pipeline)", O.restatement_shift(f0))
# what restatement_shift sees, element by element
ns = f0["facts"]["us-gaap"]
for tag in O.REV_TAGS:
    print("  rev tag", tag, "annual obs:", len([x for x in ns.get(tag, {}).get("units", {}).get("USD", []) if x.get("form") in ("10-K","10-K/A")]))
