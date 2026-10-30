import json,sys
t=sys.argv[1]; tags=sys.argv[2:]
d=json.load(open(f"{t}_companyfacts.json"))["facts"]["us-gaap"]
for tag in tags:
    if tag not in d: print(tag,"--none"); continue
    u=d[tag]["units"]; k=list(u)[0]
    out={}
    for x in u[k]:
        if x.get("form")!="10-K": continue
        if "start" in x:
            from datetime import date
            s=date.fromisoformat(x["start"]); e=date.fromisoformat(x["end"])
            if not 350<(e-s).days<380: continue
        key=x["end"]
        out.setdefault(key,(x["val"],x["accn"],x["fy"]))
    print(tag, {k:(round(v[0]/1e6,1),v[1]) for k,v in sorted(out.items()) if k>="2019-12"})
