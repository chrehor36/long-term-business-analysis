# check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment set
# directly before an id (optionally with a parenthesis between) is in that row's quote (pieces split on [...]).
# Quotes are paired in order within each paragraph, so a closing mark is never read as an opening one.
import csv, re, sys
RUN = r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-10 Run - OTIS Otis Worldwide.md'
LEDGER = r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv'
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(LEDGER, encoding='utf-8-sig'))}
txt = open(RUN, encoding='utf-8').read()


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


bad = 0
eids = re.findall(r'\[E\d+-\d+\]', txt)
if eids:
    print('E-ids found:', eids)
    bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', txt)
for i in sorted(set(ids)):
    if i not in rows:
        print('MISSING id', i)
        bad += 1
n = 0
ID_RUN = re.compile(r'\s*(?:\([^)]{0,200}\)\s*)?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,;\s]*)+)')
for para in re.split(r'\n\s*\n', txt):
    qpos = [k for k, ch in enumerate(para) if ch == '"']
    if len(qpos) % 2:
        print('ODD quote count in paragraph:', norm(para[:90]))
        bad += 1
    for a, b in zip(qpos[0::2], qpos[1::2]):
        frag = para[a + 1:b]
        mm = ID_RUN.match(para[b + 1:b + 300])
        if not mm:
            continue
        cited = re.findall(r'[MLR]\d{4}-\d{3}', mm.group(1))
        pieces = [norm(p) for p in re.split(r'\[\.\.\.\]', frag) if norm(p)]
        ok = any(all(p in norm(rows.get(c, '')) for p in pieces) for c in cited)
        n += 1
        if not ok:
            print('NOT IN ROW', cited, '::', frag[:150])
            bad += 1
print(f'ids {len(set(ids))}, quoted fragments checked {n}, problems {bad}')
sys.exit(1 if bad else 0)
