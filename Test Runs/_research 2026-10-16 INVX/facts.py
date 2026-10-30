import sys, json, os, time, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get, OUT
def facts(cik):
    p = os.path.join(OUT, f"cf_{cik}.json")
    if not os.path.exists(p):
        open(p, "wb").write(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json"))
    return json.load(open(p))
def annual(d, tags, mode="last"):
    g = d["facts"].get("us-gaap", {})
    res = {}
    for tag in tags:
        if tag not in g: continue
        for unit, arr in g[tag]["units"].items():
            for x in arr:
                if x.get("form") not in ("10-K", "10-K/A") or x.get("fp") != "FY": continue
                if "start" in x:
                    from datetime import date
                    s = date.fromisoformat(x["start"]); e = date.fromisoformat(x["end"])
                    if not (350 <= (e - s).days <= 380): continue
                fy = x["end"][:4]
                key = (fy)
                prev = res.get(key)
                # first-filed vintage
                if prev is None or (mode == "first" and x["filed"] < prev[1]) or (mode == "last" and x["filed"] > prev[1]):
                    res[key] = (x["val"], x["filed"], tag, x.get("accn"))
        if res and mode != "all": pass
    return res
if __name__ == "__main__":
    cik = sys.argv[1]; mode = sys.argv[2]; tags = sys.argv[3:]
    d = facts(cik)
    print(d["entityName"])
    for t in tags:
        r = annual(d, t.split("|"), mode)
        print(t, {k: (round(v[0]/1e6, 1), v[1], v[3]) for k, v in sorted(r.items()) if k >= "2012"})
