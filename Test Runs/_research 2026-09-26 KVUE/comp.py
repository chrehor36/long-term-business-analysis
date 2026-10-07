import re,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
for fn in ['ipo424b4_2023.txt','tenk_2023.txt','tenk_2024.txt','tenk_2025.txt','q2606_kvue-20260628.htm.txt']:
    s=re.sub(r'\s+',' ',open(fn,encoding='utf-8').read())
    print('=====',fn)
    seen=set()
    for m in re.finditer(r'(Operational|Organic) sales(?: \(a non-GAAP[^)]*\))? (increased|decreased|grew|declined)',s):
        t=s[max(0,m.start()-250):m.start()+450]
        k=s[m.start():m.start()+120]
        if k in seen: continue
        seen.add(k); print('-',t,'\n')
