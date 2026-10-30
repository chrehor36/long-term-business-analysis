# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# immediately before an id (on the same line, after the previous id) is in that row's quote.
import csv, re, sys, unicodedata
RUN = sys.argv[1]
rows = {x['﻿id']: x['quote_verbatim'] for x in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8'))}
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('�', '')
    return re.sub(r'\s+', ' ', s).strip().lower()
txt = open(RUN, encoding='utf-8').read()
bad = 0
if re.search(r'\[E\d', txt): print('E-id found'); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', txt)
for i in set(ids):
    if i not in rows: print('MISSING', i); bad += 1
# quoted fragments: for each id occurrence, the text between the previous id (or line start) and this id
for line in txt.splitlines():
    pos = 0
    for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', line):
        seg = line[pos:m.start()]; pos = m.end()
        frs = re.findall(r'"([^"]{8,})"', seg)
        if not frs: continue
        fr = frs[-1]
        q = norm(rows.get(m.group(1), ''))
        parts = [p.strip(' .,;:') for p in re.split(r'\[\.\.\.\]', fr)]
        for p in parts:
            if p and norm(p) not in q:
                print(f'FRAGMENT NOT IN {m.group(1)}: "{p[:120]}"'); bad += 1
for line in txt.splitlines():
    ms = list(re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', line))
    for k, m in enumerate(ms):
        end = ms[k+1].start() if k+1 < len(ms) else len(line)
        seg = line[m.end():end]
        mm = re.match(r'\s*[:,]\s*"([^"]{8,})"', seg)
        if not mm: continue
        q = norm(rows.get(m.group(1), ''))
        for part in re.split(r'\[\.\.\.\]', mm.group(1)):
            part = part.strip(' .,;:')
            if part and norm(part) not in q:
                print(f'FOLLOWING FRAGMENT NOT IN {m.group(1)}: "{part[:120]}"'); bad += 1
print(f'{len(set(ids))} distinct ids, {len(ids)} citations; problems: {bad}')
sys.exit(1 if bad else 0)
