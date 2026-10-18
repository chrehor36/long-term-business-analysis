import csv,re,sys
rows={r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
qcol=[c for c in next(iter(rows.values())).keys() if 'quote' in c.lower()][0]
norm=lambda s:re.sub(r'\s+',' ',s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"')).strip().lower()
t=open(sys.argv[1],encoding='utf-8').read()
bad=0;n=0
for para in re.split(r'\n\s*\n',t):
  ids=re.findall(r'\*\*\[?([MLR]\d{4}-\d{3})\]?\*\*',para)
  if not ids: continue
  for q in re.findall(r'"([^"]{12,})"|\u201c([^\u201d]{12,})\u201d',para):
    q=q[0] or q[1]
    frags=[f for f in re.split(r'\s*\[\.\.\.\]\s*|\.\.\.',q) if len(f.strip())>6]
    ok=any(all(norm(f) in norm(rows[i][qcol]) for f in frags) for i in ids if i in rows)
    n+=1
    if not ok: bad+=1; print('CHECK',ids,'|',q[:120])
print('ids',len(set(re.findall(r'[MLR]\d{4}-\d{3}',t))),'missing',[i for i in set(re.findall(r'[MLR]\d{4}-\d{3}',t)) if i not in rows],'quotes',n,'unmatched',bad, 'E-ids',re.findall(r'\[E\d-\d+\]',t))
