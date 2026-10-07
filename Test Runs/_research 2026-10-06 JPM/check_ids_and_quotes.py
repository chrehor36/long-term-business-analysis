"""JPM run 2026-10-06: every bold v5 id in the run file resolves in principle_ledger_v5.csv, and every quoted fragment
that sits directly before an id is found in that row (fragments split on [...]). A same-number-sooner check only."""
import csv, re, sys
run = sys.argv[1]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
t = open(run, encoding='utf-8').read()
ids = sorted(set(re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t)))
missing = [i for i in ids if i not in rows]
print(f"ids cited: {len(ids)}; missing from ledger: {missing}")
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip()
bad = 0
for m in re.finditer(r'"([^"]{8,})"[^"\n*]{0,12}\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t):
    q, i = m.group(1), m.group(2)
    src = norm(rows.get(i, ''))
    for frag in q.split('[...]'):
        f = norm(frag).strip(' .,;')
        if f and f not in src:
            bad += 1
            print(f"NOT FOUND in {i}: {f[:120]}")
print("quote fragments not found:", bad)
