import json, sys, os
d = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cache", "data.sec.gov_api_xbrl_companyfacts_CIK0000106640.json")))
g = d["facts"]["us-gaap"]
tags = sys.argv[1:]
for t in tags:
    if t not in g: print(t, "MISSING"); continue
    rows = {}
    for unit, arr in g[t]["units"].items():
        for x in arr:
            if x.get("fp") == "FY" and x.get("form") == "10-K":
                s, e = x.get("start"), x["end"]
                if s and (int(e[:4]) - int(s[:4]) == 1 or s[5:7] == "01") and e[5:7] == "12":
                    if s and s[:4] != e[:4]: continue
                    key = e[:4]
                    # keep first-filed
                    if key not in rows or x["filed"] < rows[key][1]:
                        rows[key] = (x["val"], x["filed"], x["accn"])
                elif not s and e[5:7] == "12":
                    key = e[:4]
                    if key not in rows or x["filed"] < rows[key][1]:
                        rows[key] = (x["val"], x["filed"], x["accn"])
    print(t, " ".join(f"{k}:{v[0]/1e6:.0f}" for k, v in sorted(rows.items()) if k >= "2010"))
