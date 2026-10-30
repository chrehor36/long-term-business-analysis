# check the run file (quotes whose closing mark is within 160 characters before an id are checked against that row): no E-ids; every M/L/R id in the v5 ledger; every quoted fragment before an id is in that row
import csv,re,sys
sys.stdout.reconfigure(encoding='utf-8')
rows={r[0]:r[2] for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8'))}
s=open('Test Runs/2026-10-17 Run - SKK Rantizo (formerly SKK Holdings).md',encoding='utf-8').read()
bad=0
if re.search(r'\[E\d-\d+\]',s): print('E-id found'); bad+=1
ids=list(re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',s))
norm=lambda x: re.sub(r'\s+',' ',x).strip()
prev=0
for m in ids:
    i=m.group(1)
    if i not in rows: print('MISSING',i); bad+=1; prev=m.end(); continue
    seg=s[max(prev,m.start()-700):m.start()]
    row=norm(rows[i])
    qs=[mm for mm in re.finditer(r'[“"]([^”"]{6,}?)[”"]',seg) if len(seg)-mm.end()<=160]
    for q in [mm.group(1) for mm in qs]:
        for piece in re.split(r'\[\.\.\.\]|\[understood\]',q):
            piece=norm(piece).strip(' ,.;:')
            if len(piece)<6: continue
            if piece not in row and piece.replace('“','"').replace('”','"') not in row.replace('“','"').replace('”','"'):
                print('NOT IN ROW',i,'|',piece[:90]); bad+=1
    prev=m.end()
print(len(ids),'id citations;',len(set(x.group(1) for x in ids)),'distinct;','problems:',bad)
