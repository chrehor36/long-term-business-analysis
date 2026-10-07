import re,sys
sys.stdout.reconfigure(encoding='utf-8')
def condense(lines):
    out=[];cur=None
    for l in lines:
        x=l.replace('|',' ').strip()
        if not x: continue
        if re.fullmatch(r'[\d,().\-—$ %]+',x):
            if cur is not None: cur[1].append(x.replace(' ',''))
        else:
            if cur: out.append(cur)
            cur=[x,[]]
    if cur: out.append(cur)
    return ['%-75s %s'%(a[:75],'  '.join(b)) for a,b in out]
if __name__=='__main__':
    L=open(sys.argv[1],encoding='utf-8').read().split('\n')
    for x in condense(L): print(x)
