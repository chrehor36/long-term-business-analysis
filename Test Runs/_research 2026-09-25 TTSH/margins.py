import statistics as st, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def load(f):
    rows={}
    for line in open(f):
        p=line.split()
        if p and p[0].isdigit(): rows[p[0]]=p[1:]
    return rows
def g(v,i):
    try: return float(v[i])
    except: return None
for f,n in [('series_TTSH.txt','TTSH'),('peers/series_FND.txt','Floor & Decor'),('peers/series_HD.txt','Home Depot'),('peers/series_LOW.txt',"Lowe's"),('peers/series_LL.txt','LL Flooring')]:
    r=load(f); out=[]
    for y,v in sorted(r.items()):
        if int(y)<2012: continue
        rev,gp,op=g(v,0),g(v,1),g(v,2)
        if rev and op is not None: out.append(f"{y} GM {100*gp/rev:.1f}% OM {100*op/rev:.1f}%" if gp else f"{y} OM {100*op/rev:.1f}%")
    print(n+': '+' | '.join(out))

# same metric, same window: operating margin 2015-2025 (LL to 2023, its last 10-K); return on average equity TTSH vs FND
print()
eq_ttsh = {2013:78.5,2014:93.7,2015:115.2,2016:138.9,2017:143.9,2018:146.3,2019:130.9,2020:139.1,2021:122.2,2022:108.8,2023:119.7,2024:122.9,2025:87.2}  # filed equity statements, $M
for f,n,last in [('series_TTSH.txt','TTSH',2025),('peers/series_FND.txt','Floor & Decor',2025),('peers/series_HD.txt','Home Depot',2025),('peers/series_LOW.txt',"Lowe's",2025),('peers/series_LL.txt','LL Flooring',2023)]:
    r=load(f)
    for a,b in [(2015,last),(2021,last),(2023,last)]:
        oms=[100*g(r[str(y)],2)/g(r[str(y)],0) for y in range(a,b+1) if str(y) in r and g(r[str(y)],2) is not None and g(r[str(y)],0)]
        print(f"{n:14s} OM mean {a}-{b}: {st.mean(oms):5.1f}%  min {min(oms):5.1f}  max {max(oms):5.1f}  n={len(oms)}")
r=load('series_TTSH.txt')
roe=[]
for y in range(2014,2026):
    ni=g(r[str(y)],3); e=(eq_ttsh[y-1]+eq_ttsh[y])/2; roe.append(100*ni/e); print(y,f"TTSH NI {ni:6.1f} avgEq {e:6.1f} ROE {100*ni/e:5.1f}%")
print('TTSH ROE mean 2015-2025',round(st.mean(roe[1:]),1),'2021-2025',round(st.mean(roe[-5:]),1))
f=load('peers/series_FND.txt'); fr=[]
for y in range(2016,2026):
    ni=g(f[str(y)],3); e0=g(f[str(y-1)],11); e1=g(f[str(y)],11)
    if e0 and e1: fr.append((y,100*ni/((e0+e1)/2)))
print('FND ROE', [(y,round(v,1)) for y,v in fr], 'mean', round(st.mean(v for _,v in fr),1), '2021-25', round(st.mean(v for y,v in fr if y>=2021),1))
