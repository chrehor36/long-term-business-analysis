# usage: python getdoc.py ACCESSION DOC TAG [--ex]
import sys, re, json, time
from fetch import get
from tables import flat
acc, doc, tag = sys.argv[1:4]
cik='1001385'
a=acc.replace('-','')
b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{doc}')
open(f'cache/{tag}.txt','w',encoding='utf-8').write(flat(b)); print(tag, acc, len(b))
if '--ex' in sys.argv:
    time.sleep(1)
    idx=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/index.json'))
    files=[i['name'] for i in idx['directory']['item']]
    for f in files:
        if f!=doc and f.endswith('.htm') and re.search(r'ex', f, re.I):
            time.sleep(0.5)
            open(f'cache/{tag}_{f}.txt','w',encoding='utf-8').write(flat(get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{f}'))); print('  ex', f)
