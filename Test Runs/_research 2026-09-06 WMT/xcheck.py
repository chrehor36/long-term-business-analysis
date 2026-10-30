import json,os,re
D=os.path.dirname(os.path.abspath(__file__))
r=json.load(open(os.path.join(D,'final.json')))
QS=list(r.keys())
def norm(x):
    if x is None: return None
    x=x.strip().replace(' ','')
    return x
def cur(q,n,k): 
    b=r[q][n] if len(r[q])>n else None
    return norm(b[k][0]) if b and b.get(k) else None
def pri(q,n,k):
    b=r[q][n] if len(r[q])>n else None
    return norm(b[k][1]) if b and b.get(k) and len(b[k])>1 else None
bad=0
for i,q in enumerate(QS):
    if i+4>=len(QS): break
    q4=QS[i+4]
    for n,seg in [(0,'WMT-US'),(1,'SAMS-US')]:
        for k in ['comp','tran','tick','ecom']:
            a=cur(q,n,k); b=pri(q4,n,k)
            if a and b and a!=b:
                print(f"MISMATCH {seg:8} {k:5} {q}(reported {a}) vs prior-yr col in {q4} ({b})"); bad+=1
print("total mismatches:",bad)
