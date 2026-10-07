import re,sys
for fy in range(2010,2022):
    s=open(f'10-K_FY{fy}.txt',encoding='utf-8').read().replace('\n',' ')
    print('=====',fy)
    seen=set()
    for m in re.finditer(r'(?i)(due to pricing|due to higher pricing|reduction due to pricing|price reductions of|decrease in net revenue|pricing pressure)',s):
        a=s.rfind('.',0,m.start()-250)
        c=s[a+1:m.end()+250].strip()
        k=c[:100]
        if k in seen: continue
        seen.add(k); print(' *',c[:800])
