import json
from fetch import get
from datetime import date
b=get('https://data.sec.gov/api/xbrl/companyfacts/CIK0000080420.json'); open('cache/facts.json','wb').write(b)
F=json.loads(b)['facts']
f=F['us-gaap']
print('dei', list(F.get('dei',{}).keys()))
def ann(tag, instant=False):
    if tag not in f: return {}
    out={}
    for u,rows in f[tag]['units'].items():
        for r in rows:
            if r.get('form') not in ('10-K','10-K/A') or r.get('fp')!='FY': continue
            if 'start' in r:
                d=(date.fromisoformat(r['end'])-date.fromisoformat(r['start'])).days
                if d<340 or d>380: continue
            out.setdefault(r['end'],{})[r['filed']]=r['val']
    return {e:v[max(v)] for e,v in out.items()}
tags=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','GrossProfit','OperatingIncomeLoss','NetIncomeLoss','NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations','PaymentsToAcquirePropertyPlantAndEquipment','ShareBasedCompensation','AllocatedShareBasedCompensationExpense','RestrictedStockExpense','Depreciation','DepreciationDepletionAndAmortization','DepreciationAndAmortization','AmortizationOfIntangibleAssets','PaymentsToAcquireBusinessesNetOfCashAcquired','StockholdersEquity','Goodwill','IntangibleAssetsNetExcludingGoodwill','LongTermDebt','LongTermDebtNoncurrent','CashAndCashEquivalentsAtCarryingValue','ShortTermInvestments','ContractWithCustomerLiability','ContractWithCustomerLiabilityCurrent','BillingsInExcessOfCost','BillingsInExcessOfCostCurrent','IncreaseDecreaseInContractWithCustomerLiability','IncreaseDecreaseInBillingsInExcessOfCostsAndEstimatedEarnings','IncreaseDecreaseInAccountsPayable','IncreaseDecreaseInAccountsReceivable','IncreaseDecreaseInInventories','IncreaseDecreaseInContractWithCustomerAsset','IncreaseDecreaseInCostsInExcessOfBillings','AccountsReceivableNetCurrent','InventoryNet','ContractWithCustomerAssetNetCurrent','AccountsPayableCurrent','PropertyPlantAndEquipmentNet','PaymentsForRepurchaseOfCommonStock','PaymentsOfDividends','PaymentsOfDividendsCommonStock','IncomeTaxesPaidNet','IncomeTaxesPaid','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','InvestmentIncomeInterest','WeightedAverageNumberOfSharesOutstandingBasic','Assets','Liabilities','ProceedsFromSaleOfPropertyPlantAndEquipment','ImpairmentOfLongLivedAssetsHeldForUse','RestructuringCharges']
res={}
for t in tags:
    a=ann(t)
    if a: res[t]=a
    print(t, {k[:7]:round(v/1e6,2) for k,v in sorted(a.items())})
json.dump(res,open('series.json','w'),indent=0)
