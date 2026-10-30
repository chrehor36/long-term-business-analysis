import json,sys,os
j=json.load(open(os.path.join(os.path.dirname(__file__),"cache","facts_0000853816.json")))
g=j["facts"]["us-gaap"]
def annual(tag):
    if tag not in g: return {}
    out={}
    for u,arr in g[tag]["units"].items():
        for x in arr:
            if x.get("form") in ("10-K","10-K/A") and x.get("fp")=="FY":
                if "start" in x:
                    from datetime import date
                    s=date.fromisoformat(x["start"]); e=date.fromisoformat(x["end"])
                    if (e-s).days<350: continue
                out.setdefault(x["end"][:4] if x["end"][5:7]!="01" else str(int(x["end"][:4])-1),(x["end"],x["val"],x["accn"]))
                # keep first filed? keep latest filed
                k=x["end"][:4]
                if k not in out or x["filed"]>out[k][3] if len(out.get(k,()))>3 else True:
                    out[k]=(x["end"],x["val"],x["accn"],x["filed"])
    return out
tags=sys.argv[1:]
for t in tags:
    a=annual(t)
    print(t, " ".join(f"{k}:{v[1]/1e6:.1f}" for k,v in sorted(a.items())))
