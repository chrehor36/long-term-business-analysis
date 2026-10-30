# usage: python getdoc.py ACCESSION DOC TAG [--ex]   -> cache/TAG.txt (flattened), with --ex also exhibits 99/2/3/10
import sys, re, os
from fetch import get
from tables import flat
acc, doc, tag = sys.argv[1:4]
a=acc.replace('-','')
cik='1601046'
b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{doc}')
open(f'cache/{tag}.txt','w',encoding='utf-8').write(flat(b)); print(tag, acc, len(b))
if '--ex' in sys.argv:
    idx=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/').decode('utf-8','ignore')
    files=sorted(set(re.findall(r'href="/Archives/edgar/data/'+cik+'/'+a+r'/([^"]+)"', idx)))
    print('  files', files)
    for f in files:
        if re.search(r'ex-?99|ex-?2|ex-?3|ex-?10|ex-?17|dex', f, re.I) and f.endswith('.htm'):
            open(f'cache/{tag}_{f}.txt','w',encoding='utf-8').write(flat(get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{f}'))); print('  ex', f)
