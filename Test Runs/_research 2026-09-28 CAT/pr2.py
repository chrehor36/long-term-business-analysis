import re,sys
sys.stdout.reconfigure(encoding='utf-8')
def doc(y):
    f=f'cache/x13_{y}.txt' if y<=2014 else f'cache/k_{y}.txt'
    return open(f,encoding='utf-8').read()
for y in range(2001,2026):
    t=re.sub(r'\s+',' ',doc(y))
    sents=re.split(r'(?<=[a-z%)])\. (?=[A-Z•])',t)
    print('=====',y)
    seen=set()
    for s in sents:
        if re.search(r'price realization|price increases|pricing',s,re.I) and re.search(r'\$\s?[\d.,]+ (million|billion)',s) and re.search(r'(sales and revenues|operating profit|sales volume)',s,re.I) and 'quarter' not in s.lower():
            k=s[:120]
            if k in seen: continue
            seen.add(k); print(' -',s[:600])
