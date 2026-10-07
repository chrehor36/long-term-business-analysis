import json, os, time
from fetch import get, strip
B='https://www.sec.gov/Archives/edgar/data/1437226/'
j=json.load(open('subs.json',encoding='utf-8')); r=j['filings']['recent']
for i in range(len(r['form'])):
    f=r['form'][i]; d=r['filingDate'][i]; acc=r['accessionNumber'][i]; doc=r['primaryDocument'][i]
    ok=(f in ('8-K','8-K/A') and d>='2024-01-01') or (f in ('SC 13D','SC 13D/A') and d>='2020-01-01') or (f=='8-K' and d in('2022-01-04','2020-09-22','2023-02-08','2024-01-19'))
    if not ok: continue
    out=('8K_' if f.startswith('8-K') else '13D_')+d.replace('-','')+'_MAIN_'+doc.replace('.htm','.txt')
    if os.path.exists(out): continue
    b=get(B+acc.replace('-','')+'/'+doc); open(out,'w',encoding='utf-8').write(strip(b)); print(out,os.path.getsize(out)); time.sleep(0.3)
