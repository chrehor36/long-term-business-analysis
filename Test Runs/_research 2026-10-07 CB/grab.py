import re,sys
def nums_after(lines,i,n=3,maxl=60):
    out=[];j=i
    s=lines[i]
    toks=re.findall(r'\(?-?[\d,]+\.?\d*\)?',s.split('|',1)[1] if '|' in s else '')
    out+=toks
    j=i+1
    while len(out)<n and j<i+maxl:
        if re.match(r'^[A-Za-z]',lines[j].strip()) and not lines[j].strip().startswith('pts'): break
        out+=re.findall(r'\(?-?[\d,]+\.?\d*\)?',lines[j]); j+=1
    return out[:n]
f=sys.argv[1]; sec=sys.argv[2]; labels=sys.argv[3:]
L=open(f,encoding='utf-8').read().split('\n')
for i,l in enumerate(L):
    if l.strip()==sec:
        for k in range(i,min(i+250,len(L))):
            for lab in labels:
                if L[k].strip().startswith(lab):
                    print(k, lab, nums_after(L,k))
        break
