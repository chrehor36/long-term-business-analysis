# Dispatcher's check: every quoted fragment beside a v5 id is in that row's quote.
import csv, re, sys
run = open(sys.argv[1], encoding='utf8').read()
rows = {}
with open('principle_ledger_v5.csv', encoding='utf8', newline='') as f:
    rd = csv.reader(f); hdr = next(rd)
    qi = [i for i, h in enumerate(hdr) if 'quote' in h.lower()][0]
    for r in rd: rows[r[0]] = r[qi]
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip().lower()
ids = re.findall(r'\b([MLR]\d{4}-\d{3})\b', run)
missing = sorted(set(i for i in ids if i not in rows))
print('distinct ids', len(set(ids)), 'missing', missing, 'E-ids', re.findall(r'\[?\bE\d-\d+\b', run))
bad = 0; n = 0
for m in re.finditer(r'["“]([^"”]{8,}?)["”][^"“\n]{0,40}?\*\*\[?([MLR]\d{4}-\d{3})', run):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    n += 1
    parts = [p for p in re.split(r'\s*\[\.\.\.\]\s*|\s*\.\.\.\s*', frag) if p.strip()]
    if not all(norm(p) in norm(rows[i]) for p in parts):
        bad += 1; print('SLIP', i, '|', frag[:120])
print('fragments checked', n, 'slips', bad)
