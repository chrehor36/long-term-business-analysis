import json, collections
s=json.load(open('cache/submissions.json'))
print(s['name'], s.get('formerNames'), s.get('sicDescription'), s.get('stateOfIncorporation'), s.get('fiscalYearEnd'))
print('files', s['filings'].get('files'))
r=s['filings']['recent']
c=collections.Counter(r['form']); print(c)
for i,f in enumerate(r['form']):
    if f in ('10-K','10-Q','DEF 14A','8-K','S-4','425','DEFM14A','PREM14A','SC TO-T','SC TO-I','SC 14D9','SC 13E3','S-1','S-3','S-8','424B4','SC 13D','SC 13D/A','8-K/A','10-K/A'):
        print(r['filingDate'][i], f, r['reportDate'][i], r['accessionNumber'][i], r['primaryDocument'][i], r['items'][i])
