import json,re,html,os
from fetch import get
# DEF 14A
u="https://www.sec.gov/Archives/edgar/data/707549/000114036125036012/ny20050572x2_def14a.htm"
if not os.path.exists('DEF14A_2025.txt'):
    d=get(u).decode('utf-8',errors='replace')
    txt=re.sub(r'<[^>]+>',' ',d); txt=html.unescape(txt); txt=re.sub(r'[ \t\xa0]+',' ',txt)
    open('DEF14A_2025.txt','w',encoding='utf-8').write(txt); print('DEF14A',len(txt))
# earnings 8-Ks
s=json.load(open('submissions.json'))
r=s['filings']['recent']
eight=[(fd,an) for f,fd,an in zip(r['form'],r['filingDate'],r['accessionNumber']) if f=='8-K' and fd>='2024-07-01']
for fd,an in eight:
    accn=an.replace('-','')
    try:
        idx=json.loads(get(f"https://www.sec.gov/Archives/edgar/data/707549/{accn}/index.json"))
    except Exception as e:
        print('idx fail',an,e); continue
    for it in idx['directory']['item']:
        n=it['name']
        if re.search(r'ex99|exhibit99',n,re.I) and n.endswith(('.htm','.html')):
            out=f"8K_{fd}_{n}.txt"
            if os.path.exists(out): continue
            try:
                d=get(f"https://www.sec.gov/Archives/edgar/data/707549/{accn}/{n}").decode('utf-8',errors='replace')
            except Exception as e:
                print('fail',n,e); continue
            txt=re.sub(r'<[^>]+>',' ',d); txt=html.unescape(txt); txt=re.sub(r'[ \t\xa0]+',' ',txt)
            open(out,'w',encoding='utf-8').write(txt)
            print(out,len(txt))
