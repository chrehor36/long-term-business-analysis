import sys,os,json,re,time
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
from fetch import get, strip
for acc,tag in [('0000200406-17-000006','2016'),('0000200406-14-000033','2013'),('0000950123-11-018128','2010'),('0000200406-22-000022','2021')]:
    a=acc.replace('-','')
    idx=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/200406/{a}/index.json'))
    for it in idx['directory']['item']:
        n=it['name']
        if not re.search(r'\.htm$',n): continue
        if re.match(r'R\d+\.htm',n) or 'index' in n: continue
        if not (re.search(r'10-?k|10k|ex-?13|ex13|jnj-2',n,re.I)): continue
        out=os.path.join(os.path.dirname(os.path.abspath(__file__)),f'jnj_{tag}_{n[:40]}.txt')
        if not os.path.exists(out):
            open(out,'w',encoding='utf-8').write(strip(get(f'https://www.sec.gov/Archives/edgar/data/200406/{a}/{n}'))); time.sleep(0.2)
        print(out,os.path.getsize(out))
