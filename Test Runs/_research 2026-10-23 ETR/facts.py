"""Print annual FY values (10-K, frame-less latest filing per FY end) for given us-gaap tags. Usage: python facts.py FACTSFILE TAG..."""
import json, sys, os
d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache", sys.argv[1])))
g = d["facts"].get("us-gaap", {})
for tag in sys.argv[2:]:
    if tag not in g: print(tag, "NOT FOUND"); continue
    units = g[tag]["units"]
    u = list(units)[0]
    rows = {}
    for r in units[u]:
        if r.get("form") not in ("10-K", "10-K/A"): continue
        if "start" in r:
            from datetime import date
            s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
            if not (350 <= (e - s).days <= 380): continue
        key = r["end"]
        # keep the first-filed value for that period end
        if key not in rows or r["filed"] < rows[key][1]:
            rows[key] = (r["val"], r["filed"], r["accn"])
    print(tag, u)
    for k in sorted(rows):
        if k >= "2014-12-31":
            v, f, a = rows[k]
            print("   ", k, f"{v/1e6:,.1f}", f, a)
