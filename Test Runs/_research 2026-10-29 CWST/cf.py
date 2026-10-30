import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json
from facts import series
d = json.load(open("cache/facts_cwst.json"))
tags = {"OCF": ["NetCashProvidedByUsedInOperatingActivities"], "SBC": ["ShareBasedCompensation"],
 "capex": ["PaymentsToAcquirePropertyPlantAndEquipment"], "acq": ["PaymentsToAcquireBusinessesNetOfCashAcquired"],
 "intpaid": ["InterestPaidNet", "InterestPaid"], "taxpaid": ["IncomeTaxesPaidNet", "IncomeTaxesPaid"],
 "intexp": ["InterestExpenseNet", "InterestExpense", "InterestExpenseNonoperating"], "rev": ["Revenues"], "OI": ["OperatingIncomeLoss"],
 "pretax": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"], "tax": ["IncomeTaxExpenseBenefit"],
 "NI": ["NetIncomeLoss"], "DA": ["DepreciationDepletionAndAmortization","DepreciationAmortizationAndAccretionNet"], "flpp": ["FinanceLeasePrincipalPayments"],
 "eqiss": ["ProceedsFromIssuanceOfCommonStock"], "buyback": ["PaymentsForRepurchaseOfCommonStock"]}
S = {k: series(d, v) for k, v in tags.items()}
print("FY   " + " ".join(f"{k:>8}" for k in tags))
for y in range(2016, 2026):
    print(y, " ".join(f"{(S[k][y][0]/1e6 if y in S[k] else float('nan')):8.1f}" for k in tags))
