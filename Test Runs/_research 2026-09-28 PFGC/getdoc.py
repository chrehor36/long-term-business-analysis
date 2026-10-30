# usage: python getdoc.py ACCESSION DOC TAG [--ex]
import sys, re
from fetch import get
from tables import flat
acc, doc, tag = sys.argv[1:4]
cik='1618673'
a=acc.replace('-','')
b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{doc}')
open(f'cache/{tag}.txt','w',encoding='utf-8').write(flat(b)); print(tag, acc, len(b))
if '--ex' in sys.argv:
    idx=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/').decode('utf-8','ignore')
    files=sorted(set(re.findall(r'href="/Archives/edgar/data/'+cik+'/'+a+r'/([^"]+)"', idx)))
    for f in files:
        if f!=doc and f.endswith('.htm') and re.search(r'ex|99|d1|d2|d3|d4|d5|d6|d7|d8|d9', f, re.I):
            open(f'cache/{tag}_{f}.txt','w',encoding='utf-8').write(flat(get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{f}'))); print('  ex', f)
