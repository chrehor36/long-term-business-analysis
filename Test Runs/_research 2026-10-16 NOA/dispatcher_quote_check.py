# Dispatcher check (overnight 2026-10-16): every quoted fragment beside a v5 id is in that row.
import csv, re, sys
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        rows[r['id']] = r
qcol = [k for k in next(iter(rows.values())).keys() if 'quote' in k.lower()][0]
norm = lambda s: re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')).strip().lower()
text = open(sys.argv[1], encoding='utf-8').read()
ids = re.findall(r'\b([MLR]\d{4}-\d{3})\b', text)
bad = [i for i in set(ids) if i not in rows]
print('ids', len(set(ids)), 'missing', bad, 'E-ids', re.findall(r'\[E\d-\d+\]', text))
slips = 0; checked = 0
for para in re.split(r'\n\s*\n', text):
    for m in re.finditer(r'[\"\u201c]([^\"\u201d]{6,}?)[\"\u201d][^\"\u201c]{0,40}?\*\*\[?([MLR]\d{4}-\d{3})', para):
        q, i = m.group(1), m.group(2)
        if i not in rows: continue
        checked += 1
        src = norm(rows[i][qcol])
        parts = [norm(p) for p in re.split(r'\[\.\.\.\]|\.\.\.|\u2026', q) if norm(p)]
        if not all(p.strip(' .,;:') in src for p in parts):
            slips += 1; print('SLIP', i, '|', q[:160])
print('checked', checked, 'slips', slips)
