import json, sys
d = json.load(open("cache/facts.json"))
def series(tag, ns="us-gaap", form="10-K"):
    try: units = d["facts"][ns][tag]["units"]
    except KeyError: return {}
    out = {}
    for u, rows in units.items():
        for r in rows:
            if r.get("form") != form or r.get("fp") != "FY": continue
            if "start" in r:
                s, e = r["start"], r["end"]
                if int(e[:4]) - int(s[:4]) != 1 and not (s[5:7]=="01" and e[5:7]=="12"): continue
                if s[5:7] != "01": continue
            y = r["end"][:4]
            # keep first-filed? keep latest filed
            if y not in out or r["filed"] > out[y][1]: out[y] = (r["val"], r["filed"])
    return {k: v[0] for k, v in out.items()}
tags = sys.argv[1:]
for t in tags:
    ns = "us-gaap"
    if ":" in t: ns, t = t.split(":")
    s = series(t, ns)
    print(f"{t:60s}", " ".join(f"{y}:{v/1e6:,.1f}" for y, v in sorted(s.items()) if y >= "2014"))
