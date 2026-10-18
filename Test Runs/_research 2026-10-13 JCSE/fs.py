import sys,re
f=sys.argv[1]
s=open(f,encoding='utf-8').read()
s=re.sub(r'[ \t]+',' ',s)
t=re.sub(r'\s*\n\s*',' ',s); t=re.sub(r' \| ',' ',t); t=re.sub(r'\s+',' ',t)
for key in ['CONSOLIDATED BALANCE SHEETS \(Amount','CONSOLIDATED STATEMENTS OF (INCOME|OPERATIONS)[A-Z ()]*\(Amount','CONSOLIDATED STATEMENTS OF CASH FLOWS \(Amount']:
    ms=list(re.finditer(key,t))
    if not ms: print('NOT FOUND',key); continue
    m=ms[-1] if len(ms)>0 else None
    m=ms[0]
    print('=====',key); print(t[m.start():m.start()+int(sys.argv[2]) if len(sys.argv)>2 else m.start()+3500]); print()
