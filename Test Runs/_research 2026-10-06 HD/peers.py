"""Competitor row: same metrics for HD, Lowe's (LOW) and Floor & Decor (FND) from each company's own 10-K XBRL
(first-filed value per fiscal year). Transcription and arithmetic only. Reads cache/*companyfacts.json."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
FILES = {"HD": "companyfacts.json", "LOW": "low_companyfacts.json", "FND": "fnd_companyfacts.json"}
TAGS = {
    "sales": ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet"],
    "gp": ["GrossProfit"],
    "opinc": ["OperatingIncomeLoss"],
    "ni": ["NetIncomeLoss"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities"],
    "sbc": ["ShareBasedCompensation"],
    "capex": ["PaymentsToAcquireProductiveAssets", "PaymentsToAcquirePropertyPlantAndEquipment"],
    "equity": ["StockholdersEquity"],
    "dilshares": ["WeightedAverageNumberOfDilutedSharesOutstanding"],
}

def series(facts, tag, duration=True):
    out = {}
    if tag not in facts:
        return out
    for unit, rows in facts[tag]["units"].items():
        for r in rows:
            if r.get("form") != "10-K":
                continue
            if duration:
                if "start" not in r:
                    continue
                y0, y1 = int(r["start"][:4]), int(r["end"][:4])
                m0, m1 = int(r["start"][5:7]), int(r["end"][5:7])
                months = (y1 - y0) * 12 + (m1 - m0)
                if months < 11:
                    continue
            if r["end"] not in out or r["filed"] < out[r["end"]][1]:
                out[r["end"]] = (r["val"], r["filed"], r["accn"])
    return out

for name, f in FILES.items():
    facts = json.load(open(os.path.join(here, "cache", f)))["facts"]["us-gaap"]
    table = {}
    for k, tags in TAGS.items():
        for t in tags:
            for end, v in series(facts, t, duration=(k != "equity")).items():
                table.setdefault(end, {}).setdefault(k, v)
    ends = [e for e in sorted(table) if e >= "2021-01-01" and "sales" in table[e]][-5:]
    print(f"== {name}")
    print("FY end       sales    opinc  opmarg%   gm%      ocf    sbc   capex  ownercash  oc/sales%  accn(sales)")
    for e in ends:
        r = table[e]
        g = lambda k: r[k][0] / 1e6 if k in r else float("nan")
        oc = g("ocf") - g("sbc") - g("capex")
        print(f"{e}  {g('sales'):8.0f} {g('opinc'):8.0f} {100*g('opinc')/g('sales'):7.1f} {100*g('gp')/g('sales'):6.1f} "
              f"{g('ocf'):8.0f} {g('sbc'):6.0f} {g('capex'):7.0f} {oc:10.0f} {100*oc/g('sales'):9.1f}  {r['sales'][2]}")
    print()
