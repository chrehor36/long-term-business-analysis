import csv,re,sys
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('../../principle_ledger_v5.csv',encoding='utf-8-sig'))}
s=open('../2026-10-05 Run - ADNT Adient.md',encoding='utf-8').read()
bad=0
e=re.findall(r'\[E\d+-\d+\]',s); print('E-ids:',e); bad+=len(e)
ids=set(re.findall(r'\[([MLR]\d{4}-\d{3})\]',s))
for i in sorted(ids):
    if i not in rows: print('MISSING',i); bad+=1
# quoted fragment immediately before an id (within same paragraph): "..." **[ID]** or "..." [ID]
norm=lambda t: re.sub(r'\s+',' ',t)
for m in re.finditer(r'"([^"]{6,600})"\s*\)?\s*(?:\*\*)?\[([MLR]\d{4}-\d{3})\]',s):
    frag,i=norm(m.group(1)),m.group(2)
    row=norm(rows.get(i,''))
    for piece in [p.strip() for p in frag.split('[...]') if p.strip()]:
        if piece not in row:
            print('NOT IN ROW',i,'|',piece[:120]); bad+=1
print('ids cited:',len(ids),'problems:',bad)
# reverse: id then ": "quote"" or id followed by ("quote")
for m in re.finditer(r'\[([MLR]\d{4}-\d{3})\]\*?\*?\s*\(?:?\s*"([^"]{6,600})"',s):
    i,frag=m.group(1),norm(m.group(2)); row=norm(rows.get(i,''))
    for piece in [p.strip() for p in frag.split('[...]') if p.strip()]:
        if piece not in row: print('AFTER-ID NOT IN ROW',i,'|',piece[:120])
