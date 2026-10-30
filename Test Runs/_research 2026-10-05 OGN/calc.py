# COMPUTATION - NOT A CLEARANCE. Organon owner cash and value range per the v5 Q7 CONVENTION.
yrs=[2021,2022,2023,2024,2025]
ocf={2021:2160,2022:858,2023:799,2024:939,2025:700}
sbc={2021:59,2022:75,2023:101,2024:105,2025:77}
capex={2021:192,2022:196,2023:251,2024:175,2025:162}
dep={2021:92,2022:96,2023:120,2024:132,2025:156}
amo={2021:103,2022:116,2023:116,2024:145,2025:205}
bd={2021:104+192,2022:107+124,2023:8+2,2024:71+105+166,2025:30+124+75}
oe={y:ocf[y]-sbc[y]-capex[y] for y in yrs}
oed={y:ocf[y]-sbc[y]-dep[y]-amo[y] for y in yrs}
oebd={y:oe[y]-bd[y] for y in yrs}
for y in yrs: print(y, 'OE capex',oe[y],'OE D&A',oed[y],'OE capex less BD',oebd[y])
avg=lambda d,ys: sum(d[y] for y in ys)/len(ys)
A=avg(oe,yrs); B=avg(oe,yrs[1:]); C=avg(oebd,yrs[1:]); D=avg(oed,yrs[1:])
print('5yr avg A',A,' whole-cycle (2022-25) B',B,' B less BD C',C,' D&A basis 2022-25 D',D)
g_shown=(oe[2025]/oe[2022])**(1/3)-1
g_bd=(oebd[2025]/oebd[2022])**(1/3)-1
print('growth shown OE 2022-25 %.2f%%'%(g_shown*100), ' OE less BD %.2f%%'%(g_bd*100))
r=0.0566; sh=262.609; shd=284.9
def pv(base,g,r,n=10):
    v=0; c=base
    for t in range(1,n+1):
        c=c*(1+g); v+=c/(1+r)**t
    v+= c/r/(1+r)**n   # no growth after year ten (zero nominal)
    return v
for lab,base in [('A 5yr',A),('B whole-cycle',B),('C less BD',C)]:
    for gl,g in [('no growth',0.0),('shown',g_shown)]:
        v=pv(base,g,r); print(f'{lab:14s} {gl:9s} @5.66% {v:8.0f}M  ${v/sh:6.2f}/sh  diluted ${v/shd:6.2f}')
print('--- at the 10% floor (fair-price test)')
for lab,base in [('B whole-cycle',B),('C less BD',C)]:
    for gl,g in [('no growth',0.0),('mid',g_shown/2),('shown',g_shown)]:
        v=pv(base,g,0.10); print(f'{lab:14s} {gl:9s} @10% {v:8.0f}M  ${v/sh:6.2f}/sh  diluted ${v/shd:6.2f}')
price=13.72; mcap=price*sh
print('mcap',mcap, 'OE yield B %.1f%% C %.1f%%'%(B/mcap*100, C/mcap*100))
# workout arithmetic
for months in (4,6):
    gross=(14.00+0.02*(months//3)-price)/price
    print(months,'months gross %.2f%% annualised %.2f%%'%(gross*100, ((1+gross)**(12/months)-1)*100))
print('unaffected 2026-04-09 implied', 14/2.03)
print('=== each series at its own shown growth')
gA=(oe[2025]/oe[2021])**(1/4)-1
gAbd=(oebd[2025]/oebd[2021])**(1/4)-1
cases=[('A capex 2021-25',A,gA),('A less BD 2021-25',avg(oebd,yrs),gAbd),('B capex 2022-25',B,g_shown),('C less BD 2022-25',C,g_bd)]
for lab,base,g in cases:
    lo=pv(base,g,r); hi=pv(base,0,r)
    f0=pv(base,0,0.10); fm=pv(base,g/2,0.10); fs=pv(base,g,0.10)
    print(f'{lab:18s} base {base:7.1f} g {g*100:6.2f}%  range ${lo/sh:6.2f}-${hi/sh:6.2f} (x{hi/lo:4.2f})  @10%: none ${f0/sh:6.2f} mid ${fm/sh:6.2f} shown ${fs/sh:6.2f}  diluted mid ${fm/shd:6.2f}')
