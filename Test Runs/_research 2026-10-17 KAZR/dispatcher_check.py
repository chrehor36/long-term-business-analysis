# Dispatcher's citation check: every quoted fragment near a v5 id must be in that row's quote.
import csv, re, sys, unicodedata
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        rows[r['id']] = r
qcol = [k for k in next(iter(rows.values())).keys() if 'quote' in k.lower()][0]
def norm(s):
    s = unicodedata.normalize('NFKC', s).replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    return re.sub(r'\s+', ' ', s).lower().strip()
text = open(sys.argv[1], encoding='utf-8').read()
paras = re.split(r'\n\s*\n', text)
bad = checked = 0; ids_seen = set()
for p in paras:
    ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', p)
    for i in ids:
        ids_seen.add(i)
        if i not in rows: print('MISSING', i); bad += 1
    if re.search(r'\[E\d', p): print('E-ID', p[:80]); bad += 1
    if not ids: continue
    for frag in re.findall(r'"([^"]{12,})"', p):
        parts = [norm(x) for x in frag.split('[...]') if len(norm(x)) > 5]
        checked += 1
        ok = all(any(pt.strip(' .,;') in norm(rows[i][qcol]) for i in ids if i in rows) for pt in parts)
        if not ok:
            print('FRAG NOT IN ROWS', ids, '|', frag[:120])
            bad += 1
print('ids', len(ids_seen), 'fragments', checked, 'problems', bad)
