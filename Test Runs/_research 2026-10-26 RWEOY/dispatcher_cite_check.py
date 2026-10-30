# Dispatcher's check (2026-10-26 overnight cycle): every quoted fragment set directly beside a v5 id
# ("quote" **[ID]**, or **[ID]**: "quote") is in that id's row of principle_ledger_v5.csv.
import csv,re,sys
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
def norm(s): return re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip().lower()
t=open(sys.argv[1],encoding='utf8').read()
ID=r'\*\*\[?([MLR]\d{4}-\d{3})\]?\*\*'
pairs=[(m.group(2),m.group(1)) for m in re.finditer(r'"([^"]{6,}?)"[\s.,;)]{0,4}'+ID,t)]
pairs+=[(m.group(2),m.group(1)) for m in re.finditer(ID+r'[\s:,(]{0,4}"([^"]{6,}?)"',t)]
ids=set(re.findall(r'[MLR]\d{4}-\d{3}',t)); miss=[i for i in ids if i not in rows]
bad=0
for q,i in pairs:
    if i not in rows: continue
    for frag in q.split('[...]'):
        f=norm(frag).strip(' .,;:')
        if len(f)>3 and f not in norm(rows[i]): print('SLIP',i,repr(q[:100])); bad+=1; break
print('ids',len(ids),'missing',miss,'fragments checked',len(pairs),'slips',bad,'E-ids',len(re.findall(r'\[E\d+-\d+\]',t)))
