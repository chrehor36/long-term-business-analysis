"""Competitor row: operating margin by fiscal year 2017-2025 and aggregate, from companyfacts (10-K, latest vintage)."""
import sys, os
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from facts import series
REV = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet", "RevenueFromContractWithCustomerIncludingAssessedTax"]
def fy(k): return int(k[:4]) - (1 if k[5:7] == "01" else 0)
def get(t, tags):
    out = {}
    for tag in tags:
        for k, v in series(t, tag).items():
            if k[5:7] in ("12", "09", "10", "01"):
                out.setdefault(fy(k), (v[0] / 1e6, v[2]))
    return out
rows = {}
for t in ["FLR", "KBR", "J", "ACM"]:
    r = get(t, REV); o = get(t, ["OperatingIncomeLoss"])
    rows[t] = {y: (r[y][0], o[y][0], o[y][1]) for y in range(2017, 2026) if y in r and y in o}
print("FY   " + "  ".join(f"{t:>7}" for t in rows))
for y in range(2017, 2026):
    print(y, "  ".join(f"{100*rows[t][y][1]/rows[t][y][0]:6.1f}%" if y in rows[t] else "      -" for t in rows))
print("agg  " + "  ".join(f"{100*sum(v[1] for v in rows[t].values())/sum(v[0] for v in rows[t].values()):6.1f}%" for t in rows))
low = sum(1 for y in range(2017, 2026) if all(y in rows[t] for t in rows) and min(rows, key=lambda t: rows[t][y][1]/rows[t][y][0]) == "FLR")
print("years FLR lowest of the four:", low, "of", sum(1 for y in range(2017,2026) if all(y in rows[t] for t in rows)))
for t in rows:
    print(t, "accessions:", sorted({v[2] for v in rows[t].values()}))
