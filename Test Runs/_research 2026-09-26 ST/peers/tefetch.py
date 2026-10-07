import sys,os,json,time,re
sys.path.insert(0,'..')
from fetch import get, strip
def tenks(cik):
    d=json.loads(get(f'https://data.sec.gov/submissions/CIK{cik:010d}.json'))
    r=d['filings']['recent']; L=[]
    for i in range(len(r['form'])):
        if r['form'][i]=='10-K': L.append((r['reportDate'][i],r['accessionNumber'][i],r['primaryDocument'][i]))
    for f in d['filings'].get('files',[]):
        dd=json.loads(get('https://data.sec.gov/submissions/'+f['name']))
        for i in range(len(dd['form'])):
            if dd['form'][i]=='10-K': L.append((dd['reportDate'][i],dd['accessionNumber'][i],dd['primaryDocument'][i]))
    return sorted(L)
t=sys.argv[1]; cik=int(sys.argv[2]); years=sys.argv[3].split(',')
for rd,acc,doc in tenks(cik):
    if rd[:4] in years:
        fn=f'{t}_10-K_FY{rd[:4]}.txt'
        if os.path.exists(fn): continue
        open(fn,'w',encoding='utf-8').write(strip(get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}')))
        print(fn,acc,rd); time.sleep(0.3)
