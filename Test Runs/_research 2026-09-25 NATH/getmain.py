import json,sys
from fetch import get,strip
CIK='69733'
for arg in sys.argv[1:]:
    acc,doc,label=arg.split('=')
    a=acc.replace('-','')
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{doc}')
    open(label+'.txt','w',encoding='utf-8').write(strip(b)); print(label,len(b))
