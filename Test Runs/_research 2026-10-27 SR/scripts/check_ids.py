# Checks the run file: no E-ids; every M/L/R id is in principle_ledger_v5.csv; every quoted fragment
# that sits in the same sentence-chunk as an id (the quote immediately before the id) is in that row.
import csv,re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
rows={x['﻿id']:x['quote_verbatim'] for x in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8'))}
t=open(sys.argv[1],encoding='utf-8').read()
bad=0
if re.search(r'\[E\d-\d+\]',t): print('E-id found'); bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',t)
for i in set(ids):
    if i not in rows: print('MISSING id',i); bad+=1
# pair each id-group with the quoted fragments right before it (same line, after the previous id)
nfrag=0
for line in t.splitlines():
    pos=0
    for m in re.finditer(r'(\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*\*\*\[[MLR]\d{4}-\d{3}\]\*\*)*)',line):
        seg=line[pos:m.start()]; grp=re.findall(r'[MLR]\d{4}-\d{3}',m.group(1)); pos=m.end()
        fm=list(re.finditer(r'"([^"]{3,})"',seg))
        if not fm: continue
        gap=seg[fm[-1].end():]
        if len(gap)>45: continue   # a quote counts as beside the id only when it closes within 45 characters before it
        frag=fm[-1].group(1)
        parts=[p.strip(' .,;') for p in frag.split('[...]') if p.strip(' .,;')]
        ok=any(all(p.replace('**','') in rows.get(g,'') for p in parts) for g in grp)
        nfrag+=1
        if not ok: print('FRAGMENT NOT IN ROW',grp,'::',frag[:120]); bad+=1
print(f'{len(set(ids))} distinct ids, {nfrag} fragments checked, {bad} problems')
sys.exit(1 if bad else 0)
