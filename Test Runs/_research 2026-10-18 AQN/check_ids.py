# check the run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment that stands
# immediately before an id (same text segment since the previous id) appears verbatim in that row
# (pieces split on [...] must appear in order). Run from the repo root: python -I "Test Runs/_research 2026-10-18 AQN/check_ids.py"
import csv, re, sys
RUN = "Test Runs/2026-10-18 Run - AQN Algonquin Power & Utilities.md"
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
text = open(RUN, encoding='utf-8').read()

def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip()

bad = 0
eids = re.findall(r'\[E\d+-\d+\]', text)
if eids:
    print('E-ids found:', eids); bad += 1
ids = list(re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text))
plain = set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', text))
for i in sorted(plain):
    if i not in rows:
        print('MISSING id', i); bad += 1
prev_end = 0
checked = 0
for m in ids:
    seg = text[prev_end:m.start()]
    prev_end = m.end()
    # the last quotation in the segment, if the segment ends right after it (only spaces, commas or "and" between)
    q = list(re.finditer(r'"([^"]{4,})"', seg))
    if not q:
        continue
    last = q[-1]
    tail = seg[last.end():]
    if len(norm(tail)) > 3 and not re.fullmatch(r'[\s,;:.\)\(]*', tail):
        continue
    frag = last.group(1)
    row = norm(rows.get(m.group(1), ''))
    pieces = [norm(p).strip(' .,;') for p in re.split(r'\[\.\.\.\]', frag)]
    pos = 0
    ok = True
    for p in pieces:
        if not p:
            continue
        k = row.find(p, pos)
        if k < 0:
            ok = False; break
        pos = k + len(p)
    checked += 1
    if not ok:
        print('NOT IN ROW', m.group(1), '|', frag[:160]); bad += 1
print(f'ids: {len(plain)} distinct, {len(ids)} citations; quoted fragments checked: {checked}; problems: {bad}')
sys.exit(1 if bad else 0)
