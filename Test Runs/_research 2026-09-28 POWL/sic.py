import json
from fetch import get
for c in ['1674101','1720635','1048268','1091587','8947','80420']:
    d=json.loads(get(f'https://data.sec.gov/submissions/CIK{c.zfill(10)}.json'))
    r=d['filings']['recent']
    print(c, d['name'], '|', d.get('sicDescription'), '| state', d.get('stateOfIncorporation'), '| last annual:', [(r['form'][i], r['reportDate'][i]) for i in range(len(r['form'])) if r['form'][i] in ('10-K','20-F')][:1], [f for f in r['form'][:200] if f in ('15-12B','15F-12B','25-NSE')][:3])
