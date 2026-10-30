# Dispatcher quote check, adjacency form: a quoted fragment followed within 25 characters by a bold id must be in that row.
import csv, re, sys
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8') as f:
    for r in csv.reader(f):
        if r: rows[r[0]] = ' '.join(r)
norm = lambda s: re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')).lower()
text = open(sys.argv[1], encoding='utf-8').read()
n = bad = 0
for m in re.finditer(r'"([^"]{8,}?)"[^"\n]{0,25}?\*\*\[([MLR]\d{4}-\d{3})\]', text, re.S):
    q, i = m.group(1), m.group(2); n += 1
    parts = [p.strip(' .,;') for p in q.split('[...]') if len(p.strip(' .,;')) > 4]
    if not all(norm(p) in norm(rows.get(i, '')) for p in parts):
        bad += 1; print('SLIP', i, '|', q[:120])
print(f'adjacent fragments {n} slips {bad}')
