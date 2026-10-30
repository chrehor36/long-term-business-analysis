import json, sys
f = json.load(open(sys.argv[1]))
tags = sys.argv[2].split(",")
g = f["facts"].get("us-gaap", {})
def annual(tag):
    out = {}
    if tag not in g: return out
    for unit, rows in g[tag]["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K", "10-K405"): continue
            fp = r.get("fp"); 
            if "start" in r:
                from datetime import date
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                if (e - s).days < 350 or (e - s).days > 380: continue
            y = int(r["end"][:4])
            # keep first-filed value for each year end
            key = r["end"]
            if key not in out or r["filed"] < out[key][1]:
                out[key] = (r["val"], r["filed"], r["accn"])
    return out
for t in tags:
    a = annual(t)
    print(t)
    for k in sorted(a):
        if k >= "2008": print("  ", k, a[k][0], a[k][2])
