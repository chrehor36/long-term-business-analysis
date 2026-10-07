import re,glob,sys
src=''
for fn in glob.glob('*.txt')+glob.glob('peers/*.txt')+['../_research 2026-09-26 GPC/k25_gpc-20251231.htm.txt']+['../../principle_ledger.csv','../../Framework/THE FRAMEWORK v4.md']:
    t=open(fn,encoding='utf-8',errors='ignore').read()
    t=re.sub(r'\s*\|\s*',' ',t); t=re.sub(r'\s+',' ',t); src+=t+'\n'
def norm(x):
    x=x.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('\ufffd',"'").replace('""','"')
    x=re.sub(r'\s*\|\s*',' ',x)
    return re.sub(r'\s+',' ',x)
srcn=norm(src)
s=open(sys.argv[1],encoding='utf-8').read()
bad=0;n=0
for q in re.findall(r'\*"([^"]*)"\*',s):
    parts=[p.strip() for p in re.split(r'\.\.\.|\[\.\.\.\]|…',q) if p.strip()]
    for p in parts:
        n+=1
        if norm(p) not in srcn:
            bad+=1; print('NOT FOUND:',p[:200])
print('checked',n,'; bad',bad)
