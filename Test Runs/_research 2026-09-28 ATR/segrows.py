import re,sys
sys.stdout.reconfigure(encoding='utf-8')
t=open('segx_out.txt',encoding='utf-8').read().replace('​',' ')
t=re.sub(r' +',' ',t)
bl=re.split(r'===== (\d{4}) line \d+\n',t)[1:]
for k in range(0,len(bl),2):
    y,b=bl[k],bl[k+1]
    if int(y)<2014: continue
    for h in ['Segment Income','Adjusted EBITDA (1):','Adjusted EBITDA:','Adjusted EBITDA (1) :','Total Assets']:
        for m in re.finditer(re.escape(h),b):
            s=b[m.start():m.start()+300]
            if 'Pharma' in s: print(y,'|',s[:300]); break
