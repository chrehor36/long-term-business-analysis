"""Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that sits
directly before an id (within 60 characters, nothing but punctuation, words like 'and' or another id between) is found
in that id's row (or one of the ids in the same group). Elisions [...] split a fragment into parts, each checked."""
import csv, re, sys, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RUN = os.path.join(ROOT, 'Test Runs', '2026-10-13 Run - CYH Community Health Systems.md')
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(os.path.join(ROOT, 'principle_ledger_v5.csv'), encoding='utf-8-sig'))}
text = open(RUN, encoding='utf-8').read()

def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('�', "'")
    return re.sub(r'\s+', ' ', s).strip().lower()

bad = 0
eids = re.findall(r'\[E\d+-\d+\]', text)
if eids:
    print('E-ids found:', eids); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', text)
missing = sorted(set(i for i in ids if i not in rows))
print(f'{len(ids)} id citations, {len(set(ids))} distinct; missing: {missing}')
bad += len(missing)

# quoted fragments directly before an id group
pat = re.compile(r'"([^"]{3,}?)"([^"\[\n]{0,60}?)((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,; ]*(?:and )?)+)')
checked = 0
for m in pat.finditer(text.replace('\r\n', '\n').replace('\n', ' ')):
    frag, gap, grp = m.group(1), m.group(2), m.group(3)
    if re.search(r'\b(Item|10-K|10-Q|proxy|Note)\b', gap):
        continue  # a filing quote with its source, not a row quote
    gids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', grp)
    parts = [p.strip(' .,;') for p in frag.split('[...]') if p.strip(' .,;')]
    for p in parts:
        checked += 1
        if not any(norm(p) in norm(rows.get(g, '')) for g in gids):
            print('NOT IN ROW', gids, '|', p[:120]); bad += 1
print(f'{checked} fragments checked')
print('PASS' if bad == 0 else f'FAIL ({bad})')
sys.exit(1 if bad else 0)
