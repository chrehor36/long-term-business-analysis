"""Print annual (FY, 10-K, 12-month) values of chosen XBRL tags, latest-filed vintage per year. Transcription only."""
import json, sys
d = json.load(open(sys.argv[1]))
g = d["facts"]["us-gaap"]
def annual(tag):
    if tag not in g: return {}
    out = {}
    for unit, rows in g[tag]["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A"): continue
            if "start" in r:
                from datetime import date
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                if not (350 <= (e - s).days <= 380): continue
            y = r["end"][:4]
            # keep the first-filed value for each year (original vintage)
            if y not in out or r["filed"] < out[y][1]:
                out[y] = (r["val"], r["filed"])
    return {k: v[0] for k, v in out.items()}
tags = sys.argv[2:]
data = {t: annual(t) for t in tags}
years = sorted(set(y for t in data.values() for y in t))
print("year".ljust(6) + "".join(t[:22].rjust(24) for t in tags))
for y in years:
    print(y.ljust(6) + "".join((f"{data[t][y]/1e6:,.1f}" if y in data[t] else "-").rjust(24) for t in tags))
