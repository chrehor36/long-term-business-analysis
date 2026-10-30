"""Check the run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment adjacent to an id is in that row."""
import csv,re,sys
sys.stdout.reconfigure(encoding='utf-8')
run=open(sys.argv[1],encoding='utf-8').read()
R={r['﻿id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8'))}
norm=lambda s:re.sub(r'\s+',' ',s.replace('“','"').replace('”','"').replace('‘',"'").replace('’',"'")).strip().lower()
eids=re.findall(r'\[E\d-\d+\]',run); print('E-ids:',eids or 'none')
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run)
missing=[i for i in set(ids) if i not in R]; print(f'ids cited: {len(ids)} occurrences, {len(set(ids))} distinct; missing: {missing or "none"}')
bad=0; checked=0
# quotes immediately followed by one or more ids
for m in re.finditer(r'"((?:[^"\n]|\n(?!\n))+?)"[\s,.;:]*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[\s,]*)+)',run):
    q=m.group(1); idl=re.findall(r'[MLR]\d{4}-\d{3}',m.group(2))
    frags=[f for f in re.split(r'\[\.\.\.\]',q) if len(norm(f))>3]
    for i in idl:
        row=norm(R.get(i,''))
        for f in frags:
            checked+=1
            if norm(f).strip(' .,;') not in row:
                bad+=1; print(f'NOT IN ROW {i}: "{f[:120]}"')
# ids followed by : "quote"
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*:\s*"((?:[^"\n]|\n(?!\n))+?)"',run):
    i=m.group(1); row=norm(R.get(i,''))
    for f in [f for f in re.split(r'\[\.\.\.\]',m.group(2)) if len(norm(f))>3]:
        checked+=1
        if norm(f).strip(' .,;') not in row: bad+=1; print(f'NOT IN ROW {i}: "{f[:120]}"')
print(f'fragments checked: {checked}; not found: {bad}')
