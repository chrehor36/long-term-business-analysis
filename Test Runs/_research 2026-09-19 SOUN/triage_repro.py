# SOUN run 2026-09-19: which bound of the triage sanity guard (yield outside -100%..+50%, or cap < $5M)
# tripped for SOUN? Reproduced on facts filed by 2026-09-01 with the a8bc84f functions and bt17 shares_asof.
# The watchlist pricing script itself was never committed (HBB run), so its exact inputs are reconstructed, not read.
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
print("a8bc84f shares_outstanding (550-day staleness test):", O.shares_outstanding(f0))
print("a8bc84f shares_outstanding with no staleness (today=2022-06-01):", O.shares_outstanding(f0, today=date(2022, 6, 1)))
print("a8bc84f share_count_shift:", O.share_count_shift(f0))
sa = B.shares_asof(f0, date(2026, 9, 1)); print("bt17 shares_asof(2026-09-01):", sa)
closes = {"2026-08-31": 7.16, "2026-09-01": 6.85}
counts = {"stale SPAC-shell dei 17,461,000 (2022-03-09)": 17461000.0,
          "cover A+B 411,574,436 + 32,535,408 (2026-08-06)": 411574436.0 + 32535408.0,
          "cover Class A only 411,574,436": 411574436.0}
for cl, px in closes.items():
    for cn, n in counts.items():
        cap = px * n
        ys = {k: v / cap for k, v in oe.items()}
        flag = [k for k, y in ys.items() if y < -1.0 or y > 0.5]
        print(f"{cl} ${px} x {cn}: cap ${cap/1e6:,.1f}M;", ", ".join(f"{k} {y:.1%}" for k, y in ys.items()),
              "| guard fires on:", flag or "none", "| cap<$5M:", cap < 5e6)
