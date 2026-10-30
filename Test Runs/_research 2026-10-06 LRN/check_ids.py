import csv,re,sys
p=r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-06 Run - LRN Stride.md'
rows={}
with open(r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv',encoding='utf-8-sig') as f:
    for r in csv.DictReader(f): rows[r['id']]=r['quote_verbatim']
t=open(p,encoding='utf-8').read()
norm=lambda s: re.sub(r'\s+',' ',s).strip()
# 1. E-ids or v4 ids
e=re.findall(r'\[(E\d+-\d+)\]',t); print('E/v4 ids:',e)
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t)
allids=re.findall(r'\[([A-Z]\d{1,4}-\d{2,3})\]',t)
missing=[i for i in set(allids) if i not in rows]; print('ids:',len(set(ids)),'missing:',missing)
# 2. quoted fragments beside ids: for each id, take text since previous id (same paragraph) and check quotes
flat=norm(t)
pos=0; bad=0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',flat):
    seg=flat[pos:m.start()]; pos=m.end()
    # restrict to the current sentence chunk: after last '. ' that is outside quotes is hard; use last 400 chars
    seg=seg[-500:]
    quotes=re.findall(r'"([^"]{3,})"',seg)
    if not quotes: continue
    q=quotes[-1]  # the quote nearest the id
    src=norm(rows[m.group(1)])
    parts=[norm(x) for x in re.split(r'\[\.\.\.\]',q) if norm(x)]
    for part in parts:
        if part not in src:
            bad+=1; print('NOT IN ROW',m.group(1),'|',part[:120])
print('quote problems:',bad)
print('em dashes outside quotes check:')
for i,line in enumerate(t.split('\n'),1):
    if '—' in line:
        stripped=re.sub(r'"[^"]*"','',line)
        if '—' in stripped: print(i,line[:140])
