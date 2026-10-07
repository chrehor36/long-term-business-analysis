import sys
sys.argv=[sys.argv[0]]
exec(open('fetch.py').read().split("cik='1590976'")[0])
import time
for acc,doc,out,cik in [('0001193125-14-031218','d621288d424b4.htm','424B4_IPO_2014.txt','1590976')]:
    # IPO prospectus filed by agent; folder under issuer cik
    url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}'
    t=totext(get(url)); open(out,'w',encoding='utf-8').write(f'SOURCE: {url}\nACCESSION: {acc}\n'+t); print(out,len(t))
