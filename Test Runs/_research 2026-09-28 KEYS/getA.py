import os
from fetch import get
from tables import flat
for l in open('agilent_list.txt'):
    rep, fd, acc, doc = (l.split()+[''])[:4]
    if not doc or rep<'2001' or rep>'2013': continue
    out=f'cache/A{rep[:4]}.txt'
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/1090872/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(flat(b) if doc.endswith('htm') else b.decode('utf-8','ignore')); print(out)
