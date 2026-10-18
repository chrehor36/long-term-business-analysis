# Dispatcher's check: each quoted fragment within the 400 characters before a v5 id must appear in that row.
import csv, re, sys
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
t = open(sys.argv[1], encoding='utf-8').read()
norm = lambda s: re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')).strip().lower()
n = bad = 0
for m in re.finditer(r'\[([MLR]\d{4}-\d{3}[a-z]?)\]', t):
    i = m.group(1)
    if i not in rows: print('MISSING', i); bad += 1; continue
    seg = t[max(0, m.start() - 400):m.start()]
    seg = re.split(r'\[[MLR]\d{4}-\d{3}[a-z]?\]', seg)[-1]
    for q in re.findall(r'"([^"]{6,})"', seg.replace('\u201c', '"').replace('\u201d', '"')):
        n += 1
        parts = [p for p in re.split(r'\s*\[\.\.\.\]\s*|\.\.\.', q) if p.strip()]
        if not all(norm(p).strip(' .,;:') in norm(rows[i]) for p in parts):
            bad += 1; print('SLIP?', i, '|', q[:150])
print('fragments', n, 'flagged', bad)
