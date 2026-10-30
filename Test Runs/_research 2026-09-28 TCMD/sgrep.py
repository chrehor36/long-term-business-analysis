import sys,re
sys.stdout.reconfigure(encoding='utf-8')
fn=sys.argv[1]; pats=sys.argv[2:]
t=re.sub(r'[\s|]+',' ',open(fn,encoding='utf-8').read())
sents=re.split(r'(?<=[.;])\s+(?=[A-Z(“"])',t)
for p in pats:
    n=0
    for s in sents:
        if re.search(p,s,re.I):
            print('['+p+']',s[:900]); n+=1
            if n>=int(__import__('os').environ.get('N','4')): break
