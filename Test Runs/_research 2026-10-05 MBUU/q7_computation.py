# COMPUTATION - NOT A CLEARANCE. MBUU, run of 2026-10-05. All $ thousands unless noted.
ocf  ={2022:164846,2023:184733,2024:55558,2025:56506,2026:67509}
sbc  ={2022:6342,2023:5894,2024:4935,2025:5916,2026:5603}
dirc ={2022:1054,2023:1136,2024:1512,2025:1091,2026:1041}
capex={2022:55064,2023:54840,2024:75962,2025:27917,2026:24663}
dep  ={2022:19365,2023:21912,2024:26178,2025:31794,2026:33147}
oc ={y:ocf[y]-sbc[y]-dirc[y]-capex[y] for y in ocf}
ocd={y:ocf[y]-sbc[y]-dirc[y]-dep[y] for y in ocf}
for y in ocf: print(y, 'owner cash (all capex)',oc[y],' depreciation variant',ocd[y])
m=sum(oc.values())/5; md=sum(ocd.values())/5
print('five-year mean, all capex',round(m),' depreciation variant',round(md))
g=(oc[2026]/oc[2022])**(1/4)-1
print('literal shown growth FY2022->FY2026 (4 intervals)',round(g*100,2),'%')
# boom-treated low base: FY2024-26, the $100,000 settlement removed and spread at $10,000 a year
low=( (oc[2024]+100000-10000)+(oc[2025]-10000)+(oc[2026]-10000) )/3
print('post-boom base (FY2024-26, settlement spread)',round(low))
r=0.0563
def pv(base,g,years=10):
    v=0;cf=base
    for t in range(1,years+1):
        cf=cf*(1+g); v+=cf/(1+r)**t
    tv=cf/r; v+=tv/(1+r)**years
    return v
N=19677264+270419
adj=203900-(165000-74419)-29900   # Saxdor at cost, less net debt, less earnout fair value
print('shares (A + LLC units)',N,' claims adjustment',adj)
def ps(x): return (x+adj)*1000/N
cases={'literal low (shown growth)':pv(m,g),'no growth, five-year mean':m/r,'post-boom low, no growth':low/r,'depreciation variant, no growth':md/r}
for k,v in cases.items(): print(f'{k:38s} business ${v/1000:7.1f}M  per share ${ps(v):6.2f}')
lit=(ps(pv(m,g)),ps(m/r)); bt=(ps(low/r),ps(m/r))
print('literal range ratio',round(lit[1]/lit[0],2),' boom-treated ratio',round(bt[1]/bt[0],2))
tax=0.248; floor_at=0.10*(1-tax)
print('after-tax floor',round(floor_at*100,2),'%')
top_floor=ps(m/floor_at); low_floor=ps(low/floor_at)
print('price where five-year mean earns the floor',round(top_floor,2),'; price where post-boom low earns the floor',round(low_floor,2))
P=22.54; mc=P*N/1000
print('market cap $M',round(mc/1000,1),' legacy business implied $M',round((mc-adj)/1000,1))
for k,b in [('five-year mean',m),('post-boom low',low)]:
    y=b/(mc-adj); print(k,'after-tax yield',round(y*100,2),'%  pre-tax equivalent',round(y/(1-tax)*100,2),'%')
# ten-year owner cash for the cycle-to-cycle check (FY2017-21; FY2017-18 director pay not read, XBRL SBC only)
c1={2017:35900-1400-9300,2018:58500-2000-10400,2019:81500-2607-791-17938,2020:94141-3042-829-41291,2021:131314-5581-834-30677}
m1=sum(c1.values())/5; print('FY2017-21 mean (approx)',round(m1),' cycle-to-cycle annual change',round(((m/m1)**(1/5)-1)*100,2),'%')
