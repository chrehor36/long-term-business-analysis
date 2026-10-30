# check a run file: no E-ids; every M/L/R id in the v5 ledger; every quoted fragment adjacent to an id is in that row.
# usage: python check_ids.py <run file>
import csv, re, sys, unicodedata
rows = {r['﻿id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8'))}
text = open(sys.argv[1], encoding='utf-8').read()
norm = lambda s: re.sub(r'\s+', ' ', unicodedata.normalize('NFC', s)).strip()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', text)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', text)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# fragments: a "..." quotation followed (within 12 chars) by **[ID]**, possibly several ids
nfrag = 0
for m in re.finditer(r'"([^"]{3,400}?)"[^"\n]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text):
    frag, i = m.group(1), m.group(2)
    nfrag += 1
    parts = [p.strip(' .,;:') for p in frag.split('...')] if '...' in frag else [frag]
    for p in parts:
        p2 = p.replace('[...]', '').strip()
        if p2 and norm(p2) not in norm(rows.get(i, '')):
            print(f'FRAGMENT NOT IN {i}: {p2!r}'); bad += 1
print(f'{len(set(ids))} ids, {nfrag} fragments checked, {bad} problems')
