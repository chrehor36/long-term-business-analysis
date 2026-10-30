import re,glob
files=sorted(glob.glob('tenk_FY20??.txt'))+['tenk25_sxc-20251231.htm.txt']
out=open('cf_statements.txt','w',encoding='utf-8')
for fn in files:
    L=open(fn,encoding='utf-8').read().split('\n')
    idx=[i for i,l in enumerate(L) if re.search(r'(?i)adjustments to reconcile net',l)]
    i=idx[0]
    j=i
    while j<len(L) and not re.search(r'(?i)at end of (the )?(year|period)',L[j]): j+=1
    body=[x.strip()[:200] for x in L[i-14:j+2] if x.strip() and x.strip()!='|']
    out.write(f'### {fn} line {i}\n'+'\n'.join(body)+'\n\n')
    print(fn,i,j-i,len(body))
