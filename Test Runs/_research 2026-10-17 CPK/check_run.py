# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# immediately beside an id (the quote closes, then the id follows within the same sentence) is in that row.
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip()
prob = 0
eids = re.findall(r'\[E\d+-\d+\]', run)
if eids: print('E-ids found:', eids); prob += len(eids)
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); prob += 1
# quoted fragments followed by ids: "....." **[ID]** or "....." [...] **[ID]**
for m in re.finditer(r'"([^"]{3,}?)"((?:\s*(?:\*\*)?\[[MLR]\d{4}-\d{3}\](?:\*\*)?,?)+)', run):
    frag = m.group(1)
    fid = re.findall(r'[MLR]\d{4}-\d{3}', m.group(2))
    parts = [p.strip() for p in re.split(r'\.\.\.|\[\.\.\.\]', frag) if p.strip()]
    for i in fid:
        if i not in rows: continue
        q = norm(rows[i])
        for p in parts:
            if norm(p) not in q:
                print(f'FRAGMENT NOT IN {i}: "{p}"'); prob += 1
print('ids cited:', len(set(ids)), 'problems:', prob)
