import os,re,json
D=os.path.dirname(os.path.abspath(__file__))
QS=json.load(open(os.path.join(D,'final.json'))).keys()
out={}
for q in QS:
    lines=open(os.path.join(D,f"8k-{q}-ex991.txt"),encoding='utf-8',errors='replace').read().split('\n')
    labs={}
    for i,l in enumerate(lines):
        s=l.strip()
        m=re.match(r'^\|?\s*(Transactions|Traffic)\s*[\d,]*\s*(\||$)', s, re.I)
        if m and 'tran' not in labs: labs['tran']=m.group(1)
        m=re.match(r'^\|?\s*(Average [Tt]icket|Ticket)\s*[\d,]*\s*(\||$)', s, re.I)
        if m and 'tick' not in labs: labs['tick']=m.group(1)
        m=re.match(r'^\|?\s*(eCommerce contribution to comp|eCommerce contribution|eCommerce|E-commerce)\s*[\d,]*\s*(\||$)', s, re.I)
        if m and 'ecom' not in labs: labs['ecom']=m.group(1)
    out[q]=labs
json.dump(out,open(os.path.join(D,'labels.json'),'w'),indent=1)
prev=None
for q,v in out.items():
    cur=(v.get('tran'),v.get('tick'),v.get('ecom'))
    if cur!=prev: print("CHANGE at",q,"->",cur)
    prev=cur
