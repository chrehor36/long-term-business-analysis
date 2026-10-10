# Checks the CB run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment directly before an id is in that row.
import csv,re,sys,unicodedata
csv.field_size_limit(10**8)
root='C:/Users/chreh/OneDrive/Documents/BRK/'
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open(root+'principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open(root+'Test Runs/2026-10-07 Run - CB Chubb.md',encoding='utf-8').read()
def norm(s):
    s=unicodedata.normalize('NFKC',s).replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    return re.sub(r'\s+',' ',s).strip()
bad=0
eids=re.findall(r'\[E\d+-\d+\]',t)
if eids: print('E-ids found',eids); bad+=1
ids=set(re.findall(r'\[([MLR]\d{4}-\d{3})\]',t))
for i in sorted(ids):
    if i not in rows: print('PHANTOM',i); bad+=1
# quoted fragment immediately followed (within 12 chars) by **[id]** ; also chains of ids after one quote
for m in re.finditer(r'"([^"]{3,600})"\s*(?:\([^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t):
    frag,i=m.group(1),m.group(2)
    if i in rows:
        parts=[p for p in re.split(r'\s*\[\.\.\.\]\s*',frag) if p.strip()]
        for p in parts:
            if norm(p) not in norm(rows[i]):
                print('NOT IN ROW',i,'|',p[:120]); bad+=1
print('ids checked',len(ids),'problems',bad)
