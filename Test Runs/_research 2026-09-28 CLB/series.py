import json, sys, os
from datetime import date
from fetch import get
CIKS = {'new':'0001958086','nv':'0001000229'}
for k,c in CIKS.items():
    p=f'cache/facts_{k}.json'
    if not os.path.exists(p):
        open(p,'wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json'))
tags = sys.argv[1:] or ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueServicesNet','SalesRevenueGoodsNet','CostOfRevenue','GrossProfit','OperatingIncomeLoss','NetIncomeLoss',
        'IncomeLossFromContinuingOperations','IncomeLossFromDiscontinuedOperationsNetOfTax',
        'NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations','CashProvidedByUsedInOperatingActivitiesDiscontinuedOperations','ShareBasedCompensation',
        'PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','ProceedsFromSaleOfPropertyPlantAndEquipment','DepreciationDepletionAndAmortization','DepreciationAndAmortization','Depreciation',
        'AmortizationOfIntangibleAssets','IncreaseDecreaseInAccountsPayable','IncreaseDecreaseInAccountsReceivable','IncreaseDecreaseInInventories',
        'PaymentsToAcquireBusinessesNetOfCashAcquired','ProceedsFromDivestitureOfBusinesses','PaymentsForRepurchaseOfCommonStock','PaymentsOfDividends','PaymentsOfDividendsCommonStock','ProceedsFromIssuanceOfCommonStock',
        'IncomeTaxesPaidNet','IncomeTaxesPaid','InterestPaidNet','InterestPaid','StockholdersEquity','LongTermDebt','LongTermDebtNoncurrent','CashAndCashEquivalentsAtCarryingValue',
        'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeTaxExpenseBenefit','Goodwill','Assets','GoodwillImpairmentLoss']
for k in CIKS:
    f = json.load(open(f'cache/facts_{k}.json'))['facts'].get('us-gaap',{})
    print('########', k, CIKS[k])
    for t in tags:
        if t not in f: continue
        rows = {}; inst={}
        for u, arr in f[t]['units'].items():
            for x in arr:
                if x.get('form') not in ('10-K','10-K/A') or x.get('fp') != 'FY': continue
                if 'start' in x:
                    d = (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days
                    if 350 <= d <= 380: rows[x['end']] = x['val']
                else: inst[x['end']] = x['val']
        src = rows or inst
        print(t, ' '.join(f"{kk[:4]}:{v/1e6:.1f}" for kk, v in sorted(src.items())))
