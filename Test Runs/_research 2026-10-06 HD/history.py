"""Ten fiscal years of HD annual figures from the XBRL company facts (transcription only; cross-checked against filed
statements in the run file). Reads cache/companyfacts.json. Prints USD millions by fiscal year end (10-K, FY frames)."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(here, "cache", "companyfacts.json")))["facts"]["us-gaap"]

TAGS = {
    "sales": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"],
    "opinc": ["OperatingIncomeLoss"],
    "ni": ["NetIncomeLoss"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities"],
    "sbc": ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"],
    "da": ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet"],
    "capex": ["PaymentsToAcquireProductiveAssets", "PaymentsToAcquirePropertyPlantAndEquipment"],
    "acq": ["PaymentsToAcquireBusinessesNetOfCashAcquired"],
    "buyback": ["PaymentsForRepurchaseOfCommonStock"],
    "div": ["PaymentsOfDividendsCommonStock", "PaymentsOfDividends"],
    "interest": ["InterestExpense", "InterestExpenseNonoperating", "InterestExpenseDebt"],
    "pretax": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"],
    "dilshares": ["WeightedAverageNumberOfDilutedSharesOutstanding"],
}

def annual(tag):
    out = {}
    if tag not in d:
        return out
    for unit, rows in d[tag]["units"].items():
        for r in rows:
            if r.get("form") != "10-K" or "start" not in r:
                continue
            days = (int(r["end"][:4]) * 365 + int(r["end"][5:7]) * 30 + int(r["end"][8:10])) - \
                   (int(r["start"][:4]) * 365 + int(r["start"][5:7]) * 30 + int(r["start"][8:10]))
            if days < 350:
                continue
            # first-filed value for each period end
            if r["end"] not in out or r["filed"] < out[r["end"]][1]:
                out[r["end"]] = (r["val"], r["filed"], r["accn"])
    return out

table = {}
for k, tags in TAGS.items():
    for t in tags:
        for end, v in annual(t).items():
            table.setdefault(end, {}).setdefault(k, (v[0], t))
ends = sorted(e for e in table if e >= "2016-01-01")
cols = list(TAGS)
print("FY end      " + " ".join(f"{c:>9}" for c in cols))
for e in ends:
    row = table[e]
    vals = []
    for c in cols:
        if c in row:
            v = row[c][0]
            vals.append(f"{v/1e6:9.0f}" if c != "dilshares" else f"{v/1e6:9.1f}")
        else:
            vals.append(f"{'-':>9}")
    print(e + "  " + " ".join(vals))
print()
for e in ends:
    print(e, {c: table[e][c][1] for c in table[e]})
