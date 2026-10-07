# usage: python fetchfiling.py LABEL ACCESSION  -> lists docs in the filing and writes text of htm docs
import sys, json, re, os
sys.path.insert(0, '.')
import edgar
CIK = 858446
label, acc = sys.argv[1], sys.argv[2]
only = sys.argv[3] if len(sys.argv) > 3 else None
a = acc.replace('-', '')
idx = json.loads(edgar.get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json'))
for it in idx['directory']['item']:
    name = it['name']; size = it.get('size')
    print(name, size)
    if name.lower().endswith(('.htm', '.html')) and (only is None or re.search(only, name)):
        h = edgar.get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{name}')
        t = edgar.strip_html(h)
        out = f'{label}__{name.rsplit(".",1)[0]}.txt'
        open(out, 'w', encoding='utf-8').write(t)
        print('  ->', out, len(t))
