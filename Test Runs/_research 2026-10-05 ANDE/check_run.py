import re, csv
p=r'c:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-05 Run - ANDE The Andersons.md'
s=open(p,encoding='utf-8').read()
rows={r[0]:r for r in csv.reader(open(r'c:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv',encoding='utf-8'))}
print('em dashes:', s.count('\u2014'), 'en dashes:', s.count('\u2013'))
eids=re.findall(r'\[E\d+-\d+\]',s); print('E-ids:',eids)
ids=set(re.findall(r'\[([MLR]\d{4}-\d{3})\]',s))
missing=[i for i in ids if i not in rows]; print('ids',len(ids),'missing',missing)
norm=lambda x: re.sub(r'\s+',' ',x.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"'))
bad=0; n=0
# quoted fragment(s) followed within the same clause by ids
for m in re.finditer(r'"([^"\n]{3,400})"([^"\n]{0,40}?)((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)', s):
    frag=m.group(1); between=m.group(2)
    if '"' in between: continue
    for i in re.findall(r'\[([MLR]\d{4}-\d{3})\]', m.group(3)):
        n+=1
        q=norm(rows[i][2]); parts=[norm(x).strip() for x in frag.split('[...]')]
        ok=all(pt in q for pt in parts if pt)
        if not ok: bad+=1; print('NOT IN ROW', i, '|', frag)
print('fragments checked', n, 'bad', bad)
