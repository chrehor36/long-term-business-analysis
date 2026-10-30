# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment ("...") immediately followed by **[id]** is in that row (elisions [...] split the fragment).
import csv, re, sys, unicodedata
run, ledger = sys.argv[1], sys.argv[2]
rows = {r['﻿id'] if '﻿id' in r else r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ledger, encoding='utf-8-sig'))}
t = open(run, encoding='utf-8').read()
def norm(s):
    s = unicodedata.normalize('NFKC', s).replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('**', '')
    return ' '.join(s.split()).lower()
bad = 0
for e in re.findall(r'\[(E\d-\d+)\]', t): print('E-ID FOUND', e); bad += 1
ids = re.findall(r'\[((?:M|L|R)\d{4}-\d{3})\]', t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING ID', i); bad += 1
# quote then (optional punctuation/space) then **[ID]**
for m in re.finditer(r'"([^"]{6,600})"[\s.,;:)]*\*\*\[((?:M|L|R)\d{4}-\d{3})\]\*\*', t):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    row = norm(rows[i])
    for part in frag.split('[...]'):
        p = norm(part).strip(' .,;:')
        if p and p not in row:
            print('FRAGMENT NOT IN ROW', i, '|', part[:90]); bad += 1
print('ids checked:', len(set(ids)), 'problems:', bad)
sys.exit(1 if bad else 0)
