# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment adjacent to an id (same sentence/line, before the id) appears in that row.
import csv, re, sys, unicodedata
RUN = "Test Runs/2026-10-18 Run - AES The AES Corporation.md"
rows = {r['﻿id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8'))}
s = open(RUN, encoding='utf-8').read()
def norm(t):
    t = unicodedata.normalize('NFKC', t)
    for a, b in [('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('—', '-'), ('–', '-'), ('�', '')]:
        t = t.replace(a, b)
    return re.sub(r'\s+', ' ', t).strip().lower()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', s)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\*\*\[((?:M|L|R)\d{4}-\d{3})\]\*\*', s)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# quoted fragments immediately preceding an id: take text since previous id or line start in the same paragraph
flat = s.replace('\n', ' ')
for m in re.finditer(r'\*\*\[((?:M|L|R)\d{4}-\d{3})\]\*\*', flat):
    i = m.group(1)
    start = max(flat.rfind(']**', 0, m.start()), flat.rfind('. ', 0, m.start() - 2) if False else -1)
    seg = flat[max(0, start):m.start()]
    # the quote(s) closest to the id: the last quoted string in the segment
    qs = re.findall(r'"([^"]{6,})"', seg)
    if not qs: continue
    q = qs[-1]
    # skip quotes that are clearly filing quotes followed by a source parenthesis before the id
    tail = seg[seg.rfind('"'):]
    if re.search(r'\((?:DEFM14A|10-K|10-Q|8-K|DEF 14A)', tail): continue
    row = norm(rows.get(i, ''))
    parts = [p for p in re.split(r'\[\.\.\.\]', q) if p.strip()]
    for p in parts:
        if norm(p) not in row:
            print(f'FRAGMENT NOT IN {i}: "{p[:90]}"'); bad += 1
print('ids checked:', len(set(ids)), '| problems:', bad)
sys.exit(1 if bad else 0)
