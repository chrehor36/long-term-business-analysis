import re,sys,os
sys.stdout.reconfigure(encoding='utf-8')
def doc(y):
    f=f'cache/x13_{y}.txt' if y<=2014 else f'cache/k_{y}.txt'
    return open(f,encoding='utf-8').read()
for y in range(2001,2026):
    t=doc(y)
    t1=re.sub(r'\s+',' ',t)
    pats=[rf'(?:Total s|S)ales and revenues for {y} were[^.]*\.[^.]*\.[^.]*\.', rf'(?:Total s|S)ales and revenues (?:for|in) {y}[^.]*\.[^.]*\.[^.]*\.']
    m=None
    for p in pats:
        m=re.search(p,t1)
        if m: break
    print('=====',y)
    print(m.group(0)[:900] if m else 'NO MATCH')
    m2=re.search(rf'Operating profit (?:for|in|was)[^.]*{y}[^.]*\.[^.]*\.[^.]*\.',t1)
    print('  OP:', m2.group(0)[:700] if m2 else 'NO OP MATCH')
