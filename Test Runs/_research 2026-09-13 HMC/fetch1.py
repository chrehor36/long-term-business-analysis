import json, sys
sys.path.insert(0, '.')
import edgar
s = edgar.submissions(715153)
json.dump(s, open('submissions.json','w'))
r = s['filings']['recent']
print(s['name'], s.get('formerNames'), s.get('tickers'), s.get('exchanges'))
for i in range(len(r['form'])):
    if r['filingDate'][i] >= '2021-01-01':
        print(r['form'][i], r['filingDate'][i], r['reportDate'][i], r['accessionNumber'][i], r['primaryDocument'][i], r['primaryDocDescription'][i])
print('files:', s['filings'].get('files'))
