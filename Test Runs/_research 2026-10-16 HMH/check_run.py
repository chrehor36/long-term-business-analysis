import csv, re, sys
LEDGER=r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv'
RUN=r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-16 Run - HMH HMH Holding.md'
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open(LEDGER,encoding='utf-8-sig'))}
s=open(RUN,encoding='utf-8').read()
bad=0
if re.search(r'\[E\d+-\d+\]',s): print('E-id found'); bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',s)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id',i); bad+=1
norm=lambda t: re.sub(r'\s+',' ',t)
# quoted fragment immediately before **[ID]** (allowing "), ", ", (x) etc. within 4 chars)
for m in re.finditer(r'"([^"]{3,600})"[^"*]{0,6}\*\*\[([MLR]\d{4}-\d{3})\]\*\*',s):
    frag,i=m.group(1),m.group(2)
    if i not in rows: continue
    row=norm(rows[i])
    for part in re.split(r'\s*(?:\.\.\.|\[\.\.\.\])\s*',frag):
        if part and norm(part) not in row:
            print('NOT IN ROW',i,'::',part); bad+=1
print('ids',len(set(ids)),'checked; problems',bad)
