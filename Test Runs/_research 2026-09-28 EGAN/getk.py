import json, os, time
from fetch import get
from tables import flat
d=json.load(open('cache/sub_0001066194.json'))
rows=[]
def add(r):
    for i in range(len(r['form'])):
        if r['form'][i] in ('10-K','10-K/A'): rows.append((r['reportDate'][i], r['form'][i], r['filingDate'][i], r['accessionNumber'][i], r['primaryDocument'][i]))
add(d['filings']['recent'])
for fx in d['filings'].get('files',[]):
    p='cache/'+fx['name']
    if os.path.exists(p): add(json.load(open(p)))
rows.sort()
with open('annual_list.txt','w') as f:
    for r in rows: f.write(' '.join(r)+'\n')
for rep, form, fd, acc, doc in rows:
    tag = ('k' if form=='10-K' else 'ka')+rep[:4]
    out=f'cache/{tag}.txt'
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/1066194/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(flat(b)); print(out, acc, len(b)); time.sleep(0.3)
