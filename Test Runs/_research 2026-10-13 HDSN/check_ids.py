# Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment immediately
# before an id (within the same sentence span) is found in that row's quote.
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2], encoding='utf-8-sig'))}
bad = 0
for m in re.finditer(r'\[(E\d[^\]]*)\]', run):
    print('E-id found:', m.group(1)); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
norm = lambda s: re.sub(r'\s+', ' ', s.replace('“','"').replace('”','"')).strip()
# fragments: a "..." quote followed within 40 chars by **[ID]**
for m in re.finditer(r'"([^"]{6,400})"[^"\[]{0,60}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run):
    frag, i = norm(m.group(1)), m.group(2)
    if i not in rows: continue
    q = norm(rows[i])
    parts = [p.strip(' ,.') for p in frag.split('[...]')]
    if not all(p in q for p in parts if p):
        print('FRAGMENT NOT IN ROW', i, '::', frag[:120]); bad += 1
print('ids checked:', len(set(ids)), 'problems:', bad)
sys.exit(1 if bad else 0)
