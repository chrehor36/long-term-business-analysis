import json,sys
sys.stdout.reconfigure(encoding='utf-8')
s=json.load(open('cache/submissions.json'))
print(s['name'], s.get('formerNames'), s.get('fiscalYearEnd'), s.get('sicDescription'))
print('older files', [f['name'] for f in s['filings'].get('files',[])])
r=s['filings']['recent']
from collections import Counter
print(Counter(r['form']))
for i in range(len(r['form'])):
    if r['filingDate'][i] < sys.argv[1]: break
    if r['form'][i] in ('4','3','144','SC 13G','SC 13G/A','5'): continue
    print(r['filingDate'][i], r['form'][i], r['accessionNumber'][i], r['primaryDocument'][i], r.get('items',[''])[i], r['reportDate'][i])
