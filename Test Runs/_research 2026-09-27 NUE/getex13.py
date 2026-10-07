import sys,os,time,json,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='73309'
L=[]
for f in ('submissions.json','submissions001.json'):
    s=json.load(open(f)); r=s['filings']['recent'] if 'filings' in s else s
    for i in range(len(r['form'])):
        if r['form'][i]=='10-K' and '2000'<=r['reportDate'][i][:4]<='2018':
            L.append((r['accessionNumber'][i],r['reportDate'][i][:4]))
for acc,fy in L:
    out='ex13_%s.txt'%fy
    if os.path.exists(out): continue
    a=acc.replace('-','')
    idx=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json'))
    names=[x['name'] for x in idx['directory']['item']]
    cand=[n for n in names if re.search(r'ex13|ex-13|dex13',n,re.I)]
    print(fy,acc,cand, [n for n in names if n.endswith(('.htm','.txt'))][:8])
    if cand:
        b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{cand[0]}')
        open(out,'w',encoding='utf-8').write(strip(b)); print(' ->',out,os.path.getsize(out))
    time.sleep(0.3)
