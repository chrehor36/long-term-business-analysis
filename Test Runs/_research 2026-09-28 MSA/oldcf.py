import re,io,sys,json
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
pats={'ocf':r'^\s*(?:Net )?Cash (?:Flow|provided by|Provided By)[^|\d]*(?:From|from|by)? ?Operating Activities','capex':r'^\s*(?:Property additions|Capital expenditures)','da':r'^\s*Depreciation and amortization','sbc':r'^\s*(?:Stock-based compensation|Stock compensation)','pl_exp':r'^\s*Product liability expense','pl_pay':r'^\s*Product liability payments','ins':r'^\s*Collections on insurance receivable'}
num=r'\(?\s*-?[\d,]+\.?\d*\s*\)?'
res={}
for y in range(1993,2026):
    L=open(f'cache/k{y}.txt',encoding='utf-8',errors='ignore').read().split('\n')
    got={}
    for k,p in pats.items():
        for i,l in enumerate(L):
            if len(l)>3000: continue
            if re.search(p,l,re.I):
                seg=l
                if len(re.findall(r'[\d,]{3,}',seg))<3: seg=' '.join(L[i:i+3])
                seg=re.sub(p,'',seg,flags=re.I)
                vals=re.findall(r'(\(\s*[\d,]+\.?\d*\s*\)|-?[\d,]+\.?\d*)',seg)
                vals=[v for v in vals if re.search(r'\d',v) and v.strip('(), ') not in ('',)]
                nums=[]
                for v in vals:
                    neg=v.strip().startswith('(')
                    x=float(v.strip('() ').replace(',',''))
                    nums.append(-x if neg else x)
                big=[n for n in nums if abs(n)>=100 or n==0]
                if len(big)>=3 and k not in got:
                    got[k]=big[:3]; break
    res[y]=got
    print(y,got)
json.dump(res,open('oldcf.json','w'))
