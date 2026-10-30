# Citation check for the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately before an id (within the same sentence) appears in that row's quote.
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
run, ledger = sys.argv[1], sys.argv[2]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ledger, encoding='utf-8-sig'))}
t = open(run, encoding='utf-8').read()
bad = 0
for m in re.finditer(r'\[(E\d+-\d+)\]', t):
    print('E-id found:', m.group(1)); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# fragments: a "..." quote followed (within 12 chars) by **[ID]**
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
nfrag = 0
for m in re.finditer(r'"([^"]{8,600})"\s*(?:[^"\[]{0,12})\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t):
    frag, i = norm(m.group(1)), m.group(2)
    nfrag += 1
    q = norm(rows.get(i, ''))
    parts = [p.strip() for p in frag.split('[...]')]
    if not all(p in q for p in parts if p):
        print('FRAGMENT NOT IN ROW', i, '::', frag[:120]); bad += 1
print(f'{len(set(ids))} distinct ids, {nfrag} fragments checked, problems: {bad}')
