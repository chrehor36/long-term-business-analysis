from fetch import get
import json,sys
for acc in sys.argv[1:]:
    a=acc.replace('-','')
    j=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/918646/{a}/index.json'))
    print(acc,[ (x['name'],x.get('size')) for x in j['directory']['item'] if x['name'].endswith('.htm')])
