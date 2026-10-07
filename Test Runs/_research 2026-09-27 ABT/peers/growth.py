import re,glob,sys
sys.stdout.reconfigure(encoding='utf-8')
files=sorted(glob.glob('*_row.txt'))+sorted(glob.glob('../../_research 2026-09-26 MDT/peers/*_row.txt'))
for f in files:
    t=open(f,encoding='utf-8').read()
    m=re.search(r'sales series: (.*)',t)
    if not m: continue
    s={k[:4]:float(v.replace(',','')) for k,v in re.findall(r'(\d{4}-\d\d-\d\d):([\d,]+)',m.group(1))}
    ys=sorted(s); last=ys[-1]
    def g(n):
        a=str(int(last)-n)
        return f"{(s[last]/s[a])**(1/n)-1:.1%}" if a in s else 'n/f'
    print(f.split('/')[-1].replace('_row.txt',''), last, 'sales', s[last], '9y', g(9), '5y', g(5))
