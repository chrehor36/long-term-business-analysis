"""ROE = net income attributable to common / average common equity, from XBRL companyfacts (first-filed 10-K values). Usage: python roe.py facts.json [NI tag] """
import json, sys, os
from datetime import date
d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache", sys.argv[1])))
g = d["facts"]["us-gaap"]
def series(tag, dur):
    out = {}
    if tag not in g: return out
    for r in g[tag]["units"]["USD"]:
        if r.get("form") not in ("10-K",): continue
        if dur:
            if "start" not in r: continue
            if not (350 <= (date.fromisoformat(r["end"]) - date.fromisoformat(r["start"])).days <= 380): continue
        if r["end"] not in out or r["filed"] < out[r["end"]][1]:
            out[r["end"]] = (r["val"], r["filed"], r["accn"])
    return out
ni = {}
for t in ["NetIncomeLossAvailableToCommonStockholdersBasic", "NetIncomeLoss"]:
    s = series(t, True)
    for k, v in s.items(): ni.setdefault(k, v)
eq = series("StockholdersEquity", False)
yrs = sorted(k for k in ni if k[5:] == "12-31" and "2015-12-31" <= k <= "2025-12-31")
tot = []
for k in yrs:
    prev = str(int(k[:4]) - 1) + "-12-31"
    if k in eq and prev in eq:
        avg = (eq[k][0] + eq[prev][0]) / 2
        r = ni[k][0] / avg
        tot.append((k, r))
        print(k, f"NI {ni[k][0]/1e6:,.0f}  avgEq {avg/1e6:,.0f}  ROE {r*100:5.1f}%  accn {ni[k][2]}")
w = [r for k, r in tot if k >= "2016-12-31"]
print("mean ROE 2016-2025:", f"{sum(w)/len(w)*100:.1f}%", "n=", len(w))
