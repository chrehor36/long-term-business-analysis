import sys, os, json
sys.path.insert(0, os.path.abspath('tools'))
import sources
f = json.load(open('Test Runs/_research 2026-09-19 DIS/companyfacts.json'))

series = {
 'OCF': ['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],
 'CAPEX': ['PaymentsToAcquireProductiveAssets','PaymentsToAcquirePropertyPlantAndEquipment'],
 'SBC': ['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],
 'DA': ['DepreciationDepletionAndAmortization','DepreciationAmortizationAndAccretionNet','DepreciationAndAmortization'],
 'DEP': ['Depreciation'],
 'NI': ['NetIncomeLoss'],
 'REV': ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'],
 'TAXPAID': ['IncomeTaxesPaidNet','IncomeTaxesPaid'],
 'PRETAX': ['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'],
 'BUYBACK': ['PaymentsForRepurchaseOfCommonStock'],
 'DIV': ['PaymentsOfDividendsCommonStock','PaymentsOfDividends'],
 'CONTENTSPEND': ['PaymentsToAcquireFilmCosts','PaymentsToAcquireProductionAndProgrammingCosts'],
}
res = {}
for k, tags in series.items():
    d, used, unit = sources.annual(f, tags, vintage='newest')
    res[k] = d
    print('==', k, '|', used, '|', unit)
    for y in sorted(d):
        print('   ', y, round(d[y],1))
json.dump(res, open('Test Runs/_research 2026-09-19 DIS/series.json','w'), indent=1)
