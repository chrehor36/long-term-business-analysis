import json, os, sys, time, urllib.request, datetime

HDR = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
D = os.path.dirname(os.path.abspath(__file__))
PEERS = {
    "APH":  "0000820313",   # Amphenol - connectors
    "TEL":  "0001385157",   # TE Connectivity - connectors
    "LFUS": "0000889331",   # Littelfuse - circuit protection
    "VICR": "0000751978",   # Vicor - board-mount power
    "AEIS": "0000927003",   # Advanced Energy - embedded/front-end power
    "MEI":  "0000065270",   # Methode Electronics
    "CTS":  "0000026058",   # CTS Corp
    "SXI":  "0000310354",   # Standex International
    "RFIL": "0000740664",   # RF Industries
    "ALNT": "0000046129",   # Allient Inc
    "VSH":  "0000103730",
    "BELFB":"0000729580",
}

def facts(cik):
    fn = os.path.join(D, "peers_%s.json" % cik)
    if not os.path.exists(fn):
        u = "https://data.sec.gov/api/xbrl/companyfacts/CIK%s.json" % cik
        r = urllib.request.Request(u, headers=HDR)
        data = urllib.request.urlopen(r, timeout=60).read()
        open(fn, "wb").write(data)
        time.sleep(0.3)
    return json.load(open(fn))

def dur(g, tags, forms=("10-K", "10-K/A")):
    out = {}
    for t in tags:
        if t not in g:
            continue
        for u, rows in g[t]["units"].items():
            for r in rows:
                if r.get("form") not in forms or not r.get("start"):
                    continue
                d1 = datetime.date.fromisoformat(r["start"])
                d2 = datetime.date.fromisoformat(r["end"])
                if not (330 <= (d2 - d1).days <= 400):
                    continue
                p = out.get(r["end"])
                if p is None or r["filed"] > p[1]:
                    out[r["end"]] = (r["val"], r["filed"], t)
    return out

def inst(g, tags, forms=("10-K", "10-K/A")):
    out = {}
    for t in tags:
        if t not in g:
            continue
        for u, rows in g[t]["units"].items():
            for r in rows:
                if r.get("form") not in forms or r.get("start"):
                    continue
                p = out.get(r["end"])
                if p is None or r["filed"] > p[1]:
                    out[r["end"]] = (r["val"], r["filed"], t)
    return out

REV = ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues",
       "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueNet", "SalesRevenueGoodsNet"]
COGS = ["CostOfGoodsAndServicesSold", "CostOfRevenue", "CostOfGoodsSold", "CostOfSales"]
GP = ["GrossProfit"]
OI = ["OperatingIncomeLoss"]
TA = ["Assets"]
TL = ["Liabilities"]
GW = ["Goodwill"]
IN = ["FiniteLivedIntangibleAssetsNet", "IntangibleAssetsNetExcludingGoodwill"]
DEBT = ["LongTermDebtNoncurrent", "LongTermDebt", "LongTermDebtAndCapitalLeaseObligations"]
DEBTC = ["LongTermDebtCurrent", "LinesOfCreditCurrent", "ShortTermBorrowings", "OtherShortTermBorrowings"]

rows = []
for tk, cik in PEERS.items():
    try:
        f = facts(cik)
    except Exception as e:
        print(tk, "FETCH FAIL", e)
        continue
    g = f["facts"].get("us-gaap", {})
    rev, gp, cogs, oi = dur(g, REV), dur(g, GP), dur(g, COGS), dur(g, OI)
    ta, tl, gw, ia = inst(g, TA), inst(g, TL), inst(g, GW), inst(g, IN)
    dbt, dbtc = inst(g, DEBT), inst(g, DEBTC)
    # newest fiscal year end that has revenue AND operating income
    cands = sorted(set(rev) & set(oi))
    if not cands:
        print(tk, "NO FY")
        continue
    e = cands[-1]
    R = rev[e][0]
    O = oi[e][0]
    G = gp[e][0] if e in gp else (R - cogs[e][0] if e in cogs else None)
    A = ta.get(e, (None,))[0]
    L = tl.get(e, (None,))[0]
    W = gw.get(e, (0,))[0] or 0
    I = ia.get(e, (0,))[0] or 0
    Dn = dbt.get(e, (0,))[0] or 0
    Dc = dbtc.get(e, (0,))[0] or 0
    nta = None
    if A is not None and L is not None:
        nta = A - W - I - (L - Dn - Dc)
    rows.append(dict(tk=tk, fy=e, rev=R, gm=(G / R if G else None), om=O / R,
                     oi=O, nta=nta, ronta=(O / nta if nta else None),
                     gw=W, ia=I, assets=A, liab=L, debt=Dn + Dc,
                     src=dict(rev=rev[e][2], oi=oi[e][2], filed=rev[e][1])))

rows.sort(key=lambda r: -(r["rev"] or 0))
print("%-6s %-11s %12s %7s %7s %12s %8s  %s" % ("tkr", "FY end", "rev $m", "GM%", "OM%", "NTA $m", "EBIT/NTA", "newest 10-K filed"))
for r in rows:
    print("%-6s %-11s %12.0f %7s %7.1f %12s %8s  %s" % (
        r["tk"], r["fy"], r["rev"] / 1e6,
        ("%.1f" % (r["gm"] * 100)) if r["gm"] else "n/a",
        r["om"] * 100,
        ("%.0f" % (r["nta"] / 1e6)) if r["nta"] else "n/a",
        ("%.1f%%" % (r["ronta"] * 100)) if r["ronta"] else "n/a",
        r["src"]["filed"]))
json.dump(rows, open(os.path.join(D, "peer_row.json"), "w"), indent=1)
