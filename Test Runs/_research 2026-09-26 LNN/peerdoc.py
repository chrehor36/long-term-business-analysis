import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
cik,acc,doc,out=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
a=acc.replace('-','')
b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{doc}')
open(out,'w',encoding='utf-8').write(strip(b)); print(out,os.path.getsize(out))
