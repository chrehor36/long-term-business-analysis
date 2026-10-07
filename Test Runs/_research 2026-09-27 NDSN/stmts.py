import re,sys,glob
def block(f, head, n=4500):
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'\s+',' ',s); s=re.sub(r'(\| )+','| ',s)
    out=[]
    for m in re.finditer(head, s):
        seg=s[m.start():m.start()+n]
        if re.search(r'\d{3},\d{3}', seg[:1500]): out.append(seg)
    return out
f=sys.argv[1]; head=sys.argv[2]; n=int(sys.argv[3]) if len(sys.argv)>3 else 4500
b=block('filings/'+f, head, n)
print(len(b)); print(b[0] if b else 'none')
