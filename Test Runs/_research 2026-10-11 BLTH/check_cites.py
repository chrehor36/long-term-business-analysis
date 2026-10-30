# Citation check for the BLTH run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately followed by a bold id is in that row (split on [...] elisions).
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2], encoding='utf-8-sig'))}
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
problems = 0
eids = re.findall(r'\[E\d+-\d+\]', run)
if eids: print('E-ids found:', eids); problems += len(eids)
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); problems += 1
frag = 0
for m in re.finditer(r'"([^"]{3,}?)"\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run):
    q, i = m.group(1), m.group(2)
    if i not in rows: continue
    for part in q.split('[...]'):
        p = norm(part).strip(' .,;')
        if not p: continue
        frag += 1
        if p not in norm(rows[i]):
            print('NOT IN ROW', i, '::', p); problems += 1
print(f'{len(set(ids))} distinct ids, {frag} fragments checked, {problems} problems')
