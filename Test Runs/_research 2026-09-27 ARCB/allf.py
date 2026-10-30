import json,sys,os,time,collections
sys.path.insert(0,'.')
from fetch import get
s=json.load(open('cache/submissions.json'))
rows=[]
def add(r):
    for i in range(len(r['form'])):
        rows.append((r['filingDate'][i],r['form'][i],r['accessionNumber'][i],r['primaryDocument'][i],r.get('items',['']*len(r['form']))[i],r['reportDate'][i]))
add(s['filings']['recent'])
for f in s['filings'].get('files',[]):
    fn='cache/'+f['name']
    if not os.path.exists(fn):
        open(fn,'wb').write(get('https://data.sec.gov/submissions/'+f['name'])); time.sleep(0.3)
    add(json.load(open(fn)))
rows.sort()
json.dump(rows,open('allfilings.json','w'))
print(rows[0][0],rows[-1][0],len(rows))
c=collections.Counter(r[1] for r in rows)
print(sorted(c.items(),key=lambda x:-x[1]))
deal={'S-4','S-4/A','425','DEFM14A','PREM14A','SC TO-T','SC TO-T/A','SC 14D9','SC 14D9/A','SC 13E3','SC TO-I','DEFM14C','SC 13D','SC 13D/A','SCHEDULE 13D','SCHEDULE 13D/A','8-K12B','S-8','S-3','S-3ASR'}
for r in rows:
    if r[1] in deal: print(r)
with open('filings_index.txt','w') as f:
    for r in rows: f.write('\t'.join(r)+'\n')
