import sys,os,time,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='894405'
rows=json.load(open('allfilings.json'))
L=[]
for d,f,acc,doc,it,rep in rows:
    if f in ('10-K','10-K/A') and d>='2004-01-01' and doc:
        L.append((acc,doc,'tenk_%s%s.txt'%(rep[:4], 'A' if f=='10-K/A' else '')))
L+=[('0001104659-26-088612','arcb-20260630x10q.htm','tenq_2606.txt'),
('0001104659-26-053753','arcb-20260331x10q.htm','tenq_2603.txt'),
('0001104659-26-027357','tmb-20260424xdef14a.htm','proxy_2026.txt'),
('0001558370-25-002960','tmb-20250425xdef14a.htm','proxy_2025.txt')]
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'cache'))
for acc,doc,out in L:
    if os.path.exists(out): continue
    try: b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    except SystemExit as e: print('FAIL',out,e); continue
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, acc, os.path.getsize(out)); time.sleep(0.3)
