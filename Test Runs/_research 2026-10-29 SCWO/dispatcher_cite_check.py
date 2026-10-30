import csv,re,sys
rows={}
with open('principle_ledger_v5.csv',encoding='utf-8') as f:
    r=csv.reader(f); h=next(r)
    for x in r: rows[x[0]]=x
qi=2  # quote_verbatim
def norm(s): return re.sub(r'\s+',' ',s.replace('’',"'").replace('“','"').replace('”','"')).strip().lower()
t=open(sys.argv[1],encoding='utf-8').read()
idre=re.compile(r'\b([MLR]\d{4}-\d{3})\b')
n=bad=0
for para in t.split('\n'):
    ids=idre.findall(para)
    if not ids: continue
    for m in re.finditer(r'[“"]([^"“”]{8,}?)[”"]\s*\**\s*\[?\**\s*([MLR]\d{4}-\d{3})',para):
        frag,i=m.group(1),m.group(2); n+=1
        if i not in rows: print('MISSING',i); bad+=1; continue
        parts=[p for p in re.split(r'\[\.\.\.\]|\.\.\.|…',frag) if p.strip()]
        if not all(norm(p) in norm(rows[i][qi]) for p in parts): bad+=1; print('SLIP?',i,'|',frag[:120])
for i in set(idre.findall(t)):
    if i not in rows: print('PHANTOM',i)
print('pairs',n,'flagged',bad, 'E-ids', len(re.findall(r'\bE\d-\d\d\b',t)))
