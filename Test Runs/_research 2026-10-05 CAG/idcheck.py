import csv,re,sys
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open(sys.argv[1],encoding='utf-8').read()
def norm(s): return re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('�',"'")).strip()
ids=re.findall(r'\[([A-Z]{1,2}\d{4}-\d{3}|E\d+-\d+)\]',t)
print('ids cited',len(ids),'distinct',len(set(ids)))
bad=[i for i in set(ids) if i not in rows]; print('missing/phantom:',bad)
print('E-ids:',[i for i in ids if i.startswith('E')])
# segments: split text at each id cluster
pos=0; problems=0
for m in re.finditer(r'(\*\*\[[A-Z]\d{4}-\d{3}\]\*\*(?:,\s*\*\*\[[A-Z]\d{4}-\d{3}\]\*\*)*)',t):
    seg=t[pos:m.start()]; cl=re.findall(r'[A-Z]\d{4}-\d{3}',m.group(1)); pos=m.end()
    # limit seg to current paragraph/sentence chunk after last blank line
    seg=seg.split('\n\n')[-1]
    frags=re.findall(r'"([^"]{4,})"',seg)
    for fr in frags:
        if not any(norm(fr) in norm(rows.get(c,'')) for c in cl):
            problems+=1; print('NOT IN ROW',cl,'::',fr[:120])
print('problems',problems)
