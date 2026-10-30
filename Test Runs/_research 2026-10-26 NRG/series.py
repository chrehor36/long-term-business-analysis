"""Print annual (FY, 10-K, 12-month) values for chosen us-gaap tags from cached companyfacts; first-filed vintage per fiscal year end."""
import json, sys, os
d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache", sys.argv[1])))
tags = sys.argv[2:]
g = d["facts"]["us-gaap"]
for t in tags:
    if t not in g: print(t, "MISSING"); continue
    units = g[t]["units"]; u = list(units)[0]
    rows = {}
    for x in units[u]:
        if x.get("form") not in ("10-K", "10-K/A"): continue
        if "start" in x:
            from datetime import date
            s = date.fromisoformat(x["start"]); e = date.fromisoformat(x["end"])
            if not (350 <= (e - s).days <= 380): continue
        key = x["end"]
        if key not in rows or x["filed"] < rows[key][1]:
            rows[key] = (x["val"], x["filed"], x["accn"])
    out = [f"{k[:4]}:{v[0]/1e6:,.0f}" for k, v in sorted(rows.items()) if k >= "2014"]
    print(t, u, " ".join(out))
