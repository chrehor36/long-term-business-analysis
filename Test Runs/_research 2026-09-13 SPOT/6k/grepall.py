import sys, io, re, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
pat=re.compile(sys.argv[1]); b=int(sys.argv[2]); a=int(sys.argv[3]); globp=sys.argv[4] if len(sys.argv)>4 else 'R_*.txt'
for fn in sorted(glob.glob(globp)):
    t=open(fn,encoding='utf-8').read(); t=re.sub(r'\s+',' ',t)
    last=-10**9
    for m in pat.finditer(t):
        if m.start()-last < a: continue
        last=m.start()
        print(f'[{fn[:12]}] ...'+t[max(0,m.start()-b):m.end()+a]+'...')
