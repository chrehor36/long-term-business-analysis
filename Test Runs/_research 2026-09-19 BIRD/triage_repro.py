# BIRD run 2026-09-19: which bound of the triage sanity guard (yield outside -100%..+50%, or cap < $5M)
# tripped for BIRD? Reproduced on facts filed by 2026-09-01 with the a8bc84f functions and bt17 shares_asof,
# under every denominator a reader could have used. The watchlist pricing script itself was never committed
# (HBB run), so its exact inputs are reconstructed, not read.
import sys, os, json, copy
from datetime import date
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here); sys.path.insert(0, os.path.join(here, "..", "..", "Screens")); sys.path.insert(0, os.path.join(here, "..", "..", "Backtests", "scripts")); sys.path.insert(0, os.path.join(here, "..", "..", "tools"))
import floor_screen_a8bc84f as O
import bt17_microcap as B
import sources
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
print("a8bc84f shares_outstanding (550-day staleness test):", O.shares_outstanding(f0))
print("a8bc84f shares_outstanding with no staleness (today=2022-01-01):", O.shares_outstanding(f0, today=date(2022, 1, 1)))
print("a8bc84f share_count_shift:", O.share_count_shift(f0))
sa = B.shares_asof(f0, date(2026, 9, 1)); print("bt17 shares_asof(2026-09-01):", sa)
sf = sources.split_factor_after("BIRD", "2021-09-30"); print("split factor after 2021-09-30 (house rule):", sf)
closes = {"2026-08-31": 2.455, "2026-09-01": 2.35}
counts = {"stale pre-IPO us-gaap 56,508,441 (2021-09-30), raw": 56508441.0,
          "same, x split factor after measurement (bt17 house rule)": 56508441.0 * sf,
          "cover A+B 9,315,794 + 2,493,399 (2026-08-10)": 9315794.0 + 2493399.0,
          "cover Class A only 9,315,794": 9315794.0,
          "Q2 2026 weighted average 9,164,890": 9164890.0,
          "FY2023 weighted average as first filed, pre-split 151,672,437": 151672437.0}
for cl, px in closes.items():
    for cn, n in counts.items():
        cap = px * n
        ys = {k: v / cap for k, v in oe.items()}
        flag = [k for k, y in ys.items() if y < -1.0 or y > 0.5]
        print(f"{cl} ${px} x {cn}: cap ${cap/1e6:,.2f}M;", ", ".join(f"{k} {y:.1%}" for k, y in ys.items()),
              "| guard fires on:", flag or "none", "| cap<$5M:", cap < 5e6)
