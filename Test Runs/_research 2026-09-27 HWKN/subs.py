import json,sys
sys.stdout.reconfigure(encoding='utf-8')
s=json.load(open('cache/submissions.json'))
print(s['name'], s.get('formerNames'), s.get('fiscalYearEnd'))
r=s['filings']['recent']
for i in range(len(r['form'])):
    if r['filingDate'][i] < sys.argv[1]: break
    print(r['filingDate'][i], r['form'][i], r['accessionNumber'][i], r['primaryDocument'][i], r.get('items',[''])[i], r['reportDate'][i])
