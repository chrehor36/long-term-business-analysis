import json,sys
d=json.load(open("facts.json"))
g=d["facts"]["us-gaap"]
def series(tag, unit="USD"):
    if tag not in g: return {}
    out={}
    for u in g[tag]["units"].get(unit,[]):
        if u.get("fp")=="FY" and u["form"] in("10-K","10-K/A") and "start" in u:
            # annual duration ~ 1 year
            from datetime import date
            s=date.fromisoformat(u["start"]); e=date.fromisoformat(u["end"])
            if 350<(e-s).days<380:
                out.setdefault(u["end"],u["val"])  # first filed
    return out
def inst(tag, unit="USD"):
    out={}
    for u in g.get(tag,{}).get("units",{}).get(unit,[]):
        if u["form"] in("10-K","10-K/A"):
            out.setdefault(u["end"],u["val"])
    return out
tags=sys.argv[1:]
rows={}
for t in tags:
    s=series(t)
    for k,v in s.items(): rows.setdefault(k,{})[t]=v
for k in sorted(rows):
    print(k, " ".join(f"{t[:28]}={rows[k].get(t,'-')/1e6 if isinstance(rows[k].get(t),(int,float)) else '-'}" for t in tags))
