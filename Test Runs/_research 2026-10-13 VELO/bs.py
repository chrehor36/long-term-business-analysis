import sys,re,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
f=sys.argv[1]
L=open(f,encoding='utf-8').read().split('\n')
# find balance sheet start
idx=[i for i,l in enumerate(L) if re.search(r'CONSOLIDATED BALANCE SHEETS',l)]
start=idx[1] if len(idx)>1 else idx[0]
seg=L[start:start+700]
t='\n'.join(seg)
keys=['Cash and cash equivalents','Short-term investments','Accounts receivable','Inventories','Total current assets','Property and equipment, net','Total assets','Accounts payable','Contract liabilities','Total current liabilities','Long-term debt','Debt','Warrant liabilities','Contingent earnout','Total liabilities','Additional paid-in capital','Accumulated deficit',"Total stockholders",'shares issued and outstanding']
toks=[x.strip() for x in re.split(r'\||\n',t)]
toks=[x for x in toks if x and x not in ('$',')')]
out=[]
for i,x in enumerate(toks):
    for k in keys:
        if x.startswith(k):
            nums=[y for y in toks[i+1:i+5] if re.fullmatch(r'\(?[\d,]+\)?|—',y)][:2]
            out.append(f'{x[:80]} :: {nums}')
            break
    if x.startswith('Total liabilities and'): break
print(start); print('\n'.join(out))
