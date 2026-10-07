import csv,re,sys
sys.stdout.reconfigure(encoding='utf-8')
run=open('Test Runs/2026-10-06 Run - NSIT Insight Enterprises.md',encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
norm=lambda s:re.sub(r'\s+',' ',s).strip()
bad=0
print('E-ids:',re.findall(r'\[E\d-\d+\]',run))
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run)
missing=[i for i in ids if i not in rows]; print('ids cited',len(ids),'distinct',len(set(ids)),'missing',missing)
flat=re.sub(r'\n\s*',' ',run)
# every "quote" immediately (<=3 chars) before a **[ID]**
for m in re.finditer(r'"([^"]{3,600})"\s*[,.;:]?\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*',flat):
    q,i=m.group(1),m.group(2)
    row=norm(rows.get(i,''))
    for piece in q.split('[...]'):
        p=norm(piece).strip(' ,.;:')
        if p and p not in row:
            bad+=1; print('NOT IN ROW',i,'::',p[:120])
print('em dashes outside quotes check: total em dashes',run.count('—'))
print('BAD',bad)
