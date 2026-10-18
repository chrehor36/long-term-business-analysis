import json, sys
d = json.load(open(sys.argv[1]))
g = d["facts"]["us-gaap"]
def ann(tag):
    out = {}
    if tag not in g: return out
    for unit, rows in g[tag]["units"].items():
        for r in rows:
            if r.get("form") != "10-K" or "start" not in r: continue
            from datetime import date
            s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
            if not (350 <= (e - s).days <= 380): continue
            y = e.year
            # keep latest-filed value per year (restated)
            if y not in out or r["filed"] > out[y][1]:
                out[y] = (r["val"], r["filed"])
    return {y: v[0] for y, v in out.items()}
tags = sys.argv[2:]
yrs = range(2014, 2026)
for t in tags:
    a = ann(t)
    print(f"{t[:60]:60s}", " ".join(f"{(a.get(y,0) or 0)/1e6:8.0f}" if y in a else "       -" for y in yrs))
print(" " * 60, " ".join(f"{y:8d}" for y in yrs))
