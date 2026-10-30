# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# in the same line as an id (and within the bullet) appears in at least one of the cited rows.
import csv,re,sys,unicodedata
run=open(sys.argv[1],encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    for a,b in (('’',"'"),('‘',"'"),('“','"'),('”','"'),('—','-'),('–','-'),('�','')):
        s=s.replace(a,b)
    return re.sub(r'\s+',' ',s).strip().lower()
eids=re.findall(r'\[E\d+-\d+\]',run)
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',run)
missing=[i for i in set(ids) if i not in rows]
problems=[]; nfrag=0
paras=re.split(r'\n(?=- |\n|\(\d\) |  - )',run)
for p in paras:
    pid=re.findall(r'\[([MLR]\d{4}-\d{3})\]',p)
    if not pid: continue
    flat=' '.join(p.split())
    # fragments: double-quoted strings immediately followed (within 8 chars) by an id
    for m in re.finditer(r'"([^"]{6,400})"[^"\[]{0,80}?\[([MLR]\d{4}-\d{3})\]',flat):
        frag,i=m.group(1),m.group(2); nfrag+=1
        parts=[x for x in frag.split('[...]')]
        ok=all(norm(x) in norm(rows.get(i,'')) for x in parts if x.strip())
        if not ok: problems.append((i,frag[:120]))
print('E-ids:',len(eids),' distinct ids:',len(set(ids)),' missing:',missing,' fragments checked:',nfrag,' problems:',len(problems))
for p in problems: print('  ',p)
