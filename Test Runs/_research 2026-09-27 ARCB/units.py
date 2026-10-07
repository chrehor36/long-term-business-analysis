import re,sys,glob
sys.stdout.reconfigure(encoding='utf-8')
files=sorted(glob.glob('cache/tenk_20*.txt'))+['cache/ex05_d33393exv13.htm.txt','cache/ex03_d13042exv13.txt.txt']
for f in files:
    s=open(f,encoding='utf-8').read().replace('​',' ')
    s=re.sub(r'\s*\|\s*',' ',s); s=re.sub(r'\s+',' ',s)
    out=[]
    for pat in [r'Tonnage per day[^A-Za-z]{0,160}', r'Billed revenue per hundredweight, including fuel surcharges[^A-Za-z]{0,160}', r'OPERATING REVENUES ABF \$[^A-Za-z]{0,80}',r'ABF \$ [\d,]+ \$ [\d,]+ \$ [\d,]+']:
        m=re.search(pat,s)
        if m: out.append(m.group(0)[:200])
    import os; print(os.path.basename(f), ' || '.join(out))
