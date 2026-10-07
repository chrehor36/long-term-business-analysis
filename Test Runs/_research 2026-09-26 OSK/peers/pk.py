import sys,os,json,time
sys.path.insert(0,'..')
from fetch import get,strip
tk,cik,years=sys.argv[1],int(sys.argv[2]),sys.argv[3].split(',')
fn=f'{tk}_sub.json'
if not os.path.exists(fn): open(fn,'wb').write(get(f'https://data.sec.gov/submissions/CIK{cik:010d}.json'))
d=json.load(open(fn)); r=d['filings']['recent']
files=[f['name'] for f in d['filings'].get('files',[])]
rows=[(r['reportDate'][i],r['accessionNumber'][i],r['primaryDocument'][i]) for i in range(len(r['form'])) if r['form'][i]=='10-K']
for f in files:
    sub=json.loads(get('https://data.sec.gov/submissions/'+f))
    rows+=[(sub['reportDate'][i],sub['accessionNumber'][i],sub['primaryDocument'][i]) for i in range(len(sub['form'])) if sub['form'][i]=='10-K']
for rd,acc,doc in sorted(rows):
    if rd[:4] in years:
        out=f'{tk}_10K_{rd[:4]}.txt'
        if not os.path.exists(out):
            open(out,'w',encoding='utf-8').write(strip(get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}'))); time.sleep(0.3)
        print(out,acc,os.path.getsize(out))
