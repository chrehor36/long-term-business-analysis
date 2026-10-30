import csv,re,sys
rows={r[0]:r for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8'))}
t=open(sys.argv[1],encoding='utf-8').read()
norm=lambda s:re.sub(r'\s+',' ',s.replace('\u2019',"'").replace('\u201c','"').replace('\u201d','"')).strip().lower()
bad=0;n=0
for m in re.finditer(r'["\u201c]([^"\u201d]{8,400})["\u201d]\s*\**\[([MLR]\d{4}-\d{3})\]',t):
    q,i=m.group(1),m.group(2);n+=1
    if i not in rows: print('MISSING',i);bad+=1;continue
    row=norm(' '.join(rows[i]))
    for frag in q.split('[...]'):
        f=norm(frag).strip(' .,;:')
        if f and f not in row: print('SLIP',i,repr(frag[:120]));bad+=1
ids=set(re.findall(r'\b([MLR]\d{4}-\d{3})\b',t))
print('ids',len(ids),'missing',[i for i in ids if i not in rows],'E-ids',re.findall(r'\[E\d-\d+\]',t)[:3],'quotes',n,'bad',bad)
