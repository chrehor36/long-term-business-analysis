# check: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment beside an id is in that row
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
L = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('../../principle_ledger_v5.csv', encoding='utf-8-sig'))}
t = open('../2026-10-12 Run - EVI EVI Industries.md', encoding='utf-8').read()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', t)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', t)
for i in sorted(set(ids)):
    if i not in L: print('MISSING id', i); bad += 1
def norm(s): return re.sub(r'\s+', ' ', s.replace('�', '').replace('—', '').replace('–','')).strip()
# fragments: a "..." quote followed within 120 chars by an id; check each id cited right after
nfrag = 0
for m in re.finditer(r'"([^"]{6,600})"', t):
    after = t[m.end():m.end()+160]
    m2 = re.search(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', after)
    if not m2: continue
    # only if no other quote intervenes
    if '"' in after[:m2.start()]: continue
    i = m2.group(1); frag = m.group(1)
    parts = [p.strip(' ,.;:') for p in re.split(r'\[\.\.\.\]', frag)]
    nfrag += 1
    for p in parts:
        if p and norm(p) not in norm(L.get(i, '')):
            print(f'FRAGMENT NOT IN {i}: {p[:120]}'); bad += 1
print(f'{len(set(ids))} ids, {nfrag} fragments checked, {bad} problems')
