"""Print annual (10-K, FY, 12-month) values of chosen us-gaap tags from cached companyfacts. Usage: facts.py TICKER tag1 tag2 ..."""
import json, sys
t = sys.argv[1]; tags = sys.argv[2:]
d = json.load(open(f"cache/facts_{t}.json"))["facts"]["us-gaap"]
from datetime import date
def days(a,b): return (date.fromisoformat(b)-date.fromisoformat(a)).days
out = {}
for tag in tags:
    if tag not in d: print("missing", tag); continue
    for unit, vals in d[tag]["units"].items():
        for v in vals:
            if v.get("form") not in ("10-K","10-K/A","10-KT"): continue
            if "start" in v and not (330 < days(v["start"], v["end"]) < 400): continue
            key = (v["end"], tag)
            # keep first filed
            if key not in out or v["filed"] < out[key][1]: out[key] = (v["val"], v["filed"], v["accn"])
ends = sorted({k[0] for k in out})
print("end       " + " ".join(f"{x[:26]:>26}" for x in tags))
for e in ends:
    print(e, " ".join(f"{(out[(e,x)][0]/1e3 if (e,x) in out else float('nan')):>26,.0f}" for x in tags))
