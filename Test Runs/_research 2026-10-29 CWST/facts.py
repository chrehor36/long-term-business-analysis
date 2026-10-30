import json, sys
def series(d, tags, unit="USD", dur=True):
    out = {}
    for tag in tags:
        f = d["facts"].get("us-gaap", {}).get(tag)
        if not f: continue
        for v in f["units"].get(unit, []):
            if v.get("form") not in ("10-K", "10-K/A"): continue
            if dur:
                if v.get("fp") != "FY" or "start" not in v: continue
                from datetime import date
                s = date.fromisoformat(v["start"]); e = date.fromisoformat(v["end"])
                if not 350 <= (e - s).days <= 380: continue
            yr = int(v["end"][:4])
            if yr not in out or v["filed"] < out[yr][1]:   # first-filed vintage
                out[yr] = (v["val"], v["filed"], tag)
    return out
for t in sys.argv[1:]:
    d = json.load(open(f"cache/facts_{t}.json"))
    rev = series(d, ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueServicesNet"])
    oi = series(d, ["OperatingIncomeLoss"])
    da = series(d, ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet", "DepreciationAndAmortization"])
    ta = series(d, ["Assets"], dur=False); gw = series(d, ["Goodwill"], dur=False)
    ia = series(d, ["IntangibleAssetsNetExcludingGoodwill", "FiniteLivedIntangibleAssetsNet"], dur=False)
    print(f"== {t}  (USD M; first-filed; op margin; OI/(assets-goodwill-intangibles) at year end)")
    for y in range(2012, 2026):
        if y in rev and y in oi:
            r = rev[y][0]/1e6; o = oi[y][0]/1e6
            tang = (ta.get(y,(0,))[0] - gw.get(y,(0,))[0] - ia.get(y,(0,))[0])/1e6 if y in ta else float('nan')
            print(f"{y} rev {r:9.1f} OI {o:8.1f} margin {100*o/r:5.1f}%  D&A {da.get(y,(0,))[0]/1e6:7.1f}  assets {ta.get(y,(0,))[0]/1e6:8.0f} gw {gw.get(y,(0,))[0]/1e6:7.0f} intang {ia.get(y,(0,))[0]/1e6:6.0f} tangible {tang:8.0f}  OI/tang {100*o/tang if tang else 0:5.1f}%")
