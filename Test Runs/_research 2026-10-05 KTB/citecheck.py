import csv,re,sys
run=open('Test Runs/2026-10-05 Run - KTB Kontoor Brands.md',encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
bad=0
print('E-ids:',re.findall(r'\[E\d+-\d+\]',run))
print('em dashes:',run.count('—'))
ids=set(re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run))
for i in sorted(ids):
    if i not in rows: print('MISSING',i); bad+=1
for line in run.split('\n'):
    pos=0
    for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',line):
        seg=line[pos:m.start()]; pos=m.end()
        q=rows.get(m.group(1),'')
        for frag in re.findall(r'"([^"]+)"',seg):
            for piece in frag.split('[...]'):
                piece=piece.strip().rstrip(',')
                if piece and piece not in q:
                    print('NOT IN',m.group(1),'|',piece[:90]); bad+=1
print('ids',len(ids),'problems',bad)
