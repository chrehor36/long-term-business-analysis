# Citation check for the KGS run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately before an id (within the same sentence) is in that row.
import csv,re,sys,unicodedata
ROOT='C:/Users/chreh/OneDrive/Documents/BRK/'
run=open(ROOT+'Test Runs/2026-10-16 Run - KGS Kodiak Gas Services.md',encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open(ROOT+'principle_ledger_v5.csv',encoding='utf-8-sig'))}
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    for a,b in [('’',"'"),('‘',"'"),('“','"'),('”','"'),('—','-'),('–','-'),('\ufffd','')]: s=s.replace(a,b)
    return re.sub(r'\s+',' ',s).strip().lower()
bad=0
if re.search(r'\[E\d',run): print('E-id found'); bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id',i); bad+=1
# fragments: a "..." quote followed within 12 chars by **[ID]** (possibly several ids)
for m in re.finditer(r'"([^"]{6,600})"\s*(?:\([^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run.replace('“','"').replace('”','"')):
    frag,i=m.group(1),m.group(2)
    if i not in rows: continue
    parts=[p for p in re.split(r'\[\.\.\.\]',frag)]
    ok=all(norm(p).strip(' .,;:') in norm(rows[i]) for p in parts if p.strip(' .,;:'))
    if not ok: print('FRAGMENT NOT IN ROW',i,'::',frag[:120]); bad+=1
print('ids:',len(set(ids)),'checked; problems:',bad)
sys.exit(1 if bad else 0)
