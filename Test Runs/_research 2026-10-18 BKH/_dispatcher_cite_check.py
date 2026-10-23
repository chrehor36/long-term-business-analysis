import csv,re,sys
rows={r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
qcol=['quote_verbatim']
t=open(sys.argv[1],encoding='utf-8').read()
norm=lambda s:re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip().lower()
n=bad=0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t):
    i=m.group(1)
    if i not in rows: print('MISSING',i); bad+=1; continue
    q=' '.join(rows[i][c] for c in qcol)
    pre=t[max(0,m.start()-400):m.start()]
    pre=pre.split('**[')[-1].split(']**')[-1]
    fr=re.findall(r'["“]([^"“”]{8,})["”]',pre)
    if not fr: continue
    f=fr[-1]; n+=1
    parts=[p.strip(' .,;:') for p in re.split(r'\[\.\.\.\]|\.\.\.',f) if len(p.strip(' .,;:'))>3]
    for p in parts:
        if norm(p) not in norm(q): print('SLIP?',i,'|',p[:120]); bad+=1
print('checked',n,'problems',bad)
