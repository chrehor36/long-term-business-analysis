# dispatcher's check (overnight 2026-10-17, TSSI): every quoted fragment set directly beside a v5 id
# (the id within 40 characters after the closing quote) is in that id's row; ids exist; no E-ids
import csv,re,sys
rows={r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
def norm(s): return re.sub(r'\s+',' ',s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"')).strip().lower()
txt=open(sys.argv[1],encoding='utf-8').read()
bad=0;n=0
for i in set(re.findall(r'\b([MLR]\d{4}-\d{3})\b',txt)):
    if i not in rows: print('MISSING',i); bad+=1
if re.search(r'\[E\d-\d+\]',txt): print('E-id present'); bad+=1
for m in re.finditer(r'[\u201c"]([^\u201d"]{6,}?)[\u201d"]([^\u201c"]{0,40})',txt):
    ids=re.findall(r'\b([MLR]\d{4}-\d{3})\b',m.group(2))
    if not ids: continue
    n+=1; q=' '.join(norm(rows[i]['quote_verbatim']) for i in ids if i in rows)
    for part in re.split(r'\[\.\.\.\]|\.\.\.|\u2026|\[[^\]]*\]',m.group(1)):
        p=norm(part).strip(' .,;:')
        if len(p)>3 and p not in q: print('NOT IN ROW',ids,'|',part[:100]); bad+=1
print('fragments beside ids',n,'problems',bad)
