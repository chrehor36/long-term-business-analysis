import json, sys
d = json.load(open("cache/filings/facts.json"))
g = d["facts"]["us-gaap"]
pat = [p.lower() for p in sys.argv[1:]]
for k, v in g.items():
    if any(p in k.lower() for p in pat):
        units = v["units"]
        for u, arr in units.items():
            fy = {}
            for x in arr:
                if x.get("form") == "10-K" and x.get("fp") == "FY" and x.get("frame") and "Q" not in x["frame"]:
                    fy[x["end"]] = x["val"]
            if fy:
                ks = sorted(fy)[-11:]
                print(k, u, " ".join(f"{e[:4]}:{fy[e]/1e6 if abs(fy[e])>1e5 else fy[e]:.0f}" for e in ks))
