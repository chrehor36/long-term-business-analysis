"""Check the HTOO run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment
that sits immediately before an id (in the same sentence, quote then id) is a substring of that row."""
import csv, re, sys, unicodedata
root = sys.argv[1]
run = open(root + '/Test Runs/2026-10-12 Run - HTOO Fusion Fuel Green.md', encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(root + '/principle_ledger_v5.csv', encoding='utf-8-sig'))}
def norm(t):
    t = unicodedata.normalize('NFKC', t).replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    return re.sub(r'\s+', ' ', t).strip().lower()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', run)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# fragment immediately followed by an id: "....." **[ID]**
n = 0
for m in re.finditer(r'"([^"\n]{6,}?)"\s*(?:\([^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run):
    frag, i = m.group(1), m.group(2)
    n += 1
    parts = [p.strip() for p in frag.split('[...]') if p.strip()]
    if not all(norm(p) in norm(rows.get(i, '')) for p in parts):
        print('NOT IN ROW', i, '|', frag); bad += 1
print(f'{len(set(ids))} distinct ids, {n} adjacent fragments checked, {bad} problems')
sys.exit(1 if bad else 0)
