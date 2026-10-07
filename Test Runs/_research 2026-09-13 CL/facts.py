"""Colgate annual facts from companyfacts (10-K, FY, full-year durations or year-end instants), NEWEST vintage per period end.
Transcription only; every driving figure is re-read against the filed statements in the run file."""
import json, os
from datetime import date
HERE = os.path.dirname(os.path.abspath(__file__))
F = json.load(open(os.path.join(HERE, "companyfacts.json"), encoding="utf-8"))["facts"]["us-gaap"]

def annual(tag, instant=False):
    if tag not in F:
        return {}
    best = {}
    for unit, arr in F[tag]["units"].items():
        if unit not in ("USD", "shares", "USD/shares", "pure"):
            continue
        for x in arr:
            if x.get("form") not in ("10-K", "10-K/A"):
                continue
            e = x["end"]
            if not instant:
                if "start" not in x:
                    continue
                d = (date.fromisoformat(e) - date.fromisoformat(x["start"])).days
                if not (340 <= d <= 380):
                    continue
            if not e.endswith("12-31"):
                continue
            y = int(e[:4])
            if y not in best or x["filed"] > best[y][1]:
                best[y] = (x["val"], x["filed"], x.get("accn"))
    return {y: v[0] for y, v in best.items()}

TAGS = {
    "sales": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"],
    "gross": ["GrossProfit"], "opinc": ["OperatingIncomeLoss"], "adv": ["AdvertisingExpense"],
    "pretax": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"],
    "taxprov": ["IncomeTaxExpenseBenefit"], "taxpaid": ["IncomeTaxesPaidNet", "IncomeTaxesPaid"],
    "ni_parent": ["NetIncomeLoss"], "da": ["DepreciationDepletionAndAmortization"],
    "sbc": ["ShareBasedCompensation"], "esop_exp": ["EmployeeStockOwnershipPlanESOPCompensationExpense"],
    "esop_contrib": ["EmployeeStockOwnershipPlanESOPCashContributionsToESOP"],
    "div": ["PaymentsOfDividendsCommonStock", "PaymentsOfDividends"], "buyback": ["PaymentsForRepurchaseOfCommonStock"],
    "optproc": ["ProceedsFromStockOptionsExercised"], "interest": ["InterestExpense", "InterestExpenseNonoperating"],
    "rd": ["ResearchAndDevelopmentExpense"],
}
ITAGS = {
    "assets": ["Assets"], "cash": ["CashAndCashEquivalentsAtCarryingValue"], "goodwill": ["Goodwill"],
    "intang": ["IntangibleAssetsNetExcludingGoodwill"], "curliab": ["LiabilitiesCurrent"],
    "debtcur": ["DebtCurrent"], "rou": ["OperatingLeaseRightOfUseAsset"], "ppe": ["PropertyPlantAndEquipmentNet"],
    "equity_parent": ["StockholdersEquity"], "ltdebt": ["LongTermDebtNoncurrent"], "mktsec": ["MarketableSecuritiesCurrent"],
    "shares_out": ["CommonStockSharesOutstanding"],
}
out = {}
for k, tags in TAGS.items():
    d = {}
    for t in tags:
        for y, v in annual(t).items():
            d.setdefault(y, v)
    out[k] = d
for k, tags in ITAGS.items():
    d = {}
    for t in tags:
        for y, v in annual(t, instant=True).items():
            d.setdefault(y, v)
    out[k] = d
json.dump({k: {str(y): v for y, v in d.items()} for k, d in out.items()}, open(os.path.join(HERE, "facts_out.json"), "w"), indent=1)
yrs = range(2014, 2026)
print("year " + " ".join(f"{k:>9}" for k in out))
for y in yrs:
    print(y, " ".join(f"{(out[k].get(y, float('nan'))/1e6 if abs(out[k].get(y, 0)) > 1e4 else out[k].get(y, float('nan'))):9.1f}" for k in out))
