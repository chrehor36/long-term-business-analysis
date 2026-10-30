import csv,re,sys,unicodedata
R={r[0]:r[2] for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open(sys.argv[1],encoding='utf-8').read()
norm=lambda s:re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip()
ids=re.findall(r'\[([A-Z]+\d{0,4}-\d{2,3})\]',t)
bad=[i for i in ids if i not in R]
print('ids',len(ids),'distinct',len(set(ids)),'missing',bad)
print('E-ids',re.findall(r'\[E\d+-\d+\]',t))
print('em dashes',t.count('—'))
# chunk: text between consecutive ids
pos=[(m.start(),m.end(),m.group(1)) for m in re.finditer(r'\*\*\[([A-Z]+\d{0,4}-\d{2,3})\]\*\*',t)]
prev=0; probs=0
for s,e,i in pos:
    chunk=t[prev:s]; prev=e
    # only the last sentence-ish part: after last newline-dash or period-space outside quotes is hard; take last 400 chars
    chunk=chunk[-500:]
    qs=re.findall(r'"([^"]{3,})"',chunk)
    if not qs: continue
    q=qs[-1]
    row=norm(R.get(i,''))
    for frag in re.split(r'\s*\[\.\.\.\]\s*',norm(q)):
        f=frag.strip(' .,;:')
        if f and f not in row:
            probs+=1; print('MISMATCH',i,'|',f[:120])
print('problems',probs)
