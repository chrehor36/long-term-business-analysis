import csv,re,sys
R=sys.argv[1]
rows={r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
qcol=[c for c in next(iter(rows.values())).keys() if 'quote' in c.lower()][0]
norm=lambda s:re.sub(r'\s+',' ',s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"')).strip().lower()
t=open(R,encoding='utf-8').read()
ids=set(re.findall(r'\b([MLR]\d{4}-\d{3})\b',t)); bad=[i for i in ids if i not in rows]
print('ids',len(ids),'missing',bad,'E-ids',re.findall(r'\[E\d-\d+\]',t))
n=0;slips=[]
for m in re.finditer(r'["\u201c]([^"\u201d]{8,}?)["\u201d][^\n"\u201c]{0,40}?\*\*\[?([MLR]\d{4}-\d{3})',t):
    n+=1;frag,i=m.group(1),m.group(2)
    if i in rows:
        q=norm(rows[i][qcol])
        if not all(norm(p) in q for p in re.split(r'\[\.\.\.\]|\.\.\.|\u2026',frag) if norm(p)): slips.append((i,frag[:80]))
print('fragments',n,'slips',slips)
