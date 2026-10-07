import os, time, sys, json, re
sys.path.insert(0,'.')
from fetch import get, strip
for line in open('k_list.txt'):
    p=line.split()
    if len(p)<5 or p[2] not in ('10-K','10-K405'): continue
    fy=int(p[1][:4])-1
    if fy<2000 or fy>2014: continue
    acc=p[3]; a=acc.replace('-','')
    fn=f'cache/x13_{fy}.txt'
    if os.path.exists(fn): continue
    idx=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/18230/{a}/index.json'))
    names=[it['name'] for it in idx['directory']['item'] if re.search(r'(ex|exx|ex_)[-_]?13',it['name'],re.I) and re.search(r'\.htm',it['name'],re.I)]
    if not names:
        names=[it['name'] for it in idx['directory']['item'] if re.search(r'13',it['name']) and it['name'].endswith(('htm','txt'))]
    print(fy, names)
    if not names: continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/18230/{a}/{names[0]}')
    open(fn,'w',encoding='utf-8').write(strip(b)); print(fy, os.path.getsize(fn)); time.sleep(0.3)
