"""Check the AEP run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
in the same bullet/sentence as an id is found in at least one cited row of that sentence. python -I check_ids.py"""
import csv, re, os, sys
sys.stdout.reconfigure(encoding='utf-8')
here=os.path.dirname(os.path.abspath(__file__))
root=os.path.join(here,'..','..')
run=open(os.path.join(here,'..','2026-10-18 Run - AEP American Electric Power.md'),encoding='utf-8').read()
rows={r['﻿id']:r['quote_verbatim'] for r in csv.DictReader(open(os.path.join(root,'principle_ledger_v5.csv'),encoding='utf-8'))}
norm=lambda t:re.sub(r'\s+',' ',t.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip().lower()
bad=0
if re.search(r'\[E\d-\d+\]',run): print('E-id found'); bad+=1
ids=set(re.findall(r'\[([MLR]\d{4}-\d{3})\]',run))
for i in sorted(ids):
    if i not in rows: print('MISSING',i); bad+=1
# split into sentences-ish units: lines, then by '; ' boundaries kept together
for line in run.split('\n'):
    cited=re.findall(r'\[([MLR]\d{4}-\d{3})\]',line)
    if not cited: continue
    # take each quote and the ids that follow it within the same clause
    for m in re.finditer(r'"([^"]{12,}?)"\s*(?:[^"\[]{0,40}?)\*\*\[([MLR]\d{4}-\d{3})\]',line):
        frag,i=m.group(1),m.group(2)
        parts=[p for p in re.split(r'\[\.\.\.\]',frag) if p.strip()]
        ok=all(norm(p).strip(' .,;') in norm(rows.get(i,'')) for p in parts)
        if not ok: print('NOT IN ROW',i,'|',frag[:120]); bad+=1
print('ids cited:',len(ids),'problems:',bad)
