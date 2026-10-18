# Check the AMBBY run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted
# fragment followed within a few characters by an id is in that row (elisions marked [...] split the fragment;
# whitespace and line wraps normalised).
import csv, re, sys
run, ledger = sys.argv[1], sys.argv[2]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ledger, encoding='utf-8-sig'))}
text = open(run, encoding='utf-8').read()
norm = lambda s: re.sub(r'\s+', ' ', s)
bad = 0
for e in re.findall(r'\[E\d+-\d+\]', text):
    print('E-id found:', e); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', text)
for i in sorted(set(ids)):
    if i not in rows:
        print('MISSING id', i); bad += 1
print(len(ids), 'id citations,', len(set(ids)), 'distinct')
pat = re.compile(r'"([^"]{6,600})"(.{0,40}?)\*\*\[([MLR]\d{4}-\d{3})\]\*\*', re.S)
checked = 0
for m in pat.finditer(text):
    frag, gap, i = m.group(1), m.group(2), m.group(3)
    if '"' in gap:
        continue
    checked += 1
    row = norm(rows.get(i, ''))
    pieces = [norm(p).strip(' .,') for p in frag.split('[...]')]
    if not all(p in row for p in pieces if p):
        print(f'NOT IN ROW {i}: "{norm(frag)}"'); bad += 1
print(checked, 'quoted fragments checked against their rows')
print('PASS' if bad == 0 else f'FAIL ({bad})')
