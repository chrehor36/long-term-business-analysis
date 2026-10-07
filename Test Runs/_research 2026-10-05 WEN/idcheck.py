import csv,re,sys
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open('Test Runs/2026-10-05 Run - WEN Wendys.md',encoding='utf-8').read()
ids=re.findall(r'\[([A-Z]+\d{4}-\d{3}|E\d+-\d+)\]',t)
bad=[i for i in ids if i not in rows]; print('ids cited',len(ids),'distinct',len(set(ids)),'missing',bad)
print('E-ids',re.findall(r'\[E\d+-\d+\]',t))
# quoted fragments immediately followed (within 12 chars, optional punctuation) by an id
flat=re.sub(r'\s*\n\s*',' ',t)
n=0;fails=0
for m in re.finditer(r'"([^"]{3,400}?)"\s*\.?\s*(?:\*\*)?\s*\[([A-Z]\d{4}-\d{3})\]',flat):
    frag,i=m.group(1),m.group(2); n+=1
    q=rows.get(i,'')
    parts=[p.strip(' .') for p in frag.split('...')]
    ok=all(p in q for p in parts if p)
    if not ok: fails+=1; print('FAIL',i,'|',frag[:120])
print('quoted fragments beside ids',n,'fails',fails)
# also ids preceded by a quote in the form "...", **[ID]**  (comma)
for m in re.finditer(r'"([^"]{3,400}?)"[,;:]?\s*\*\*\[([A-Z]\d{4}-\d{3})\]',flat):
    frag,i=m.group(1),m.group(2)
    if not all(p.strip(' .') in rows.get(i,'') for p in frag.split('...') if p.strip(' .')): print('FAIL2',i,frag[:100])
# em dashes outside quotes
nq=re.sub(r'"[^"]*"','',flat)
print('em dashes outside quotes:',nq.count('—'),' total em dashes:',t.count('—'))
