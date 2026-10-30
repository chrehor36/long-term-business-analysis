import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK = '109563'
rows = json.load(open('allfilings.json'))
os.makedirs('filings', exist_ok=True)
want8 = {'0000109563-26-000031', '0001193125-24-263833', '0001193125-25-249961', '0000109563-25-000049',
         '0001193125-18-006483', '0000109563-18-000052', '0000109563-25-000063', '0000109563-26-000035',
         '0000109563-26-000019', '0000109563-26-000013', '0000109563-25-000103', '0000109563-24-000092'}
for d, f, it, acc, doc in rows:
    ok = (f.startswith('10-K') and d >= '2000-01-01') or acc in want8 or (f == 'DEF 14A' and d >= '2026-01-01') or (f == '10-Q' and d >= '2026-04-01')
    if not ok: continue
    tag = f.replace(' ', '').replace('/', '')
    out = f'filings/{d}_{tag}_{acc}.txt'
    if os.path.exists(out): continue
    b = get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-", "")}/{doc}')
    open(out, 'w', encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.2)
    if f.startswith('8-K'):
        try:
            ix = json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-", "")}/index.json'))
            for itm in ix['directory']['item']:
                n = itm['name']
                if n.lower().endswith(('.htm', '.html', '.txt')) and n != doc and 'ex' in n.lower():
                    b = get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-", "")}/{n}')
                    o2 = f'filings/{d}_{tag}_{acc}_{n}.txt'
                    open(o2, 'w', encoding='utf-8').write(strip(b)); print(o2, os.path.getsize(o2)); time.sleep(0.2)
        except Exception as e:
            print('ix fail', acc, e)
