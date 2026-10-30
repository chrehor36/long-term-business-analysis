# Checks the run file: no E-ids; every M/L/R id in the v5 ledger; every quoted fragment adjacent to an id is in that row.
import csv,re,sys,os
base=os.path.dirname(os.path.abspath(__file__))
run=os.path.join(base,'..','2026-10-12 Run - GIC Global Industrial.md')
led=os.path.join(base,'..','..','principle_ledger_v5.csv')
rows={r['﻿id']:r['quote_verbatim'] for r in csv.DictReader(open(led,encoding='utf-8'))}
t=open(run,encoding='utf-8').read()
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('�',"'")
    return re.sub(r'\s+',' ',s).strip().lower()
prob=0
eids=re.findall(r'\[E\d-\d+\]',t)
if eids: print('E-ids found',eids); prob+=1
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t)
allids=set(re.findall(r'\[([MLR]\d{4}-\d{3})\]',t))
for i in sorted(allids):
    if i not in rows: print('MISSING',i); prob+=1
print('distinct ids',len(allids))
# fragments: a quoted string ending within 40 chars before an id cite
n=0
for m in re.finditer(r'"([^"]{6,400})"[^"\[]{0,40}\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t):
    frag,i=m.group(1),m.group(2)
    n+=1
    if i not in rows: continue
    parts=[p for p in re.split(r'\s*(?:\[\.\.\.\]|\.\.\.)\s*',frag) if p.strip()]
    for p in parts:
        if norm(p) not in norm(rows[i]):
            print('FRAGMENT NOT IN ROW',i,'|',p[:120]); prob+=1
print('fragments checked',n,'problems',prob)
