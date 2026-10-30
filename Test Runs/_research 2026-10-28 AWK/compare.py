"""Competitor row: same metrics from each filer's own XBRL (10-K, FY, latest vintage per year).
ROE = net income / average common equity; operating margin = operating income / revenue;
cash after all capex = OCF - capex - removal(not tagged everywhere, so OCF - PaymentsToAcquirePPE) per revenue.
Usage: python -I compare.py"""
import json, os
from datetime import date
HERE = os.path.dirname(os.path.abspath(__file__))
COS = {"AWK": "0001410636", "WTRG": "0000078128", "AWR": "0001056903", "CWT": "0001035201"}
TAGS = {
    "ni": ["NetIncomeLoss", "NetIncomeLossAvailableToCommonStockholdersBasic", "ProfitLoss"],
    "eq": ["StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],
    "rev": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "RegulatedAndUnregulatedOperatingRevenue", "OperatingRevenue"],
    "oi": ["OperatingIncomeLoss"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets", "PaymentsForProceedsFromProductiveAssets"],
    "da": ["DepreciationDepletionAndAmortization", "DepreciationAndAmortization", "Depreciation"],
}

def series(g, names, instant=False):
    acc, used = {}, []
    for n in names:
        if n not in g:
            continue
        out = {}
        for u, rows in g[n]["units"].items():
            if u != "USD":
                continue
            for r in rows:
                if r.get("form") not in ("10-K", "10-K/A"):
                    continue
                if not instant:
                    if "start" not in r:
                        continue
                    d = (date.fromisoformat(r["end"]) - date.fromisoformat(r["start"])).days
                    if not 350 <= d <= 380:
                        continue
                y = int(r["end"][:4]) if r["end"][5:7] == "12" else None
                if y is None:
                    continue
                if y not in out or r["filed"] > out[y][1]:
                    out[y] = (r["val"] / 1e6, r["filed"], r["accn"])
        merged = {k: v[0] for k, v in out.items()}
        for k, v in merged.items():
            acc.setdefault(k, v)
        used.append(n)
    return acc, "+".join(used) if used else None

res = {}
for co, cik in COS.items():
    j = json.load(open(os.path.join(HERE, "cache", f"facts_{cik}.json"), encoding="utf-8"))
    g = j["facts"]["us-gaap"]
    d = {}
    for k, names in TAGS.items():
        d[k], tag = series(g, names, instant=(k == "eq"))
        d[k + "_tag"] = tag
    res[co] = d

years = list(range(2016, 2026))
for co, d in res.items():
    print(f"\n{co}  tags: " + ", ".join(f"{k}={d[k+'_tag']}" for k in TAGS))
    print("  year    rev     oi   oi/rev    ni   avgEq   ROE   ocf-capex  (ocf-capex)/rev  capex/da")
    roes, margins, fcf = [], [], []
    for y in years:
        rev = d["rev"].get(y); oi = d["oi"].get(y); ni = d["ni"].get(y)
        e1, e0 = d["eq"].get(y), d["eq"].get(y - 1)
        ocf, cx, da = d["ocf"].get(y), d["capex"].get(y), d["da"].get(y)
        roe = ni / ((e1 + e0) / 2) if ni and e1 and e0 else None
        m = oi / rev if oi and rev else None
        f = (ocf - cx) if ocf is not None and cx is not None else None
        cr = cx / da if cx and da else None
        if roe: roes.append(roe)
        if m: margins.append(m)
        if f is not None and rev: fcf.append(f / rev)
        fmt = lambda v, p=0: "    -" if v is None else (f"{v*100:5.1f}%" if p else f"{v:7,.0f}")
        print(f"  {y} {fmt(rev)} {fmt(oi)} {fmt(m,1)} {fmt(ni)} {fmt((e1+e0)/2 if e1 and e0 else None)} {fmt(roe,1)} {fmt(f)} {fmt(f/rev if f is not None and rev else None,1)} {'' if cr is None else f'{cr:4.2f}x'}")
    if roes and margins and fcf:
        print(f"  mean ROE {sum(roes)/len(roes)*100:.1f}% over {len(roes)} yrs; mean op margin {sum(margins)/len(margins)*100:.1f}% over {len(margins)}; mean (ocf-capex)/rev {sum(fcf)/len(fcf)*100:.1f}% over {len(fcf)}")
    r = d["rev"]
    ys = [y for y in years if y in r]
    if len(ys) >= 2:
        n = ys[-1] - ys[0]
        print(f"  revenue CAGR {ys[0]}-{ys[-1]}: {((r[ys[-1]]/r[ys[0]])**(1/n)-1)*100:.1f}%")

