# print annual (10-K, FY, 12-month or instant) values for given us-gaap tags, latest filed value per fiscal-year end
import json, sys
def annual(cf, tag, unit="USD"):
    f = cf["facts"].get("us-gaap", {}).get(tag) or cf["facts"].get("dei", {}).get(tag)
    if not f: return {}
    out = {}
    for u, rows in f["units"].items():
        if u != unit: continue
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A"): continue
            end = r["end"]
            if "start" in r:
                from datetime import date
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(end)
                if not (350 <= (e - s).days <= 380): continue
            y = end[:4]
            if end[5:7] != "12": continue
            # prefer the latest filing
            if y not in out or r["filed"] > out[y][1]:
                out[y] = (r["val"], r["filed"], r["accn"])
    return out
if __name__ == "__main__":
    cf = json.load(open(sys.argv[1]))
    for tag in sys.argv[2:]:
        a = annual(cf, tag)
        print(tag, {y: round(v[0]/1e6) for y, v in sorted(a.items()) if y >= "2014"})
