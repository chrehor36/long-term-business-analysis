# Dispatcher's check (tight): the quotation that ends within 40 characters before each v5 id is in that id's row.
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')).strip().lower()
t = run.replace('\u201c', '"').replace('\u201d', '"')
n = bad = 0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t):
    i = m.group(1)
    if i not in rows: print('MISSING ID', i); bad += 1; continue
    pre = t[max(0, m.start() - 40):m.start()]
    c = pre.rfind('"')
    if c < 0: continue
    end = m.start() - 40 + c if m.start() >= 40 else c
    o = t.rfind('"', 0, end)
    q = t[o + 1:end]
    if len(q) > 1500 or '\n\n' in q: continue
    n += 1
    for p in [p for p in re.split(r'\[\.\.\.\]|\.\.\.|\u2026', q) if p.strip()]:
        if norm(p).strip(' .,;:') not in norm(rows[i]):
            bad += 1; print('NOT IN ROW', i, '|', p[:150].replace('\n', ' '))
print('quotes checked', n, 'flags', bad)
