# Check: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment adjacent to an id is in that row.
import csv,re,sys
sys.stdout.reconfigure(encoding='utf-8')
run=sys.argv[1]
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
s=open(run,encoding='utf-8').read()
bad=0
for m in re.finditer(r'\[E\d+-\d+\]',s): print('E-id',m.group(0)); bad+=1
ids=re.findall(r'\[((?:M|L|R)\d{4}-\d{3})\]',s)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING',i); bad+=1
norm=lambda x: re.sub(r'\s+',' ',x.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip()
# quoted fragments: "..." followed within 12 chars by **[ID]** (possibly several ids)
for m in re.finditer(r'"([^"]{6,})"[^"]{0,16}?\*\*\[((?:M|L|R)\d{4}-\d{3})\]\*\*',s):
    frag,i=m.group(1),m.group(2)
    parts=[norm(p) for p in frag.split('[...]') if norm(p)]
    q=norm(rows.get(i,''))
    for p in parts:
        if p not in q: print('NOT IN ROW',i,'|',p[:90]); bad+=1
print('ids',len(set(ids)),'problems',bad)
# second pass: id immediately before a quotation ("**[ID]**: "...")
n=0
for m in re.finditer(r'\*\*\[((?:M|L|R)\d{4}-\d{3})\]\*\*[^"\*]{0,6}"([^"]{6,})"',s):
    i,frag=m.group(1),m.group(2); n+=1
    q=norm(rows.get(i,''))
    for p in [norm(p) for p in frag.split('[...]') if norm(p)]:
        if p not in q: print('NOT IN ROW (id before)',i,'|',p[:90]); bad+=1
print('id-before quotes checked',n,'problems now',bad)
