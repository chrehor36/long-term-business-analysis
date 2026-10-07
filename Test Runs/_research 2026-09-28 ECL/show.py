import sys, re
def clean(path):
    s=open(path,encoding='utf-8').read().replace('\u200b','').replace('\xa0',' ')
    out=[]
    for ln in s.split('\n'):
        t=ln.strip()
        if re.fullmatch(r'[|\s]*',t): continue
        out.append(t)
    s='\n'.join(out)
    # join table fragments: lines starting with '|' appended to previous
    s=re.sub(r'\n\|\s*',' | ',s)
    return s
if __name__=='__main__':
    s=clean(sys.argv[1])
    if len(sys.argv)>2:
        a,b=int(sys.argv[2]),int(sys.argv[3]); print('\n'.join(s.split('\n')[a:b]))
    else: print(s)
