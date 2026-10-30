import json,sys
f=json.load(open("cache/facts.json"))["facts"]
def ann(tag,ns="us-gaap",dur=True):
    if tag not in f.get(ns,{}): return {}
    out={}
    for u,vals in f[ns][tag]["units"].items():
        for v in vals:
            if v.get("form") not in("10-K","10-K/A"): continue
            if dur:
                if "start" not in v: continue
                from datetime import date
                s=date.fromisoformat(v["start"]); e=date.fromisoformat(v["end"])
                if not 350<(e-s).days<380: continue
            y=v["end"][:4]
            # keep latest filed
            if y not in out or v["filed"]>out[y][1]: out[y]=(v["val"],v["filed"])
    return {k:v[0] for k,v in sorted(out.items())}
tags=sys.argv[1:]
for t in tags:
    dur = not t.startswith("@")
    t=t.lstrip("@")
    s=ann(t,dur=dur)
    print(t, {k:round(v/1e6,1) for k,v in s.items() if k>="2014"})
