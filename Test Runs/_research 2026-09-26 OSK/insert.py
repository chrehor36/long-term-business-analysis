import re,sys,glob
p='../2026-09-26 Run - OSK Oshkosh.md'
t=open(p,encoding='utf-8').read()
s=open(sys.argv[1],encoding='utf-8').read()
src=''
for fn in glob.glob('*.txt')+glob.glob('peers/*.txt'):
    x=open(fn,encoding='utf-8',errors='ignore').read(); x=re.sub(r'\s*\|\s*',' ',x); src+=re.sub(r'\s+',' ',x)+'\n'
src+=re.sub(r'\s+',' ',open('../../principle_ledger.csv',encoding='utf-8-sig').read()+open('../../Framework/THE FRAMEWORK v4.md',encoding='utf-8').read())
def fix(m):
    q=m.group(1)
    if "'" not in q: return m.group(0)
    parts=[x for x in re.split(r'\.\.\.|\[\.\.\.\]',q)]
    out=[]
    for part in parts:
        if "'" in part and re.sub(r'\s+',' ',part.strip()) not in src:
            part=part.replace("'","’")
        out.append(part)
    return '*"'+'...'.join(out)+'"*'
s=re.sub(r'\*"([^"]*)"\*',fix,s)
start,end=sys.argv[2],sys.argv[3]
a=t.index(start); b=len(t) if end=="__EOF__" else t.index(end)
t=t[:a]+s.rstrip('\n')+'\n\n'+t[b:]
if len(sys.argv)>4: t=t.replace(sys.argv[4],sys.argv[5],1)
open(p,'w',encoding='utf-8').write(t)
print('ok')
