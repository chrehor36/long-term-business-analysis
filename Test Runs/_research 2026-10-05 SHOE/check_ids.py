import csv,re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
run=open('Test Runs/2026-10-05 Run - SHOE Shoe Station Group.md',encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
ids=re.findall(r'\[([A-Z]+\d{0,4}-\d+)\]',run)
bad=[i for i in ids if not re.match(r'^[MLR]\d{4}-\d{3}$',i)]
print('ids cited',len(ids),'distinct',len(set(ids)),'non-MLR ids',bad)
print('missing',[i for i in set(ids) if i not in rows])
print('E-ids', re.findall(r'\bE\d-\d+\b',run))
norm=lambda s: re.sub(r'\s+',' ',s)
problems=0
# for every quoted fragment within 260 chars before an id, check it is in the row
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run):
    i=m.group(1); pre=run[max(0,m.start()-400):m.start()]
    # take the last quoted fragment immediately preceding
    q=re.findall(r'"([^"]{6,})"',pre)
    if not q: continue
    frag=q[-1]
    # ignore fragments that are separated by another id
    tail=pre[pre.rfind('"'+frag+'"'):]
    if re.search(r'\[[MLR]\d{4}-\d{3}\]',tail): continue
    parts=[p.strip(' .,') for p in frag.split('[...]')]
    ok=all(norm(p) in norm(rows[i]) for p in parts if p)
    if not ok:
        problems+=1; print('NOT IN ROW',i,'::',frag)
print('fragment problems',problems)
