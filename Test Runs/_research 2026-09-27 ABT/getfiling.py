import sys, os, json, time, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='1800'
def filing(acc, prefix, only_main=False):
    a=acc.replace('-','')
    idx=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json'))
    out=[]
    for it in idx['directory']['item']:
        n=it['name']
        if not re.search(r'\.(htm|html|txt)$',n,re.I): continue
        if n.endswith('-index.htm') or n.endswith('-index-headers.html') or n==f'{acc}.txt': continue
        if re.match(r'R\d+\.htm',n): continue
        fn=f'{prefix}_{re.sub(r"[^A-Za-z0-9._-]","",n)[:40]}.txt'
        if not os.path.exists(fn):
            b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{n}')
            open(fn,'w',encoding='utf-8').write(strip(b)); time.sleep(0.2)
        out.append((fn,os.path.getsize(fn)))
    return out
if __name__=='__main__':
    for x in filing(sys.argv[1], sys.argv[2]): print(x)
