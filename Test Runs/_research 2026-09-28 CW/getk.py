import os, time
from fetch import get
from tables import flat
for line in open('annual_list.txt'):
    doc, acc, rep = line.split()
    yr = rep[:4]
    out=f'cache/k{yr}.txt'
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/26324/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(flat(b)); print(out, acc, len(b)); time.sleep(0.4)
