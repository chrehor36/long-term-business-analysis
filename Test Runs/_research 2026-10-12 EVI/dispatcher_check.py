# Dispatcher quote check (overnight cycle 2026-10-12): every quoted fragment near a v5 id must be in that row.
import csv, re, sys
run = sys.argv[1]
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8') as f:
    for r in csv.reader(f):
        if r: rows[r[0]] = ' '.join(r)
norm = lambda s: re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')).lower()
text = open(run, encoding='utf-8').read()
ids = set(re.findall(r'\b([MLR]\d{4}-\d{3})\b', text))
eids = re.findall(r'\[E\d-\d+\]', text)
missing = [i for i in ids if i not in rows]
slips = 0; n = 0
for para in re.split(r'\n\s*\n', text):
    pids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', para)
    if not pids: continue
    for q in re.findall(r'"([^"]{12,})"', para):
        n += 1
        parts = [p.strip(' .,;') for p in q.split('[...]') if len(p.strip(' .,;')) > 5]
        if not any(all(norm(p) in norm(rows.get(i, '')) for p in parts) for i in pids):
            slips += 1; print('NOT IN ROW', pids, '|', q[:100])
print(f'ids {len(ids)} missing {missing} E-ids {len(eids)} fragments {n} unmatched {slips}')
