# Check the run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment immediately before an id is in that row.
import csv, re, sys
RUN = 'Test Runs/2026-10-13 Run - SIEGY Siemens AG.md'
rows = {r['﻿id'] if '﻿id' in r else r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('—', '-').replace('–', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()
txt = open(RUN, encoding='utf-8').read()
bad = 0
for e in re.findall(r'\[E\d+-\d+\]', txt):
    print('E-id found:', e); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', txt)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# quoted fragment followed (within 6 chars) by **[ID]**, possibly several ids
for m in re.finditer(r'"([^"]{3,600})"\s*(?:\([^)]{0,80}\)\s*)?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,; ]*)+)', txt):
    frag = m.group(1); idl = re.findall(r'[MLR]\d{4}-\d{3}', m.group(2))
    parts = [p for p in re.split(r'\[\.\.\.\]', frag) if p.strip()]
    ok = any(all(norm(p).strip(' .,;:') in norm(rows.get(i, '')) for p in parts) for i in idl)
    if not ok:
        print('NOT IN ROW', idl, '::', frag[:120]); bad += 1
print('ids:', len(set(ids)), 'problems:', bad)
sys.exit(1 if bad else 0)
