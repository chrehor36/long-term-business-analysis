import json, sys
sys.path.insert(0, 'scripts')
from facts import annual
F = 'cache/facts.json'
import facts
f = json.load(open(F)); g = f['facts']['us-gaap']
facts.g = g
tags = ['RevenueFromContractWithCustomerIncludingAssessedTax','RegulatedAndUnregulatedOperatingRevenue','Revenues','OperatingIncomeLoss','InterestExpense','IncomeTaxExpenseBenefit','NetIncomeLoss',
'UtilitiesOperatingExpenseDepreciationAndAmortization','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment',
'PaymentsToAcquireBusinessesNetOfCashAcquired','PaymentsToAcquireBusinessesGross','ShareBasedCompensation','RestrictedStockExpense','PaymentsOfDividends','ProceedsFromIssuanceOfCommonStock',
'ProceedsFromIssuanceOfLongTermDebt','RepaymentsOfLongTermDebt','ProceedsFromRepaymentsOfShortTermDebt',
'CashAndCashEquivalentsAtCarryingValue','AccountsReceivableNetCurrent','UnbilledContractsReceivable','RegulatoryAssets','Goodwill','PublicUtilitiesPropertyPlantAndEquipmentNet','Assets',
'LongTermDebtNoncurrent','LongTermDebtCurrent','ShortTermBorrowings','StockholdersEquity','RetainedEarningsAccumulatedDeficit','PensionAndOtherPostretirementAndPostemploymentBenefitPlansLiabilitiesNoncurrent','DeferredIncomeTaxLiabilities','CapitalizationLongtermDebtAndEquity','IncreaseDecreaseInAccountsReceivable']
years = [str(y) for y in range(2015, 2026)]
print('tag'.ljust(60), ' '.join(y.rjust(8) for y in years))
for t in tags:
    a = annual(t)
    row = {}
    for k,v in a.items():
        row[k[:4]] = v[0]
    print(t[:60].ljust(60), ' '.join((f"{row[y]/1e6:8.1f}" if y in row else '       -') for y in years))
