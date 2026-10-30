import re,sys
f=sys.argv[1]; key=sys.argv[2] if len(sys.argv)>2 else 'CONSOLIDATED STATEMENTS OF OPERATIONS'
s=open(f,encoding='utf-8').read()
idx=[m.start() for m in re.finditer(key,s)]
# choose occurrence followed by 'REVENUES'
for i in idx:
    chunk=s[i:i+9000]
    if 'REVENUES' in chunk[:1500] or 'Revenues' in chunk[:600]:
        break
t=re.sub(r'[|$\n]',' ',chunk)
t=re.sub(r'\(\s*([\d,\.]+)\s*\)',r'-\1',t)
t=re.sub(r'\s+',' ',t)
labels=['New vehicle retail sales','Used vehicle retail sales','Used vehicle wholesale sales','Parts and service sales','Finance, insurance and other, net','Total revenues','Total cost of sales','GROSS PROFIT','Selling, general and administrative expenses','Depreciation and amortization expense','Asset impairments','INCOME FROM OPERATIONS','Floorplan interest expense','Other interest expense, net','INCOME BEFORE INCOME TAXES','Provision for income taxes','NET INCOME']
pos=0
for L in labels:
    j=t.find(L,pos)
    if j<0: print(L,'--'); continue
    m=re.findall(r'-?[\d,]+\.?\d*|—',t[j+len(L):j+len(L)+80])[:3]
    print(L,m); pos=j+len(L)
