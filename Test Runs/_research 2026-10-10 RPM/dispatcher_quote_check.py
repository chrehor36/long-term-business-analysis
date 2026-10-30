# Dispatcher's check (overnight 2026-10-10): every quoted fragment beside a v5 id is in that row's quote.
import csv, re, sys
csv.field_size_limit(10**9)
rows = {r['id']: r for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
t = open('Test Runs/2026-10-10 Run - RPM RPM International.md', encoding='utf-8').read()
norm = lambda s: re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')).strip().lower()
bad = n = 0
for m in re.finditer(r'["\u201c]([^"\u201d]{4,600}?)["\u201d][^"\u201c\[]{0,40}?\*{0,2}\[([MLR]\d{4}-\d{3}[a-z]?)\]', t):
    q, i = m.group(1), m.group(2)
    if i not in rows: print('PHANTOM', i); bad += 1; continue
    src = norm(rows[i]['quote_verbatim'])
    for frag in re.split(r'\[\.\.\.\]|\.\.\.|\u2026', q):
        f = norm(frag).strip(' ,.;:')
        if len(f) < 3: continue
        n += 1
        if f not in src: print('MISS', i, repr(f[:100])); bad += 1
print('E-ids:', len(re.findall(r'\[E\d-\d+\]', t)), '| fragments checked', n, '| problems', bad)
