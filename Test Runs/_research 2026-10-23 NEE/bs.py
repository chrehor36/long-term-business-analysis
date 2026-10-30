import json, sys
cf = json.load(open(sys.argv[1]))
def inst(tag):
    f = cf["facts"]["us-gaap"].get(tag)
    if not f: return {}
    out = {}
    for u, rows in f["units"].items():
        if u != "USD": continue
        for r in rows:
            if r.get("form") not in ("10-K",) or "start" in r or r["end"][5:] != "12-31": continue
            y = r["end"][:4]
            if y not in out or r["filed"] > out[y][1]:
                out[y] = (r["val"], r["filed"])
    return out
tags = sys.argv[2:]
years = [str(y) for y in range(2015, 2026)]
print("tag".ljust(50), " ".join(y.rjust(8) for y in years))
for t in tags:
    d = inst(t)
    print(t[:50].ljust(50), " ".join((str(round(d[y][0]/1e6)) if y in d else "-").rjust(8) for y in years))
