# Dispatcher's check: every quoted fragment immediately before a v5 ledger id is in that row.
import csv, re, sys
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        rows[r['id']] = r
qcol = [k for k in next(iter(rows.values())).keys() if 'quote' in k.lower()][0]
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip().lower()
text = open(sys.argv[1], encoding='utf-8').read()
pairs = slips = 0
for m in re.finditer(r'[\"“]([^\"“”]{8,600})[\"”][^\"“\[]{0,40}\*\*\[([MLR]\d{4}-\d{3}[a-z]?)\]\*\*', text):
    frag, rid = m.group(1), m.group(2)
    pairs += 1
    if rid not in rows:
        print('MISSING ID', rid); slips += 1; continue
    q = norm(rows[rid][qcol])
    parts = [p.strip(' .,;:') for p in re.split(r'\[\.\.\.\]|\.\.\.|…', norm(frag)) if p.strip(' .,;:')]
    if not all(p in q for p in parts):
        slips += 1; print('SLIP?', rid, '|', frag[:120])
print('pairs', pairs, 'flagged', slips)
