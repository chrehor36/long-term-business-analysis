import re, sys
sys.stdout.reconfigure(encoding='utf-8')
files={'2008':'cache/k2008_ex13c.txt','2009':'cache/k2009_ex13c.txt','2010':'cache/k2010_ex13c.txt','2011':'cache/k2011_ex13c.txt','2012':'cache/k2012_ex13c.txt','2013':'cache/k2013_ex13c.txt','2014':'cache/k2014_ex13c.txt'}
for y in range(2015,2026): files[str(y)]=f'cache/k{y}c.txt'
files['Q2-2026']='cache/q2606c.txt'
for y,f in files.items():
    L=open(f,encoding='utf-8').read().split('\n')
    for i,l in enumerate(L):
        if re.match(r'^Price changes',l.strip()):
            # find a segment heading in prior 25 lines
            ctx=' '.join(x.strip() for x in L[max(0,i-25):i+4])
            ctx=re.sub(r'\s+',' ',ctx)
            print(y,i,'...',ctx[-420:]); print()
