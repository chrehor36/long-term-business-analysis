import csv,re,sys
run=open(sys.argv[1],encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
norm=lambda s:re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip()
bad=0
if re.search(r'\bE\d-\d\d\b',run): print('E-id found'); bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',run)
for i in set(ids):
    if i not in rows: print('MISSING',i); bad+=1
# fragments: for each paragraph, segment by id markers; quotes in the segment before an id belong to it
for para in re.split(r'\n\s*\n|\n- |\n\|',run):
    pos=0
    for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',para):
        seg=para[pos:m.start()]; pos=m.end()
        masked=re.sub(r'"[^"]*"',lambda x:'Q'*len(x.group(0)),seg)
        cut=max(masked.rfind('. '),masked.rfind('; '),masked.rfind(': '),masked.rfind(chr(10)))
        seg=seg[cut+1:] if cut>=0 else seg
        # only the last sentence-ish chunk: after the previous ';' or '. ' boundary that contains a quote
        for q in re.findall(r'"([^"]{3,})"',seg):
            for frag in q.split('[...]'):
                f=norm(frag).strip(' .,;:')
                if len(f)<3: continue
                if norm(f) not in norm(rows.get(m.group(1),'')):
                    print('NOT IN',m.group(1),'::',f[:90])
print('ids cited',len(set(ids)),'bad',bad)
