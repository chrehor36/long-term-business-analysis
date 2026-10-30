"""Ten-year series from XBRL companyfacts (transcription; cross-checked against filed statements in the run).
Takes, for each fiscal year, the value from the LATEST 20-F that reports it (restated where restated),
and also the first-filed value. Prints EUR millions."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "cache", "facts.json")))
g = d["facts"]["us-gaap"]

TAGS = [
    ("Revenues", ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"]),
    ("GrossProfit", ["GrossProfit"]),
    ("R&D", ["ResearchAndDevelopmentExpense"]),
    ("SG&A", ["SellingGeneralAndAdministrativeExpense"]),
    ("OpIncome", ["OperatingIncomeLoss"]),
    ("PreTax", ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"]),
    ("Tax", ["IncomeTaxExpenseBenefit"]),
    ("NetIncome", ["NetIncomeLoss"]),
    ("EqMethod", ["IncomeLossFromEquityMethodInvestments"]),
    ("OCF", ["NetCashProvidedByUsedInOperatingActivities", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"]),
    ("Capex", ["PaymentsToAcquirePropertyPlantAndEquipment"]),
    ("IntangCapex", ["PaymentsToAcquireIntangibleAssets"]),
    ("Acq", ["PaymentsToAcquireBusinessesNetOfCashAcquired"]),
    ("D&A", ["DepreciationDepletionAndAmortization"]),
    ("Dep", ["Depreciation"]),
    ("Amort", ["AmortizationOfIntangibleAssets"]),
    ("SBC", ["ShareBasedCompensation"]),
    ("Buyback", ["PaymentsForRepurchaseOfCommonStock"]),
    ("Dividends", ["PaymentsOfDividendsCommonStock", "PaymentsOfDividends"]),
    ("InterestExp", ["InterestExpense"]),
    ("TaxPaid", ["IncomeTaxesPaidNet"]),
    ("SharesWavg", ["WeightedAverageNumberOfSharesOutstandingBasic"]),
]


def series(tags):
    latest, first = {}, {}
    for t in tags:
        if t not in g:
            continue
        for unit, vals in g[t]["units"].items():
            for x in vals:
                if x.get("form") not in ("20-F", "20-F/A"):
                    continue
                if "start" in x:
                    from datetime import date
                    s = date.fromisoformat(x["start"]); e = date.fromisoformat(x["end"])
                    if not (350 <= (e - s).days <= 380):
                        continue
                fy = x["end"][:4]
                if fy not in latest or x["filed"] > latest[fy][1]:
                    latest[fy] = (x["val"], x["filed"])
                if fy not in first or x["filed"] < first[fy][1]:
                    first[fy] = (x["val"], x["filed"])
    return latest, first


years = [str(y) for y in range(2014, 2026)]
print("EUR millions; latest-filed value per year (first-filed differs -> marked *)")
print("%-12s" % "line" + "".join("%9s" % y for y in years))
out = {}
for name, tags in TAGS:
    lt, fs = series(tags)
    row = []
    for y in years:
        if y in lt:
            v = lt[y][0]
            mark = "*" if fs[y][0] != v else " "
            div = 1e6 if name != "SharesWavg" else 1e6
            row.append("%8.0f%s" % (v / div, mark))
            out.setdefault(name, {})[y] = v / div
        else:
            row.append("%9s" % "-")
    print("%-12s" % name + "".join(row))
json.dump(out, open(os.path.join(HERE, "series.json"), "w"), indent=1)
