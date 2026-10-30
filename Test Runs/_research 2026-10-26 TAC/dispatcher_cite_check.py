# Dispatcher's check (overnight 2026-10-26): every quoted fragment adjacent to a v5 id is in that id's row.
import csv, re, sys
rows = {r['id']: r for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
qcol = [c for c in next(iter(rows.values())).keys() if 'quote' in c.lower()][0]
def norm(s): return re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip().lower()
txt = open('Test Runs/2026-10-26 Run - TAC TransAlta.md', encoding='utf-8').read()
ids = re.findall(r'\*\*\[?([MLR]\d{4}-\d{3})\]?\*\*', txt)
bad = [i for i in set(ids) if i not in rows]; print('ids', len(set(ids)), 'missing', bad)
print('E-ids', re.findall(r'\[E\d+-\d+\]', txt))
pat = re.compile(r'["“]([^"”]{8,600})["”]\s*\*\*\[?([MLR]\d{4}-\d{3})\]?\*\*')
n = slips = 0
for frag, i in pat.findall(txt):
    if i not in rows: continue
    n += 1
    src = norm(rows[i][qcol])
    for part in re.split(r'\[\s*\.\.\.\s*\]|\.\.\.|…', frag):
        p = norm(part).strip(' .,;:')
        if len(p) > 3 and p not in src:
            slips += 1; print('SLIP', i, '|', part[:120])
print('pairs checked', n, 'slips', slips)
