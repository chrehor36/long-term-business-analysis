import sys, os, json, time
sys.path.insert(0, '..')
from fetch import get, strip
cik, acc, doc, out = sys.argv[1:5]
if not os.path.exists(out):
    b=get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); time.sleep(0.3)
print(out, os.path.getsize(out))
