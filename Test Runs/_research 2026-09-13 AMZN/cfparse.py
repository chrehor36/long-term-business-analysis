# cfparse.py FILE START END : join multi-line table cells into "label: n1 n2 n3" rows (read-only helper)
import re,sys
f,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
L=open(f,encoding='utf-8',errors='replace').read().split('\n')[a-1:b]
rows=[];cur=None
for l in L:
    s=l.replace('|',' ').strip()
    if not s or s in ('$',')'): continue
    if re.fullmatch(r'\(?[\d,]+\)?|\(?[\d,]+|—|-',s):
        if cur is not None: cur[1].append(s)
    else:
        cur=[s,[]]; rows.append(cur)
for lab,nums in rows:
    if nums: print(lab[:110],':',' '.join(nums))
