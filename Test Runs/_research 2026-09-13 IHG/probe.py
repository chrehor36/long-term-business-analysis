import json, sys
sys.path.insert(0, '.')
import edgar
s = edgar.submissions(858446)
json.dump(s, open('submissions.json','w'))
print(s['name'], s.get('formerNames'), s.get('fiscalYearEnd'), s.get('stateOfIncorporation'))
r = s['filings']['recent']
from collections import Counter
print(Counter(r['form']))
for i in range(len(r['form'])):
    if r['form'][i] in ('20-F','20-F/A','6-K') and i < 400:
        if r['form'][i] != '6-K' or i < 30:
            print(r['form'][i], r['filingDate'][i], r['reportDate'][i], r['accessionNumber'][i], r['primaryDocument'][i], r.get('primaryDocDescription',[''])[i] if 'primaryDocDescription' in r else '')
print('older files', s['filings'].get('files'))
f = edgar.companyfacts(858446)
json.dump(f, open('companyfacts.json','w'))
print('namespaces', {k: len(v) for k, v in f['facts'].items()})
for ns in f['facts']:
    for tag in ['CashFlowsFromUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivities','PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities','AdjustmentsForSharebasedPayments','Revenue','ProfitLoss']:
        if tag in f['facts'][ns]:
            u = f['facts'][ns][tag]['units']
            for unit, facts in u.items():
                ann = sorted({(x['end'], x.get('form'), x.get('accn')) for x in facts if x.get('fp') == 'FY' or x.get('form','').startswith('20-F')})
                ends = sorted({x['end'] for x in facts})
                print(ns, tag, unit, len(facts), ends[:3], ends[-3:])
