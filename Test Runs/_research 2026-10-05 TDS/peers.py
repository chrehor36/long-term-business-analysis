import json,sys
def annual(f, tags):
    d=json.load(open(f))["facts"]
    out={}
    for t in tags:
        for ns in ("us-gaap","dei"):
            if t in d.get(ns,{}):
                for u,vals in d[ns][t]["units"].items():
                    for v in vals:
                        if v.get("form") in ("10-K","10-K/A") and v.get("fp")=="FY" and "start" in v:
                            # full-year duration ~ 1 year
                            from datetime import date
                            s=date.fromisoformat(v["start"]); e=date.fromisoformat(v["end"])
                            if 350<(e-s).days<380:
                                y=e.year
                                # keep first-filed per (tag, year)
                                key=(t,y)
                                if key not in out or v["filed"]<out[key][1]:
                                    out[key]=(v["val"],v["filed"],v["accn"])
    return out
tick=sys.argv[1]
tags=sys.argv[2].split(",")
o=annual(f"peers/{tick}_facts.json",tags)
years=sorted({y for (_,y) in o})
for t in tags:
    row=[f"{t[:38]:38}"]
    for y in years:
        v=o.get((t,y))
        row.append(f"{y}:{v[0]/1e6:,.0f}" if v else f"{y}:-")
    print(" ".join(row))
acc={}
for (t,y),v in o.items(): acc.setdefault(y,set()).add(v[2])
for y in years: print(y, sorted(acc[y])[:3])
