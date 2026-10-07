import os, time
from fetch import get
from tables import flat
for line in open('annual_list.txt'):
    doc, acc, fd = line.split()
    yr = str(int(fd[:4])-1)
    out=f'cache/k{yr}.txt'
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/1141391/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(flat(b)); print(out, acc, len(b)); time.sleep(0.5)
