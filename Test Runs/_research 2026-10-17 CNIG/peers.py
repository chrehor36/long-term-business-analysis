# Competitor row (CONVENTION of this run: the 10-K names no rival company): net income / year-end total assets and
# net income / year-end equity, from each filer's own XBRL 10-K facts (first-filed vintage), fiscal years 2013-2025.
import json, urllib.request, os, time
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
def facts(cik):
    p = f"cache/facts_{cik}.json"
    if not os.path.exists(p):
        b = urllib.request.urlopen(urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json", headers=UA), timeout=60).read()
        open(p, "wb").write(b); time.sleep(0.5)
    return json.load(open(p))
def annual(f, tag, dur=True):
    out = {}
    u = f["facts"]["us-gaap"].get(tag, {}).get("units", {}).get("USD", [])
    for x in u:
        if x.get("form") != "10-K": continue
        if dur:
            if "start" not in x: continue
            from datetime import date
            s = date.fromisoformat(x["start"]); e = date.fromisoformat(x["end"])
            if not 340 <= (e - s).days <= 380: continue
        k = x["end"]
        if k not in out or x["filed"] < out[k][1]: out[k] = (x["val"], x["filed"], x["accn"])
    return out
for name, cik in [("CNIG", 1582244), ("RGCO RGC Resources", 1069533), ("OGS ONE Gas", 1587732)]:
    f = facts(cik)
    ni = annual(f, "NetIncomeLoss"); ta = annual(f, "Assets", False)
    eq = annual(f, "StockholdersEquity", False)
    print("==", name)
    for k in sorted(ni):
        if k < "2013": continue
        a = ta.get(k, (None,))[0]; e = eq.get(k, (None,))[0]
        print(f"  {k}  NI {ni[k][0]/1e6:9.2f}M  assets {a/1e6 if a else float('nan'):9.1f}M  NI/assets {100*ni[k][0]/a if a else float('nan'):5.2f}%  NI/equity {100*ni[k][0]/e if e else float('nan'):5.2f}%  accn {ni[k][2]}")
