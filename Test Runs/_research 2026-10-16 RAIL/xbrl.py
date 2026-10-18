"""Print annual (10-K, FY, 12-month) values of chosen us-gaap tags from a cached companyfacts file."""
import json, sys
def annual(path, tag, unit="USD"):
    d = json.load(open(path))
    f = d["facts"].get("us-gaap", {}).get(tag)
    if not f: return {}
    out = {}
    for u, rows in f["units"].items():
        if u != unit: continue
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A", "10-KT"): continue
            s, e = r.get("start"), r["end"]
            if s:
                from datetime import date
                ds, de = date.fromisoformat(s), date.fromisoformat(e)
                if not (350 <= (de - ds).days <= 380): continue
            # keep the first-filed value for each end date
            if e not in out or r["filed"] < out[e][1]:
                out[e] = (r["val"], r["filed"], r["accn"])
    return out
if __name__ == "__main__":
    path = sys.argv[1]
    for tag in sys.argv[2:]:
        a = annual(path, tag)
        print(tag)
        for e in sorted(a):
            print("  ", e, round(a[e][0]/1e6, 1), a[e][2])
