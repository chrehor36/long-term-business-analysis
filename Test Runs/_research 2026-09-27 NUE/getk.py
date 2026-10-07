import sys,os,time,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='73309'
L=[]
for f in ('submissions.json','submissions001.json'):
    s=json.load(open(f)); r=s['filings']['recent'] if 'filings' in s else s
    for i in range(len(r['form'])):
        if r['form'][i]=='10-K' and r['primaryDocument'][i] and '2001'<=r['reportDate'][i][:4]<='2024':
            L.append((r['accessionNumber'][i],r['primaryDocument'][i],'tenk_%s.txt'%r['reportDate'][i][:4]))
for acc,doc,out in L:
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.25)
