import os, time
from fetch import get
from tables import flat
for line in open('annual_list.txt'):
    p=line.split(); rep,form,fd,acc=p[:4]; doc=p[4] if len(p)>4 else ''
    tag=('k' if form=='10-K' else 'ka'+fd.replace('-',''))+rep[:4]
    out=f'cache/{tag}.txt'
    if os.path.exists(out) and os.path.getsize(out)>20000: continue
    a=acc.replace('-','')
    urls=([f'https://www.sec.gov/Archives/edgar/data/842023/{a}/{doc}'] if doc else [])+[f'https://www.sec.gov/Archives/edgar/data/842023/{a}/{acc}.txt']
    for u in urls:
        try:
            b=get(u); break
        except SystemExit as e: print('miss',u); b=None
    if b is None: continue
    open(out,'w',encoding='utf-8').write(flat(b)); print(out, acc, len(b)); time.sleep(0.3)
