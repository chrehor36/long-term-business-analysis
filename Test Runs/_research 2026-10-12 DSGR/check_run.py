# Citation check for the DSGR run of 2026-10-12.
# (1) no E-ids; (2) every M/L/R id exists in principle_ledger_v5.csv; (3) every quoted fragment that sits beside an id
# (in the same sentence or the same line, before the id) is in that row's quote, after splitting on [...].
import csv, re, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
RUN = os.path.join(ROOT, 'Test Runs', '2026-10-12 Run - DSGR Distribution Solutions Group.md')
rows = {}
for x in csv.DictReader(open(os.path.join(ROOT, 'principle_ledger_v5.csv'), encoding='utf-8')):
    rows[x.get('﻿id') or x.get('id')] = x['quote_verbatim']
t = open(RUN, encoding='utf-8').read()
probs = []
e_ids = re.findall(r'\[E\d+-\d+\]', t)
if e_ids: probs.append('E-ids present: %s' % e_ids)
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', t)
for i in sorted(set(ids)):
    if i not in rows: probs.append('missing id %s' % i)
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip()
exact_ok = norm_ok = 0
# a fragment is a "..." span; it is checked against the first id that follows it within the same paragraph
paras = re.split(r'\n\s*\n', t)
checked = 0
for p in paras:
    flat = re.sub(r'\s+', ' ', p)
    for m in re.finditer(r'"([^"]{6,}?)"', flat):
        frag = m.group(1)
        after = flat[m.end():m.end() + 160]
        idm = re.search(r'\[([MLR]\d{4}-\d{3})\]', after)
        if not idm: continue
        between = after[:idm.start()]
        if '"' in between: continue  # another quote sits closer to the id
        rid = idm.group(1)
        q = rows.get(rid, '')
        checked += 1
        pieces = [x.strip(' .,;:') for x in frag.split('[...]') if x.strip(' .,;:')]
        for piece in pieces:
            if piece in q: exact_ok += 1
            elif norm(piece) in norm(q): norm_ok += 1; probs.append('typographic only (%s): "%s"' % (rid, piece[:70]))
            else: probs.append('NOT IN ROW %s: "%s"' % (rid, piece[:90]))
print('ids cited: %d distinct, %d uses; fragments checked beside an id: %d; pieces exact %d, typographic-only %d' % (
    len(set(ids)), len(ids), checked, exact_ok, norm_ok))
print('\n'.join(probs) if probs else 'no problems')
