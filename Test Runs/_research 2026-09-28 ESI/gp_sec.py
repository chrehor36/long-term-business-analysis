import re, sys
sys.stdout.reconfigure(encoding='utf-8')
for y in range(2016, 2026):
    L=open(f'cache/t{y}.txt',encoding='utf-8').read().split('\n')
    print('#########', y)
    for i,l in enumerate(L):
        if re.match(r'^\s*Gross Profit\s*$', l):
            for k in L[i+1:i+16]:
                if re.search(r'Operating Expenses|Selling, Technical', k): break
                print('   ', k.strip()[:1200])
            print('   ---')
