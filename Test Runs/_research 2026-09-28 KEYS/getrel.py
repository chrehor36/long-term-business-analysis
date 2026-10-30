# fetch the EX-99.1 earnings releases furnished with the Item 2.02 8-Ks -> cache/rel_<period>.txt
import re, json, os
from fetch import get
from tables import flat
d=json.load(open('cache/sub_0001601046.json')); r=d['filings']['recent']
for i in range(len(r['form'])):
    if r['form'][i]!='8-K' or '2.02' not in r['items'][i] or r['filingDate'][i]<'2023-01-01': continue
    acc=r['accessionNumber'][i]; a=acc.replace('-','')
    out=f"cache/rel_{r['filingDate'][i]}.txt"
    if os.path.exists(out): continue
    idx=get(f'https://www.sec.gov/Archives/edgar/data/1601046/{a}/').decode('utf-8','ignore')
    fs=[f for f in sorted(set(re.findall(r'href="/Archives/edgar/data/1601046/'+a+r'/([^"]+)"', idx))) if re.search(r'(?i)ex.*99|99.*press|pressrelease',f) and f.endswith('.htm')]
    for f in fs[:1]:
        open(out,'w',encoding='utf-8').write(flat(get(f'https://www.sec.gov/Archives/edgar/data/1601046/{a}/{f}'))); print(out, acc, f)
