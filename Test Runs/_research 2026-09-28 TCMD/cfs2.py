import re,glob,sys
sys.stdout.reconfigure(encoding='utf-8')
for fn in sorted(glob.glob('cache/K2_*.txt'))+['cache/Q2_2026-06-30.txt']:
    L=open(fn,encoding='utf-8').read().split('\n')
    hits=[i for i,l in enumerate(L) if re.search(r'(?i)cash flows? from operating activities',l)]
    for i in hits:
        blk=L[i:i+90]
        if any(re.search(r'(?i)depreciation',x) for x in blk[:15]):
            print('=====',fn); s=max(0,i-4)
            for x in L[s:i+95]:
                print(x)
                if re.search(r'(?i)cash paid for interest|non-?cash investing',x): break
            break
