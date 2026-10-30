# dispatcher's citation check: every quoted fragment beside a v5 id is in that row
import csv, re, sys
run = sys.argv[1]
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        rows[r[list(r.keys())[0]]] = ' '.join(r.values())
def norm(s): return re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')).strip().lower()
t = open(run, encoding='utf-8').read()
ids = set(re.findall(r'\b([MLR]\d{4}-\d{3})\b', t))
missing = [i for i in ids if i not in rows]
print('ids', len(ids), 'missing', missing, 'E-ids', re.findall(r'\[E\d-\d+\]', t))
bad = 0
for para in re.split(r'\n\s*\n', t):
    for m in re.finditer(r'["\u201c]([^"\u201d]{8,}?)["\u201d][^"\u201c]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', para):
        q, i = m.group(1), m.group(2)
        if i not in rows: continue
        for frag in re.split(r'\[\.\.\.\]|\.\.\.|\u2026', q):
            frag = norm(frag).strip(' .,;:')
            if len(frag) > 5 and frag not in norm(rows[i]):
                bad += 1; print('SLIP', i, '|', frag[:120])
print('slips', bad)
