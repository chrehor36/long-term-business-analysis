# -*- coding: utf-8 -*-
import json, io, sys
from datetime import date

REV_TAGS = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
            "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueNet"]
GP_TAGS = ["GrossProfit"]
COGS_TAGS = ["CostOfGoodsAndServicesSold", "CostOfRevenue", "CostOfGoodsSold"]


def annual(facts, tags, forms=("10-K",), lo=340, hi=380):
    g = facts["facts"].get("us-gaap", {})
    out = {}
    for tag in tags:
        if tag not in g:
            continue
        for u, arr in g[tag]["units"].items():
            if u != "USD":
                continue
            for e in arr:
                if e.get("form") not in forms:
                    continue
                s, en = e.get("start"), e["end"]
                if not s:
                    continue
                dd = (date.fromisoformat(en) - date.fromisoformat(s)).days
                if not (lo <= dd <= hi):
                    continue
                out.setdefault(en, {}).setdefault(tag, e["val"])
    return out


def series(path, label):
    f = json.load(io.open(path, encoding="utf-8"))
    rev = annual(f, REV_TAGS)
    gp = annual(f, GP_TAGS)
    cogs = annual(f, COGS_TAGS)
    rows = []
    for end in sorted(set(rev) | set(gp)):
        r = None
        for t in REV_TAGS:
            if end in rev and t in rev[end]:
                r = rev[end][t]
                break
        g = gp.get(end, {}).get("GrossProfit")
        if g is None and r is not None:
            for t in COGS_TAGS:
                if end in cogs and t in cogs[end]:
                    g = r - cogs[end][t]
                    break
        if r and g is not None:
            rows.append((end, r / 1e6, g / 1e6, 100.0 * g / r))
    print("===", label)
    for end, r, g, m in rows[-9:]:
        print("  %s  rev %10.1f  gp %10.1f  gm %5.1f%%" % (end, r, g, m))


for p, l in [("companyfacts.json", "BRBR"),
             ("peers/SMPL_companyfacts.json", "SMPL"),
             ("peers/MED_companyfacts.json", "MED"),
             ("peers/HLF_companyfacts.json", "HLF"),
             ("peers/CELH_companyfacts.json", "CELH"),
             ("peers/POST_companyfacts.json", "POST"),
             ("peers/ABT_companyfacts.json", "ABT")]:
    try:
        series(p, l)
    except Exception as e:
        print("===", l, "ERROR", e)
