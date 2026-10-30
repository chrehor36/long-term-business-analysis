import json,sys
s=json.load(open('submissions.json'))
print(s['name'], s['cik'], s.get('formerNames'), s.get('fiscalYearEnd'), s.get('stateOfIncorporation'))
r=s['filings']['recent']
for i in range(len(r['form'])):
    if r['filingDate'][i]>=sys.argv[1] and (len(sys.argv)<3 or r['form'][i] in sys.argv[2].split(',')):
        print(r['filingDate'][i], r['form'][i], r['accessionNumber'][i], r['primaryDocument'][i], r.get('items',[''])[i], r['reportDate'][i])
