import re,sys,glob,os
sys.stdout.reconfigure(encoding='utf-8')
pat=re.compile(sys.argv[1], re.I)
ctx=int(sys.argv[2]) if len(sys.argv)>2 else 250
files=sys.argv[3:] or sorted(glob.glob('cache/k[12]*.txt'))
excl=re.compile(r'black-scholes|option[- ]pricing|pricing model|transfer pricing|stock price|pricing of these investments|valuation', re.I)
for f in files:
    t=re.sub(r'\s+',' ',open(f,encoding='utf-8',errors='ignore').read())
    seen=set()
    for m in pat.finditer(t):
        s=t[max(0,m.start()-ctx):m.end()+ctx]
        if excl.search(s[ctx-60:ctx+60+len(m.group(0))]): continue
        k=s[ctx-40:ctx+40]
        if k in seen: continue
        seen.add(k); print(os.path.basename(f)[1:5] if 'k' in os.path.basename(f) else f, '::', s); print()
