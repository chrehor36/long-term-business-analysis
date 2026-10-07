import sys,re
pat=re.compile(sys.argv[1],re.I); w=int(sys.argv[2]); files=sys.argv[3:]
for f in files:
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'[​\xa0|]',' ',t); t=re.sub(r'\s+',' ',t)
    print('=====',f)
    n=0
    for m in pat.finditer(t):
        print('  ...',t[max(0,m.start()-w//4):m.end()+w]); n+=1
        if n>=int(__import__('os').environ.get('MAXN','6')): break
