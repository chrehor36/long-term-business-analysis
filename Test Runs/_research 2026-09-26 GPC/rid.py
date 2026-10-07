import csv,re,sys
ids={r['﻿id'] for r in csv.DictReader(open('principle_ledger.csv',encoding='utf-8'))}
s=open(sys.argv[1],encoding='utf-8').read()
found=sorted(set(re.findall(r'E\d-\d\d',s)))
print(len(found),'ids cited; missing:',[x for x in found if x not in ids])
