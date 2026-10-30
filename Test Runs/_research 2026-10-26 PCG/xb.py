"""usage: xb.py facts.json tag [tag...] -- print FY annual values (10-K, full-year duration or instant at FY end)"""
import json, sys, datetime
f = json.load(open(sys.argv[1]))
def get(tag):
    for ns in ("us-gaap","ifrs-full","dei","pcg"):
        if tag in f["facts"].get(ns,{}): return f["facts"][ns][tag]
    return None
for tag in sys.argv[2:]:
    t = get(tag)
    if not t: print(tag, "NONE"); continue
    for unit, vals in t["units"].items():
        out = {}
        for v in vals:
            if v.get("form") not in ("10-K","10-K/A"): continue
            end = v["end"]
            if "start" in v:
                d = (datetime.date.fromisoformat(end)-datetime.date.fromisoformat(v["start"])).days
                if not 350 <= d <= 380: continue
            if not end.endswith("12-31"): continue
            y = end[:4]
            # keep latest filed value (restated) but record first too
            out.setdefault(y, []).append((v["filed"], v["val"], v["accn"]))
        row = []
        for y in sorted(out):
            if int(y) < 2014: continue
            vs = sorted(out[y]); row.append(f"{y}:{vs[-1][1]/1e6 if unit=='USD' else vs[-1][1]:,.0f}")
        print(tag, unit, " ".join(row))
