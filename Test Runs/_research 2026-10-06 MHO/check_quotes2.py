import csv,re,sys
R={r[0]:r[2] for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open(sys.argv[1],encoding='utf-8').read()
def norm(s): return re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip()
T=norm(t)
ids=re.findall(r'\[([A-Z]\d{4}-\d{3})\]',T)
print('ids',len(ids),'distinct',len(set(ids)),'missing',[i for i in ids if i not in R])
print('E-style ids',re.findall(r'\[E\d+-\d+\]',T)); print('em dashes',t.count('—'),'en dashes',t.count('–'))
# for each id, find all quoted strings that END within 80 chars before the id, after the previous id
prev=0; bad=0; checked=0
for m in re.finditer(r'\*\*\[([A-Z]\d{4}-\d{3})\]\*\*',T):
    i=m.group(1); seg=T[prev:m.start()]; prev=m.end()
    quotes=[(q.group(1),q.end()) for q in re.finditer(r'"([^"]{2,})"',seg)]
    row=norm(R[i])
    for q,end in quotes:
        if len(seg)-end>90: continue
        checked+=1
        for frag in re.split(r'\s*\[\.\.\.\]\s*',q):
            f=frag.strip(' .,;:?')
            if f and f not in row:
                bad+=1; print('MISMATCH',i,'|',f[:140])
print('quotes checked',checked,'mismatches',bad)
