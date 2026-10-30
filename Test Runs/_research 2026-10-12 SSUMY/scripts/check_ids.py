# Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that sits
# immediately before an id (same clause, after the previous id) is a substring of that id's row (normalized).
import csv, re, sys
RUN = sys.argv[1]; LEDGER = sys.argv[2]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(LEDGER, encoding='utf-8-sig'))}
txt = open(RUN, encoding='utf-8').read()
def norm(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('\ufffd', '').replace('\u2014', '-').replace('\u2013', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()
bad = 0
for m in re.finditer(r'\[E\d', txt):
    print('E-ID FOUND at', m.start()); bad += 1
ids = list(re.finditer(r'\[([MLR]\d{4}-\d{3})\]', txt))
for m in ids:
    if m.group(1) not in rows:
        print('MISSING ID', m.group(1)); bad += 1
prev = 0
checked = 0
for m in ids:
    seg = txt[prev:m.start()]
    prev = m.end()
    # only the text after the last sentence break before the id and its own clause: take last 400 chars
    seg = seg[-400:]
    for q in re.findall(r'[\u201c"]([^\u201c\u201d"]{6,}?)[\u201d"]', seg):
        parts = [p for p in re.split(r'\[\.\.\.\]', q) if p.strip()]
        row = norm(rows.get(m.group(1), ''))
        ok = all(norm(p).strip(' .,') in row for p in parts)
        checked += 1
        if not ok:
            print(f'NOT IN ROW {m.group(1)}: "{q[:120]}"')
print(f'ids: {len(ids)} ({len(set(i.group(1) for i in ids))} distinct); fragments checked: {checked}; hard failures (E-ids, missing ids): {bad}')
