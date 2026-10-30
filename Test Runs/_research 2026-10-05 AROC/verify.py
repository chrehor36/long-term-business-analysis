import csv,re,sys
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
s=open('Test Runs/2026-10-05 Run - AROC Archrock.md',encoding='utf-8').read()
ids=re.findall(r'\[([A-Z]+\d{4}-\d{3})\]',s)
bad=[i for i in ids if i not in rows]; eids=[i for i in ids if i.startswith('E')]
print('ids cited',len(ids),'distinct',len(set(ids)),'missing',bad,'E-ids',eids)
norm=lambda t: re.sub(r'\s+',' ',t).strip()
fails=0; checked=0
for m in re.finditer(r'\*\*\[([A-Z]+\d{4}-\d{3})\]\*\*',s):
    i=m.group(1); before=s[max(0,m.start()-90):m.start()]
    # closing quote must be within the window and only connective text between it and the id
    q=re.search(r'"([^"]{3,})"([^"]*)$',before)
    if not q: continue
    tail=q.group(2)
    if re.search(r'\*\*\[',tail) or len(tail)>60: continue
    # find full quote start (may be beyond window)
    end=m.start()-len(tail)-1
    start=s.rfind('"',0,end)
    frag=s[start+1:end]
    pieces=[p.strip(' .,;:') for p in frag.split('[...]')]
    row=norm(rows[i])
    for p in pieces:
        p=norm(p)
        if not p: continue
        checked+=1
        if p not in row:
            fails+=1; print('FAIL',i,'|',p[:120])
print('fragments checked',checked,'fails',fails)
print('--- id-before-quote form')
f2=0;c2=0
for m in re.finditer(r'\*\*\[([A-Z]+\d{4}-\d{3})\]\*\*\s*[:,]?\s*"([^"]+)"',s):
    i=m.group(1)
    for p in m.group(2).split('[...]'):
        p=norm(p.strip(' .,;:'))
        if not p: continue
        c2+=1
        if p not in norm(rows[i]): f2+=1; print('FAIL',i,'|',p[:120])
print('checked',c2,'fails',f2)
