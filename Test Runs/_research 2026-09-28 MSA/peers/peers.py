import json,sys,os
sys.path.insert(0,'..')
from fetch import get,strip
P={'MMM':'0000066740','HON':'0000773840','LAKE':'0000798081'}
for t,c in P.items():
    if not os.path.exists(f'{t}_sub.json'):
        open(f'{t}_sub.json','wb').write(get(f'https://data.sec.gov/submissions/CIK{c}.json'))
    if not os.path.exists(f'{t}_facts.json'):
        open(f'{t}_facts.json','wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json'))
    d=json.load(open(f'{t}_sub.json'));r=d['filings']['recent']
    ks=[(r['reportDate'][i],r['accessionNumber'][i],r['primaryDocument'][i]) for i in range(len(r['form'])) if r['form'][i]=='10-K']
    print(t,ks[:8])
