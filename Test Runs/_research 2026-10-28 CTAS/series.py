import json, sys
from datetime import date
d = json.load(open("cache/ctas_companyfacts.json"))["facts"]["us-gaap"]
def ann(tag):
    out = {}
    if tag not in d: return out
    for unit, rows in d[tag]["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A"): continue
            if "start" in r:
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                if not (350 <= (e - s).days <= 380): continue
            e = r["end"]
            if not e.endswith("-05-31") and not e.endswith("-06-01"): continue
            fy = int(e[:4])
            # keep earliest-filed value for that FY (first vintage) unless later restated; record both
            out.setdefault(fy, []).append((r["filed"], r["val"], r["accn"]))
    return {k: sorted(v)[0] for k, v in out.items()}
tags = sys.argv[1:]
for t in tags:
    a = ann(t)
    print(t)
    for fy in sorted(a):
        if fy >= 2014: print("  ", fy, a[fy][1], a[fy][2])
