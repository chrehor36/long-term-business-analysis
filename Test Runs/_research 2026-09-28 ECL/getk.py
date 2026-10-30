import os, json, re
from fetch import get, strip
from show import clean
for line in open('tenk_list.txt'):
    p=line.split()
    if len(p)<5: continue
    fd, form, acc, doc, rep = p
    if form not in ('10-K',) or rep < '2007-12-31' or rep >= '2025-12-31': continue
    a=acc.replace('-','')
    d=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/31462/{a}/index.json'))
    names=[it['name'] for it in d['directory']['item']]
    ex13=[n for n in names if re.search(r'(ex13|ex-13|ex_13|x13)',n.lower()) and n.endswith('.htm')]
    for n,tag in [(doc,'')]+[(e,'_ex13') for e in ex13]:
        out=f'cache/k{rep[:4]}{tag}.txt'
        if os.path.exists(out): continue
        b=get(f'https://www.sec.gov/Archives/edgar/data/31462/{a}/{n}')
        open(out,'w',encoding='utf-8').write(strip(b))
        open(out.replace('.txt','c.txt'),'w',encoding='utf-8').write(clean(out))
        print(out, acc, n, os.path.getsize(out))
