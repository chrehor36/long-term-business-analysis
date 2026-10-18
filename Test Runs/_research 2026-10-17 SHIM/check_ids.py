# Check for the SHIM run of 2026-10-17: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment directly beside an id (before or after it) is in that row's quote.
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
run = sys.argv[1]; ledger = sys.argv[2]
t = open(run, encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ledger, encoding='utf-8-sig'))}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', t)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
Q = r'["“]([^"“”]{3,400})["”]'
checked = 0
for m in re.finditer(Q + r'[,.:;]?\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t):
    frag, i = m.group(1), m.group(2); checked += 1
    if i in rows and norm(frag).rstrip('.') not in norm(rows[i]): print('NOT IN ROW (before)', i, '|', frag); bad += 1
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*[,:]?\s*' + Q, t):
    i, frag = m.group(1), m.group(2); checked += 1
    if i in rows and norm(frag).rstrip('.') not in norm(rows[i]): print('NOT IN ROW (after)', i, '|', frag); bad += 1
print(f'ids cited: {len(set(ids))} distinct, {len(ids)} uses; fragments checked: {checked}; problems: {bad}')
sys.exit(1 if bad else 0)
