import json, sys, os
d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache", "companyfacts.json")))
g = d["facts"]["us-gaap"]
def annual(tag, unit="USD"):
    if tag not in g: return {}
    out = {}
    for f in g[tag]["units"].get(unit, []):
        if f.get("form") in ("10-K", "10-K/A") and f.get("fp") == "FY" and "start" in f:
            from datetime import date
            s = date.fromisoformat(f["start"]); e = date.fromisoformat(f["end"])
            if 350 < (e - s).days < 380:
                out.setdefault(f["end"], (f["val"], f["accn"]))
    return out
def inst(tag, unit="USD"):
    out = {}
    for f in g.get(tag, {}).get("units", {}).get(unit, []):
        if f.get("form") in ("10-K",) :
            out.setdefault(f["end"], (f["val"], f["accn"]))
    return out
tags = sys.argv[1:]
for t in tags:
    unit = "shares" if "Shares" in t or "Number" in t else "USD"
    a = annual(t, unit) or inst(t, unit)
    print("==", t)
    for k in sorted(a): 
        if k >= "2014": print("  ", k, a[k][0], a[k][1])
