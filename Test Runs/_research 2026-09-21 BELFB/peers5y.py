import json, os, datetime

D = os.path.dirname(os.path.abspath(__file__))
PEERS = {"APH": "0000820313", "TEL": "0001385157", "LFUS": "0000889331", "VICR": "0000751978",
         "AEIS": "0000927003", "MEI": "0000065270", "CTS": "0000026058", "SXI": "0000310354",
         "RFIL": "0000740664", "ALNT": "0000046129", "VSH": "0000103730", "BELFB": "0000729580"}
REV = ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues",
       "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueNet", "SalesRevenueGoodsNet"]
OI = ["OperatingIncomeLoss"]
GP = ["GrossProfit"]


def dur(g, tags):
    out = {}
    for t in tags:
        if t not in g:
            continue
        for u, rows in g[t]["units"].items():
            for r in rows:
                if r.get("form") not in ("10-K", "10-K/A") or not r.get("start"):
                    continue
                d1 = datetime.date.fromisoformat(r["start"])
                d2 = datetime.date.fromisoformat(r["end"])
                if not (330 <= (d2 - d1).days <= 400):
                    continue
                p = out.get(r["end"])
                if p is None or r["filed"] > p[1]:
                    out[r["end"]] = (r["val"], r["filed"], t)
    return out


print("%-6s  %-10s  %s" % ("tkr", "window", "operating margin % by fiscal year, oldest first  | 5y mean | 5y min"))
res = {}
for tk, cik in PEERS.items():
    fn = os.path.join(D, "peers_%s.json" % cik)
    if not os.path.exists(fn):
        print(tk, "no cache")
        continue
    g = json.load(open(fn))["facts"].get("us-gaap", {})
    rev, oi, gp = dur(g, REV), dur(g, OI), dur(g, GP)
    ys = sorted(set(rev) & set(oi))[-5:]
    oms = [oi[y][0] / rev[y][0] * 100 for y in ys]
    gms = [(gp[y][0] / rev[y][0] * 100) if y in gp else None for y in ys]
    res[tk] = dict(years=ys, om=oms, gm=gms)
    print("%-6s  %s..%s  %s | %5.1f | %5.1f" % (
        tk, ys[0], ys[-1], " ".join("%6.1f" % v for v in oms),
        sum(oms) / len(oms), min(oms)))
    print("%-6s  %-21s %s (gross margin)" % ("", "",
          " ".join(("%6.1f" % v) if v is not None else "   n/a" for v in gms)))
json.dump(res, open(os.path.join(D, "peer_5y.json"), "w"), indent=1)
