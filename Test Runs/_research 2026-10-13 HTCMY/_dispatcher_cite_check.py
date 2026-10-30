import csv,re,sys
F=sys.argv[1]
rows={r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
qcol=[c for c in next(iter(rows.values())).keys() if 'quote' in c.lower()][0]
norm=lambda s:re.sub(r'\s+',' ',s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"')).strip().lower()
t=open(F,encoding='utf-8').read()
bad=0;n=0
for m in re.finditer(r'\*\*\[?([MLR]\d{4}-\d{3}[a-z]?)\]?\*\*',t):
    i=m.group(1)
    if i not in rows: print('MISSING',i);bad+=1;continue
for m in re.finditer(r'"([^"\n]{8,})"[^"\n]{0,40}?\*\*\[?([MLR]\d{4}-\d{3}[a-z]?)\]?\*\*',t):
    q,i=m.groups();n+=1
    if i not in rows: continue
    src=norm(rows[i][qcol])
    for frag in re.split(r'\s*\[\.\.\.\]\s*|\.\.\.',q):
        f=norm(frag).strip(' .,;:')
        if f and f not in src: print('SLIP',i,repr(frag[:80]));bad+=1
print('E-ids:',len(re.findall(r'\[E\d+-\d+\]',t)),'pairs checked',n,'problems',bad)
