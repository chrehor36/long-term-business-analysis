# Dispatcher's check (overnight cycle 2026-10-14): every quoted fragment beside a v5 id is in that row.
import csv, re, sys, unicodedata
run = sys.argv[1]
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    return re.sub(r'\s+', ' ', s).strip().lower()
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8') as f:
    r = csv.reader(f); hdr = next(r)
    qi = [i for i, h in enumerate(hdr) if 'quote' in h.lower()][0]
    for row in r:
        rows[row[0]] = norm(row[qi])
text = open(run, encoding='utf-8').read()
ids = re.findall(r'\b([MLR]\d{4}-\d{3})\b', text)
missing = sorted(set(i for i in ids if i not in rows))
print('ids cited', len(set(ids)), 'missing', missing, 'E-ids', len(re.findall(r'\bE\d-\d+', text)))
slips = 0; checked = 0
for para in re.split(r'\n\s*\n', text):
    pids = re.findall(r'\b([MLR]\d{4}-\d{3})\b', para)
    if not pids: continue
    quotes = re.findall(r'"([^"]{12,})"|\u201c([^\u201d]{12,})\u201d', para)
    for q in quotes:
        q = q[0] or q[1]
        parts = [norm(p) for p in re.split(r'\[\.\.\.\]|\.\.\.|\u2026', q) if len(norm(p)) >= 8]
        ok = all(any(p.strip(' .,;:') in rows.get(i, '') for i in pids) for p in parts)
        checked += 1
        if not ok:
            slips += 1
            print('NOT IN ROW', pids, '|', q[:140])
print('quotes checked', checked, 'not found', slips)
