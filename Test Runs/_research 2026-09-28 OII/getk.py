import os
from fetch import get, strip
for line in open('tenk_list.txt'):
    fd, form, acc, doc, rep = (line.split()+[''])[:5]
    if form!='10-K' or rep < '2008-12-31' or rep >= '2025-12-31': continue
    out = f'cache/k{rep[:4]}.txt'
    if os.path.exists(out): continue
    a = acc.replace('-','')
    b = get(f'https://www.sec.gov/Archives/edgar/data/73756/{a}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, acc, os.path.getsize(out))
