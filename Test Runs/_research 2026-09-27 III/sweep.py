import glob,re,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
pats=[r'pricing pressure',r'price increase',r'increase[sd]? (in )?(our )?(billing )?rates',r'rate increase',r'pressure on (our )?(pricing|rates|fees)',r'reduced pricing',r'lower (average )?(billing )?rates',r'higher (average )?(billing )?rates',r'limited barriers to entry',r'similar services to us',r'fee pressure',r'discount',r'realized rate',r'bill rate',r'price competition',r'competitive pricing']
out=open('pricing_hits.txt','w',encoding='utf-8')
for f in sorted(glob.glob('flat/*10-K*.txt'))+sorted(glob.glob('flat/*10-Q*.txt'))+sorted(glob.glob('flat/*ex99*.txt')):
    s=open(f,encoding='utf-8').read()
    seen=set()
    for p in pats:
        for m in re.finditer(p,s,re.I):
            a=max(0,m.start()-250); b=min(len(s),m.end()+250)
            snip=re.sub(r'\s+',' ',s[a:b])
            key=snip[200:320]
            if key in seen: continue
            seen.add(key)
            out.write(f'{f[5:40]} [{p}] ...{snip}...\n')
out.close()
