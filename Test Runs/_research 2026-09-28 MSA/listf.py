import json
d=json.load(open('sub.json'))
print(d['name'], d.get('fiscalYearEnd'), d.get('stateOfIncorporation'), d.get('sicDescription'), d.get('category'))
print('former', d.get('formerNames'))
r=d['filings']['recent']
for i in range(len(r['form'])):
    f=r['form'][i]
    if f in ('10-K','10-K/A','10-Q','8-K','DEF 14A','S-1','S-3','424B4','424B3','SC 13D','SC TO-I','SC TO-T','DEFM14A','S-4','425','10-KT','8-K/A','PRE 14A','S-8','SC 13E3') or f.startswith('SC'):
        print(r['filingDate'][i], f, r['accessionNumber'][i], r['primaryDocument'][i], r.get('items',['']*9999)[i], r['reportDate'][i])
print(d['filings'].get('files'))
