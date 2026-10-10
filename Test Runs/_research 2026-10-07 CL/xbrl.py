# annual (10-K, FY) values of named us-gaap tags from a companyfacts file; latest-filed value per fiscal year end
import json, sys
def annual(path, tags, years=range(2010, 2027)):
    d = json.load(open(path))["facts"]["us-gaap"]
    out = {}
    for t in tags:
        if t not in d: out[t] = {}; continue
        vals = {}
        for unit, arr in d[t]["units"].items():
            for x in arr:
                if x.get("form") not in ("10-K", "10-K/A") or x.get("fp") != "FY": continue
                if "start" in x:
                    from datetime import date
                    s = date.fromisoformat(x["start"]); e = date.fromisoformat(x["end"])
                    if not (350 <= (e - s).days <= 380): continue
                y = int(x["end"][:4])
                if (y not in vals) or x["filed"] > vals[y][1]: vals[y] = (x["val"], x["filed"])
        out[t] = {y: v[0] for y, v in vals.items()}
    return out
if __name__ == "__main__":
    path = sys.argv[1]; tags = sys.argv[2].split(",")
    o = annual(path, tags)
    ys = sorted({y for t in o for y in o[t] if y >= int(sys.argv[3] if len(sys.argv) > 3 else 2012)})
    print("tag".ljust(55), *[str(y).rjust(8) for y in ys])
    for t in tags:
        print(t[:55].ljust(55), *[(f"{o[t][y]/1e6:8.0f}" if y in o[t] and abs(o[t][y])>1e4 else (f"{o[t][y]:8.2f}" if y in o[t] else "       -")) for y in ys])
