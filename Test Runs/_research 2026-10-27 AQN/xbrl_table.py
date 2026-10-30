import json, sys
d=json.load(open("cache/facts.json"))
g=d["facts"]["us-gaap"]
def annual(k, inst=False):
    if k not in g: return {}
    out={}
    for unit,vals in g[k]["units"].items():
        for x in vals:
            if x.get("fp")!="FY" and x["form"] not in ("40-F","40-F/A"): continue
            if not inst:
                if "start" not in x: continue
                from datetime import date
                s=date.fromisoformat(x["start"]); e=date.fromisoformat(x["end"])
                if not (350<(e-s).days<380): continue
            if not x["end"].endswith("12-31"): continue
            y=int(x["end"][:4])
            # prefer latest filed
            if y not in out or x["filed"]>out[y][1]:
                out[y]=(x["val"],x["filed"],x["accn"])
    return out
if __name__=="__main__":
    for k in sys.argv[1:]:
        inst = k.startswith("@")
        k2=k.lstrip("@")
        a=annual(k2, inst)
        print(k2, {y:round(v[0]/1e6,1) for y,(v0) in sorted(a.items()) for v in [v0]})
