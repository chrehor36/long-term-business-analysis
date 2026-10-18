"""Annual (FY, 10-K, 12-month) values from companyfacts; latest filed vintage per fiscal-year end. Usage: facts.py TICKER tag [tag...]"""
import json, sys, os
here = os.path.dirname(os.path.abspath(__file__))
def series(t, tag):
    d = json.load(open(os.path.join(here, "cache", "edgar", f"facts_{t}.json")))
    for ns in ("us-gaap", "dei"):
        if tag in d["facts"].get(ns, {}):
            u = d["facts"][ns][tag]["units"]
            vals = list(u.values())[0]
            break
    else:
        return {}
    out = {}
    from datetime import date
    for v in vals:
        if v.get("form") not in ("10-K", "10-K/A", "10-KT"): continue
        if "start" in v:
            s = date.fromisoformat(v["start"]); e = date.fromisoformat(v["end"])
            if not (350 <= (e - s).days <= 380): continue
        key = v["end"]
        if key not in out or v["filed"] > out[key][1]:
            out[key] = (v["val"], v["filed"], v["accn"])
    return out
if __name__ == "__main__":
    t = sys.argv[1]
    for tag in sys.argv[2:]:
        s = series(t, tag)
        print(tag)
        for k in sorted(s):
            if k >= "2013": print("  ", k, round(s[k][0]/1e6, 1) if abs(s[k][0])>1e4 else s[k][0], s[k][2])
