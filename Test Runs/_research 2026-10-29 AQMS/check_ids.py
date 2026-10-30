# Checks the AQMS run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# immediately before an id (same sentence, "..." then **[id]**) appears in that row's quote.
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2], encoding='utf-8-sig'))}
bad = 0
if re.search(r'\[E\d', run): print('E-id found'); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING', i); bad += 1
for m in re.finditer(r'"([^"\n]{4,}?)"\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run):
    frag, i = m.group(1), m.group(2)
    if i in rows and frag not in rows[i]:
        print('NOT IN ROW', i, '::', frag); bad += 1
print('ids:', len(set(ids)), 'problems:', bad)
