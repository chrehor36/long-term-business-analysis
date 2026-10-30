# print annual 12-month values from companyfacts for listed tags, latest-filed value per fiscal year end
import json, sys
from datetime import date
def annual(cik, tags, ns=None):
    d = json.load(open(f"cache/cf_{cik}.json"))
    out = {}
    for nsk, facts in d["facts"].items():
        for t in tags:
            if t not in facts: continue
            for unit, vals in facts[t]["units"].items():
                for v in vals:
                    if v.get("form") not in ("10-K", "20-F", "10-K/A", "20-F/A"): continue
                    if "start" in v:
                        s = date.fromisoformat(v["start"]); e = date.fromisoformat(v["end"])
                        if not (350 <= (e - s).days <= 380): continue
                    e = v["end"]
                    key = (t, e[:4])
                    if key not in out or v["filed"] > out[key][1]:
                        out[key] = (v["val"], v["filed"], v["accn"], unit)
    return out
if __name__ == "__main__":
    cik = sys.argv[1]; tags = sys.argv[2].split(",")
    o = annual(cik, tags)
    years = sorted({k[1] for k in o})
    for t in tags:
        row = [t[:45].ljust(45)]
        for y in years:
            v = o.get((t, y))
            row.append(f"{y}:{v[0]/1e6:,.0f}" if v else f"{y}:-")
        print(" ".join(row))
