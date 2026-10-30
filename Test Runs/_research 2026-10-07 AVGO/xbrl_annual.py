# annual values from SEC companyfacts: 10-K duration facts (~1 year), latest filing per period end. Transcription only.
import json, sys, datetime as dt
def load(t): return json.load(open(f"{t}_facts.json"))
def annual(facts, concepts, years=None, instant=False):
    out = {}
    for c in concepts:
        node = facts["facts"].get("us-gaap", {}).get(c)
        if not node: continue
        for unit, rows in node["units"].items():
            if unit != "USD": continue
            for r in rows:
                if r.get("form") not in ("10-K", "10-K/A"): continue
                if not instant:
                    if "start" not in r: continue
                    d = (dt.date.fromisoformat(r["end"]) - dt.date.fromisoformat(r["start"])).days
                    if d < 340 or d > 380: continue
                end = r["end"]
                prev = out.get(end)
                if prev is None or (prev[2] == c and r["filed"] > prev[1]) :
                    if prev is None or prev[2] == c:
                        out[end] = (r["val"], r["filed"], c, r.get("accn"))
    return dict(sorted(out.items()))
if __name__ == "__main__":
    t = sys.argv[1]; f = load(t)
    for name, cs in [("revenue", ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet"]),
                     ("opinc", ["OperatingIncomeLoss"]),
                     ("ocf", ["NetCashProvidedByUsedInOperatingActivities"]),
                     ("sbc", ["ShareBasedCompensation"]),
                     ("capex", ["PaymentsToAcquirePropertyPlantAndEquipment"]),
                     ("da", ["DepreciationDepletionAndAmortization","DepreciationAndAmortization"]),
                     ("acq", ["PaymentsToAcquireBusinessesNetOfCashAcquired"]),
                     ("intpaid", ["InterestPaidNet","InterestPaid"]),
                     ("intexp", ["InterestExpense","InterestExpenseNonoperating"]),
                     ("taxpaid", ["IncomeTaxesPaidNet","IncomeTaxesPaid"]),
                     ("pretax", ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest","IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"]),
                     ("taxexp", ["IncomeTaxExpenseBenefit"]),
                     ("netinc", ["NetIncomeLoss"]),
                     ("buyback", ["PaymentsForRepurchaseOfCommonStock"]),
                     ("withhold", ["PaymentsRelatedToTaxWithholdingForShareBasedCompensation"]),
                     ("divs", ["PaymentsOfDividendsCommonStock","PaymentsOfDividends"]),
                     ("debtiss", ["ProceedsFromIssuanceOfLongTermDebt","ProceedsFromIssuanceOfSeniorLongTermDebt"]),
                     ("debtrep", ["RepaymentsOfLongTermDebt","RepaymentsOfSeniorDebt"])]:
        a = annual(f, cs)
        print(name.ljust(9), "  ".join(f"{k[:7]}:{v[0]/1e6:,.0f}" for k, v in a.items() if k >= "2015"))
