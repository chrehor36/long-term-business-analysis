# Check for the BETA run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment
# in the text between the previous id (or paragraph start) and an id is in that id's row. Fragments that are
# filing quotes are reported as UNMATCHED for manual review, not silently passed.
import csv,re,sys
run=open(sys.argv[1],encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2],encoding='utf-8-sig'))}
eids=re.findall(r'\[E\d-\d+\]',run)
print('E-ids:',eids or 'none')
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',run)
missing=sorted({i for i in ids if i not in rows})
print('ids cited:',len(set(ids)),'missing:',missing or 'none')
norm=lambda s:re.sub(r'\s+',' ',s.replace('“','"').replace('”','"')).strip()
bad=0
for para in re.split(r'\n\s*\n',run):
    last=0
    for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',para):
        seg=para[last:m.start()]; last=m.end()
        frags=re.findall(r'"([^"]{6,}?)"',seg.replace('“','"').replace('”','"'))
        if not frags: continue
        q=norm(rows.get(m.group(1),''))
        # only the fragment nearest the id must be the row's; earlier ones are reported if unmatched
        for k,f in enumerate(frags):
            ok=norm(f) in q
            if not ok:
                tag='NEAREST-FAIL' if k==len(frags)-1 else 'unmatched(earlier)'
                if tag=='NEAREST-FAIL': bad+=1
                print(tag,m.group(1),'|',f[:110])
print('nearest-fragment failures:',bad)
