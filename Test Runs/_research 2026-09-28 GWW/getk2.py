import os
from fetch import get, strip
cik='277135'
for l in open('tenk_list.txt'):
    p=l.split(); acc=p[2]; fy=p[-1][:4]
    if int(fy)>2000: continue
    a=acc.replace('-','')
    out=f'cache/k{fy}_full.txt'
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{acc}.txt')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out))
