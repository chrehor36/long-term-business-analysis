import sys,os,json,time
sys.path.insert(0,'..')
from fetch import get,strip
tk,cik=sys.argv[1],sys.argv[2]; years=sys.argv[3].split(',')
fn=f'{tk}_sub.json'
if not os.path.exists(fn): open(fn,'wb').write(get(f'https://data.sec.gov/submissions/CIK{int(cik):010d}.json'))
d=json.load(open(fn)); L=[]
r=d['filings']['recent']
for f in d['filings'].get('files',[]):
    g=f'{tk}_{f["name"]}'
    if not os.path.exists(g): open(g,'wb').write(get('https://data.sec.gov/submissions/'+f['name']))
subs=[r]+[json.load(open(f'{tk}_{f["name"]}')) for f in d['filings'].get('files',[])]
for r in subs:
    for i in range(len(r['form'])):
        if r['form'][i]=='10-K' and r['reportDate'][i][:4] in years:
            L.append((r['reportDate'][i],r['accessionNumber'][i],r['primaryDocument'][i]))
print(d['name'])
for rd,acc,doc in sorted(set(L)):
    out=f'{tk}_{rd[:4]}.txt'; print(rd,acc,doc)
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); time.sleep(0.3)
