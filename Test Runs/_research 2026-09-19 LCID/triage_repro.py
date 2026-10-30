# LCID run 2026-09-19: which bound of the triage sanity guard (yield outside -100%..+50%, or cap < $5M)
# tripped for LCID? Reproduced on facts filed by 2026-09-01 with the a8bc84f functions. The watchlist
# pricing script itself was never committed (HBB run), so its exact inputs are reconstructed, not read.
import sys, os, json, copy
from datetime import date
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here); sys.path.insert(0, os.path.join(here, "..", "..", "Screens")); sys.path.insert(0, os.path.join(here, "..", "..", "Backtests", "scripts"))
import floor_screen_a8bc84f as O
import bt17_microcap as B
facts = json.load(open(os.path.join(here, "companyfacts.json")))
def cut(f, before):
    g = copy.deepcopy(f)
    for ns in g["facts"].values():
        for t in ns.values():
            for u, L in t["units"].items():
                t["units"][u] = [x for x in L if x.get("filed", "9999") <= before]
    return g
f0 = cut(facts, "2026-09-01"); O.TODAY = date(2026, 9, 1)
oe = O.owner_earnings(f0); print("a8bc84f owner_earnings:", oe)
so = O.shares_outstanding(f0); print("a8bc84f shares_outstanding:", so)
print("a8bc84f share_count_shift:", O.share_count_shift(f0))
sa = B.shares_asof(f0, date(2026, 9, 1)); print("bt17 shares_asof(2026-09-01):", sa)
closes = {"2026-08-31": 4.85, "2026-09-01": 4.55}
counts = {"cover 394,070,176 (post-split, 2026-07-29)": so[1],
          "stale pre-split dei 3,072,494,911 (2025-07-30)": 3072494911.0}
for cl, px in closes.items():
    for cn, n in counts.items():
        cap = px * n
        ys = {k: v / cap for k, v in oe.items()}
        flag = [k for k, y in ys.items() if y < -1.0 or y > 0.5]
        print(f"{cl} ${px} x {cn}: cap ${cap/1e6:,.1f}M;", ", ".join(f"{k} {y:.1%}" for k, y in ys.items()),
              "| guard fires on:", flag or "none", "| cap<$5M:", cap < 5e6)
# the cap at which the yield would sit exactly at -100%
for k, v in oe.items(): print(k, "needs cap above", f"${-v/1e6:,.1f}M", "to clear -100%, i.e. price above", f"${-v/so[1]:.2f}")
