# Dispatcher's check: every quoted fragment immediately before a v5 id is in that id's row.
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')).strip().lower()
idre = re.compile(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
prev = 0
for m in idre.finditer(run):
    seg = run[prev:m.start()]; prev = m.end()
    seg = seg[-400:]
    i = m.group(1)
    if i not in rows: print('MISSING ID', i); continue
    for q in re.findall(r'["\u201c]([^"\u201d]{4,})["\u201d]', seg):
        parts = [p for p in re.split(r'\[\.\.\.\]|\.\.\.', q) if p.strip()]
        for p in parts:
            if norm(p).strip(' .,;:') not in norm(rows[i]):
                print('NOT IN ROW', i, '|', p[:120])
print('done')
