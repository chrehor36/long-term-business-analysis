"""Competitor row: revenue, operating income, operating margin, FY2016-FY2025, from each filer's own XBRL (10-K, latest
vintage), for KO, PepsiCo, Keurig Dr Pepper and Monster. USD millions. Usage: python peers.py"""
import json, os
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
REV_TAGS = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet", "SalesRevenueGoodsNet"]


def annual(F, tag):
    out = {}
    try:
        units = F["us-gaap"][tag]["units"]["USD"]
    except KeyError:
        return out
    for r in units:
        if r.get("form") != "10-K" or "start" not in r:
            continue
        d0, d1 = date.fromisoformat(r["start"]), date.fromisoformat(r["end"])
        if not (350 <= (d1 - d0).days <= 380):
            continue
        y = d1.year if d1.month > 6 else d1.year - 1
        if y not in out or r["filed"] > out[y][1]:
            out[y] = (r["val"] / 1e6, r["filed"], r["accn"])
    return out


for t in ["KO", "PEP", "KDP", "MNST"]:
    F = json.load(open(os.path.join(HERE, "cache", f"companyfacts_{t}.json")))["facts"]
    rev = {}
    for tag in REV_TAGS:
        for y, v in annual(F, tag).items():
            if y not in rev or v[1] > rev[y][1]:
                rev[y] = v
    oi = annual(F, "OperatingIncomeLoss")
    print(f"== {t}")
    for y in range(2016, 2026):
        if y in rev and y in oi:
            print(f"  {y}  revenue {rev[y][0]:>10,.0f}  op income {oi[y][0]:>9,.0f}  margin {oi[y][0]/rev[y][0]*100:5.1f}%  ({oi[y][2]})")
    ys = [y for y in (2016, 2025) if y in rev]
    if len(ys) == 2:
        g = (rev[2025][0] / rev[2016][0]) ** (1 / 9) - 1
        print(f"  revenue CAGR 2016-2025: {g*100:.1f}%")
