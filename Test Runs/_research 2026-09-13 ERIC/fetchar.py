# usage: python fetchar.py LABEL ACCESSION -> row-form text of the main 20-F doc and every exhibit over 200KB
import sys, json
sys.path.insert(0, '.')
import edgar, rows
CIK = 717826
label, acc = sys.argv[1], sys.argv[2]; a = acc.replace('-', '')
idx = json.loads(edgar.get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json'))
for it in idx['directory']['item']:
    n = it['name']; sz = int(it.get('size') or 0)
    if n.lower().endswith(('.htm', '.html')) and not n.startswith(acc) and not n.startswith('R') and (sz > 200000 or '20f' in n.lower()):
        h = edgar.get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{n}')
        out = f'{label}__{n.rsplit(".",1)[0]}.txt'
        o = rows.rows(h); open(out, 'w', encoding='utf-8').write('\n'.join(o))
        print(out, sz, len(o))
