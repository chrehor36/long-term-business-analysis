"""Citation check for the LRCX run file (the brief's Output section).
1. no E-ids; 2. every M/L/R id resolves in principle_ledger_v5.csv;
3. every quoted fragment that stands directly before an id (a quote, optional punctuation, then the id) is in that row,
   elisions written ' ... ' or '[...]' split into parts that must each be in the row, in order.
Run from the repo root: python "Test Runs/_research 2026-10-10 LRCX/check_citations.py"
"""
import csv, re, sys

RUN = "Test Runs/2026-10-10 Run - LRCX Lam Research.md"
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
text = open(RUN, encoding='utf-8').read()
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
fail = 0

e_ids = re.findall(r'\[E\d-\d+\]', text)
if e_ids:
    print('E-ids found:', e_ids); fail += 1

ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
for i in sorted(set(ids)):
    if i not in rows:
        print('MISSING id', i); fail += 1

pat = re.compile(r'"([^"]{3,}?)"[\s.,;:)]*\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
checked = 0
for m in pat.finditer(text):
    frag, i = m.group(1), m.group(2)
    if i not in rows:
        continue
    row = norm(rows[i])
    pos, ok = 0, True
    for part in re.split(r'\s*(?:\.\.\.|\[\.\.\.\])\s*', frag):
        part = norm(part).strip(' .,;')
        if not part:
            continue
        k = row.find(part, pos)
        if k < 0:
            ok = False; break
        pos = k + len(part)
    checked += 1
    if not ok:
        fail += 1
        print(f'NOT IN ROW {i}: "{frag[:120]}"')
print(f'{len(set(ids))} distinct ids, {checked} quoted fragments checked, {fail} failures')
sys.exit(1 if fail else 0)
