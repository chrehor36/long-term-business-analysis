import json, sys
from datetime import date
def load(t):
    return json.load(open(f"cache/cf_{t}.json"))
def annual(cf, tag, ns="us-gaap", unit="USD", mode="latest"):
    try: u = cf["facts"][ns][tag]["units"][unit]
    except KeyError: return {}
    out = {}
    for f in u:
        if f.get("form") not in ("10-K","10-K/A"): continue
        if "start" in f:
            d = (date.fromisoformat(f["end"]) - date.fromisoformat(f["start"])).days
            if d < 350 or d > 380: continue
        y = f["end"][:4]
        key = (y)
        if mode == "first":
            if y not in out or f["filed"] < out[y][1]: out[y] = (f["val"], f["filed"], f["accn"])
        else:
            if y not in out or f["filed"] > out[y][1]: out[y] = (f["val"], f["filed"], f["accn"])
    return out
def tags(cf, sub):
    for ns in cf["facts"]:
        for t in cf["facts"][ns]:
            if sub.lower() in t.lower(): print(ns, t)
if __name__ == "__main__":
    t = sys.argv[1]; cf = load(t)
    if sys.argv[2] == "find": tags(cf, sys.argv[3]); sys.exit()
    mode = sys.argv[3] if len(sys.argv) > 3 else "latest"
    ns = "us-gaap"; tag = sys.argv[2]
    if ":" in tag: ns, tag = tag.split(":")
    r = annual(cf, tag, ns, mode=mode)
    for y in sorted(r): print(y, r[y])
