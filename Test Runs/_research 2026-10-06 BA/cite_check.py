"""Check the BA run file's v5 citations: every id exists; every quoted fragment immediately before an id is found in
that id's row (split on [...]; quotes and apostrophes normalised). Usage: python -I cite_check.py"""
import csv, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
RUN = os.path.join(ROOT, 'Test Runs', '2026-10-06 Run - BA Boeing.md')
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(os.path.join(ROOT, 'principle_ledger_v5.csv'), encoding='utf-8-sig'))}


def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip().lower()


text = open(RUN, encoding='utf-8').read()
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', text)
bad_ids = sorted({i for i in ids if i not in rows})
eids = re.findall(r'\[(E\d+-\d+)\]', text)
problems = 0
# fragment = the last double-quoted string before the id, within 400 chars, on the same paragraph
for m in re.finditer(r'"([^"]{3,600})"\s*(?:\*\*)?\s*\[([MLR]\d{4}-\d{3})\]', text):
    frag, i = m.group(1), m.group(2)
    if i not in rows:
        continue
    row = norm(rows[i])
    for part in frag.split('[...]'):
        p = norm(part).strip(' .,;:')
        if p and p not in row:
            problems += 1
            print('NOT FOUND', i, '|', part[:120])
print(f'distinct ids {len(set(ids))}; missing {bad_ids}; E-ids {eids}; fragment problems {problems}')
