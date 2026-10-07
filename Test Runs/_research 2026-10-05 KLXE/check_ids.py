import csv,re,sys
f=sys.argv[1]
txt=open(f,encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
ids=re.findall(r'\[([MLRE]\d{4}-\d{3}|E\d+-\d+)\]',txt)
bad=[i for i in ids if i.startswith('E') or i not in rows]
print('ids cited',len(ids),'distinct',len(set(ids)),'bad',bad)
print('E-ids:',re.findall(r'\[E\d',txt))
def norm(s):
    s=s.replace('“','"').replace('”','"').replace('’',"'").replace('‘',"'")
    return re.sub(r'\s+',' ',s)
# quoted fragment immediately before an id: "..." then optional punctuation/spaces then ** [id]
probs=0
for m in re.finditer(r'"([^"]{3,600}?)"[\s\.,;:]*(?:\([^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*',norm(txt)):
    frag,i=m.group(1),m.group(2)
    row=norm(rows[i])
    parts=[p.strip(' .,;') for p in frag.split('[...]')]
    for p in parts:
        p2=p.replace('...','').strip()
        for sub in [s.strip(' .,;') for s in p.split('...') if s.strip()]:
            if sub not in row:
                probs+=1; print('NOT IN ROW',i,'::',sub[:120])
print('fragment problems',probs)
