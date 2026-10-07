import json, sys
f = json.load(open(sys.argv[1]))["facts"]
tags = sys.argv[2].split(",")
def annual(tag):
    out = {}
    for ns in ("us-gaap","dei"):
        if tag in f.get(ns,{}):
            for unit, vals in f[ns][tag]["units"].items():
                for v in vals:
                    if v.get("form","").startswith("10-K") and v.get("fp")=="FY":
                        dur = v.get("start")
                        end = v["end"]
                        if dur:
                            from datetime import date
                            d0 = date.fromisoformat(dur); d1 = date.fromisoformat(end)
                            if (d1-d0).days < 300: continue
                        key = end
                        # keep first filed
                        if key not in out or v["filed"] < out[key][1]:
                            out[key] = (v["val"], v["filed"], v.get("accn"))
    return out
for t in tags:
    a = annual(t)
    print("==", t)
    for k in sorted(a):
        print("  ", k, round(a[k][0]/1e6,1) if abs(a[k][0])>1e4 else a[k][0], a[k][1], a[k][2])
