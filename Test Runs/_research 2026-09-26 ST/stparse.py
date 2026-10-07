import re, json, sys
def nums(t, k=3):
    t=t.replace('$','').replace('—','0').replace('—','0').replace('�','0').replace('–','0')
    toks=re.findall(r'\(\s*[\d,]+\.?\d*\s*\)|-?[\d,]+\.\d+|-?[\d,]{1,9}(?=\s*\|)|(?<=\|)\s*0\s*(?=\|)',t)
    out=[]
    for x in toks:
        x=x.strip(); neg=x.startswith('(')
        v=float(x.strip('() ').replace(',','')) if x.strip('() ') else 0.0
        out.append(-v if neg else v)
        if len(out)==k: break
    return out
def section(s, head, nxt, occ=None):
    idx=[m.start() for m in re.finditer(head,s)]
    best=None
    for i in idx:
        j=s.find(nxt,i+50)
        seg=s[i:j if j>0 else i+20000]
        if re.search(r'\d{2,3}\.\d',seg[:3000]) and len(seg)<40000:
            best=seg
    return best
def grab(seg, label, k=3):
    m=re.search(label, seg)
    if not m: return None
    return nums(seg[m.end():m.end()+250], k)
if __name__=='__main__':
    fy=sys.argv[1]
    s=open(f'10-K_FY{fy}.txt',encoding='utf-8').read()
    cf=section(s,r'(?i)Consolidated Statements of Cash Flows',r'(?i)Consolidated Statements of (Changes in )?(Shareholders|Stockholders)')
    print(cf[:6000] if cf else 'NONE')
