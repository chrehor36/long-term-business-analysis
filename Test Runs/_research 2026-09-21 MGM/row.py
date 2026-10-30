# -*- coding: utf-8 -*-
"""The competitor row, same metric, same window, each from its own companyfacts.
Arithmetic only; it concludes nothing (operator rule 8)."""
import json, io, os
D = os.path.dirname(os.path.abspath(__file__))
res = json.load(io.open(os.path.join(D, "peers", "peer_series.json"), encoding="utf-8"))
YRS = ["2021-12-31", "2022-12-31", "2023-12-31", "2024-12-31", "2025-12-31"]
ORDER = ["MGM", "LVS", "WYNN", "CZR", "BYD", "PENN", "MLCO"]


def g(d, k, y):
    v = d.get(k, {}).get(y)
    return None if v is None else v / 1e6


print("A. OPERATING MARGIN = OperatingIncomeLoss / Revenues, each filer's own 10-K/20-F")
print("ticker," + ",".join(y[:4] for y in YRS))
for t in ORDER:
    d = res[t]
    row = []
    for y in YRS:
        r, o = g(d, "REV", y), g(d, "OPINC", y)
        row.append("" if not r or o is None else "%.1f%%" % (100.0 * o / r))
    print(t + "," + ",".join(row))

print()
print("B. RETURN ON THE REAL ESTATE USED, owned OR rented:")
print("   (OperatingIncomeLoss + OperatingLeaseCost) / (PP&E net + operating ROU asset)")
print("   built so an OWNER (LVS, WYNN, BYD, MLCO) and a TENANT (MGM) are on one scale")
print("ticker," + ",".join(y[:4] for y in YRS))
for t in ORDER:
    d = res[t]
    row = []
    for y in YRS:
        o = g(d, "OPINC", y)
        lc = g(d, "OPLEASECOST", y) or 0.0
        ppe = g(d, "PPE", y)
        rou = g(d, "ROU", y) or 0.0
        if o is None or ppe is None:
            row.append("")
        else:
            row.append("%.1f%%" % (100.0 * (o + lc) / (ppe + rou)))
    print(t + "," + ",".join(row))

print()
print("C. REVENUE, $M")
print("ticker," + ",".join(y[:4] for y in YRS))
for t in ORDER:
    d = res[t]
    print(t + "," + ",".join("" if g(d, "REV", y) is None else "%.0f" % g(d, "REV", y) for y in YRS))

print()
print("D. OPERATING CASH FLOW LESS CAPEX, $M (a crude free-cash line, not owner earnings)")
print("ticker," + ",".join(y[:4] for y in YRS))
for t in ORDER:
    d = res[t]
    row = []
    for y in YRS:
        o, c = g(d, "OCF", y), g(d, "CAPEX", y)
        row.append("" if o is None or c is None else "%.0f" % (o - c))
    print(t + "," + ",".join(row))

print()
print("E. MGM, the lease block alone, from its own 10-K notes")
d = res["MGM"]
for y in YRS:
    print(y[:4], "op lease cost $%.0fM" % (g(d, "OPLEASECOST", y) or 0),
          " op lease liab (noncurrent) $%.0fM" % (g(d, "OPLEASELIAB_NC", y) or 0),
          " ROU $%.0fM" % (g(d, "ROU", y) or 0))
