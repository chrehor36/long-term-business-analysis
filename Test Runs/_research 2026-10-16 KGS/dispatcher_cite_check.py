# Dispatcher's check (overnight 2026-10-16): every id exists; every quoted fragment in the same sentence/line before an id is in that row.
import csv,re,sys,unicodedata
def n(s):
    s=unicodedata.normalize('NFKC',s).replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    return re.sub(r'\s+',' ',s).strip().lower()
rows={r['id']:n(r['quote_verbatim']) for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open(sys.argv[1],encoding='utf-8').read()
ids=set(re.findall(r'\b[MLR]\d{4}-\d{3}\b',t)); bad=[i for i in ids if i not in rows]
print('ids',len(ids),'missing',bad,'E-ids',re.findall(r'\[E\d-\d+\]',t))
slips=0
for line in t.split('\n'):
    for m in re.finditer(r'\[([MLR]\d{4}-\d{3})\]',line):
        pre=line[:m.start()]
        qs=re.findall(r'[“"]([^“”"]{6,})[”"]',pre)
        if not qs: continue
        q=qs[-1]
        parts=[p.strip(' .,;:') for p in re.split(r'\[\.\.\.\]|\.\.\.|…',q)]
        for p in parts:
            if len(p)>3 and n(p) not in rows.get(m.group(1),''):
                slips+=1; print('SLIP',m.group(1),'|',p[:120])
print('slips',slips)
