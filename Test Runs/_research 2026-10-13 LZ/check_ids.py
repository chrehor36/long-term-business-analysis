# Check the LZ run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment that sits beside an id (same sentence-run before the id) is in that id's row.
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2], encoding='utf-8-sig'))}
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', run)
if eids:
    print('E-ids found:', eids); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)
for i in sorted(set(ids)):
    if i not in rows:
        print('MISSING id', i); bad += 1
norm = lambda s: re.sub(r'\s+', ' ', s.replace('�', '').strip())
# a quote followed (within 12 chars, allowing ")", "," and spaces) by one or more bold ids
pat = re.compile(r'"([^"]{6,}?)"((?:[\s,.;:)]*(?:and\s+)?\*\*\[[MLR]\d{4}-\d{3}\]\*\*)+)')
checked = 0
for m in pat.finditer(run):
    frag = m.group(1)
    near = re.findall(r'\[([MLR]\d{4}-\d{3})\]', m.group(2))
    parts = [p for p in re.split(r'\s*\[\.\.\.\]\s*', frag) if p.strip()]
    ok = any(all(norm(p) in norm(rows.get(i, '')) for p in parts) for i in near)
    checked += 1
    if not ok:
        print('FRAGMENT NOT IN ROW', near, '::', frag[:120]); bad += 1
print(f'ids used: {len(set(ids))}; quoted fragments checked: {checked}; problems: {bad}')
sys.exit(1 if bad else 0)
