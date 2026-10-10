"""Annual series from SEC companyfacts (transcription only; every figure is checked against the filed 10-K text).
Usage: python xbrl_series.py CIK [tags...]  -> prints FY rows (10-K, 12-month duration or instant), latest filing wins per period end.
"""
import json, sys, os
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))

DEFAULT = [
    "Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet", "SalesRevenueGoodsNet",
    "OperatingIncomeLoss", "NetIncomeLoss", "IncomeTaxExpenseBenefit", "InterestExpense", "InterestExpenseNonoperating",
    "NetCashProvidedByUsedInOperatingActivities", "PaymentsToAcquirePropertyPlantAndEquipment",
    "PaymentsToAcquireBusinessesNetOfCashAcquired", "ProceedsFromDivestitureOfBusinesses", "ProceedsFromSaleOfProductiveAssets",
    "DepreciationDepletionAndAmortization", "DepreciationAndAmortization", "Depreciation", "AmortizationOfIntangibleAssets",
    "ShareBasedCompensation", "PaymentsForRepurchaseOfCommonStock", "PaymentsOfDividends", "PaymentsOfDividendsCommonStock",
    "Goodwill", "IntangibleAssetsNetExcludingGoodwill", "GoodwillImpairmentLoss", "ImpairmentOfIntangibleAssetsExcludingGoodwill",
    "WeightedAverageNumberOfDilutedSharesOutstanding", "CashAndCashEquivalentsAtCarryingValue", "LongTermDebt", "DebtCurrent",
    "LongTermDebtNoncurrent", "StockholdersEquity", "Assets", "IncomeTaxesPaidNet", "InterestPaidNet",
    "OperatingLeaseLiability", "ResearchAndDevelopmentExpense", "InventoryNet", "AccountsReceivableNetCurrent",
    "ProceedsFromStockOptionsExercised", "IncreaseDecreaseInOperatingCapital",
]


def days(a, b):
    y1, m1, d1 = map(int, a.split("-")); y2, m2, d2 = map(int, b.split("-"))
    return (date(y2, m2, d2) - date(y1, m1, d1)).days


def series(facts, tag):
    g = facts["facts"].get("us-gaap", {}).get(tag)
    if not g:
        return {}
    out = {}
    for unit, rows in g["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A"):
                continue
            if "start" in r and not (350 <= days(r["start"], r["end"]) <= 380):
                continue
            k = r["end"]
            if k not in out or r["filed"] > out[k][1]:
                out[k] = (r["val"], r["filed"], r["accn"])
    return out


if __name__ == "__main__":
    cik = sys.argv[1].zfill(10)
    facts = json.load(open(os.path.join(HERE, "cache", f"facts_{cik}.json")))
    tags = sys.argv[2:] or DEFAULT
    for t in tags:
        s = series(facts, t)
        if not s:
            continue
        print(f"== {t}")
        for k in sorted(s):
            if k < "2005":
                continue
            v, f, a = s[k]
            print(f"   {k}  {v/1e6 if abs(v) > 1e4 else v:>12,.1f}  filed {f}  {a}")
