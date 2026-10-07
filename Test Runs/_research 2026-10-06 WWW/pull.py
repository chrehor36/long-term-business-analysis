import sys, json
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources as S
tk = sys.argv[1]; vint = sys.argv[2] if len(sys.argv)>2 else "newest"
cik, name = S.cik_for(tk)
f = S.sec_facts(cik)
rows = {
 "rev": ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet","SalesRevenueGoodsNet"],
 "gp": ["GrossProfit"],
 "opinc": ["OperatingIncomeLoss"],
 "ni": ["NetIncomeLoss","ProfitLoss"],
 "ocf": ["NetCashProvidedByUsedInOperatingActivities","NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
 "capex": ["PaymentsToAcquirePropertyPlantAndEquipment"],
 "da": ["DepreciationDepletionAndAmortization","DepreciationAndAmortization","DepreciationAmortizationAndAccretionNet"],
 "sbc": ["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"],
 "div": ["PaymentsOfDividendsCommonStock","PaymentsOfDividends"],
 "buyback": ["PaymentsForRepurchaseOfCommonStock"],
 "int": ["InterestExpense","InterestExpenseNonoperating","InterestExpenseDebt"],
 "acq": ["PaymentsToAcquireBusinessesNetOfCashAcquired"],
 "divest": ["ProceedsFromDivestitureOfBusinesses","ProceedsFromDivestitureOfBusinessesNetOfCashDivested"],
 "impair": ["GoodwillAndIntangibleAssetImpairment","ImpairmentOfIntangibleAssetsExcludingGoodwill","GoodwillImpairmentLoss","ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill"],
 "pretax": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest","IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"],
 "dilsh": ["WeightedAverageNumberOfDilutedSharesOutstanding"],
}
res = {}
for k,t in rows.items():
    d,used,u = S.annual(f,t,vintage=vint)
    res[k]=d
ends = sorted(set(e for d in res.values() for e in d))
print(name, cik)
print("end       " + "".join(f"{k:>9}" for k in rows))
for e in ends:
    print(e, "".join(f"{res[k].get(e, float('nan')):9.1f}" for k in rows))
