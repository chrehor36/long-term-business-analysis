# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that sits
# within the same sentence-span before an id is found (normalized) in that row's quote.
import csv,re,sys,unicodedata
run=open(sys.argv[1],encoding='utf-8').read()
rows={r['﻿id']:r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2],encoding='utf-8'))}
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('—','-').replace('–','-')
    s=s.replace('*','')
    return re.sub(r'\s+',' ',s).strip().lower()
bad=0
eids=re.findall(r'\[E\d-\d+\]',run)
if eids: print('E-ids found:',eids); bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id',i); bad+=1
# quoted fragments immediately followed (within 12 chars) by an id
flat=re.sub(r'\s+',' ',run)
for m in re.finditer(r'"([^"]{6,400})"[^"\[]{0,14}\*\*\[([MLR]\d{4}-\d{3})\]\*\*',flat):
    frag,i=m.group(1),m.group(2)
    if i in rows:
        parts=[p for p in re.split(r'\[\.\.\.\]',frag) if p.strip()]
        for p in parts:
            if norm(p) not in norm(rows[i]):
                print('NOT IN ROW',i,'::',p[:120]); bad+=1
print('ids checked:',len(set(ids)),'problems:',bad)
# also: an id immediately followed by a quoted fragment
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*[,:]? "([^"]{6,400})"',flat):
    i,frag=m.group(1),m.group(2)
    if i in rows:
        for p in [p for p in re.split(r'\[\.\.\.\]',frag) if p.strip()]:
            if norm(p) not in norm(rows[i]): print('AFTER-ID NOT IN ROW',i,'::',p[:120])
