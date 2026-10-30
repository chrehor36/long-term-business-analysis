"""Check the ASTE run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
standing in the same sentence-chunk just before an id appears in that id's row (normalised quotes and spaces)."""
import csv, re, sys
run = "Test Runs/2026-10-13 Run - ASTE Astec Industries.md"
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
t = open(run, encoding='utf-8').read()
def norm(x):
    x = x.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    return re.sub(r'\s+', ' ', x).strip().lower()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', t)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# quoted fragments followed (within the same chunk) by one or more ids
for m in re.finditer(r'((?:"[^"\n]*(?:\n[^"\n]*)*?"[^"\[]{0,40})+)((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[ ,]*)+)', t):
    quotes = re.findall(r'"([^"]+)"', m.group(1))
    idl = re.findall(r'[MLR]\d{4}-\d{3}', m.group(2))
    for q in quotes:
        for piece in re.split(r'\s*\[\.\.\.\]\s*', q):
            piece = piece.strip(' ,.;:')
            if len(piece) < 4: continue
            if not any(norm(piece) in norm(rows.get(i, '')) for i in idl):
                print('NOT IN ROW', idl, '::', piece[:90]); bad += 1
print('ids cited:', len(set(ids)), '| problems:', bad)
sys.exit(1 if bad else 0)
