import csv,re,sys
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open('Test Runs/2026-10-06 Run - CVSA Covista.md',encoding='utf-8').read()
E=re.findall(r'\bE[1-5]-\d{2}\b',t); print('E-ids:',E)
ids=re.findall(r'\b[MLR](?:19|20)\d{2}-\d{3}\b',t)
missing=[i for i in set(ids) if i not in rows]; print('ids cited:',len(set(ids)),'missing:',missing)
norm=lambda s: re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip()
# every "quote" followed (within 12 chars) by **[ID]** possibly several ids
bad=0;n=0
for m in re.finditer(r'"([^"]{6,}?)"\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[ ,;and]*)+)',t):
    q=m.group(1); idl=re.findall(r'[MLR]\d{4}-\d{3}',m.group(2))
    frags=[f.strip(' .,;') for f in q.split('[...]') if f.strip(' .,;')]
    for i in idl:
        src=norm(rows.get(i,''))
        for f in frags:
            n+=1
            if norm(f) not in src:
                bad+=1; print('NOT IN ROW',i,'|',f[:120])
print('fragments checked',n,'bad',bad)
# also quotes using curly double quotes
for m in re.finditer(r'“([^”]{6,}?)”\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t):
    print('curly',m.group(2),m.group(1)[:60])
# id before the quote: **[ID]**: "quote"  or **[ID]** ("quote")
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*[:(]?\s*\(?"([^"]{6,}?)"',t):
    i=m.group(1); src=norm(rows[i])
    for f in [x.strip(' .,;') for x in m.group(2).split('[...]') if x.strip(' .,;')]:
        print('pre-id',i,'OK' if norm(f) in src else 'NOT IN ROW','|',f[:80])
