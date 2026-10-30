import re,sys,glob
sys.stdout.reconfigure(encoding='utf-8')
fs=['cache/k2008_ex13c.txt','cache/k2009_ex13c.txt','cache/k2010_ex13c.txt','cache/k2011_ex13c.txt','cache/k2012_ex13c.txt','cache/k2013_ex13c.txt','cache/k2014_ex13c.txt']+[f'cache/k{y}c.txt' for y in range(2015,2026)]
for f in fs:
    s=re.sub(r'\s+',' ',open(f,encoding='utf-8').read())
    for m in re.finditer(r'[Rr]eported gross margin[^.]*?\d+\.\d\s*%[^.]*?(?:\.\d[^.]*?)*\.',s):
        print(f[6:12], m.group(0)[:300]); break
    for m in re.finditer(r'[Gg]ross profit as a percent of net sales[ \d.%]{0,60}',s):
        print(f[6:12], m.group(0)[:200]); break
