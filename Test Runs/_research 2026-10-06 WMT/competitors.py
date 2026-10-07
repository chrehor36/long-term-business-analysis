"""Competitor row: annual revenue, cost of sales, operating income from each competitor's own 10-K XBRL (SEC companyfacts),
with the accession of the filing each figure came from. Same metrics for WMT. Raw JSON cached under cache/ (gitignored).
Usage: python competitors.py"""
import json, os, time, urllib.request

UA = "LTBA research chrehor36@gmail.com"
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
COS = {"WMT": 104169, "COST": 909832, "TGT": 27419, "KR": 56873, "AMZN": 1018724}
TAGS = {
    "rev": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"],
    "cogs": ["CostOfGoodsAndServicesSold", "CostOfRevenue", "CostOfGoodsSold", "MerchandiseCostsAndOccupancy"],
    "opinc": ["OperatingIncomeLoss"],
}


def facts(cik):
    fn = os.path.join(CACHE, f"companyfacts_{cik}.json")
    if not os.path.exists(fn):
        req = urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json", headers={"User-Agent": UA})
        open(fn, "wb").write(urllib.request.urlopen(req, timeout=60).read())
        time.sleep(0.4)
    return json.load(open(fn))


def annual(f, tag):
    u = f["facts"].get("us-gaap", {}).get(tag, {}).get("units", {}).get("USD", [])
    out = {}
    for x in u:
        if x.get("form") == "10-K" and x.get("fp") == "FY" and x.get("frame") is None or (x.get("form") == "10-K" and x.get("fp") == "FY"):
            # keep full-year durations only (about 52-53 weeks)
            if "start" in x:
                from datetime import date
                d = (date.fromisoformat(x["end"]) - date.fromisoformat(x["start"])).days
                if 350 <= d <= 380:
                    out[x["end"]] = (x["val"], x["accn"], x["filed"])
    return out


for tk, cik in COS.items():
    f = facts(cik)
    row = {}
    for k, tags in TAGS.items():
        for tg in tags:
            a = annual(f, tg)
            if a:
                row[k] = (tg, a)
                break
    ends = sorted(row.get("opinc", (None, {}))[1].keys())[-3:]
    print(f"== {tk}")
    for e in ends:
        rv = row["rev"][1].get(e) if "rev" in row else None
        cg = row["cogs"][1].get(e) if "cogs" in row else None
        op = row["opinc"][1].get(e)
        s = f"  FY end {e}: revenue {rv[0]/1e6:,.0f}M" if rv else f"  FY end {e}: revenue n/a"
        if rv and cg:
            s += f"; gross margin {(rv[0]-cg[0])/rv[0]:.1%} ({row['cogs'][0]})"
        if rv and op:
            s += f"; operating margin {op[0]/rv[0]:.1%}; op income {op[0]/1e6:,.0f}M"
        s += f"; accn {op[1]} filed {op[2]}"
        print(s)
