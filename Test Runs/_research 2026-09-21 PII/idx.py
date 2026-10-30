import json,sys
from fetch import get
cik='931015'
for acc in sys.argv[1:]:
    a=acc.replace('-','')
    j=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/index.json'))
    for it in j['directory']['item']:
        n=it['name']
        if n.endswith(('.htm','.txt')) and not n.startswith('R'):
            print(acc,n,it.get('size'))
