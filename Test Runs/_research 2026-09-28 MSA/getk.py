import os
from fetch import get, strip
cik='66570'
for l in open('tenk_list.txt'):
    fd,form,acc,doc,rd=l.split()
    fy=rd[:4]
    out=f'cache/k{fy}.txt'
    if os.path.exists(out): continue
    a=acc.replace('-','')
    if int(fy)<=2008 or doc=='-':
        url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{acc}.txt'
    else:
        url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{doc}'
    b=get(url)
    open(out,'w',encoding='utf-8').write(strip(b))
    print(out,os.path.getsize(out))
