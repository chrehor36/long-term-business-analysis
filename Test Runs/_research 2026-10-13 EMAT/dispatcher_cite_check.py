# Dispatcher's check (overnight 2026-10-13): every quoted fragment beside a v5 id is in that row's quote.
import csv, re, sys, unicodedata
run = sys.argv[1]
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8') as f:
    r = csv.reader(f); hdr = next(r)
    for row in r: rows[row[0]] = row
def norm(s):
    s = unicodedata.normalize('NFKC', s).replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip().lower()
txt = open(run, encoding='utf-8').read()
bad = 0; n = 0
for m in re.finditer(r'[“"]([^"“”]{4,600})[”"]\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', txt):
    frag, rid = m.group(1), m.group(2); n += 1
    if rid not in rows: print('MISSING ID', rid); bad += 1; continue
    body = norm(' '.join(rows[rid]))
    for piece in re.split(r'\[\.\.\.\]|\.\.\.|…', frag):
        p = norm(piece).strip(' .,;:')
        if p and p not in body: print('SLIP', rid, repr(piece[:90])); bad += 1
ids = set(re.findall(r'\b([MLR]\d{4}-\d{3})\b', txt)); miss = [i for i in ids if i not in rows]
print('quoted pairs', n, 'ids', len(ids), 'missing', miss, 'E-ids', re.findall(r'\[E\d-\d+\]', txt), 'slips', bad)
