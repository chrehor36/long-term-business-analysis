# Checks: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment adjacent (same sentence
# window, before the id) appears in that row's quote. Fragments with [...] are split and each piece checked.
import csv,re,sys,unicodedata
run=open(sys.argv[1],encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    return re.sub(r'\s+',' ',s).strip().lower()
probs=0
for m in re.finditer(r'\[E\d+-\d+\]',run): print('E-id',m.group()); probs+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING',i); probs+=1
# quotes: a "..." fragment followed within 12 chars by **[ID]** (possibly several ids)
for m in re.finditer(r'"([^"]{3,600})"\s*(?:\([^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run):
    frag,i=m.group(1),m.group(2)
    if i not in rows: continue
    q=norm(rows[i])
    for piece in re.split(r'\[\.\.\.\]',frag):
        p=norm(piece).strip(' .,;:')
        if p and p not in q:
            print('NOT IN ROW',i,'|',piece[:120]); probs+=1
print('ids',len(set(ids)),'problems',probs)
