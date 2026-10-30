import csv,re,sys
sys.stdout.reconfigure(encoding='utf-8')
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('../../principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open(sys.argv[1],encoding='utf-8').read()
bad=0
if re.search(r'\bE\d-\d+\b',t): print('E-id found'); bad=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',t)
for i in set(ids):
    if i not in rows: print('MISSING',i); bad=1
# quoted fragments followed (within the same line run) by an id: check the fragment appears in that row
norm=lambda s: re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip()
for m in re.finditer(r'"([^"]{8,}?)"\s*\**\s*\[([MLR]\d{4}-\d{3})\]', t.replace('\n',' ')):
    frag,i=m.group(1),m.group(2)
    row=norm(rows.get(i,''))
    for part in [p for p in frag.split('[...]')]:
        part=norm(part).strip(' .,;')
        if part and part not in row:
            print('NOT IN ROW',i,'::',part[:120]); bad=1
print('ids:',len(set(ids)),'checked; bad=',bad)
