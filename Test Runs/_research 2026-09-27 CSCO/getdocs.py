import sys, os, time, json, re
from fetch import get, strip
CIK = '858877'
rows = json.load(open('allfilings.json'))
os.makedirs('filings', exist_ok=True)
want = {'0001193125-25-033389','0001193125-24-070175','0001193125-24-046231','0001193125-24-028353','0001193125-23-239165',
        '0001104659-23-102595','0000858877-22-000018','0000858877-22-000029','0000858877-22-000015',
        '0000858877-26-000106','0000858877-26-000075','0000858877-26-000006','0001193125-25-277624',
        '0001193125-25-179820','0001193125-25-119864','0001193125-25-025114','0001193125-24-257224',
        '0001193125-24-200636','0001193125-24-139371','0001193125-24-036201','0001193125-23-277891','0001193125-23-214316'}
def fetch_idx(acc):
    return json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/index.json'))
for d, f, it, acc, doc in rows:
    ok = (f.startswith('10-K') and d >= '1995-01-01') or acc in want or (f=='DEF 14A' and d>='2023-01-01') or (f=='10-Q' and d>='2025-11-01')
    if not ok: continue
    tag = f.replace(' ', '').replace('/', '')
    out = f'filings/{d}_{tag}_{acc}.txt'
    if os.path.exists(out): continue
    try:
        if not doc:
            ix = fetch_idx(acc); names=[i['name'] for i in ix['directory']['item']]
            cand=[n for n in names if n.endswith('.txt') and not n.endswith('index.txt')] or names
            doc=cand[0]
        b = get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-", "")}/{doc}')
        open(out, 'w', encoding='utf-8').write(strip(b) if doc.endswith(('htm','html')) else b.decode('latin-1')); print(out, os.path.getsize(out)); time.sleep(0.15)
    except SystemExit as e:
        print('FAIL', acc, e); continue
    if f.startswith('8-K') or (f.startswith('10-K') and d<'2003-01-01'):
        try:
            ix = fetch_idx(acc)
            for itm in ix['directory']['item']:
                n = itm['name']
                if n.lower().endswith(('.htm', '.html', '.txt')) and n != doc and ('ex' in n.lower() or 'dex' in n.lower()) and 'index' not in n:
                    b = get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-", "")}/{n}')
                    o2 = f'filings/{d}_{tag}_{acc}_{n}.txt'
                    open(o2, 'w', encoding='utf-8').write(strip(b) if n.endswith(('htm','html')) else b.decode('latin-1')); print(o2, os.path.getsize(o2)); time.sleep(0.15)
        except Exception as e:
            print('ix fail', acc, e)
