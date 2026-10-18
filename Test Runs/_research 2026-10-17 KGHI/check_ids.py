"""Run check: no E-ids; every M/L/R id exists in the v5 ledger; every quoted fragment
on a line (or the paragraph) carrying an id appears in one of the ids' rows."""
import csv, re, sys
root = sys.argv[1]
run = open(sys.argv[2], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(root + '/principle_ledger_v5.csv', encoding='utf-8-sig'))}
bad = 0
if re.search(r'\[E\d', run):
    print('E-id found'); bad += 1
ids = set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', run))
for i in sorted(ids):
    if i not in rows:
        print('MISSING', i); bad += 1
norm = lambda s: re.sub(r'\s+', ' ', s.replace('‘', "'").replace('’', "'").replace('“', '"').replace('”', '"')).strip()
for para in re.split(r'\n\s*\n', run):
    pids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', para)
    if not pids: continue
    flat = ' '.join(para.split())
    # split on ids: each quote is checked against the ids that follow it in the same sentence group
    for m in re.finditer(r'"([^"]{6,})"\s*(?:\([^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]', flat):
        q, i = m.group(1), m.group(2)
        parts = [p.strip(' .,;') for p in re.split(r'\[\.\.\.\]', q)]
        src = norm(rows.get(i, ''))
        for p in parts:
            if p and norm(p) not in src:
                print('NOT IN ROW', i, '::', p[:90]); bad += 1
print('ids:', len(ids), 'problems:', bad)
sys.exit(1 if bad else 0)
