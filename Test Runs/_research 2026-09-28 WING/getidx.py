import json, sys
from fetch import get
for acc in sys.argv[1:]:
    a = acc.replace('-', '')
    j = json.loads(get(f'https://www.sec.gov/Archives/edgar/data/1636222/{a}/index.json'))
    for it in j['directory']['item']:
        if it['name'].endswith(('.htm', '.txt')) and 'index' not in it['name']:
            print(acc, it['name'], it.get('size'))
