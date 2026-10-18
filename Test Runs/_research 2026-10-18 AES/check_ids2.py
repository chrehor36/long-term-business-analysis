# Second pass: every quoted fragment in a paragraph that contains a v5 id is checked against the ids of that paragraph.
# A fragment passes if it is in any id row of its paragraph; failures are printed for manual review (filing quotes expected).
import csv, re, unicodedata
RUN = "Test Runs/2026-10-18 Run - AES The AES Corporation.md"
rows = {r['﻿id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8'))}
def norm(t):
    t = unicodedata.normalize('NFKC', t)
    for a, b in [('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('—', '-'), ('–', '-'), ('�', '')]:
        t = t.replace(a, b)
    return re.sub(r'\s+', ' ', t).strip().lower()
s = open(RUN, encoding='utf-8').read()
paras = re.split(r'\n\s*\n|\n(?=- )|\n(?=  - )', s)
for p in paras:
    ids = re.findall(r'\[((?:M|L|R)\d{4}-\d{3})\]', p)
    if not ids: continue
    for q in re.findall(r'"([^"]{6,})"', p.replace('\n', ' ')):
        frags = [f for f in re.split(r'\[\.\.\.\]', q) if f.strip()]
        ok = all(any(norm(f) in norm(rows[i]) for i in ids if i in rows) for f in frags)
        if not ok:
            print(f'NOT IN ANY ROW OF ITS PARAGRAPH {ids}: "{q[:110]}"')
