import csv,re,sys
rows={r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
qcol=[k for k in next(iter(rows.values())).keys() if 'quote' in k.lower()][0]
t=open(sys.argv[1],encoding='utf-8').read()
def norm(s): return re.sub(r'\s+',' ',s.replace('\u2019',"'").replace('\u201c','"').replace('\u201d','"')).strip().lower()
bad=0;n=0
for m in re.finditer(r'[\"\u201c]([^\"\u201d]{6,}?)[\"\u201d][^\"\u201c\n]{0,40}?\*\*\[?([MLR]\d{4}-\d{3}[^\]\*]*)\]?\*\*',t):
    frag,ids=m.group(1),re.findall(r'[MLR]\d{4}-\d{3}',m.group(2))
    for i in ids:
        n+=1
        if i not in rows: print('MISSING',i);bad+=1;continue
        q=norm(rows[i][qcol])
        parts=[p for p in re.split(r'\[\.\.\.\]|\.\.\.|\u2026',norm(frag)) if p.strip()]
        if not all(p.strip(' .,;') in q for p in parts): print('SLIP',i,'|',frag[:90]);bad+=1
for i in set(re.findall(r'\b[MLR]\d{4}-\d{3}\b',t)):
    if i not in rows: print('PHANTOM',i);bad+=1
print('checked',n,'bad',bad, 'E-ids', len(re.findall(r'\[E\d-\d+\]',t)))
