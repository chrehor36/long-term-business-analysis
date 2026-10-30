import json,sys,os,time
sys.path.insert(0,'.')
from fetch import get,strip
P={'GD':'0000040533','BWXT':'0001486957','LMT':'0000936468','NOC':'0001133421','LHX':'0000202058'}
for t,c in P.items():
    fn=f'{t}_facts.json'
    if not os.path.exists(fn): open(fn,'wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json')); time.sleep(0.3)
    fn=f'{t}_sub.json'
    if not os.path.exists(fn): open(fn,'wb').write(get(f'https://data.sec.gov/submissions/CIK{c}.json')); time.sleep(0.3)
# 10-K text for GD and BWXT
for t in ['GD','BWXT']:
    d=json.load(open(f'{t}_sub.json')); r=d['filings']['recent']
    ks=[(r['reportDate'][i],r['accessionNumber'][i],r['primaryDocument'][i]) for i in range(len(r['form'])) if r['form'][i]=='10-K']
    fl=d['filings'].get('files',[])
    for f in fl:
        dd=json.loads(get('https://data.sec.gov/submissions/'+f['name']))
        ks+=[(dd['reportDate'][i],dd['accessionNumber'][i],dd['primaryDocument'][i]) for i in range(len(dd['form'])) if dd['form'][i]=='10-K']
    cik=P[t].lstrip('0')
    for rd,acc,doc in sorted(set(ks)):
        fy=int(rd[:4])
        if fy<2010 or fy not in (2012,2013,2015,2016,2018,2019,2021,2022,2024,2025): continue
        fn=f'{t}_10K_FY{fy}.txt'
        if os.path.exists(fn): continue
        b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}')
        open(fn,'w',encoding='utf-8').write(strip(b)); print(fn,acc,os.path.getsize(fn)); time.sleep(0.3)
