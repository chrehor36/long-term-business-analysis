import csv,re,sys
run=open(sys.argv[1],encoding='utf-8').read()
rows={r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
norm=lambda s:re.sub(r'\s+',' ',s.replace('\u2019',"'").replace('\u201c','"').replace('\u201d','"')).strip().lower()
bad=0;n=0
for m in re.finditer(r'"([^"]{8,})"[^"\n]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run):
    q,i=m.group(1),m.group(2);n+=1
    if i not in rows: print('MISSING',i);bad+=1;continue
    qt=norm(rows[i]['quote_verbatim'])
    for frag in re.split(r'\[\.\.\.\]|\.\.\.',q):
        f=norm(frag).strip(' .,;')
        if f and f not in qt: print('SLIP',i,repr(frag[:80]));bad+=1
ids=set(re.findall(r'\[([MLRE]\d{4}-\d{3}|E\d+-\d+)\]',run))
print('ids',len(ids),'missing',[i for i in ids if i not in rows]);print('fragments',n,'problems',bad)
