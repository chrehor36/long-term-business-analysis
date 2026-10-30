import json, sys
d = json.load(open(sys.argv[1], encoding="utf-8"))["facts"]["us-gaap"]
def series(tag):
    if tag not in d: return {}
    out = {}
    for unit, arr in d[tag]["units"].items():
        for f in arr:
            if f.get("form") not in ("10-K","10-K/A"): continue
            s, e = f.get("start"), f["end"]
            if s:
                from datetime import date
                y1,m1,d1 = map(int,s.split("-")); y2,m2,d2 = map(int,e.split("-"))
                if (date(y2,m2,d2)-date(y1,m1,d1)).days < 350: continue
            if not e.endswith("-08-31"): continue
            out.setdefault(e[:4], f["val"])   # first filed
    return out
tags = sys.argv[2:]
years = [str(y) for y in range(2012, 2026)]
print("tag".ljust(70), " ".join(y.rjust(8) for y in years))
for t in tags:
    s = series(t)
    print(t[:70].ljust(70), " ".join((f"{s[y]/1e6:8.2f}" if y in s else "       -") for y in years))
