import json, sys
sys.path.insert(0, '.')
import edgar
s = edgar.submissions(313838)
json.dump(s, open('submissions.json','w'))
r = s['filings']['recent']
print(s['name'], s.get('formerNames'))
for i in range(len(r['form'])):
    if r['form'][i] in ('20-F','20-F/A','6-K','SC TO-I','8-K','F-3','S-8','SC 13D','SC 13G') and r['filingDate'][i] >= '2021-01-01':
        print(r['form'][i], r['filingDate'][i], r['reportDate'][i], r['accessionNumber'][i], r['primaryDocument'][i], r.get('primaryDocDescription',[''])[i] if 'primaryDocDescription' in r else '')
