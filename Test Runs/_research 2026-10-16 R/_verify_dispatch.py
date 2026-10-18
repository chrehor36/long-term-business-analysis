# Dispatcher's citation check: every quoted fragment beside a v5 id is in that row's quote.
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
def norm(s): return re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')).strip().lower()
ids = re.findall(r'\*\*\[?([MLR]\d{4}-\d{3})\]?\*\*', run)
print('ids cited', len(ids), 'distinct', len(set(ids)), 'missing', sorted(set(i for i in ids if i not in rows)))
print('E-ids', re.findall(r'\[E\d-\d+\]', run))
slips = 0; checked = 0
for m in re.finditer(r'"([^"]{8,}?)"[^"\n]{0,12}?\*\*\[?([MLR]\d{4}-\d{3})', run.replace('\u201c', '"').replace('\u201d', '"')):
    q, i = m.group(1), m.group(2)
    if i not in rows: continue
    src = norm(rows[i]['quote_verbatim'])
    checked += 1
    parts = [p for p in re.split(r'\[\.\.\.\]|\.\.\.', q) if p.strip()]
    if not all(norm(p).strip(' .,;:') in src for p in parts):
        slips += 1; print('SLIP', i, '|', q[:150])
print('quotes checked', checked, 'slips', slips)
