"""Operating margin by year from each competitor's own 10-K facts (EDGAR company facts, first-filed vintage).
Transcription; the latest 10-K accession is printed per company. Usage: python peers.py"""
import sys, os, json
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get

PEERS = {"GD": "0000040533", "HII": "0001501585", "LMT": "0000936468", "NOC": "0001133421",
         "TXT": "0000217346", "LDOS": "0001336920", "CACI": "0000016058", "BAH": "0001443646"}
REV = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet",
       "SalesRevenueGoodsNet", "SalesRevenueServicesNet"]
OPI = ["OperatingIncomeLoss"]


def annual(facts, tags):
    out = {}
    for tag in tags:
        node = facts.get("us-gaap", {}).get(tag)
        if not node:
            continue
        for unit, rows in node["units"].items():
            for r in rows:
                if r.get("form") != "10-K" or "start" not in r:
                    continue
                d = (date.fromisoformat(r["end"]) - date.fromisoformat(r["start"])).days
                if not 350 <= d <= 380:
                    continue
                y = int(r["end"][:4])
                if y not in out or r["filed"] < out[y][1]:
                    if y in out and out[y][2] != tag:
                        continue
                    out[y] = (r["val"], r["filed"], tag, r["accn"])
    return out


for t, cik in PEERS.items():
    p = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json", f"companyfacts_{cik}.json")
    f = json.load(open(p))["facts"]
    rev = annual(f, REV); opi = annual(f, OPI)
    yrs = [y for y in sorted(opi) if y in rev and y >= 2012]
    last = max(rev.values(), key=lambda v: v[1])[3] if rev else "?"
    line = ", ".join(f"{y}: {100*opi[y][0]/rev[y][0]:.1f}" for y in yrs)
    print(f"{t} (latest 10-K accession {last}) op margin %: {line}")
