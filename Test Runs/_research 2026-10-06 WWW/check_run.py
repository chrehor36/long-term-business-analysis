import csv,re,sys
R={r['id']:r['quote_verbatim'] for r in csv.DictReader(open(r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv",encoding='utf-8-sig'))}
t=open(r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-06 Run - WWW Wolverine World Wide.md",encoding='utf-8').read()
bad=0
e=re.findall(r'\[E\d+-\d+\]',t); print("E-ids:",e); bad+=len(e)
ids=set(re.findall(r'\[([MLR]\d{4}-\d{3})\]',t))
for i in sorted(ids):
    if i not in R: print("MISSING",i); bad+=1
print("ids cited:",len(ids))
# fragments: "..." immediately followed (optional punctuation/space/words up to 3) by **[ID]**
para=re.sub(r'\s+',' ',t)
for m in re.finditer(r'"([^"]{3,}?)"[\s,.;:]*(?:\([^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*',para):
    frag,i=m.group(1),m.group(2)
    row=R.get(i,"")
    parts=[p.strip(' .,') for p in frag.split('[...]') if p.strip(' .,')]
    for p in parts:
        if p not in row: print("NOT IN ROW",i,"::",p); bad+=1
print("fragments checked:",len(re.findall(r'"[^"]{3,}?"[\s,.;:]*(?:\([^)]*\)\s*)?\*\*\[',para)))
print("em dashes:",t.count('\u2014'))
print("FAIL" if bad else "OK")
