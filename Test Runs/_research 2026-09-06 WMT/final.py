import os,re,json
D=os.path.dirname(os.path.abspath(__file__))
QS=['q1fy17','q2fy17','q3fy17','q4fy17','q1fy18','q2fy18','q3fy18','q4fy18','q1fy19','q2fy19',
'q3fy19','q4fy19','q1fy20','q2fy20','q3fy20','q4fy20','q1fy21','q2fy21','q3fy21','q4fy21',
'q1fy22','q2fy22','q3fy22','q4fy22','q1fy23','q2fy23','q3fy23','q4fy23','q1fy24','q2fy24',
'q3fy24','q4fy24','q1fy25','q2fy25','q3fy25','q4fy25','q1fy26','q2fy26','q3fy26','q4fy26',
'q1fy27','q2fy27']
ACC={'q1fy17':('0000104169-16-000083','2016-05-19'),'q2fy17':('0000104169-16-000116','2016-08-18'),
'q3fy17':('0000104169-16-000134','2016-11-17'),'q4fy17':('0000104169-17-000013','2017-02-21'),
'q1fy18':('0000104169-17-000025','2017-05-18'),'q2fy18':('0000104169-17-000052','2017-08-17'),
'q3fy18':('0000104169-17-000075','2017-11-16'),'q4fy18':('0000104169-18-000020','2018-02-20'),
'q1fy19':('0000104169-18-000047','2018-05-17'),'q2fy19':('0000104169-18-000081','2018-08-16'),
'q3fy19':('0000104169-18-000103','2018-11-15'),'q4fy19':('0000104169-19-000011','2019-02-19'),
'q1fy20':('0000104169-19-000021','2019-05-16'),'q2fy20':('0000104169-19-000058','2019-08-15'),
'q3fy20':('0000104169-19-000081','2019-11-14'),'q4fy20':('0000104169-20-000007','2020-02-18'),
'q1fy21':('0000104169-20-000016','2020-05-19'),'q2fy21':('0000104169-20-000037','2020-08-18'),
'q3fy21':('0000104169-20-000073','2020-11-17'),'q4fy21':('0000104169-21-000022','2021-02-18'),
'q1fy22':('0000104169-21-000037','2021-05-18'),'q2fy22':('0000104169-21-000054','2021-08-17'),
'q3fy22':('0000104169-21-000063','2021-11-16'),'q4fy22':('0000104169-22-000009','2022-02-17'),
'q1fy23':('0000104169-22-000024','2022-05-17'),'q2fy23':('0000104169-22-000065','2022-08-16'),
'q3fy23':('0000104169-22-000077','2022-11-15'),'q4fy23':('0000104169-23-000010','2023-02-21'),
'q1fy24':('0000104169-23-000043','2023-05-18'),'q2fy24':('0000104169-23-000088','2023-08-17'),
'q3fy24':('0000104169-23-000124','2023-11-16'),'q4fy24':('0000104169-24-000019','2024-02-20'),
'q1fy25':('0000104169-24-000088','2024-05-16'),'q2fy25':('0000104169-24-000131','2024-08-15'),
'q3fy25':('0000104169-24-000170','2024-11-19'),'q4fy25':('0000104169-25-000010','2025-02-20'),
'q1fy26':('0000104169-25-000069','2025-05-15'),'q2fy26':('0000104169-25-000120','2025-08-21'),
'q3fy26':('0000104169-25-000177','2025-11-20'),'q4fy26':('0000104169-26-000032','2026-02-19'),
'q1fy27':('0000104169-26-000095','2026-05-21'),'q2fy27':('0000104169-26-000145','2026-08-20')}
VAL=re.compile(r'^(NP|N/?A|flat|--|[<>~]?\s*\(?[+-]?[\d.]+\)?\s*(%|bps)?)$', re.I)
def cells(l): return [c.strip() for c in l.split('|') if c.strip()]
def grab(lines,i):
    c=cells(lines[i]); v=[x for x in c[1:] if VAL.match(x)]
    if len(v)>=2: return v
    v=[]
    for j in range(i+1,min(i+14,len(lines))):
        c2=cells(lines[j])
        if not c2: continue
        if len(c2)>=2 and all(VAL.match(x) for x in c2): return c2
        if len(c2)==1 and VAL.match(c2[0]): v.append(c2[0]); continue
        break
    return v
L=r'^\|?\s*%s\s*[\d,]*\s*(\||$)'
rows={}
for q in QS:
    lines=open(os.path.join(D,f"8k-{q}-ex991.txt"),encoding='utf-8',errors='replace').read().split('\n')
    blocks=[]
    for i,l in enumerate(lines):
        s=l.strip()
        if not re.match(L % r'(Transactions|Traffic)', s, re.I): continue
        comp=None; ns=None
        for j in range(i-1,max(-1,i-40),-1):
            sj=lines[j].strip()
            if comp is None and re.match(r'^\|?\s*Comp(arable)? [Ss]ales( \(ex\. fuel\))?\s*[\d,]*\s*(\||$)', sj, re.I): comp=grab(lines,j)
            if ns is None and re.match(L % r'Net [Ss]ales', sj, re.I): ns=grab(lines,j)
            if comp and ns: break
        tk=None; ec=None
        for j in range(i+1,min(i+30,len(lines))):
            sj=lines[j].strip()
            if tk is None and re.match(L % r'(Average [Tt]icket|Ticket)', sj, re.I): tk=grab(lines,j)
            if ec is None and re.match(r'^\|?\s*(eCommerce|E-commerce)( contribution.*)?\s*[\d,]*\s*(\||$)', sj, re.I): ec=grab(lines,j)
            if tk and ec: break
        blocks.append({'ns':ns,'comp':comp,'tran':grab(lines,i),'tick':tk,'ecom':ec})
    rows[q]=blocks
json.dump(rows,open(os.path.join(D,'final.json'),'w'),indent=1)
def g(b,k,n=0):
    v=b.get(k)
    return v[n] if v and len(v)>n else '--'
print("QTR    | seg | netsales | comp | tran | tick | ecom || prior-yr: comp/tran/tick/ecom")
for q in QS:
    for n,b in enumerate(rows[q][:2]):
        seg='WMT-US' if n==0 else 'SAMS-US'
        print(f"{q:7}|{seg:8}|{g(b,'ns'):9}|{g(b,'comp'):7}|{g(b,'tran'):7}|{g(b,'tick'):7}|{g(b,'ecom'):10}|| {g(b,'comp',1)} {g(b,'tran',1)} {g(b,'tick',1)} {g(b,'ecom',1)}")
    if len(rows[q])!=2: print(f"   !!! {q} has {len(rows[q])} blocks")
