import re,glob,sys
src=''
for fn in glob.glob('*.txt')+glob.glob('peers/*.txt'):
    t=open(fn,encoding='utf-8',errors='ignore').read()
    t=re.sub(r'\s*\|\s*',' ',t); t=re.sub(r'\s+',' ',t); src+=t+'\n'
def norm(x): return re.sub(r'\s+',' ',x.replace('’',"'").replace('“','"').replace('”','"').replace('�',"'"))
srcn=norm(src)
s=open(sys.argv[1],encoding='utf-8').read()
bad=0
for q in re.findall(r'\*"([^"]*)"\*',s):
    parts=[p.strip() for p in re.split(r'\.\.\.|\[\.\.\.\]',q) if p.strip()]
    for p in parts:
        pn=norm(p)
        if pn not in srcn:
            bad+=1; print('NOT FOUND:',p[:160])
print('checked; bad',bad)
