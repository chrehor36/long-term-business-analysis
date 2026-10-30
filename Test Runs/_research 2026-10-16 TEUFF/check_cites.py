"""Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
immediately before an id (same sentence, in double quotes) appears verbatim in that row (elisions [...] split)."""
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
run, ledger = sys.argv[1], sys.argv[2]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ledger, encoding='utf-8-sig'))}
t = open(run, encoding='utf-8').read()
bad = 0
for m in re.finditer(r'\[(E\d[\w-]*)\]', t):
    print('E-ID', m.group(1)); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING', i); bad += 1
# fragment check: a quote "..." followed within 3 chars by **[ID]**
for m in re.finditer(r'"([^"]{4,}?)"\s*(?:\(\w[^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t):
    frag, i = re.sub(r"\s+", " ", m.group(1)), m.group(2)
    row = rows.get(i, '')
    parts = [p.strip(' .') for p in frag.split('[...]')]
    ok = all(p in row for p in parts if p)
    if not ok:
        print('FRAG NOT IN ROW', i, '|', frag); bad += 1
print('ids:', len(set(ids)), 'bad:', bad)
