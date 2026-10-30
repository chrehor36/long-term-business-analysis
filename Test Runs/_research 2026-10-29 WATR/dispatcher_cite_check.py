# Dispatcher's check (overnight cycle 2026-10-29, copied for WATR): each quoted fragment adjacent to a v5 id is in that row's quote.
import csv, re, sys, unicodedata
def n(s):
    s = unicodedata.normalize('NFKC', s).replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip().lower()
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        rows[r[list(r.keys())[0]]] = n(' '.join(r.values()))
t = open(sys.argv[1], encoding='utf-8').read()
pat = re.compile(r'["“]([^"”]{6,}?)["”][^"“\n]{0,40}?\*\*\[?([MLR]\d{4}-\d{3})')
bad = 0; k = 0
for m in pat.finditer(t):
    q, i = m.group(1), m.group(2); k += 1
    if i not in rows: print('MISSING ID', i); bad += 1; continue
    parts = [p for p in re.split(r'\[\s*\.\.\.\s*\]|\.\.\.|…', q) if p.strip()]
    if not all(n(p).strip(' .,;:') in rows[i] for p in parts):
        print('CHECK', i, '|', q[:120]); bad += 1
ids = set(re.findall(r'\b([MLR]\d{4}-\d{3})\b', t)); miss = [i for i in ids if i not in rows]
print('pairs', k, 'flagged', bad, 'ids', len(ids), 'missing', miss, 'E-ids', re.findall(r'\[E\d-\d+\]', t))
