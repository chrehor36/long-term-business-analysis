# Dispatcher's citation check (overnight 2026-10-17): every quoted fragment in a line that carries a v5 id must be in one of that line's rows.
import csv,re,sys
rows={}
with open('principle_ledger_v5.csv',encoding='utf-8') as f:
    r=csv.reader(f);h=next(r)
    for x in r: rows[x[0]]=' '.join(x)
norm=lambda s:re.sub(r'\s+',' ',s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"')).lower()
txt=open(sys.argv[1],encoding='utf-8').read()
ids_re=re.compile(r'\b([MLR]\d{4}-\d{3})\b')
bad=0;n=0
for para in re.split(r'\n\s*\n',txt):
    ids=set(ids_re.findall(para))
    if re.search(r'\bE\d-\d+\b',para): print('E-ID:',para[:120]);bad+=1
    for i in ids:
        if i not in rows: print('PHANTOM',i);bad+=1
    if not ids: continue
    for q in re.findall(r'["\u201c]([^"\u201d]{12,})["\u201d]',para):
        n+=1
        parts=[p.strip(' .,;:') for p in re.split(r'\[\.\.\.\]|\.\.\.|\u2026',q) if len(p.strip(' .,;:'))>=6]
        if all(any(norm(p) in norm(rows[i]) for i in ids) for p in parts): continue
        # quote may be a filing quote, not a ledger quote; report for reading
        print('CHECK:',sorted(ids),'|',q[:110])
print('quotes checked',n,'hard faults',bad)
