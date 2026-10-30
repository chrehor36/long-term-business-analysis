import csv,re,sys
rows={}
for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf8')):
    k=list(r.keys())
    rows[r[k[0]]]=' '.join(r.values())
t=open(sys.argv[1],encoding='utf8').read()
norm=lambda s:re.sub(r'\s+',' ',s.replace('\u2019',"'").replace('\u201c','"').replace('\u201d','"')).lower()
ids=set(re.findall(r'\b([MLR]\d{4}-\d{3})\b',t)); bad=[i for i in ids if i not in rows]
print('ids',len(ids),'missing',bad, 'E-ids',re.findall(r'\bE\d-\d+\b',t)[:5])
slips=0;n=0
for m in re.finditer(r'"([^"\n]{8,}?)"[^"\n]{0,40}?\*\*\[?([MLR]\d{4}-\d{3})',t):
    q,i=m.group(1),m.group(2); n+=1
    if i not in rows: continue
    for frag in re.split(r'\s*\[\.\.\.\]\s*|\s*\.\.\.\s*',q):
        if len(frag)>3 and norm(frag) not in norm(rows[i]): slips+=1; print('SLIP',i,'|',frag[:90])
print('quoted pairs',n,'slips',slips)
