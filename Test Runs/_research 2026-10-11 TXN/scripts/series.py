import json, sys
d = json.load(open(sys.argv[1]))
g = d["facts"]["us-gaap"]
def annual(tag):
    if tag not in g: return {}
    out = {}
    for unit, arr in g[tag]["units"].items():
        for x in arr:
            if x.get("form") != "10-K" or x.get("fp") != "FY": continue
            if "start" in x:
                s, e = x["start"], x["end"]
                if int(e[:4]) - int(s[:4]) not in (0, 1): continue
                # full-year duration only
                from datetime import date
                ds = date.fromisoformat(s); de = date.fromisoformat(e)
                if not (350 <= (de - ds).days <= 380): continue
            yr = int(x["end"][:4])
            # keep latest filed
            if yr not in out or x["filed"] > out[yr][1]:
                out[yr] = (x["val"], x["filed"])
    return {k: v[0] for k, v in out.items()}
tags = sys.argv[2:]
rows = {t: annual(t) for t in tags}
years = sorted(set(y for r in rows.values() for y in r))
print("year," + ",".join(tags))
for y in years:
    print(str(y) + "," + ",".join(str(round(rows[t][y]/1e6)) if y in rows[t] else "" for t in tags))
