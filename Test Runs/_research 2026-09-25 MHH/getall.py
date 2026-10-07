import json, re, os, time
from fetch import get, strip
B='https://www.sec.gov/Archives/edgar/data/1437226/'
j=json.load(open('subs.json',encoding='utf-8')); r=j['filings']['recent']
want={'10-K':'2016-01-01','10-Q':'2026-01-01','DEF 14A':'2026-01-01'}
docs=[]
for i in range(len(r['form'])):
    f=r['form'][i]; d=r['filingDate'][i]
    if f in want and d>=want[f]:
        tag={'10-K':'10K','10-Q':'10Q','DEF 14A':'DEF14A'}[f]
        docs.append((tag+'_'+d,r['accessionNumber'][i],r['primaryDocument'][i]))
for name,acc,doc in docs:
    out=name+'.txt'
    if os.path.exists(out): continue
    b=get(B+acc.replace('-','')+'/'+doc); open(out,'w',encoding='utf-8').write(strip(b)); print(out,os.path.getsize(out)); time.sleep(0.4)
# all 8-Ks since 2024-01-01 plus key older ones, all htm docs in each
for i in range(len(r['form'])):
    f=r['form'][i]; d=r['filingDate'][i]; acc=r['accessionNumber'][i]
    if not ((f in ('8-K','8-K/A') and d>='2024-01-01') or (f in ('SC 13D','SC 13D/A','8-K','8-K/A') and d>='2020-09-01' and d<='2020-10-31') or (f=='8-K' and d in ('2017-07-19','2017-07-13','2022-01-04','2021-04-07','2023-02-08'))): continue
    ix=B+acc.replace('-','')+'/'+acc+'-index.htm'
    h=get(ix).decode('utf-8','ignore')
    links=re.findall(r'href="(/Archives/edgar/data/1437226/[^"]+\.htm)"',h)
    for L in links:
        fn=L.split('/')[-1]
        out=('8K_' if f.startswith('8-K') else '13D_')+d.replace('-','')+'_'+fn.replace('.htm','.txt')
        if os.path.exists(out): continue
        b=get('https://www.sec.gov'+L); open(out,'w',encoding='utf-8').write(strip(b)); print(out,os.path.getsize(out)); time.sleep(0.3)
