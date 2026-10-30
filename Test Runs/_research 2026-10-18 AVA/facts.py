import json, sys
def annual(f, tag, unit="USD"):
    d = json.load(open(f))["facts"]
    for ns in ("us-gaap", "dei"):
        if tag in d.get(ns, {}):
            u = d[ns][tag]["units"].get(unit)
            if not u: return {}
            out = {}
            for x in u:
                if x.get("form") in ("10-K", "10-K/A") and x.get("fp") == "FY":
                    if "start" in x:
                        from datetime import date
                        s = date.fromisoformat(x["start"]); e = date.fromisoformat(x["end"])
                        if not (350 <= (e - s).days <= 380): continue
                    y = int(x["end"][:4])
                    # keep latest filed value for the period (restated) -> use first filed? keep latest
                    if y not in out or x["filed"] > out[y][1]:
                        out[y] = (x["val"], x["filed"])
            return {k: v[0] for k, v in out.items()}
    return {}
if __name__ == "__main__":
    f = sys.argv[1]
    for t in sys.argv[2:]:
        a = annual(f, t)
        print(t, {k: round(v/1e6,1) for k, v in sorted(a.items()) if k >= 2014})
