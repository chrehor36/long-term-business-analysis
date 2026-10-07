import sys, json, os, re, time
sys.path.insert(0, os.path.dirname(__file__))
from fetch import get, strip
cik='3453'
def docs(acc):
    a=acc.replace('-','')
    idx=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/index.json'))
    return a,[i['name'] for i in idx['directory']['item']]
if __name__=='__main__':
    acc,prefix=sys.argv[1],sys.argv[2]
    out=os.path.dirname(__file__)
    a,names=docs(acc)
    print(acc,names)
    for n in names:
        if n.lower().endswith(('.htm','.txt')) and not n.endswith('-index.htm') and not n.endswith('-index-headers.html') and n!=acc+'.txt':
            b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{n}')
            fn=os.path.join(out,f'{prefix}_{n.rsplit(".",1)[0]}.txt')
            open(fn,'w',encoding='utf-8').write(strip(b)); print(fn,os.path.getsize(fn))
            time.sleep(0.3)
