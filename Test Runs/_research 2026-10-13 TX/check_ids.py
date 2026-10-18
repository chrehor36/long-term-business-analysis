# TX run citation check: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment directly before an id
# (or before a run of ids) is in one of those rows, elisions [...] split, quotes normalised only to report near-misses.
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2], encoding='utf-8-sig'))}
bad = 0
e_ids = re.findall(r'\[E\d+-\d+\]', run)
print('E-ids:', e_ids or 'none'); bad += len(e_ids)
ids = sorted(set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)))
missing = [i for i in ids if i not in rows]
print('ids cited:', len(ids), 'missing:', missing or 'none'); bad += len(missing)
norm = lambda s: s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('—', '-')
# a quoted fragment followed by one or more bold ids
pat = re.compile(r'"([^"\n]{3,}?(?:\n[^"\n]*?)*?)"[ ,.;:)]*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:, )?)+)')
n = 0
for m in pat.finditer(run):
    frag = ' '.join(m.group(1).split())
    cited = re.findall(r'\[([MLR]\d{4}-\d{3})\]', m.group(2))
    pieces = [p.strip(' .,;:') for p in frag.split('[...]') if p.strip(' .,;:')]
    ok_exact = any(all(p in ' '.join(rows.get(c, '').split()) for p in pieces) for c in cited)
    ok_norm = any(all(norm(p) in norm(' '.join(rows.get(c, '').split())) for p in pieces) for c in cited)
    n += 1
    if not ok_exact:
        print(('NEAR-MISS (quote marks only) ' if ok_norm else 'NOT FOUND ') + str(cited) + ': ' + frag[:160])
        if not ok_norm: bad += 1
print('fragments checked:', n, ' failures:', bad)
