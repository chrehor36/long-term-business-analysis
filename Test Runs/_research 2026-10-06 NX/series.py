import json, sys
d = json.load(open(sys.argv[1]))["facts"]["us-gaap"]
tags = sys.argv[2].split(",")
fye_month = sys.argv[3] if len(sys.argv)>3 else None
for t in tags:
    if t not in d: print(t, "MISSING"); continue
    units = d[t]["units"]; u = list(units)[0]
    rows = {}
    for r in units[u]:
        if r.get("form") not in ("10-K","10-K/A","20-F"): continue
        if "start" in r:
            from datetime import date
            s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
            if not 350 <= (e-s).days <= 380: continue
        if r.get("fp") not in (None,"FY"): pass
        e = r["end"]
        # keep earliest filed (first vintage)
        if e not in rows or r["filed"] < rows[e][1]:
            rows[e] = (r["val"], r["filed"], r["accn"])
    print("==", t, u)
    for e in sorted(rows):
        if fye_month and e[5:7] != fye_month: continue
        v = rows[e][0]
        print(f"  {e}  {v/1e6 if abs(v)>1e4 else v:>12.1f}  {rows[e][2]}")
