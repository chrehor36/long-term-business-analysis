import sys,re
fn=sys.argv[1]; pat=sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 1200
t=open(fn,encoding='utf-8').read()
t=re.sub(r'\s+',' ',t)
for m in re.finditer(pat,t,re.I):
    print('=== @%d ==='%m.start())
    print(t[max(0,m.start()-w//3):m.start()+w])
    print()
