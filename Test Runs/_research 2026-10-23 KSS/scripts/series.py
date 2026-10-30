import json, sys, datetime as dt
f = json.load(open(sys.argv[1]))["facts"]
tags = sys.argv[2].split(",")
def annual(tag):
    for ns in ("us-gaap","dei"):
        if tag in f.get(ns,{}):
            units = f[ns][tag]["units"]
            u = list(units)[0]
            out = {}
            for x in units[u]:
                if x.get("form","").startswith("10-K"):
                    if "start" in x:
                        d = (dt.date.fromisoformat(x["end"]) - dt.date.fromisoformat(x["start"])).days
                        if d < 350: continue
                    out.setdefault(x["end"], x["val"])  # first filed vintage
            return out
    return {}
data = {t: annual(t) for t in tags}
ends = sorted(set(e for t in data for e in data[t]))
ends = [e for e in ends if e >= "2014-12-01"]
print("end".ljust(12) + "".join(t[:14].rjust(15) for t in tags))
for e in ends:
    print(e.ljust(12) + "".join((f"{data[t][e]/1e6:,.0f}" if e in data[t] else "-").rjust(15) for t in tags))
