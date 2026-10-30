"""Competitor series from each filer's own XBRL company facts (10-K annual values, first filed).
Usage: python -I comps.py <cachedir>   (expects companyfacts_<TICKER>.json in cachedir)
Prints revenue, growth, operating margin, SBC/revenue, owner cash (OCF - SBC - capex)/revenue, by fiscal year.
"""
import json, sys, os
from datetime import date

CANDS = {
    "rev": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax"],
    "opinc": ["OperatingIncomeLoss"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities"],
    "sbc": ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"],
    "capsw": ["PaymentsToDevelopSoftware", "PaymentsForSoftware"],
    "gp": ["GrossProfit"],
}


def annual(g, tag):
    out = {}
    if tag not in g:
        return out
    for u, rows in g[tag]["units"].items():
        if u != "USD":
            continue
        for r in rows:
            if r.get("form") != "10-K" or "start" not in r:
                continue
            d = (date.fromisoformat(r["end"]) - date.fromisoformat(r["start"])).days
            if 350 <= d <= 380 and r["end"] not in out:
                out[r["end"]] = (r["val"], r["accn"])
    return out


def main():
    cache = sys.argv[1]
    for t in ("PLTR", "SNOW", "DDOG", "AI", "BAH"):
        fn = os.path.join(cache, "companyfacts.json" if t == "PLTR" else f"companyfacts_{t}.json")
        g = json.load(open(fn))["facts"]["us-gaap"]
        ser = {}
        for k, tags in CANDS.items():
            merged = {}
            for tag in tags:
                for e, v in annual(g, tag).items():
                    merged.setdefault(e, v)
            ser[k] = merged
        years = sorted(e for e in ser["rev"] if e >= "2019-06-01")
        print(f"=== {t}")
        prev = None
        for e in years:
            rev = ser["rev"][e][0]
            def gv(k):
                v = ser[k].get(e)
                return None if v is None else v[0]
            op, ocf, sbc, cap, csw, gp = (gv(k) for k in ("opinc", "ocf", "sbc", "capex", "capsw", "gp"))
            oc = None if None in (ocf, sbc) else ocf - sbc - (cap or 0) - (csw or 0)
            gr = "" if prev is None else f"{rev/prev-1:6.1%}"
            f = lambda x: "   n/a" if x is None else f"{x/rev:6.1%}"
            print(f"  FY end {e}: rev {rev/1e6:9.1f}M {gr:>7} | gross {f(gp)} | op {f(op)} | SBC {f(sbc)}"
                  f" | owner cash {f(oc)} ({'' if oc is None else f'{oc/1e6:8.1f}M'}) | accn {ser['rev'][e][1]}")
            prev = rev


main()
