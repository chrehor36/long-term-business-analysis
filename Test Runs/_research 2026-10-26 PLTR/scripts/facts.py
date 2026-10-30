"""Print annual (FY, 10-K) and latest quarterly values for selected us-gaap tags from companyfacts.json.
Usage: python -I facts.py <companyfacts.json>
"""
import json, sys

TAGS = [
    "Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
    "OperatingIncomeLoss", "NetIncomeLoss", "InvestmentIncomeInterest", "InterestIncomeOther",
    "IncomeTaxExpenseBenefit", "IncomeTaxesPaidNet",
    "NetCashProvidedByUsedInOperatingActivities", "ShareBasedCompensation",
    "PaymentsToAcquirePropertyPlantAndEquipment", "DepreciationDepletionAndAmortization", "DepreciationAndAmortization",
    "PaymentsForRepurchaseOfCommonStock", "PaymentsRelatedToTaxWithholdingForShareBasedCompensation",
    "ProceedsFromStockOptionsExercised",
    "WeightedAverageNumberOfDilutedSharesOutstanding", "WeightedAverageNumberOfSharesOutstandingBasic",
    "PaymentsToAcquireBusinessesNetOfCashAcquired",
    "AccountsReceivableNetCurrent", "ContractWithCustomerLiabilityCurrent",
]


def main():
    d = json.load(open(sys.argv[1]))
    g = d["facts"].get("us-gaap", {})
    for t in TAGS:
        if t not in g:
            continue
        units = g[t]["units"]
        for u, rows in units.items():
            annual = {}
            for r in rows:
                if r.get("form") == "10-K" and r.get("fp") == "FY" and "start" in r:
                    # keep full-year spans only (approx 365 days)
                    from datetime import date
                    s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                    if 350 <= (e - s).days <= 380:
                        annual.setdefault(r["end"], (r["val"], r["accn"]))
                elif r.get("form") == "10-K" and "start" not in r:
                    annual.setdefault(r["end"], (r["val"], r["accn"]))
            if annual:
                print(t, u)
                for k in sorted(annual):
                    print("   ", k, annual[k][0], annual[k][1])
            q = [r for r in rows if r.get("form") == "10-Q" and r.get("fy") == 2026]
            for r in q[-4:]:
                print("    10-Q", r.get("start"), r["end"], r["val"], r["accn"])


main()
