import re,sys
def sents(t):
    t=re.sub(r'\s+',' ',t)
    return re.split(r'(?<=[a-z%\)”"])\.\s+(?=[A-Z“"(•])',t)
if __name__=='__main__':
    f=sys.argv[1]; pat=re.compile(sys.argv[2],re.I); n=int(sys.argv[3]) if len(sys.argv)>3 else 40
    k=0
    for s in sents(open(f,encoding='utf-8').read()):
        if pat.search(s):
            print('-',s[:900]); k+=1
            if k>=n: break
