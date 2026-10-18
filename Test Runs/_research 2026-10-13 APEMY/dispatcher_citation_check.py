# Dispatcher's check (overnight 2026-10-13): every quoted fragment beside a v5 id is in that row.
import csv, re, sys, unicodedata
run = open(sys.argv[1], encoding='utf-8').read()
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8', newline='') as f:
    for r in csv.DictReader(f):
        rows[r[list(r.keys())[0]]] = r
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"').replace('\u2014', '-').replace('\u2013', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()
ids = set(re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run))
missing = [i for i in ids if i not in rows]
eids = re.findall(r'\[E\d-\d+\]', run)
slips = []
for m in re.finditer(r'"([^"]{8,}?)"\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run.replace('\u201c', '"').replace('\u201d', '"')):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    text = norm(' '.join(rows[i].values()))
    for part in re.split(r'\[\.\.\.\]|\.\.\.', frag):
        p = norm(part).strip(' .,;:')
        if len(p) > 3 and p not in text:
            slips.append((i, part[:90]))
print('ids', len(ids), 'missing', missing, 'E-ids', len(eids))
print('slips', len(slips))
for s in slips: print(' ', s)
