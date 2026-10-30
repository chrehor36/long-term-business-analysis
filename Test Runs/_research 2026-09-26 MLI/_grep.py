import re,sys
fn=sys.argv[1]; pat=sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 250; n=int(sys.argv[4]) if len(sys.argv)>4 else 6
t=open(fn,encoding='utf-8',errors='replace').read()
t=re.sub(r'\s+',' ',t.replace('\xa0',' '))
for i,m in enumerate(re.finditer(pat,t,re.I)):
    if i>=n: break
    print('--',t[max(0,m.start()-w):m.end()+w]); print()
