import re
def num(c):
    c=c.strip().replace(',','').replace('$','').replace(' ','')
    neg=c.startswith('(')
    c=c.strip('()')
    try: v=float(c)
    except: return None
    return -v if neg else v
out={}
for f,yrs in [('k2011',[2011,2010,2009]),('k2014',[2014,2013,2012]),('k2017',[2017,2016,2015]),('k2020',[2020,2019,2018]),('k2023',[2023,2022,2021]),('k2025',[2025,2024,2023])]:
    L=open(f'cache/{f}.txt',encoding='utf-8').read().split('\n')
    i=[k for k,l in enumerate(L) if re.search(r'CONSOLIDATED STATEMENTS OF CASH FLOWS',l)][-1]
    j=[k for k in range(i,len(L)) if re.search(r'(?i)changes in operating assets and liabilities',L[k])][0]
    e=[k for k in range(j,len(L)) if re.search(r'(?i)^Net cash .*operating activities',L[k])][0]
    print('==',f, 'lines',j,e)
    tot=[0,0,0]
    for l in L[j+1:e+1]:
        cells=[x for x in l.split('|')]
        vals=[num(x) for x in cells[1:]]
        vals=[v for v in vals if v is not None][:3]
        print('  ', cells[0].strip()[:70], vals)
        if len(vals)==3 and not re.search(r'(?i)^Net cash',cells[0].strip()):
            tot=[a+b for a,b in zip(tot,vals)]
    for y,t in zip(yrs,tot): out.setdefault(y,{})[f]=round(t/1000,1)
print('WC block sum by year ($M) by source file:', out)
