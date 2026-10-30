# Arithmetic only: pulls annual XBRL facts for a ticker and prints by fiscal year.
import sys, os, json
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources as S
tk = sys.argv[1]
cik, name = S.cik_for(tk)
f = S.sec_facts(cik)
g = f["facts"].get("us-gaap", {})
want = sys.argv[2].split(",") if len(sys.argv) > 2 else None
out = {}
for tag, d in g.items():
    if want and tag not in want: continue
    for unit, rows in d["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A"): continue
            if "start" in r:
                from datetime import date
                a = date.fromisoformat(r["start"]); b = date.fromisoformat(r["end"])
                if not (340 <= (b - a).days <= 380): continue
            key = (tag, r["end"])
            # keep earliest filed vintage
            if key not in out or r["filed"] < out[key][1]:
                out[key] = (r["val"], r["filed"], r["accn"])
print(name, cik)
tags = sorted(set(k[0] for k in out))
for t in tags:
    yrs = sorted(k[1] for k in out if k[0] == t)
    vals = " ".join(f"{y[:4]}:{out[(t,y)][0]/1e6:.0f}" for y in yrs if abs(out[(t,y)][0])>=1e4)
    print(t, "|", vals)
