# -*- coding: utf-8 -*-
import json, io
from datetime import date

REV_TAGS = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
            "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueNet"]
GP_TAGS = ["GrossProfit"]
COGS_TAGS = ["CostOfGoodsAndServicesSold", "CostOfRevenue", "CostOfGoodsSold"]


def periods(facts, tags, lo, hi):
    g = facts["facts"].get("us-gaap", {})
    out = {}
    for tag in tags:
        if tag not in g:
            continue
        for u, arr in g[tag]["units"].items():
            if u != "USD":
                continue
            for e in arr:
                s, en = e.get("start"), e["end"]
                if not s:
                    continue
                dd = (date.fromisoformat(en) - date.fromisoformat(s)).days
                if not (lo <= dd <= hi):
                    continue
                out.setdefault((s, en), {})[tag] = (e["val"], e.get("accn"), e.get("form"))
    return out


def show(path, label, lo, hi, n=4):
    f = json.load(io.open(path, encoding="utf-8"))
    rev = periods(f, REV_TAGS, lo, hi)
    gp = periods(f, GP_TAGS, lo, hi)
    cogs = periods(f, COGS_TAGS, lo, hi)
    keys = sorted(set(rev) | set(gp), key=lambda k: k[1])
    print("===", label, "window days", lo, "-", hi)
    for k in keys[-n:]:
        r = acc = None
        for t in REV_TAGS:
            if k in rev and t in rev[k]:
                r, acc, _ = rev[k][t]
                break
        gv = gp.get(k, {}).get("GrossProfit")
        g = gv[0] if gv else None
        if g is None and r is not None:
            for t in COGS_TAGS:
                if k in cogs and t in cogs[k]:
                    g = r - cogs[k][t][0]
                    break
        if r and g is not None:
            print("  %s..%s  rev %9.1f  gp %9.1f  gm %5.1f%%  %s" %
                  (k[0], k[1], r / 1e6, g / 1e6, 100.0 * g / r, acc))


for p, l in [("companyfacts.json", "BRBR"),
             ("peers/SMPL_companyfacts.json", "SMPL"),
             ("peers/CELH_companyfacts.json", "CELH"),
             ("peers/POST_companyfacts.json", "POST"),
             ("peers/HLF_companyfacts.json", "HLF"),
             ("peers/MED_companyfacts.json", "MED"),
             ("peers/ABT_companyfacts.json", "ABT")]:
    try:
        show(p, l, 250, 285)   # 9-month / 3-quarter periods
    except Exception as e:
        print("===", l, "ERR", e)
    try:
        show(p, l, 80, 100, 3)  # single quarters
    except Exception as e:
        pass
