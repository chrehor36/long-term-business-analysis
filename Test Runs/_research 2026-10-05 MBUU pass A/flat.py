import re,sys
def flat(f,pat,n=9000,occ=-1,skip=0):
    t=open(f,encoding='utf-8').read()
    idx=[m.start() for m in re.finditer(pat,t)]
    if not idx: return 'NOT FOUND '+pat
    i=idx[occ]
    s=t[i+skip:i+skip+n*3]; s=re.sub(r'\s*\|\s*',' | ',s); s=re.sub(r'(\|\s*)+','| ',s); s=re.sub(r'\s+',' ',s)
    return s[:n]
if __name__=='__main__':
    f,pat=sys.argv[1],sys.argv[2]; n=int(sys.argv[3]) if len(sys.argv)>3 else 9000; occ=int(sys.argv[4]) if len(sys.argv)>4 else -1
    sys.stdout.buffer.write(flat(f,pat,n,occ).encode()+b'\n')
