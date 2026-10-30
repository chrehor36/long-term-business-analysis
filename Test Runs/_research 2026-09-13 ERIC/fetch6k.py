import json, sys, re
sys.path.insert(0, '.')
import edgar, rows
CIK = 717826
s = json.load(open('submissions.json')); r = s['filings']['recent']
since = sys.argv[1]
for i in range(len(r['form'])):
    if r['form'][i] in ('6-K', '6-K/A') and r['filingDate'][i] >= since:
        acc = r['accessionNumber'][i]; a = acc.replace('-', '')
        idx = json.loads(edgar.get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json'))
        for it in idx['directory']['item']:
            n = it['name']
            if n.lower().endswith('.htm') and not n.startswith(acc):
                out = f"6k/{r['filingDate'][i]}_{acc[-6:]}__{n.rsplit('.',1)[0]}.txt"
                try:
                    h = edgar.get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{n}')
                    open(out, 'w', encoding='utf-8').write('\n'.join(rows.rows(h)))
                except Exception as e:
                    print('ERR', out, e)
        print('done', r['filingDate'][i], acc)
