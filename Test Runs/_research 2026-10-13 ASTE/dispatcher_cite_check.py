# Dispatcher's check (overnight 2026-10-13): every quoted fragment beside a v5 id is in that row.
import csv, re, sys
run = sys.argv[1]
rows = {r['id']: r for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
def norm(s): return re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')).strip().lower()
txt = open(run, encoding='utf-8').read()
bad = 0; n = 0
for line in txt.split('\n'):
    ids = re.findall(r'\[?\*\*\[?([MLR]\d{4}-\d{3})\]?\*\*', line) + re.findall(r'\[([MLR]\d{4}-\d{3})\]', line)
    ids = list(dict.fromkeys(ids))
    if not ids: continue
    for i in ids:
        if i not in rows: print('MISSING ID', i); bad += 1
    if re.search(r'\bE\d-\d', line): print('E-ID?', line[:120])
    quotes = re.findall(r'"([^"]{8,})"', line.replace('\u201c', '"').replace('\u201d', '"'))
    for q in quotes:
        n += 1
        frags = [f for f in re.split(r'\s*\[\.\.\.\]\s*|\.\.\.', q) if len(f.strip()) > 3]
        ok = any(all(norm(f) in norm(rows[i]['quote_verbatim']) for f in frags) for i in ids if i in rows)
        if not ok: bad += 1; print('NOT IN ROW', ids, '|', q[:140])
print('quotes checked', n, 'problems', bad)
