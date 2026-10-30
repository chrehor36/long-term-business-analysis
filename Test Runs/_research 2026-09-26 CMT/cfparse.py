import re, json, sys
def parse(fn):
    s=open(fn,encoding='utf-8').read()
    i=[m.start() for m in re.finditer(r'(?i)cash flows? (from|provided by)[^\n]{0,20}operating activities:',s)]
    # choose the occurrence that is followed within 400 chars by 'Net income'
    st=None
    for k in i:
        if re.search(r'(?i)net (income|loss|earnings)',s[k:k+600]): st=k;break
    en=s.find('end of',st); en=s.find('\n',en+200)
    seg=s[st:en]
    toks=[t.strip() for t in re.split(r'[|\n]',seg)]
    rows=[];cur=None;neg=False
    for t in toks:
        if not t or t in ('$',')','$ ('): 
            continue
        t2=t.replace('$','').strip()
        m=re.fullmatch(r'\(?\s*([\d,]+)\s*\)?',t2)
        if m and cur is not None and re.search(r'\d',t2):
            v=int(m.group(1).replace(',',''))
            if t2.startswith('('): v=-v
            cur[1].append(v)
        elif t2 in ('—','-','–'):
            if cur is not None: cur[1].append(0)
        elif re.search(r'[A-Za-z]',t2):
            if cur and not cur[1] and len(cur[0])<200: cur=(cur[0]+' '+t2,cur[1]); rows[-1]=cur
            else:
                cur=(t2,[]); rows.append(cur)
    return rows
if __name__=='__main__':
    for fy in sys.argv[1:]:
        print('=====',fy)
        for l,v in parse(f'tenk_{fy}.txt'): 
            if v: print(f'{l[:70]:70s}',v)
