import csv,re,sys
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open('Test Runs/2026-10-06 Run - INSW International Seaways.md',encoding='utf-8').read()
ids=re.findall(r'\[([A-Z]\d{4}-\d{3})\]',t)
bad=[i for i in ids if i not in rows]; e=[i for i in ids if i.startswith('E')]
print('ids cited',len(ids),'distinct',len(set(ids)),'missing',bad,'E-ids',e)
norm=lambda x:re.sub(r'\s+',' ',x.replace('’',"'").replace('“','"').replace('”','"')).strip()
# split paragraphs into segments ending with a run of ids
fails=0
for para in re.split(r'\n\s*\n|\n(?=[-|#])',t):
    pos=0
    for m in re.finditer(r'(?:\*\*\[[A-Z]\d{4}-\d{3}\]\*\*(?:\s*,\s*)?)+',para):
        seg=para[pos:m.start()]; grp=re.findall(r'[A-Z]\d{4}-\d{3}',m.group(0)); pos=m.end()
        for q in re.findall(r'"([^"]+)"',seg):
            parts=[p.strip(' .,;:') for p in re.split(r'\[\.\.\.\]',q) if p.strip(' .,;:')]
            ok=all(any(norm(p) in norm(rows[g]) for g in grp if g in rows) for p in parts)
            if not ok:
                fails+=1; print('NOT IN ROW',grp,'|',q[:120])
print('fragment failures',fails)
