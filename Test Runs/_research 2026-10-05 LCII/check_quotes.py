import csv,re,sys
RUN=r"Test Runs/2026-10-05 Run - LCII LCI Industries.md"
txt=open(RUN,encoding='utf-8').read()
rows={}
with open('principle_ledger_v5.csv',encoding='utf-8-sig') as f:
    for r in csv.DictReader(f): rows[r['id']]=r['quote_verbatim']
eids=re.findall(r'\[E\d+-\d+\]',txt); print('E-ids:',eids)
ids=set(re.findall(r'\[([MLR]\d{4}-\d{3})\]',txt)); bad=[i for i in ids if i not in rows]
print('ids cited:',len(ids),'missing:',bad)
print('em dashes in file:',txt.count('—'))
norm=lambda s: re.sub(r'\s+',' ',s)
fails=0; checked=0
# each (**[ID]**: "quote") or **[ID]** ("quote") pattern, and "quote" (**[ID]**) pattern
for m in re.finditer(r'\[([MLR]\d{4}-\d{3})\]\*\*\)?\s*[:(]?\s*((?:"[^"]+"(?:;\s*|\s*and\s*|,\s*)?)+)',txt):
    i=m.group(1)
    for q in re.findall(r'"([^"]+)"',m.group(2)):
        checked+=1
        if norm(q) not in norm(rows.get(i,'')): fails+=1; print('FAIL after',i,':',q)
for m in re.finditer(r'"([^"]+)"\s*\(\*\*\[([MLR]\d{4}-\d{3})\]\*\*\)',txt):
    q,i=m.group(1),m.group(2); checked+=1
    if norm(q) not in norm(rows.get(i,'')): fails+=1; print('FAIL before',i,':',q)
print('fragments checked',checked,'fails',fails)
# list every id occurrence with its following 160 chars for manual review
for m in re.finditer(r'\[([MLR]\d{4}-\d{3})\]',txt):
    pass
