# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that sits
# immediately before an id (between the previous id and this one) is found in that row's verbatim text.
import csv,re,sys,unicodedata
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
txt=open('Test Runs/2026-10-06 Run - GPOR Gulfport Energy.md',encoding='utf-8').read()
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('�','')
    s=s.replace('—','-').replace('–','-')
    s=re.sub(r'\*\*','',s); s=re.sub(r'\s+',' ',s)
    return s.strip().lower()
E=re.findall(r'\[E\d-\d+\]',txt); print('E-ids:',E)
ids=list(re.finditer(r'\[([MLR]\d{4}-\d{3})\]',txt))
missing=sorted(set(m.group(1) for m in ids if m.group(1) not in rows)); print('missing ids:',missing)
print('distinct ids:',len(set(m.group(1) for m in ids)))
prev=0; bad=0; checked=0
for m in ids:
    seg=txt[prev:m.start()]; prev=m.end()
    # only quotes in the last 700 chars before the id
    seg=seg[-700:]
    qs=re.findall(r'"([^"]{6,})"',seg)
    if not qs: continue
    q=qs[-1]
    row=norm(rows.get(m.group(1),''))
    for frag in re.split(r'\[\.\.\.\]',q):
        f=norm(frag).strip(' .,;:')
        if len(f)<4: continue
        checked+=1
        if f not in row:
            bad+=1; print('NOT IN ROW',m.group(1),'|',frag[:140])
print('fragments checked',checked,'failures',bad)
