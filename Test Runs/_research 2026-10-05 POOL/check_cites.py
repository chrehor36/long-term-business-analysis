import csv,re,sys
rows={x['﻿id']:x['quote_verbatim'] for x in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8'))}
txt=open(sys.argv[1],encoding='utf-8').read()
bad=0
if re.search(r'\[E\d',txt): print('E-id found'); bad+=1
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',txt)
for i in set(ids):
    if i not in rows: print('MISSING',i); bad+=1
norm=lambda s: re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('�',"'"))
# paragraph-level: each quoted fragment in a sentence ending with an id must be in that id's row
paras=re.split(r'\n(?=\s*[-|*#]|\s*\n)',txt)
for p in paras:
    for m in re.finditer(r'"([^"]+)"((?:[^"]{0,25}?)\*\*\[([MLR]\d{4}-\d{3})\]\*\*)',p):
        frag,i=m.group(1),m.group(3)
        if i not in rows: continue
        for part in frag.split('[...]'):
            part=part.strip().rstrip('.,;')
            if part and norm(part) not in norm(rows[i]):
                print('NOT IN ROW',i,'::',part); bad+=1
print('ids',len(set(ids)),'problems',bad)
