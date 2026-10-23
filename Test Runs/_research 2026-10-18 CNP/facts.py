import json, sys
from datetime import date
d = json.load(open(sys.argv[1]))["facts"]["us-gaap"]
for t in sys.argv[2:]:
    if t not in d: print(t, "NOT FOUND"); continue
    u = d[t]["units"]; unit = list(u)[0]
    rows = {}
    for x in u[unit]:
        if x.get("form") != "10-K": continue
        if "start" in x:
            if (date.fromisoformat(x["end"])-date.fromisoformat(x["start"])).days < 350: continue
        rows.setdefault(x["end"], x["val"])
    print(t, {k[:4]:round(v/1e6,1) for k,v in sorted(rows.items()) if k>="2015-12-31"})
