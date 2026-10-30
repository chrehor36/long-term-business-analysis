"""Pull annual XBRL series for LRCX and its rivals. Transcription only; no judgment.
Run from the repo root: python "Test Runs/_research 2026-10-10 LRCX/pull_facts.py"
Output: series_<TICKER>.csv beside this script (fiscal_end, metric, value USD millions, tag).
"""
import os, sys, csv
sys.path.insert(0, "tools")
import sources as S

HERE = os.path.dirname(os.path.abspath(__file__))

METRICS = {
    "revenue": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet",
                "RevenueFromContractWithCustomerIncludingAssessedTax", "Revenue"],
    "cost_of_rev": ["CostOfRevenue", "CostOfGoodsAndServicesSold", "CostOfGoodsSold", "CostOfSales"],
    "gross_profit": ["GrossProfit"],
    "rnd": ["ResearchAndDevelopmentExpense", "ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost",
            "ResearchAndDevelopmentExpense"],
    "sga": ["SellingGeneralAndAdministrativeExpense"],
    "op_income": ["OperatingIncomeLoss", "ProfitLossFromOperatingActivities"],
    "pretax": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
               "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments",
               "ProfitLossBeforeTax"],
    "tax": ["IncomeTaxExpenseBenefit", "IncomeTaxExpenseContinuingOperations"],
    "net_income": ["NetIncomeLoss", "ProfitLoss", "ProfitLossAttributableToOwnersOfParent"],
    "interest_exp": ["InterestExpense", "InterestExpenseNonoperating", "InterestExpenseDebt", "FinanceCosts"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities",
            "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations", "CashFlowsFromUsedInOperatingActivities"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets",
              "PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"],
    "dna": ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet",
            "DepreciationAndAmortization", "DepreciationAndAmortisationExpense"],
    "sbc": ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense",
            "AdjustmentsForSharebasedPayments"],
    "buyback": ["PaymentsForRepurchaseOfCommonStock", "PaymentsToAcquireOrRedeemEntitysShares"],
    "dividends": ["PaymentsOfDividendsCommonStock", "PaymentsOfDividends", "DividendsPaidClassifiedAsFinancingActivities"],
    "acq_paid": ["PaymentsToAcquireBusinessesNetOfCashAcquired", "PaymentsToAcquireBusinessesGross",
                 "CashFlowsUsedInObtainingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities"],
    "diluted_shares": ["WeightedAverageNumberOfDilutedSharesOutstanding",
                       "WeightedAverageNumberOfSharesOutstandingDiluted"],
    "eps_diluted": ["EarningsPerShareDiluted", "DilutedEarningsLossPerShare"],
}


def main(ticker, vintage="newest"):
    cik, title = S.cik_for(ticker)
    facts = S.sec_facts(cik)
    rows = []
    for m, tags in METRICS.items():
        series, used, unit = S.annual(facts, tags, vintage=vintage)
        for end, v in sorted(series.items()):
            rows.append((end, m, round(v, 3), used, unit))
    out = os.path.join(HERE, f"series_{ticker}.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["fiscal_end", "metric", "value_millions", "tags_used", "unit"])
        w.writerows(sorted(rows))
    print(ticker, cik, title, len(rows), "rows ->", out)


if __name__ == "__main__":
    for t in sys.argv[1:] or ["LRCX", "AMAT", "KLAC", "ASML"]:
        try:
            main(t)
        except Exception as e:
            print(t, "FAILED", e)
