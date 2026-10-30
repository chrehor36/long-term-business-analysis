import csv,re,sys
rows={r['id']:re.sub(r'\s+',' ',r['quote_verbatim']) for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
txt=open('Test Runs/2026-10-05 Run - ENSG Ensign Group.md',encoding='utf-8').read()
bad=0
if re.search(r'\[E\d',txt): print('E-id found'); bad+=1
ids=set(re.findall(r'\[([MLR]\d{4}-\d{3})\]',txt))
for i in ids:
    if i not in rows: print('MISSING',i); bad+=1
print('ids cited',len(ids))
def norm(s): return re.sub(r'\s+',' ',s).strip()
for ln,line in enumerate(txt.split('\n'),1):
    lids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',line)
    if not lids: continue
    frags=re.findall(r'"([^"]{4,})"',line)+re.findall(r'“([^”]{4,})”',line)
    for fr in frags:
        parts=[norm(p) for p in fr.split('[...]') if norm(p)]
        ok=any(all(p.rstrip('.').strip() in rows.get(i,'') for p in parts) for i in lids)
        if not ok: print(f'L{ln} FRAG NOT IN ROW {lids}: {fr[:120]}'); bad+=1
# em dashes outside quotes and headings
for ln,line in enumerate(txt.split('\n'),1):
    if line.startswith('#'): continue
    s=re.sub(r'"[^"]*"','',line); s=re.sub(r'“[^”]*”','',s)
    if '—' in s and 'COMPUTATION — NOT A CLEARANCE' not in s: print(f'L{ln} em dash in prose: {s[:120]}'); bad+=1
print('PROBLEMS',bad)
