import csv,re,sys,unicodedata
run=open(sys.argv[1],encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('�','')
    s=s.replace('—','-').replace('–','-')
    return re.sub(r'\s+',' ',s).strip().lower()
bad=0
if re.search(r'\[E\d',run): print('E-id found'); bad+=1
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING',i); bad+=1
# quoted fragment immediately before an id (same paragraph, no other id between)
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run):
    pre=run[max(0,m.start()-300):m.start()]
    pre=re.split(r'\*\*\[[A-Z0-9-]+\]\*\*',pre)[-1]
    mm=re.search(r'"([^"]{6,})"[\s.;,:]*$',pre)   # a quotation that ends right before the id
    if not mm: continue
    frag=mm.group(1)
    rt=norm(rows.get(m.group(1),''))
    for piece in re.split(r'\[\.\.\.\]',frag):
        p=norm(piece).strip(' .,;')
        if p and p not in rt:
            print('NOT IN ROW',m.group(1),'|',piece[:120]); bad+=1
print('ids',len(set(ids)),'problems',bad)
