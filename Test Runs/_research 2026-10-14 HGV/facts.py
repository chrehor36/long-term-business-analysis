import json, sys
def load(name):
    return json.load(open("cache/"+name))
def annual(d, tag, unit="USD", ns="us-gaap"):
    try: arr = d["facts"][ns][tag]["units"][unit]
    except KeyError: return {}
    out = {}
    for x in arr:
        if x.get("form") in ("10-K","10-K/A") and x.get("fp")=="FY":
            # duration ~1y or instant
            if "start" in x:
                from datetime import date
                s=date.fromisoformat(x["start"]); e=date.fromisoformat(x["end"])
                if not 350<= (e-s).days <=380: continue
            key = x["end"]
            # keep first-filed
            if key not in out or x["filed"] < out[key][1]:
                out[key]=(x["val"], x["filed"], x["accn"])
    return out
if __name__=="__main__":
    d=load(sys.argv[1])
    for tag in sys.argv[2:]:
        ns="us-gaap"
        if ":" in tag: ns,tag=tag.split(":")
        a=annual(d,tag,ns=ns)
        print(tag, {k[:4]:round(v[0]/1e6,1) for k,v in sorted(a.items())})
