import json, sys
from datetime import date
from fetch import get
import os
if not os.path.exists('cache/facts.json'):
    b = get('https://data.sec.gov/api/xbrl/companyfacts/CIK0000031462.json'); open('cache/facts.json','wb').write(b)
f = json.load(open('cache/facts.json'))['facts']['us-gaap']
tags = sys.argv[1:] or ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','GrossProfit','OperatingIncomeLoss','NetIncomeLoss',
        'NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations','ShareBasedCompensation',
        'PaymentsToAcquirePropertyPlantAndEquipment','ProceedsFromSaleOfPropertyPlantAndEquipment','DepreciationDepletionAndAmortization','DepreciationAndAmortization','Depreciation',
        'AmortizationOfIntangibleAssets','IncreaseDecreaseInAccountsPayable','IncreaseDecreaseInAccountsReceivable','IncreaseDecreaseInInventories',
        'IncreaseDecreaseInContractWithCustomerAsset','PaymentsToAcquireBusinessesNetOfCashAcquired','PaymentsForRepurchaseOfCommonStock',
        'IncomeTaxesPaidNet','InterestPaidNet','StockholdersEquity','LongTermDebt','CashAndCashEquivalentsAtCarryingValue','InventoryNet','AccountsPayableCurrent',
        'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeTaxExpenseBenefit','Goodwill','Assets']
for t in tags:
    if t not in f: print(t, 'ABSENT'); continue
    rows = {}; inst={}
    for u, arr in f[t]['units'].items():
        for x in arr:
            if x.get('form') not in ('10-K','10-K/A') or x.get('fp') != 'FY': continue
            if 'start' in x:
                d = (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days
                if 350 <= d <= 380:
                    rows[x['end']] = x['val']   # latest-filed wins (arrays in filing order)
            else:
                inst[x['end']] = x['val']
    src = rows or inst
    print(t, ' '.join(f"{k[:7]}:{v/1e6:.1f}" for k, v in sorted(src.items())))
