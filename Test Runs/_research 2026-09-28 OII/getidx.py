import json, sys
from fetch import get
for acc in sys.argv[1:]:
    a = acc.replace('-','')
    b = get(f'https://www.sec.gov/Archives/edgar/data/73756/{a}/index.json')
    d = json.loads(b)
    print('==', acc)
    for it in d['directory']['item']:
        n = it['name']
        if n.endswith(('.htm','.txt')) and not n.endswith('-index.htm'):
            print('  ', n, it.get('size'))
