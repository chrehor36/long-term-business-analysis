import sys
exec(open('fetch.py').read().split("cik='1590976'")[0])
import time
for arg in sys.argv[1:]:
    cik,acc,doc,out=arg.split(',')
    url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}'
    t=totext(get(url)); open(out,'w',encoding='utf-8').write(f'SOURCE: {url}\nACCESSION: {acc}\n'+t); print(out,len(t)); time.sleep(0.3)
