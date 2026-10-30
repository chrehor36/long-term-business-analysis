import json, sys
d = json.load(open(sys.argv[1]))
f = d["facts"]["us-gaap"]
tags = sys.argv[2].split(",")
for t in tags:
    if t not in f: print(t, "MISSING"); continue
    u = list(f[t]["units"].values())[0]
    seen = {}
    for x in u:
        if x.get("fp") == "FY" and x.get("form","").startswith("10-K"):
            s, e = x.get("start"), x["end"]
            if s and (int(e[:4]) - int(s[:4])) * 12 + int(e[5:7]) - int(s[5:7]) < 11: continue
            seen.setdefault(e, (x["val"], x["accn"]))
    print(t, {k[:4]: round(v[0]/1e3) for k, v in sorted(seen.items()) if k >= "2015"})
