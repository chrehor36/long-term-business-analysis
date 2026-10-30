# Citation check for the CWCO run: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment
# that sits between the previous id (or paragraph start) and an id is looked for in that id's row (or the group's rows).
# Fragments not found are printed for a manual read (filing quotes beside an id are expected to show here).
import csv, re, sys
run = sys.argv[1]
rows = {x['id']: x['quote_verbatim'] for x in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
def norm(s):
    s = s.replace('�', "'")
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('—', '-'), ('–', '-')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()
txt = open(run, encoding='utf-8').read()
bad = re.findall(r'\[E\d', txt)
print('E-ids:', len(bad))
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', txt)
missing = sorted(set(i for i in ids if i not in rows))
print('ids cited:', len(ids), 'distinct:', len(set(ids)), 'missing:', missing)
paras = txt.split('\n\n')
problems = 0
for p in paras:
    p1 = p.replace('\n', ' ')
    # split into segments ending at an id cluster
    for m in re.finditer(r'(.*?)((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)', p1):
        seg, idgrp = m.group(1), m.group(2)
        gids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', idgrp)
        # only the last sentence-ish chunk of the segment
        quotes = re.findall(r'"([^"]{4,})"', seg.replace('“', '"').replace('”', '"'))
        for q in quotes[-2:]:
            parts = [x for x in re.split(r'\s*\[\.\.\.\]\s*', q) if x.strip()]
            ok = all(any(norm(pt.strip(' .,;:')) in norm(rows.get(g, '')) for g in gids) for pt in parts)
            if not ok:
                problems += 1
                print('NOT IN ROW', gids, '::', q[:160])
print('fragments not found:', problems)
