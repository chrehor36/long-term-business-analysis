import json, sys
from fetch import get
ciks = {'YUM':'0001041061','QSR':'0001618756','DPZ':'0001286681','LOCO':'0001606366','BWLD':'0001062449','JACK':'0000807882','PZZA':'0000901491'}
for t, c in ciks.items():
    d = json.loads(get(f'https://data.sec.gov/submissions/CIK{c}.json'))
    r = d['filings']['recent']
    out = []
    for i in range(len(r['form'])):
        if r['form'][i] in ('10-K', '10-Q'):
            out.append((r['filingDate'][i], r['form'][i], r['accessionNumber'][i], r['primaryDocument'][i], r['reportDate'][i]))
    print(t, d['name'], len(out))
    for o in out[:4] + [x for x in out if x[1]=='10-K'][:12]:
        print('  ', *o)
    if d['filings'].get('files'): print('   more files', [f['name'] for f in d['filings']['files']])
