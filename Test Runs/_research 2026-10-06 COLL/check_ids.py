import csv,re
rows={r['\ufeffid']:r['quote_verbatim'] for r in csv.DictReader(open(r'C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv',encoding='utf-8'))}
s=open(r'C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-10-06 Run - COLL Collegium Pharmaceutical.md',encoding='utf-8').read()
norm=lambda t: re.sub(r'\s+',' ',t).strip()
flat=norm(s); bad=0
if re.search(r'\[E\d-\d+\]',flat): print('E-ID FOUND'); bad+=1
ids=set(re.findall(r'\[([MLR]\d{4}-\d{3})\]',flat))
for i in sorted(ids):
    if i not in rows: print('MISSING',i); bad+=1
print(len(ids),'distinct ids, all present' if not bad else '')
pat=re.compile(r'"([^"]{4,}?)"\s*(?:\([^)]{0,40}\))?\s*(?:\*\*)?\[([MLR]\d{4}-\d{3})\]')
n=0
for m in pat.finditer(flat):
    n+=1; q,i=m.groups(); src=norm(rows[i])
    for part in q.split('[...]'):
        part=norm(part)
        if part and part not in src: print('NOT IN ROW',i,'|',part); bad+=1
print('quoted fragments checked:',n)
# ids with no quote immediately before: show context for eyeball
for m in re.finditer(r'\[([MLR]\d{4}-\d{3})\]',flat):
    pre=flat[max(0,m.start()-4):m.start()]
    if '"' not in pre: print('NO-QUOTE-ADJ',m.group(1),'|',flat[max(0,m.start()-90):m.start()])
print('BAD',bad)
