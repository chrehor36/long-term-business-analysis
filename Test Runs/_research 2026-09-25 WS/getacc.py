import json,sys
from fetch import get,strip
CIK='1968487'
def fetch_acc(acc,label):
    a=acc.replace('-','')
    items=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json'))['directory']['item']
    for it in items:
        n=it['name']
        if n.lower().endswith(('.htm','.html')) and not n.startswith(('R','Financial_Report')) and 'index' not in n:
            b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{n}')
            out=f"{label}_{n.rsplit('.',1)[0]}.txt"
            open(out,'w',encoding='utf-8').write(strip(b)); print(out,len(b))
for arg in sys.argv[1:]:
    acc,label=arg.split('=')
    fetch_acc(acc,label)
