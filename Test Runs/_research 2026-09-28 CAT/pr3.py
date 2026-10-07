import re,sys
sys.stdout.reconfigure(encoding='utf-8')
def doc(y):
    f=f'cache/x13_{y}.txt' if y<=2014 else f'cache/k_{y}.txt'
    return open(f,encoding='utf-8').read()
bad=re.compile(r'quarter|Construction|Resource|Energy|Power|Machinery|Engine|North America|EAME|Latin|Asia|Europe|Transportation|Mining|Industries|Financial Products Segment|Cat Financial|segment|Rail',re.I)
for y in range(2001,2026):
    t=re.sub(r'\s+',' ',doc(y))
    sents=re.split(r'(?<=[a-z%)])\. (?=[A-Z•])',t)
    print('=====',y)
    seen=set()
    for s in sents:
        if re.search(r'price realization',s,re.I) and re.search(r'\$\s?[\d.,]+ (million|billion)',s) and not bad.search(s) and str(y) in s:
            k=s[:100]
            if k in seen: continue
            seen.add(k); print(' -',s[:500])
