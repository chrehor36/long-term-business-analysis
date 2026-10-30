import sys, json, os
sys.path.insert(0, '.')
import edgar, fetch_lib
CIK = 715153
lines = [l.split() for l in open('filings_list.txt', encoding='utf-8') if l.startswith('6-K ')]
since = sys.argv[1] if len(sys.argv) > 1 else '2021-04-01'
for p in lines:
    form, fdate, rdate, acc = p[0], p[1], p[2], p[3]
    if fdate < since: continue
    nd = acc.replace('-', '')
    try:
        idx = json.loads(edgar.get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{nd}/index.json'))
    except Exception as e:
        print('ERR', acc, e); continue
    for it in idx['directory']['item']:
        n = it['name']
        if not n.lower().endswith(('.htm', '.html')) or 'index' in n.lower(): continue
        if n[0] == 'R' and n[1:2].isdigit(): continue
        dest = os.path.join('6k', f"{fdate}_{acc[-6:]}__{n.rsplit('.',1)[0]}.txt")
        if os.path.exists(dest): continue
        try:
            r = fetch_lib.rows(edgar.get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{nd}/{n}'))
        except Exception as e:
            print('ERR', n, e); continue
        open(dest, 'w', encoding='utf-8').write('\n'.join(r))
print('done')
