# Citation check for the ANIOY run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment written immediately before an id is in that row (elisions [...] or ... split the fragment).
import csv, re, sys
RUN = sys.argv[1]; LEDGER = sys.argv[2]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(LEDGER, encoding='utf-8-sig'))}
def norm(t):
    t = t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    t = t.replace('—', '-').replace('–', '-').replace('�', '')
    return re.sub(r'\s+', ' ', t).strip().lower()
text = open(RUN, encoding='utf-8').read()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', text)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
flat = re.sub(r'\s+', ' ', text)
n = 0
for m in re.finditer(r'"([^"]{6,}?)"[\s,.;:)]*(?:\([^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    row = norm(rows[i]); n += 1
    for piece in re.split(r'\[\.\.\.\]|\.\.\.', frag):
        p = norm(piece).strip(' .,;:')
        if len(p) >= 4 and p not in row:
            print(f'NOT IN ROW {i}: "{piece.strip()}"'); bad += 1
print(f'{len(set(ids))} distinct ids, {n} quoted fragments checked, {bad} problems')
sys.exit(1 if bad else 0)
