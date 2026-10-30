"""Check the run file's citations: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted
fragment written directly before an id (within the same sentence) is in that row's quote (elisions [...] split)."""
import csv, re, sys
RUN = sys.argv[1]
LEDGER = sys.argv[2]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(LEDGER, encoding='utf-8-sig'))}
text = open(RUN, encoding='utf-8').read()
problems = 0
e_ids = re.findall(r'\[E\d+-\d+\]', text)
if e_ids:
    print('E-ids found:', e_ids); problems += len(e_ids)
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', text)
for i in sorted(set(ids)):
    if i not in rows:
        print('MISSING id', i); problems += 1
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip()
# fragment immediately followed (optionally after a short gap) by one or more ids
pat = re.compile(r'"([^"]{3,700})"[^"]{0,40}?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[ ,]*)+)')
checked = 0
for m in pat.finditer(text):
    frag = m.group(1)
    cites = re.findall(r'\[([MLR]\d{4}-\d{3})\]', m.group(2))
    parts = [p.strip(' .,;') for p in re.split(r'\[\.\.\.\]', frag) if p.strip(' .,;')]
    ok_any = False
    for c in cites:
        q = norm(rows.get(c, ''))
        if all(norm(p) in q for p in parts):
            ok_any = True
    checked += 1
    if not ok_any:
        print('FRAGMENT NOT IN ROW', cites, '::', frag[:160]); problems += 1
print(f'ids: {len(set(ids))} distinct; fragments checked: {checked}; problems: {problems}')
