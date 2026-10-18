import json, sys
def annual(path, tags, forms=("10-K","20-F","10-K/A","20-F/A")):
    d = json.load(open(path))
    out = {}
    for t in tags:
        for ns in ("us-gaap","ifrs-full"):
            node = d["facts"].get(ns, {}).get(t)
            if not node: continue
            for unit, vals in node["units"].items():
                for v in vals:
                    if v.get("form") not in forms: continue
                    if "start" in v:
                        from datetime import date
                        s = date.fromisoformat(v["start"]); e = date.fromisoformat(v["end"])
                        if not (350 <= (e-s).days <= 380): continue
                    fy = v["end"][:4]
                    key = (t, fy)
                    # keep latest filed
                    if key not in out or v["filed"] > out[key][1]:
                        out[key] = (v["val"], v["filed"], v["accn"])
    return out
if __name__ == "__main__":
    path = sys.argv[1]; tags = sys.argv[2].split(",")
    o = annual(path, tags)
    years = sorted({k[1] for k in o})
    for t in tags:
        row = [t[:38].ljust(38)]
        for y in years:
            v = o.get((t,y))
            row.append(f"{y}:{v[0]/1e6:,.0f}" if v else f"{y}:-")
        print(" ".join(row))
