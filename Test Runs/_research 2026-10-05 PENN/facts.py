import json,sys
d=json.load(open(sys.argv[1]))
g=d["facts"]["us-gaap"]
tags=sys.argv[2].split(",")
for t in tags:
    if t not in g: print("NO",t); continue
    u=list(g[t]["units"].values())[0]
    best={}
    for x in u:
        if x.get("form") not in ("10-K","10-K/A"): continue
        if "start" in x:
            from datetime import date
            a=date.fromisoformat(x["start"]); b=date.fromisoformat(x["end"])
            if not (340<=(b-a).days<=380): continue
        fy=x["end"][:4]
        # keep earliest filed (first-filed vintage)
        if fy not in best or x["filed"]<best[fy]["filed"]: best[fy]=x
    print(t, {k:round(best[k]["val"]/1e6,1) for k in sorted(best)})
