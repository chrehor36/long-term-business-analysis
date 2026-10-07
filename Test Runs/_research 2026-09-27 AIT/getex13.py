import sys, os, time, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK = '109563'
rows = json.load(open('allfilings.json'))
for d, f, it, acc, doc in rows:
    if not (f.startswith('10-K') and '2000' <= d[:4] <= '2013') or f == '10-KA': continue
    if d.startswith('2005'): continue
    base = f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-", "")}/'
    ix = json.loads(get(base + 'index.json'))
    names = [i['name'] for i in ix['directory']['item']]
    cands = [n for n in names if re.search(r'ex[-_]?13|ex13|exv13', n, re.I)]
    if not cands:
        print(d, 'no ex13 in', names); continue
    for n in cands:
        out = f'filings/{d}_EX13_{acc}.txt'
        b = get(base + n)
        open(out, 'w', encoding='utf-8').write(strip(b)); print(out, n, os.path.getsize(out)); time.sleep(0.3)
