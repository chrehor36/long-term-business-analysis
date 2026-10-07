import sys, json, os
sys.path.insert(0, 'tools')
import sources as s
R = 'Test Runs/_research 2026-09-29 PAYO'
cik, title = s.cik_for('PAYO')
print(cik, title)
txt = s._get(f'https://data.sec.gov/submissions/CIK{cik}.json', s.SEC_UA, None)
open(os.path.join(R, 'sub.json'), 'w', encoding='utf-8').write(txt)
d = json.loads(txt)
print(d['name'], d.get('formerNames'), d.get('stateOfIncorporation'), d.get('fiscalYearEnd'), d.get('category'))
r = d['filings']['recent']
for i in range(len(r['form'])):
    if r['filingDate'][i] >= '2025-06-01' or r['form'][i] in ('10-K','S-4','S-4/A','DEFM14A','PREM14A','425','8-K12B','SC 13E3','SC TO-T'):
        print(r['filingDate'][i], r['form'][i], r['accessionNumber'][i], r['primaryDocument'][i], r.get('items',[''])[i] if 'items' in r else '')
print(d['filings'].get('files'))
