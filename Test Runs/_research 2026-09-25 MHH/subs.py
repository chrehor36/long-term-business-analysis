import json,sys
sys.path.insert(0,'../../tools')
import sources as S
from fetch import get
print(S.cik_for('MHH'))
cik=S.cik_for('MHH')[0]
b=get('https://data.sec.gov/submissions/CIK%010d.json'%int(cik)); open('subs.json','wb').write(b)
j=json.loads(b); r=j['filings']['recent']
print(j['name'], j.get('formerNames'), j.get('fiscalYearEnd'))
for i in range(len(r['form'])):
    if r['form'][i] in ('10-K','10-Q','8-K','DEF 14A','S-4','425','SC TO-T','SC 13D','SC 13D/A','DEFM14A','10-K/A','8-K/A','S-8','S-3','SC 13E3','PRE 14A','SCHEDULE 13D','SCHEDULE 13D/A') and r['filingDate'][i]>='2016-01-01':
        print(r['filingDate'][i], r['form'][i], r['accessionNumber'][i], r['primaryDocument'][i], r.get('items',[''])[i] if 'items' in r else '')
print('files',j['filings'].get('files'))
