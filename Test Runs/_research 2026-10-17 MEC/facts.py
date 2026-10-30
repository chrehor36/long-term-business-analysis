import json, sys
d = json.load(open(sys.argv[1]))["facts"]["us-gaap"]
tags = sys.argv[2].split(",")
for t in tags:
    if t not in d: print(t, "MISSING"); continue
    units = d[t]["units"]; u = list(units)[0]
    rows = {}
    for x in units[u]:
        if x.get("fp") == "FY" and x["form"].startswith("10-K"):
            dur = None
            if "start" in x:
                from datetime import date
                s = date.fromisoformat(x["start"]); e = date.fromisoformat(x["end"])
                if (e - s).days < 300: continue
            rows.setdefault(x["end"], x["val"])
    print(t, " ".join(f"{k[:4]}:{v/1e3 if abs(v)>1e4 else v:,.0f}" for k, v in sorted(rows.items())))
