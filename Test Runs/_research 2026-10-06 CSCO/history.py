"""Annual (10-K, full fiscal year) series from the XBRL company facts in cache/facts.json.
Transcription only; the filed statements are the record. Usage: python -I history.py"""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(here, "cache", "facts.json")))["facts"]["us-gaap"]

TAGS = {
    "revenue": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"],
    "product_rev": ["RevenueFromContractWithCustomerExcludingAssessedTax:product"],
    "gross_profit": ["GrossProfit"],
    "op_income": ["OperatingIncomeLoss"],
    "pretax": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
               "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"],
    "net_income": ["NetIncomeLoss"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
    "sbc": ["ShareBasedCompensation"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment"],
    "da": ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndOther"],
    "rnd": ["ResearchAndDevelopmentExpense"],
    "buyback": ["PaymentsForRepurchaseOfCommonStock"],
    "dividends": ["PaymentsOfDividendsCommonStock", "PaymentsOfDividends"],
    "acq": ["PaymentsToAcquireBusinessesNetOfCashAcquired"],
    "diluted_shares": ["WeightedAverageNumberOfDilutedSharesOutstanding"],
    "restructuring": ["RestructuringCharges"],
    "amort_intang": ["AmortizationOfIntangibleAssets"],
    "interest_exp": ["InterestExpense", "InterestExpenseNonoperating"],
}


def annual(tag):
    out = {}
    node = d.get(tag)
    if not node:
        return out
    for unit, rows in node["units"].items():
        for r in rows:
            if r.get("form") != "10-K" or r.get("fp") != "FY":
                continue
            if "start" in r:
                from datetime import date
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                if not (350 <= (e - s).days <= 380):
                    continue
            end = r["end"]
            # first-filed vintage
            if end not in out or r["filed"] < out[end][1]:
                out[end] = (r["val"], r["filed"])
    return out


series = {}
for k, tags in TAGS.items():
    merged = {}
    for t in tags:
        if ":" in t:
            continue
        for end, v in annual(t).items():
            merged.setdefault(end, v)
    series[k] = merged

ends = sorted(set().union(*[set(s) for s in series.values()]))
ends = [e for e in ends if e >= "2008-01-01"]
cols = list(TAGS)
print("fiscal_end," + ",".join(cols))
for e in ends:
    row = []
    for c in cols:
        v = series[c].get(e)
        if v is None:
            row.append("")
        elif c == "diluted_shares":
            row.append(f"{v[0]/1e6:.0f}")
        else:
            row.append(f"{v[0]/1e6:.0f}")
    print(e + "," + ",".join(row))
