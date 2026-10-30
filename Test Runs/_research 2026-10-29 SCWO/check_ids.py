# Check: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# directly before an id (or run of ids) appears in one of those rows (quotes normalised).
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")).strip()
bad = 0
if re.search(r'\[E\d', run): print('E-id found'); bad += 1
ids = set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', run))
for i in sorted(ids):
    if i not in rows: print('MISSING', i); bad += 1
pat = re.compile(r'"([^"]{6,}?)"\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,\s]*)+)')
n = 0
for m in pat.finditer(run):
    frag = norm(m.group(1)); n += 1
    cited = re.findall(r'[MLR]\d{4}-\d{3}', m.group(2))
    parts = [norm(p) for p in frag.split('[...]')]
    if not any(all(p.strip(' .') in norm(rows.get(c, '')) for p in parts) for c in cited):
        print('NOT IN ROW', cited, frag[:90]); bad += 1
print(f'{len(ids)} ids, {n} quoted fragments checked, {bad} problems')
