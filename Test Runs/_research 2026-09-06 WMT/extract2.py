import os,re,json
D=os.path.dirname(os.path.abspath(__file__))
order=['q4fy18','q1fy19','q2fy19','q3fy19','q4fy19','q1fy20','q2fy20','q3fy20','q4fy20',
'q1fy21','q2fy21','q3fy21','q4fy21','q1fy22','q2fy22','q3fy22','q4fy22','q1fy23','q2fy23',
'q3fy23','q4fy23','q1fy24','q2fy24','q3fy24','q4fy24','q1fy25','q2fy25','q3fy25','q4fy25',
'q1fy26','q2fy26','q3fy26','q4fy26','q1fy27','q2fy27']
VAL=re.compile(r'^(NP|N/?A|flat|--|~?\(?-?[\d.]+\)?\s*%?|[<>~]\s*\(?-?[\d.]+\)?\s*(%|bps)?|~?\(?-?[\d.]+\)?\s*bps)$', re.I)
def cells(l): return [c.strip() for c in l.split('|') if c.strip()]
def grab(lines,i):
    c=cells(lines[i])
    v=[x for x in c[1:] if VAL.match(x)]
    if len(v)>=2: return v
    v=[]
    for j in range(i+1, min(i+14,len(lines))):
        c2=cells(lines[j])
        if not c2: continue
        if len(c2)>=2 and all(VAL.match(x) for x in c2): return c2
        if len(c2)==1 and VAL.match(c2[0]): v.append(c2[0]); continue
        break
    return v
LBL=r'^\|?\s*%s\s*[\d,]*\s*(\||$)'
out={}
for q in order:
    lines=open(os.path.join(D,f"8k-{q}-ex991.txt"),encoding='utf-8',errors='replace').read().split('\n')
    blocks=[]
    for i,l in enumerate(lines):
        s=l.strip()
        if not re.match(LBL % r'(Transactions|Traffic)', s, re.I): continue
        comp=None; ns=None; hdr=None
        for j in range(i-1, max(-1,i-40), -1):
            sj=lines[j].strip()
            if comp is None and re.match(r'^\|?\s*Comp(arable)? [Ss]ales \(ex\. fuel\)', sj, re.I): comp=grab(lines,j)
            if ns is None and re.match(LBL % r'Net sales', sj, re.I): ns=grab(lines,j)
            if hdr is None and re.search(r"(Walmart U\.?S\.?|Sam.{0,3}s Club|^\|?\s*U\.S\.)", sj): hdr=sj[:50]
            if comp and ns and hdr: break
        tk=None; ec=None
        for j in range(i+1, min(i+30,len(lines))):
            sj=lines[j].strip()
            if tk is None and re.match(LBL % r'(Average [Tt]icket|Ticket)', sj, re.I): tk=grab(lines,j)
            if ec is None and re.match(r'^\|?\s*eCommerce( contribution.*)?\s*[\d,]*\s*(\||$)', sj, re.I): ec=grab(lines,j)
            if tk and ec: break
        blocks.append({'hdr':hdr,'ns':ns,'comp':comp,'tran':grab(lines,i),'tick':tk,'ecom':ec})
    out[q]=blocks
    print("="*70); print(q, len(blocks),"blocks")
    for b in blocks:
        print(f"  hdr={b['hdr']}\n   NS  {b['ns']}\n   COMP{b['comp']}\n   TRAN{b['tran']}\n   TICK{b['tick']}\n   ECOM{b['ecom']}")
json.dump(out,open(os.path.join(D,'extract.json'),'w'),indent=1)
