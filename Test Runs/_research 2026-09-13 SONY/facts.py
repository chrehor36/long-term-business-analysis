import json, sys
sys.path.insert(0, '.')
import edgar
raw = edgar.get('https://data.sec.gov/api/xbrl/companyfacts/CIK0000313838.json')
open('companyfacts.json','w',encoding='utf-8').write(raw)
f = json.loads(raw)
print(list(f['facts'].keys()))
for tax, d in f['facts'].items():
    for k in d:
        if any(s in k for s in ('CashFlowsFromUsedInOperatingActivities','PurchaseOfPropertyPlantAndEquipment','DepreciationAndAmortisationExpense','SharebasedPayment','AdjustmentsForSharebasedPayments')):
            for u, arr in d[k]['units'].items():
                for x in arr:
                    if x.get('form') in ('20-F',) and x.get('fp')=='FY':
                        print(tax, k, u, x.get('start'), x['end'], x['val'], x['accn'], x.get('frame'))
