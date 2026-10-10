# Checks for the COKE run file: (1) no E-ids; (2) every M/L/R id exists in principle_ledger_v5.csv;
# (3) every quoted fragment that is followed by an id within the same sentence is found in that row
#     (apostrophes and the transcripts' replacement character treated as equal; [...] splits a quote into parts).
import csv, re, os, sys
here = os.path.dirname(os.path.abspath(__file__))
run = os.path.join(here, '..', '2026-10-07 Run - COKE Coca-Cola Consolidated.md')
led = os.path.join(here, '..', '..', 'principle_ledger_v5.csv')
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(led, encoding='utf-8-sig'))}
t = open(run, encoding='utf-8').read()
def norm(x):
    x = x.replace('�', "'").replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    x = x.replace('—', '-').replace('–', '-')
    return re.sub(r'\s+', ' ', x).strip().lower()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', t)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', t)
missing = sorted(set(i for i in ids if i not in rows))
if missing: print('ids missing from ledger:', missing); bad += 1
print('ids cited:', len(ids), 'distinct:', len(set(ids)))
# quoted fragment followed (within 220 chars, no intervening quote) by one or more ids
for m in re.finditer(r'"([^"\n]{3,600}?)"', t.replace('\n', ' ')):
    frag = m.group(1); tail = t.replace('\n', ' ')[m.end(): m.end() + 220]
    nxt = tail.find('"')
    seg = tail if nxt < 0 else tail[:nxt]
    seg = re.split(r'\.\s|\s-\s\*\*', seg)[0]   # same sentence only
    near = re.findall(r'\[([MLR]\d{4}-\d{3})\]', seg)
    if not near: continue
    first = near[0]
    # the fragment must be in the first id that follows it (or any id in the same group)
    parts = [p.strip(' .,;:') for p in frag.split('[...]') if p.strip(' .,;:')]
    ok = any(all(norm(p) in norm(rows.get(i, '')) for p in parts) for i in near)
    if not ok:
        print('NOT IN ROW', near, '|', frag[:120]); bad += 1
print('RESULT:', 'PASS' if not bad else 'FAIL (%d)' % bad)
