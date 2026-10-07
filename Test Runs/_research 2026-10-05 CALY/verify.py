import csv,re,sys
F='Test Runs/2026-10-05 Run - CALY Callaway Golf.md'
t=open(F,encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
print('em dashes:',t.count('—'),' en dashes:',t.count('–'))
print('E-ids:',re.findall(r'\[E\d-\d+\]',t))
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',t)
missing=sorted(set(i for i in ids if i not in rows)); print('ids',len(set(ids)),'missing',missing)
norm=lambda s: re.sub(r'\s+',' ',s.replace('’',"'").replace('“','"').replace('”','"')).strip()
bad=0
for para in re.split(r'\n\s*\n|\n(?=\s*[-\d]+[.)]? )|\n\|',t):
    # segment paragraph at each id: text since previous id belongs to this id
    pos=0
    for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',para):
        seg=para[pos:m.start()]; pos=m.end()
        # only the last sentence-ish chunk before the id
        quotes=re.findall(r'"([^"]{3,})"',seg)
        if not quotes: continue
        pass
        row=norm(rows.get(m.group(1),''))
        for frag in "[...]".join(quotes).split('[...]'):
            f=norm(frag).strip(' .,;')
            if f and f not in row:
                bad+=1; print('NOT IN',m.group(1),'::',f[:120])
print('fragments not found:',bad)
