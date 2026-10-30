import json,os
from fetch import get
if not os.path.exists('companyfacts.json'):
    open('companyfacts.json','wb').write(get('https://data.sec.gov/api/xbrl/companyfacts/CIK0000100885.json'))
d=json.load(open('companyfacts.json'))['facts']['us-gaap']
tags=[t for t in d if any(k in t for k in ('NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquire','Depreciation','ShareBasedCompensation','AllocatedShareBased','PaymentsForRepurchaseOfCommonStock','PaymentsOfDividends','Acquisition','BusinessCombination'))]
for t in sorted(tags):
    vals={}
    for u in d[t]['units'].values():
        for f in u:
            if f.get('fp')=='FY' and f['form'].startswith('10-K') and 'start' in f:
                from datetime import date
                s=date.fromisoformat(f['start']); e=date.fromisoformat(f['end'])
                if 350<(e-s).days<380: vals[f['end'][:4]]=f['val']
    if vals: print(t, {k:round(v/1e6) for k,v in sorted(vals.items())})
