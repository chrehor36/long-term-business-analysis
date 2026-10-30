import os, time
from fetch import get
from tables import flat
for line in open('annual_list.txt'):
    doc, acc, fd = line.split()
    rep = fd[:4]; yr = str(int(rep)-1)
    out=f'cache/t{yr}.txt'
    if os.path.exists(out): continue
    cik = '1590714'
    b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(flat(b)); print(out, acc, len(b)); time.sleep(0.5)
