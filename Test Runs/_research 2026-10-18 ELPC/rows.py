import sys,re
f,start,n=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
L=open(f,encoding='utf-8').read().split('\n')[start-1:start-1+n]
num=re.compile(r'^\(?-?[\d.,]+\)?$|^-$|^—$')
rows=[];cur=[];nums=[]
for l in L:
    s=l.strip().strip('|').strip()
    if not s or 'TABLE OF CONTENTS' in s or 'COPEL and Sub' in s or 'COMPANHIA PARANAENSE' in s: continue
    if num.match(s) and not re.match(r'^\d{1,2}(\.\d+)*$',s):
        nums.append(s)
    elif re.match(r'^\d{1,2}(\.\d+)*$',s) or re.match(r'^\d+\.\d+ and \d',s) or s.startswith('and '):
        continue
    else:
        if nums:
            rows.append((' '.join(cur),nums)); cur=[];nums=[]
        cur.append(s)
if cur or nums: rows.append((' '.join(cur),nums))
sys.stdout.reconfigure(encoding='utf-8')
for a,b in rows: print(f"{a[:90]:90} | {' | '.join(b)}")
