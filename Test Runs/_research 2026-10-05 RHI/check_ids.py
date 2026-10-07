# Checks the RHI run file: no em dashes, no E-ids, every M/L/R id in principle_ledger_v5.csv,
# and every double-quoted fragment that precedes an id (within the same list item or paragraph) is in that id's row.
import csv,re
p="Test Runs/2026-10-05 Run - RHI Robert Half.md"
s=open(p,encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
bad=0
print('em dashes:', s.count('—'))
print('E-ids:', re.findall(r'\[E\d-\d+\]',s))
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',s)
print('ids cited:',len(ids),'distinct',len(set(ids)))
for i in sorted(set(ids)):
    if i not in rows: print('MISSING',i); bad+=1
checked=0
for para0 in s.split('\n\n'):
    for para in re.split(r'\n(?=\s*(?:\d+\. |- |\| ))',para0):
        para=re.sub(r'\s*\n\s*',' ',para)
        pos=0
        for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',para):
            seg=para[pos:m.start()]; pos=m.end()
            for q in re.findall(r'"([^"]+)"',seg):
                for pc in [x.strip() for x in q.split('[...]') if x.strip()]:
                    checked+=1
                    if pc not in rows[m.group(1)]:
                        print('NOT IN ROW',m.group(1),'|',pc[:140]); bad+=1
print('fragments checked',checked,'problems',bad)
