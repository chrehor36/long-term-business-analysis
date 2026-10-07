import json,re,html,os
from fetch import get
peers={'ASML':'0000937966','NVMI':'0001109345','ONTO':'0000704532','ACLS':'0001113232','ACMR':'0001680062','CAMT':'0001109138'}
for tick,cik in peers.items():
    out=f'peer_{tick}.txt'
    if os.path.exists(out): print('skip',out); continue
    try:
        s=json.loads(get(f'https://data.sec.gov/submissions/CIK{cik.zfill(10)}.json'))
    except Exception as e:
        print(tick,'sub fail',e); continue
    r=s['filings']['recent']
    row=None
    for f,fd,rd,an,pd in zip(r['form'],r['filingDate'],r['reportDate'],r['accessionNumber'],r['primaryDocument']):
        if f in ('10-K','20-F'):
            row=(f,fd,rd,an,pd); break
    if not row: print(tick,'no annual'); continue
    f,fd,rd,an,pd=row
    u=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{an.replace('-','')}/{pd}"
    try:
        d=get(u).decode('utf-8',errors='replace')
    except Exception as e:
        print(tick,'doc fail',e,u); continue
    txt=re.sub(r'<[^>]+>',' ',d); txt=html.unescape(txt); txt=re.sub(r'[ \t\xa0]+',' ',txt)
    open(out,'w',encoding='utf-8').write(txt)
    print(tick,f,fd,rd,an,len(txt))
