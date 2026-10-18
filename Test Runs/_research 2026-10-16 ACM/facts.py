import json, sys
def load(t): return json.load(open(f"cache/facts_{t}.json"))
def annual(d, tag, ns="us-gaap", unit="USD"):
    out = {}
    try: rows = d["facts"][ns][tag]["units"][unit]
    except KeyError: return out
    for r in rows:
        if r.get("form") not in ("10-K", "10-K/A"): continue
        if "start" in r:
            from datetime import date
            s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
            if not (340 <= (e - s).days <= 380): continue
        fy_end = r["end"]
        # keep earliest filed vintage for each end
        if fy_end not in out or r["filed"] < out[fy_end][1]:
            out[fy_end] = (r["val"], r["filed"], r["accn"])
    return dict(sorted(out.items()))
if __name__ == "__main__":
    t = sys.argv[1]; d = load(t); print(d["entityName"])
    for tag in sys.argv[2:]:
        a = annual(d, tag)
        print(tag); [print("  ", k, round(v[0]/1e6,1), v[2]) for k, v in a.items() if k >= "2014"]
