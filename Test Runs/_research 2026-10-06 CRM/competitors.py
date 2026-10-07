"""Competitor row: latest 10-K per competitor from EDGAR, revenue and operating income from XBRL companyfacts
(first-filed annual values, FY form 10-K), and the 10-K text saved to cache/ for reading the competitor's own words.
Usage: python -I competitors.py
"""
import json, os, sys, time, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
COS = {"CRM": 1108524, "MSFT": 789019, "NOW": 1373715, "HUBS": 1404655, "ORCL": 1341439}
REV = ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet"]


def annual(facts, tag):
    try:
        units = facts["facts"]["us-gaap"][tag]["units"]["USD"]
    except KeyError:
        return {}
    out = {}
    for u in units:
        if u.get("form") == "10-K" and u.get("fp") == "FY" and "start" in u:
            days = (time.mktime(time.strptime(u["end"], "%Y-%m-%d")) - time.mktime(time.strptime(u["start"], "%Y-%m-%d"))) / 86400
            if 350 < days < 380 and u["end"] not in out:
                out[u["end"]] = (u["val"], u["accn"])
    return out


for tk, cik in COS.items():
    facts = json.loads(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"))
    rev = {}
    for t in REV:
        for k, v in annual(facts, t).items():
            rev.setdefault(k, v)
    op = annual(facts, "OperatingIncomeLoss")
    print(f"== {tk}")
    for end in sorted(rev)[-11:]:
        r, accn = rev[end]
        o = op.get(end, (None, ""))[0]
        m = f"{100*o/r:.1f}%" if o is not None else "n/a"
        print(f"  {end}  revenue {r/1e6:>10,.0f}M  op income {('%10.0fM' % (o/1e6)) if o is not None else '       n/a'}  margin {m:>6}  {accn}")
    if tk == "CRM":
        continue
    sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))["filings"]["recent"]
    for i, f in enumerate(sub["form"]):
        if f == "10-K":
            acc, doc, date = sub["accessionNumber"][i], sub["primaryDocument"][i], sub["filingDate"][i]
            b = get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{doc}")
            with open(os.path.join(OUT, f"comp_{tk}_10K.txt"), "w") as fh:
                fh.write(strip(b))
            print(f"  latest 10-K {date} {acc} {doc} saved")
            break
