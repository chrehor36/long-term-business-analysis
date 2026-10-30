import csv,re,sys
sys.stdout.reconfigure(encoding="utf-8")
rows={r[0]:r[2] for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8'))}
txt=open(sys.argv[1],encoding='utf-8').read()
bad=0
if re.search(r'\[E\d',txt): print('E-id found'); bad+=1
ids=set(re.findall(r'\[((?:M|L|R)\d{4}-\d{3})\]',txt))
for i in sorted(ids):
    if i not in rows: print('MISSING',i); bad+=1
def norm(s): return re.sub(r'\s+',' ',s.replace('�','’').replace("'",'’')).strip()
# quoted fragments immediately before an id (same sentence): "..." **[ID]** or "..." [ID]
for m in re.finditer(r'"([^"]{3,400})"([^"\n]{0,60}?)\*\*\[((?:M|L|R)\d{4}-\d{3})\]\*\*',txt):
    frag,between,i=m.group(1),m.group(2),m.group(3)
    if i not in rows: continue
    parts=[p.strip() for p in frag.split('[...]')]
    for p in parts:
        if p and norm(p) not in norm(rows[i]):
            print('NOT IN ROW',i,'::',p[:120]); bad+=1
print('ids',len(ids),'problems',bad)
