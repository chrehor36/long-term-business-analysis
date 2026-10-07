import re, json
from fetch import get, strip
d=json.load(open('cache/sub_0001066194.json'))
r=d['filings']['recent']
for i in range(len(r['form'])):
    if 'SCHEDULE 13' in r['form'][i] or 'SC 13D' in r['form'][i]:
        if r['filingDate'][i] < '2023-01-01': continue
        acc=r['accessionNumber'][i]; a=acc.replace('-','')
        idx=get(f'https://www.sec.gov/Archives/edgar/data/1066194/{a}/').decode('utf-8','ignore')
        files=sorted(set(re.findall(r'href="/Archives/edgar/data/1066194/'+a+r'/([^"]+)"', idx)))
        print('#####', r['filingDate'][i], r['form'][i], acc, files)
        for f in files:
            if f.endswith('.xml') and 'primary' in f:
                t=strip(get(f'https://www.sec.gov/Archives/edgar/data/1066194/{a}/{f}'))
                open(f'cache/13d_{r["filingDate"][i]}.txt','w',encoding='utf-8').write(t)
                print(re.sub(r'\s+',' ',t)[:2500])
