# Checks the KLAC run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment that directly precedes an id (quote, optional punctuation, the id) is in that row.
import csv, re, sys, unicodedata
RUN = "Test Runs/2026-10-07 Run - KLAC KLA.md"
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
t = open(RUN, encoding='utf-8').read()
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip()
bad = 0
for e in re.findall(r'\[(E\d+-\d+)\]', t):
    print('E-id found', e); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING', i); bad += 1
# quote immediately before an id: "..." [punct/space] **[ID]**
for m in re.finditer(r'"([^"\n]{6,}?)"[\s.,;:)]*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', norm(t)):
    frag, i = m.group(1), m.group(2)
    row = norm(rows.get(i, ''))
    for piece in [p.strip(' .,') for p in frag.split('[...]') if p.strip(' .,')]:
        if piece not in row:
            print('FRAGMENT NOT IN ROW', i, '|', piece[:90]); bad += 1
print('ids', len(set(ids)), 'checked;', 'PASS' if not bad else f'FAIL ({bad})')
sys.exit(1 if bad else 0)
