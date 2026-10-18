# Dispatcher's citation check (overnight 2026-10-13): every quoted fragment near a v5 id is in that row.
import csv, re, sys
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        rows[r['id']] = r['quote_verbatim']
def norm(s): return ' '.join(s.replace('\u2019', "'").replace('\u201c','"').replace('\u201d','"').split()).lower()
text = open(sys.argv[1], encoding='utf-8').read()
ids = set(re.findall(r'\b([MLR]\d{4}-\d{3}[a-z]?)\b', text))
missing = [i for i in ids if i not in rows]
print('ids', len(ids), 'missing', missing, 'E-ids', re.findall(r'\[E\d-\d+\]', text))
slips = 0
for para in re.split(r'\n\s*\n', text):
    pids = re.findall(r'\b([MLR]\d{4}-\d{3}[a-z]?)\b', para)
    if not pids: continue
    for q in re.findall(r'"([^"]{12,})"', para.replace('\u201c','"').replace('\u201d','"')):
        frags = [norm(x) for x in re.split(r'\[\.\.\.\]|\.\.\.', q) if len(x.strip()) > 6]
        if not any(all(fr in norm(rows.get(p, '')) for fr in frags) for p in pids):
            slips += 1; print('NOT IN ROW', pids, '|', q[:110])
print('unmatched quotes (may be filing quotes, not ledger quotes):', slips)
