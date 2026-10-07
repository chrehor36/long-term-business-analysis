import sys,json,re,os
sys.path.insert(0,'.')
from fetch import get, strip
cik,form,year,out=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
d=json.loads(get(f'https://data.sec.gov/submissions/CIK{int(cik):010d}.json'))
rows=[]
def add(r):
    for i in range(len(r['form'])):
        if r['form'][i]==form: rows.append((r['reportDate'][i],r['filingDate'][i],r['accessionNumber'][i],r['primaryDocument'][i]))
add(d['filings']['recent'])
for f in d['filings'].get('files',[]): add(json.loads(get('https://data.sec.gov/submissions/'+f['name'])))
rows=[r for r in rows if r[0].startswith(year)]
print(rows)
r=rows[0]
b=get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{r[2].replace("-","")}/{r[3]}')
open(out,'w',encoding='utf-8').write(strip(b)); print(out,os.path.getsize(out),r)
