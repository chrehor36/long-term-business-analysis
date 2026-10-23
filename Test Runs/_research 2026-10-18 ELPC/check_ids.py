# Check for the ELPC run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# placed between the previous id (or paragraph start) and an id is found in that id's row (elisions [...] split).
import csv,re,sys
sys.stdout.reconfigure(encoding='utf-8')
run=open(sys.argv[1],encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2],encoding='utf-8-sig'))}
def norm(t):
    t=t.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"').replace('\ufffd','')
    t=re.sub(r'[\u2014\u2013-]',' ',t); t=re.sub(r'\s+',' ',t)
    return t.strip().lower()
bad=0
eids=re.findall(r'\[E\d-\d+\]',run)
if eids: print('E-ids found:',eids); bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id',i); bad+=1
for para in re.split(r'\n\s*\n|\n- |\n\| ',run):
    flat=para.replace('\n',' ')
    pos=0
    for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',flat):
        seg=flat[pos:m.start()]; pos=m.end()
        seg=re.split(r'(?<=[.;:)])\s+(?=[A-Z(*])',seg)[-1]   # the clause that carries the id
        # only quotes after the last id-free break: take quotes in seg
        for q in re.findall(r'"([^"]{6,})"|\u201c([^\u201d]{6,})\u201d',seg):
            q=q[0] or q[1]
            parts=[x for x in re.split(r'\[\.\.\.\]',q) if x.strip()]
            row=norm(rows.get(m.group(1),''))
            if not all(norm(x) in row for x in parts):
                # allow a quote that belongs to a filing (no id); report for manual review
                print('CHECK', m.group(1), '|', q[:110])
                bad+=1
print('ids cited:',len(set(ids)),'problems:',bad)
