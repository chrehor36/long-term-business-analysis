import json, sys
from datetime import date
def series(tk, tag, dur=True):
    d = json.load(open(f"cache/facts_{tk}.json"))["facts"]
    for ns in ("us-gaap", "dei"):
        if tag in d.get(ns, {}): break
    else:
        return {}
    out = {}
    for unit, rows in d[ns][tag]["units"].items():
        if unit != "USD" and unit != "shares": continue
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A"): continue
            e = date.fromisoformat(r["end"])
            if dur:
                if "start" not in r: continue
                if not (350 <= (e - date.fromisoformat(r["start"])).days <= 380): continue
            else:
                if "start" in r: continue
            fy = e.year if (tk == "CMC" or e.month > 6) else e.year - 1
            if tk == "CMC" and not (e.month in (8, 9)): continue
            if tk != "CMC" and e.month != 12: continue
            if fy not in out or r["filed"] > out[fy][1]:
                out[fy] = (r["val"], r["filed"])
    return out
def pick(tk, tags, dur=True):
    res = {}
    for tag in tags:
        for fy, v in series(tk, tag, dur).items():
            if fy not in res: res[fy] = (v[0], tag)
    return res
ITEMS = [
 ("rev", ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet", "SalesRevenueGoodsNet"], True),
 ("opinc", ["OperatingIncomeLoss"], True),
 ("pretax", ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic"], True),
 ("tax", ["IncomeTaxExpenseBenefit"], True),
 ("int", ["InterestExpense", "InterestExpenseNonoperating", "InterestExpenseDebt", "InterestPaidNet"], True),
 ("ni", ["NetIncomeLoss"], True),
 ("ocf", ["NetCashProvidedByUsedInOperatingActivities", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"], True),
 ("capex", ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"], True),
 ("da", ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet", "DepreciationAndAmortization", "Depreciation"], True),
 ("sbc", ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"], True),
 ("acq", ["PaymentsToAcquireBusinessesNetOfCashAcquired", "PaymentsToAcquireBusinessesGross"], True),
 ("div", ["PaymentsOfDividendsCommonStock", "PaymentsOfDividends"], True),
 ("buyb", ["PaymentsForRepurchaseOfCommonStock"], True),
 ("assets", ["Assets"], False),
 ("equity", ["StockholdersEquity"], False),
 ("cash", ["CashAndCashEquivalentsAtCarryingValue", "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"], False),
 ("gw", ["Goodwill"], False),
 ("ltd", ["LongTermDebtNoncurrent", "LongTermDebtAndCapitalLeaseObligations"], False),
 ("ltdc", ["LongTermDebtCurrent", "LongTermDebtAndCapitalLeaseObligationsCurrent"], False),
]
if __name__ == "__main__":
    tk = sys.argv[1]; y0 = int(sys.argv[2]) if len(sys.argv) > 2 else 2012
    data = {k: pick(tk, tags, dur) for k, tags, dur in ITEMS}
    yrs = sorted({y for v in data.values() for y in v if y >= y0})
    print(tk, "USD millions")
    print("item  " + " ".join(f"{y:>8}" for y in yrs))
    for k, _, _ in ITEMS:
        print(f"{k:6}" + " ".join(f"{data[k][y][0]/1e6:8.0f}" if y in data[k] else "       -" for y in yrs))
    print("tags:", {k: sorted({v[1] for v in data[k].values()}) for k in data})
