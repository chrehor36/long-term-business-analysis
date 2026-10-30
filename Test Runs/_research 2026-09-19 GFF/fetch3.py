import sys, os, re, json
sys.path.insert(0, os.path.abspath('tools'))
import sources
sys.path.insert(0, os.path.abspath(os.path.join('Test Runs', '_research 2026-09-19 GFF')))
from fetch import strip

OUT = os.path.abspath(os.path.join('Test Runs', '_research 2026-09-19 GFF'))
CIK = '50725'

for name, acc in [('k8_20260819', '0000930413-26-002595'),
                  ('k8_20260811', '0001628280-26-055694'),
                  ('k8_20260804', '0001628280-26-052181'),
                  ('k8_20260611', '0000930413-26-001842'),
                  ('k8_20260205', '0001628280-26-005611'),
                  ('k8_20251119', '0000050725-25-000079')]:
    a = acc.replace('-', '')
    idx = 'https://www.sec.gov/Archives/edgar/data/%s/%s/index.json' % (CIK, a)
    try:
        j = json.loads(sources._get(idx, headers=sources.SEC_UA, cache_name='gff3_idx_' + name))
        items = [it['name'] for it in j['directory']['item']
                 if it['name'].lower().endswith('.htm') and not re.match(r'^R\d+\.htm$', it['name'])]
        print(name, acc, items)
        for doc in items:
            path = os.path.join(OUT, name + '_' + doc.replace('.htm', '') + '.txt')
            if os.path.exists(path):
                continue
            url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/%s' % (CIK, a, doc)
            raw = sources._get(url, headers=sources.SEC_UA, cache_name='gff3_' + name + '_' + doc)
            txt = strip(raw.decode('utf-8', 'replace') if isinstance(raw, bytes) else raw)
            open(path, 'w', encoding='utf-8').write(txt)
            print('   wrote', path.rsplit(os.sep, 1)[-1], len(txt))
    except Exception as e:
        print('FAIL', name, e)
