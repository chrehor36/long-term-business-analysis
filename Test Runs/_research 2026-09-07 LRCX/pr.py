import json,re,html,os
from fetch import get
s=json.load(open('submissions.json'))
r=s['filings']['recent']
eight=[(fd,an) for f,fd,an in zip(r['form'],r['filingDate'],r['accessionNumber']) if f=='8-K' and fd>='2024-04-01']
for fd,an in eight:
    accn=an.replace('-','')
    try:
        idx=json.loads(get(f"https://www.sec.gov/Archives/edgar/data/707549/{accn}/index.json"))
    except Exception as e:
        print('idx fail',an,e); continue
    for it in idx['directory']['item']:
        n=it['name']
        if 'exhibit' in n.lower() and n.endswith('.htm'):
            out=f"PR_{fd}.txt"
            if os.path.exists(out): continue
            d=get(f"https://www.sec.gov/Archives/edgar/data/707549/{accn}/{n}").decode('utf-8',errors='replace')
            txt=re.sub(r'<[^>]+>',' ',d); txt=html.unescape(txt); txt=re.sub(r'[ \t\xa0]+',' ',txt)
            open(out,'w',encoding='utf-8').write(txt)
            print(out,n,len(txt))
