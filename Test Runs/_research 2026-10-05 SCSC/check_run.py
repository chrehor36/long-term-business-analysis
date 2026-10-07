import csv,re,sys
RUN='Test Runs/2026-10-05 Run - SCSC ScanSource.md'
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open(RUN,encoding="utf-8").read()
W=lambda s: re.sub(r"\s+"," ",s).strip()
ids=re.findall(r'\[([A-Z]\d{4}-\d{3}|E\d+-\d+)\]',t)
bad=[i for i in ids if i not in rows]
eids=[i for i in ids if i.startswith('E')]
print('ids cited',len(ids),'distinct',len(set(ids)),'missing',bad,'E-ids',eids)
# quoted fragment immediately before an id (same sentence region): "..." **[ID]** or "..." ([...]) **[ID]**
fails=0;checked=0
for m in re.finditer(r'"([^"]{6,400})"[^"\n]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t):
    frag,i=m.group(1),m.group(2)
    q=rows.get(i,'')
    parts=[p.strip(' .,') for p in frag.split('[...]')]
    ok=all(W(p) in W(q) for p in parts if p)
    checked+=1
    if not ok:
        fails+=1; print('NOT IN ROW',i,'|',frag[:120])
# fragments in parentheses after id: **[ID]** ("...")
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*\s*\("([^"]{6,300})"\)',t):
    i,frag=m.group(1),m.group(2); q=rows.get(i,''); checked+=1
    if not all(W(p.strip(' .,')) in W(q) for p in frag.split('[...]') if p.strip()):
        fails+=1; print('NOT IN ROW (paren)',i,'|',frag[:120])
print('fragments checked',checked,'fails',fails)
# em dashes outside quotes
for n,line in enumerate(t.split('\n'),1):
    if '—' in line:
        stripped=re.sub(r'"[^"]*"','',line)
        if '—' in stripped: print('EM DASH outside quote line',n,':',line[:120])
