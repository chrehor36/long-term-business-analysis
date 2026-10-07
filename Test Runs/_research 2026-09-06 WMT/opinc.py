import os,re,json
D=os.path.dirname(os.path.abspath(__file__))
QS=['q1fy22','q2fy22','q3fy22','q4fy22','q1fy23','q2fy23','q3fy23','q4fy23','q1fy24','q2fy24',
'q3fy24','q4fy24','q1fy25','q2fy25','q3fy25','q4fy25','q1fy26','q2fy26','q3fy26','q4fy26','q1fy27','q2fy27']
VAL=re.compile(r'^(NP|N/?A|flat|--|\(?\$?[+-]?[\d.,]+\)?\s*(%|bps)?|[<>~]\s*.*)$')
def cells(l): return [c.strip() for c in l.split('|') if c.strip()]
def grab(lines,i):
    c=cells(lines[i]); v=[x for x in c[1:] if VAL.match(x)]
    if len(v)>=3: return v
    v=[]
    for j in range(i+1,min(i+12,len(lines))):
        c2=cells(lines[j])
        if not c2: continue
        if len(c2)>=3 and all(VAL.match(x) for x in c2): return c2
        if len(c2)==1 and VAL.match(c2[0]): v.append(c2[0]); continue
        break
    return v
for q in QS:
    lines=open(os.path.join(D,f"8k-{q}-ex991.txt"),encoding='utf-8',errors='replace').read().split('\n')
    tr=[i for i,l in enumerate(lines) if re.match(r'^\|?\s*Transactions\s*[\d,]*\s*(\||$)', l.strip(), re.I)]
    res=[]
    for k in tr[:2]:
        oi=None
        for j in range(k+1,min(k+25,len(lines))):
            if re.match(r'^\|?\s*Operating income\s*[\d,]*\s*(\||$)', lines[j].strip(), re.I):
                oi=grab(lines,j); break
        res.append(oi)
    print(f"{q}: WMT-US OI {res[0] if res else None}  ||  SAMS-US OI {res[1] if len(res)>1 else None}")
