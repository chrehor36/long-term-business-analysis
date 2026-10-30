import json, sys
from datetime import date
f = sys.argv[1]; tags = sys.argv[2:]
d = json.load(open(f))["facts"]["us-gaap"]
for t in tags:
    if t not in d: print(t, "MISSING"); continue
    out = {}
    for unit, rows in d[t]["units"].items():
        for r in rows:
            if r.get("form") != "10-K": continue
            if "start" in r:
                dd = (date.fromisoformat(r["end"]) - date.fromisoformat(r["start"])).days
                if not 350 <= dd <= 380: continue
            out.setdefault(r["end"], []).append((r["filed"], r["val"]))
    print(t, " | ".join(f"{e[:7]}:{sorted(v)[-1][1]/1e6:,.1f}" for e, v in sorted(out.items()) if e >= "2015-06"))
