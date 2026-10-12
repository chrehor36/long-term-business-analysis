import json, sys
d = json.load(open(sys.argv[1]))
g = d["facts"]["us-gaap"]
for tag in sys.argv[2:]:
    if tag not in g: print(tag, "none"); continue
    out = {}
    for u, arr in g[tag]["units"].items():
        for x in arr:
            if x.get("form") != "10-K" or "start" in x: continue
            if not x["end"].endswith("12-31"): continue
            y = int(x["end"][:4])
            if y not in out or x["filed"] > out[y][1]: out[y] = (x["val"], x["filed"])
    print(tag, {k: round(v[0]/1e6) for k, v in sorted(out.items()) if k >= 2012})
