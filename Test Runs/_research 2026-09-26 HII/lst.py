import json
d=json.load(open('submissions.json'))
r=d['filings']['recent']
print(d['name'], d.get('fiscalYearEnd'), 'files:', d['filings'].get('files'))
for i in range(len(r['form'])):
    f=r['form'][i]
    if f in ('10-K','10-K/A','10-Q','DEF 14A','10-12B','10-12B/A') or (f=='8-K' and r['filingDate'][i]>='2025-01-01'):
        print(r['filingDate'][i], f, r['accessionNumber'][i], r['primaryDocument'][i], r.get('items',[''])[i])
