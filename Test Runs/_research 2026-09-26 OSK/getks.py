import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
L=[]
for fn in ['submissions.json','sub001.json','sub002.json']:
    d=json.load(open(fn)); r=d['filings']['recent'] if 'filings' in d else d
    for i in range(len(r['form'])):
        if r['form'][i] in ('10-K','10-K405','10-K/A','10-QT','10-KT') and r['primaryDocument'][i]:
            L.append((r['reportDate'][i],r['form'][i],r['accessionNumber'][i],r['primaryDocument'][i],r['filingDate'][i]))
for rd,form,acc,doc,fd in sorted(L):
    print(rd,form,acc,doc,fd)
    if rd<'2006-01-01': continue
    tag={'10-K':'tenk','10-K/A':'tenkA','10-QT':'tenqt','10-KT':'tenkt','10-K405':'tenk'}[form]
    fn=f'{tag}_{rd}.txt'
    if os.path.exists(fn): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/775158/{acc.replace("-","")}/{doc}')
    open(fn,'w',encoding='utf-8').write(strip(b)); print('  ->',fn,os.path.getsize(fn)); time.sleep(0.3)
