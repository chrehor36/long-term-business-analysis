"""Competitor row for the HON run: operating margin and operating income on tangible assets from each company's own
10-K XBRL facts (SEC company facts API). Transcription and arithmetic only. Raw JSON is cached under cache/.
Usage: python -I peers.py
"""
import datetime, json, os, time, urllib.request

UA = "LTBA research chrehor36@gmail.com"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
PEERS = {"EMR": 32604, "ROK": 1024478, "JCI": 833444, "ZBRA": 877212, "MSA": 66570, "ITRI": 780571, "HON": 773840}


def facts(cik):
    p = os.path.join(CACHE, f"facts_{cik}.json")
    if not os.path.exists(p):
        req = urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json",
                                     headers={"User-Agent": UA})
        open(p, "wb").write(urllib.request.urlopen(req, timeout=60).read())
        time.sleep(0.3)
    return json.load(open(p))


def annual(f, tag):
    """FY values from 10-K filings, keyed by fiscal-year end date; the latest filing's value for each date."""
    out = {}
    node = f["facts"].get("us-gaap", {}).get(tag)
    if not node:
        return out
    for unit, vals in node["units"].items():
        if unit != "USD":
            continue
        for v in vals:
            if v.get("form") not in ("10-K", "10-K/A") or v.get("fp") != "FY":
                continue
            if "start" in v:
                d0 = v["start"]; d1 = v["end"]
                days = (datetime.date.fromisoformat(d1) - datetime.date.fromisoformat(d0)).days
                if days < 340:
                    continue
            out[v["end"]] = (v["val"], v["accn"])
    return out


def first(f, tags):
    """Union over the tags; an earlier tag wins for a date both carry."""
    out, used = {}, []
    for t in reversed(tags):
        a = annual(f, t)
        if a:
            out.update(a); used.append(t)
    return out, "+".join(reversed(used)) or None


for tk, cik in PEERS.items():
    f = facts(cik)
    rev, rt = first(f, ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"])
    oi, ot = first(f, ["OperatingIncomeLoss"])
    if not oi or max(oi) < "2023-01-01":
        oi, ot = first(f, ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"])
        ot = "PRE-TAX INCOME (no operating-income tag): " + str(ot)
    ta, _ = first(f, ["Assets"])
    gw, _ = first(f, ["Goodwill"])
    ia, _ = first(f, ["IntangibleAssetsNetExcludingGoodwill", "FiniteLivedIntangibleAssetsNet"])
    print(f"{tk}  revenue tag {rt}; profit tag {ot}")
    for end in sorted(rev):
        if end < "2019-01-01" or end not in oi:
            continue
        r = rev[end][0]; o = oi[end][0]
        line = f"  FY{end}  revenue {r/1e6:,.0f}  op income {o/1e6:,.0f}  margin {o/r:.1%}"
        if end in ta and end in gw:
            tang = ta[end][0] - gw[end][0] - (ia[end][0] if end in ia else 0)
            line += f"  tangible assets {tang/1e6:,.0f}  op income/tangible {o/tang:.1%}"
        line += f"  accn {oi[end][1]}"
        print(line)
