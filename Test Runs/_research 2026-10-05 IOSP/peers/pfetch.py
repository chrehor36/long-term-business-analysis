import sys,re,html,urllib.request,time
sys.path.insert(0,'..')
from fetch import get,totext
for arg in sys.argv[1:]:
    cik,acc,doc,out=arg.split(',')
    b=get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}")
    open(out,'w',encoding='utf-8').write(totext(b)); print(out,len(b)); time.sleep(0.3)
