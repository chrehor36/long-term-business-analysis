import json, sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "tools")))
import sources
f = sources.sec_facts("0000886346")
g = f["facts"]["us-gaap"]
tags = sys.argv[1:]
for t in tags:
    if t not in g: print(t, "NOT FOUND"); continue
    u = g[t]["units"]; unit = list(u)[0]
    seen = {}
    for x in u[unit]:
        if x.get("form") != "10-K" or x.get("fp") != "FY": continue
        if "start" in x:
            from datetime import date
            s = date.fromisoformat(x["start"]); e = date.fromisoformat(x["end"])
            if not (340 <= (e - s).days <= 380): continue
        k = x["end"]
        if k not in seen: seen[k] = (x["val"], x["accn"])
    print(t, unit)
    for k in sorted(seen): print("  ", k, round(seen[k][0]/1e6, 3) if unit=="USD" else seen[k][0], seen[k][1])
