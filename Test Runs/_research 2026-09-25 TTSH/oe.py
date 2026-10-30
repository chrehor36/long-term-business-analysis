import statistics as st
rows={}
for l in open('series_TTSH.txt'):
    p=l.split()
    if p and p[0].isdigit(): rows[int(p[0])]=p[1:]
H='Rev GP OpInc NI OCF Capex DA SBC dAPAcc dRec dInv Eq Div Buyback Acq Impair Debt'.split()
def v(y,k):
    x=rows[y][H.index(k)]; return None if x=='-' else float(x)
CAP=80.0
print('year    OCF   SBC  capex    DA  OE_capexend  OE_DAend   inv increase (+ = cash used)')
oe={}
for y in sorted(rows):
    if y<2012: continue   # SBC tag absent 2010-2011 (pre-merger LLC years); not priced
    ocf,sbc,cx,da=v(y,'OCF'),v(y,'SBC'),v(y,'Capex'),v(y,'DA')
    a,b=ocf-sbc-cx,ocf-sbc-da
    oe[y]=(a,b)
    print(f"{y} {ocf:6.1f} {sbc:5.1f} {cx:6.1f} {da:5.1f}  {a:10.1f} {b:9.1f}   {v(y,'dInv'):6.1f}")
for n,lab in ((3,'3y'),(5,'5y'),(10,'10y'),(14,'14y full public')):
    ys=sorted(oe)[-n:]
    mc=st.mean(oe[y][0] for y in ys); md=st.mean(oe[y][1] for y in ys)
    lo,hi=min(mc,md),max(mc,md)
    print(f"{lab:16s} {ys[0]}-{ys[-1]}: capex-end {mc:6.1f}  DA-end {md:6.1f}  band {lo:6.1f}..{hi:6.1f}  yield {100*lo/CAP:6.2f}%..{100*hi/CAP:6.2f}%  mean OCF {st.mean(v(y,'OCF') for y in ys):.1f} capex {st.mean(v(y,'Capex') for y in ys):.1f} DA {st.mean(v(y,'DA') for y in ys):.1f}")
# the 9-year OCF window the screen read, with and without the two inventory-release years
w=list(range(2017,2026)); o=[v(y,'OCF') for y in w]
print('OCF 2017-2025', o, 'mean', round(st.mean(o),1))
print('without 2020 and 2023', round(st.mean([v(y,'OCF') for y in w if y not in (2020,2023)]),1))
print('2020+2023 share of 9y OCF sum', round(100*(v(2020,'OCF')+v(2023,'OCF'))/sum(o),1),'%')
print('inventory cash effect 2020..2025', [(y,v(y,'dInv')) for y in range(2020,2026)], 'sum', round(sum(v(y,'dInv') for y in range(2020,2026)),1))
