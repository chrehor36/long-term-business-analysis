import json, sys
from fetch import get
b = get('https://data.sec.gov/api/xbrl/companyfacts/CIK0001636222.json'); open('cache/facts.json','wb').write(b)
f = json.loads(b)['facts']['us-gaap']
tags = ['NetCashProvidedByUsedInOperatingActivities','ShareBasedCompensation','AllocatedShareBasedCompensationExpense',
        'PaymentsToAcquirePropertyPlantAndEquipment','DepreciationDepletionAndAmortization','DepreciationAndAmortization',
        'PaymentsToAcquireBusinessesNetOfCashAcquired','PaymentsForRepurchaseOfCommonStock','PaymentsOfDividends','Revenues',
        'RevenueFromContractWithCustomerExcludingAssessedTax','OperatingIncomeLoss','InterestPaidNet','IncomeTaxesPaidNet',
        'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','NetIncomeLoss']
for t in tags:
    if t not in f: print(t, 'ABSENT'); continue
    rows = {}
    for u, arr in f[t]['units'].items():
        for x in arr:
            if x.get('form') in ('10-K','10-K/A') and x.get('fp') == 'FY' and 'start' in x:
                from datetime import date
                d = (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days
                if 350 <= d <= 380:
                    rows.setdefault(x['end'], x['val'])
    print(t, ' '.join(f"{k[:4]}:{v/1e6:.2f}" for k, v in sorted(rows.items())))
