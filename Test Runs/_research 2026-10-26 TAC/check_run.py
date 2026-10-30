# Run-file check: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# immediately before an id (within the same sentence) is in that row's quote. Usage: python -I check_run.py RUNFILE LEDGER
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2], encoding='utf-8-sig'))}
def norm(s):
    s = s.replace('�', "'").replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('—', '-').replace('–', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', run)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# quoted fragment directly followed by an id: "...." **[ID]** or "...." (x) **[ID]**
pairs = re.findall(r'[\"“]([^\"“”]{6,400})[\"”][^\"“”\n]{0,12}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run)
checked = 0
for frag, i in pairs:
    if i not in rows: continue
    q = norm(rows[i]); checked += 1
    for piece in norm(frag).split('[...]'):
        piece = piece.strip(' .,;:')
        if piece and piece not in q:
            print('FRAGMENT NOT IN ROW', i, '|', piece[:120]); bad += 1
print('ids cited:', len(set(ids)), 'fragment pairs checked:', checked, 'problems:', bad)
