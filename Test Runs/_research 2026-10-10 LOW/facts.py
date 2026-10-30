# Transcription of annual figures from SEC companyfacts (XBRL). Arithmetic only; read the filed statements.
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(HERE, "cache")

CONCEPTS = {
 "rev": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet", "SalesRevenueGoodsNet", "RevenueFromContractWithCustomerIncludingAssessedTax"],
 "opinc": ["OperatingIncomeLoss"],
 "ni": ["NetIncomeLoss", "ProfitLoss"],
 "ocf": ["NetCashProvidedByUsedInOperatingActivities", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
 "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"],
 "da": ["DepreciationDepletionAndAmortization", "DepreciationAndAmortization", "DepreciationAmortizationAndAccretionNet"],
 "sbc": ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"],
 "assets": ["Assets"],
 "equity": ["StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],
 "cash": ["CashAndCashEquivalentsAtCarryingValue"],
 "inv": ["InventoryNet"],
 "ppe": ["PropertyPlantAndEquipmentNet"],
 "gw": ["Goodwill"],
 "ap": ["AccountsPayableCurrent"],
 "buyback": ["PaymentsForRepurchaseOfCommonStock"],
 "div": ["PaymentsOfDividendsCommonStock", "PaymentsOfDividends"],
 "dilsh": ["WeightedAverageNumberOfDilutedSharesOutstanding"],
 "intexp": ["InterestExpense", "InterestIncomeExpenseNonoperatingNet", "InterestExpenseNonoperating"],
 "tax": ["IncomeTaxExpenseBenefit"],
 "pretax": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"],
 "acq": ["PaymentsToAcquireBusinessesNetOfCashAcquired"],
}

def load(t):
    return json.load(open(os.path.join(C, f"facts_{t}.json"), encoding="utf-8"))

def annual(j, names, instant=False):
    """first-filed 10-K value per fiscal-year end, ~12-month duration (or instant)."""
    out = {}
    from datetime import date
    for n in names:
        f = j["facts"].get("us-gaap", {}).get(n)
        if not f: continue
        for unit, vals in f["units"].items():
            if unit not in ("USD", "shares"): continue
            for v in vals:
                if not v.get("form", "").startswith("10-K"): continue
                end = v["end"]
                if instant:
                    if "start" in v: continue
                else:
                    if "start" not in v: continue
                    d0 = date.fromisoformat(v["start"]); d1 = date.fromisoformat(end)
                    if not (350 <= (d1 - d0).days <= 380): continue
                key = end
                if key in out and out[key][1] <= v["filed"]: continue
                out[key] = (v["val"], v["filed"], n)
    return out

def table(t, years_from="2004"):
    j = load(t)
    inst = {"assets", "equity", "cash", "inv", "ppe", "gw", "ap"}
    data = {}
    for k, names in CONCEPTS.items():
        # take each concept in priority order, filling gaps
        merged = {}
        for n in names:
            a = annual(j, [n], instant=(k in inst))
            for e, v in a.items():
                merged.setdefault(e, v)
        data[k] = merged
    ends = sorted({e for k in ("rev", "opinc", "ocf") for e in data[k]})
    ends = [e for e in ends if e >= years_from]
    return data, ends

if __name__ == "__main__":
    t = sys.argv[1]
    keys = sys.argv[2].split(",") if len(sys.argv) > 2 else list(CONCEPTS)
    data, ends = table(t)
    print(t, "USD millions (shares millions); first-filed 10-K value; transcription")
    print("end        " + " ".join(f"{k:>9s}" for k in keys))
    for e in ends:
        row = []
        for k in keys:
            v = data[k].get(e)
            row.append(f"{v[0]/1e6:9.0f}" if v else f"{'-':>9s}")
        print(e, " ".join(row))
