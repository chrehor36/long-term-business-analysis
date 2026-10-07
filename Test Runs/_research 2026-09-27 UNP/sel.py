import re
def nums_after(lines,i,n,maxl=80):
    out=[]
    for l in lines[i+1:i+maxl]:
        for t in re.findall(r'\(?-?[\d,]+\.?\d*\)?',l):
            t2=t.replace(',','').strip('()')
            if t2 and t2.replace('.','').isdigit():
                v=float(t2); out.append(-v if t.startswith('(') else v)
        if len(out)>=n: break
    return out[:n]
for y in (2004,2009,2014,2019):
    L=open(f'tenk_{y}.txt',encoding='utf-8').read().split('\n')
    print('==',y)
    for lab in ('Freight revenues','Revenue carloads','Operating ratio (%)','Return on average common','Operating revenues','Average employees','Includes fuel surcharge'):
        for i,l in enumerate(L):
            if l.strip().startswith(lab) or (lab.startswith('Includes') and lab in l):
                if lab.startswith('Includes'):
                    print(lab, l.strip()[:400]); break
                print(lab, nums_after(L,i-1 if False else i,5)); break
