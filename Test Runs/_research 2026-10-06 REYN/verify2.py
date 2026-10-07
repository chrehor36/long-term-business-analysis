import csv,re
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open('Test Runs/2026-10-06 Run - REYN Reynolds Consumer Products.md',encoding='utf-8').read()
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('�','')
    return re.sub(r'\s+',' ',s).strip().lower()
Q=r'"([^"]{4,}?)"'
pairs=[]
for m in re.finditer(Q+r'[\s,.;:)(]{0,4}\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t): pairs.append((m.group(2),m.group(1)))
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*[:,]?\s*'+Q,t): pairs.append((m.group(1),m.group(2)))
bad=0
for i,q in pairs:
    for frag in q.split('[...]'):
        f=norm(frag).strip(' .,;:')
        if len(f)<4: continue
        if f not in norm(rows[i]): bad+=1; print('MISS',i,'|',frag[:100])
print('pairs',len(pairs),'misses',bad)
