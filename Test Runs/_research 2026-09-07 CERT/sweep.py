import re,sys
sys.stdout.reconfigure(encoding='utf-8',errors='replace')
def load(fn):
    t=open(fn,encoding='utf-8').read()
    return re.sub(r'\s+',' ',t)
def show(fn,pats,w=800,b=350,limit=3):
    t=load(fn)
    print('='*70); print('FILE',fn,'len',len(t))
    for pat in pats:
        ms=list(re.finditer(pat,t,re.I))
        print(f'--- /{pat}/  hits={len(ms)}')
        for m in ms[:limit]:
            print('   >',t[max(0,m.start()-b):m.start()+w].strip()); print()
