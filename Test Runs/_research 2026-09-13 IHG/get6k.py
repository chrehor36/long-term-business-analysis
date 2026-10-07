import json, sys, os
sys.path.insert(0, '.')
import edgar
s = json.load(open('submissions.json'))
r = s['filings']['recent']
want = sys.argv[1:]  # date prefixes or 'all2026'
for i in range(len(r['form'])):
    if r['form'][i] != '6-K': continue
    d = r['filingDate'][i]
    if not any(d.startswith(w) for w in want): continue
    acc = r['accessionNumber'][i]; doc = r['primaryDocument'][i]
    url = f"https://www.sec.gov/Archives/edgar/data/858446/{acc.replace('-','')}/{doc}"
    t = edgar.strip_html(edgar.get(url))
    desc = r['primaryDocDescription'][i].replace(' ','_').replace('/','-')
    fn = f"k/{d}_{desc}_{acc}.txt"
    open(fn, 'w', encoding='utf-8').write(t)
    print(fn, len(t))
