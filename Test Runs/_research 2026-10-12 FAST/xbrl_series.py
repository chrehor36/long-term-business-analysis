# print annual (FY, 10-K) values for chosen tags, by fiscal year end; first-filed vintage and latest vintage
import json, sys, os
here=os.path.dirname(os.path.abspath(__file__))
d=json.load(open(os.path.join(here,"cache","facts.json")))["facts"]["us-gaap"]
tags=sys.argv[1:]
for t in tags:
    if t not in d: print(t,"MISSING"); continue
    u=list(d[t]["units"].values())[0]
    rows={}
    for r in u:
        if r.get("form")!="10-K" or "frame" not in r and False: pass
        if r.get("form")!="10-K": continue
        if "start" in r:
            from datetime import date
            s=date.fromisoformat(r["start"]); e=date.fromisoformat(r["end"])
            if (e-s).days<350: continue
        rows.setdefault(r["end"],[]).append((r["filed"],r["val"],r["accn"]))
    print(t)
    for e in sorted(rows):
        v=sorted(rows[e]); print("  ",e,"first",v[0][1],v[0][2],"latest",v[-1][1])
