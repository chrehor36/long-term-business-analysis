import json, sys
def annual(path, tags, ns=("us-gaap","ifrs-full")):
    d=json.load(open(path))
    out={}
    for n in ns:
        f=d["facts"].get(n,{})
        for t in tags:
            if t not in f: continue
            for unit,arr in f[t]["units"].items():
                for x in arr:
                    if x.get("form") not in ("10-K","40-F","10-K/A","20-F"): continue
                    fy=x.get("end","")[:4]
                    if "start" in x:
                        from datetime import date
                        s=date.fromisoformat(x["start"]); e=date.fromisoformat(x["end"])
                        if not (330<(e-s).days<400): continue
                    key=(t,x["end"])
                    # keep first filed
                    if key not in out or x["filed"]<out[key][1]:
                        out[key]=(x["val"],x["filed"],x["accn"])
    return out
if __name__=="__main__":
    path=sys.argv[1]; tags=sys.argv[2].split(",")
    o=annual(path,tags)
    for t in tags:
        rows=sorted((k[1],v) for k,v in o.items() if k[0]==t)
        print(t)
        for e,v in rows: print("  ",e, round(v[0]/1e6,1), v[2])
