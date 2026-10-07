rows={}
for l in open('series_DMC.txt'):
    p=l.split()
    if p and p[0].isdigit(): rows[int(p[0])]=p[1:]
H='Rev GP OpInc NI OCF Capex DA SBC dAPAcc dRec dInv Eq Div Buyback Acq Impair Debt'.split()
def v(y,k): return float(rows[y][H.index(k)])
print('year   OCF   SBC  capex    DA  OE_capex  OE_DA   WCnet(rec,inv,ap)')
oe={}
for y in sorted(rows):
    ocf,sbc,cx,da=v(y,'OCF'),v(y,'SBC'),v(y,'Capex'),v(y,'DA')
    a,b=ocf-sbc-cx,ocf-sbc-da
    oe[y]=(min(a,b),max(a,b),a,b)
    wc=-v(y,'dRec')-v(y,'dInv')+v(y,'dAPAcc')
    print(f"{y} {ocf:6.1f} {sbc:5.1f} {cx:6.1f} {da:5.1f} {a:8.1f} {b:7.1f}   {wc:7.1f}  ({-v(y,'dRec'):.1f},{-v(y,'dInv'):.1f},{v(y,'dAPAcc'):.1f})")
import statistics as st
cap=1438.4
for n in (3,5,10,18):
    ys=[y for y in sorted(rows)][-n:]
    lo=st.mean(oe[y][0] for y in ys); hi=st.mean(oe[y][1] for y in ys)
    mc=st.mean(oe[y][2] for y in ys); md=st.mean(oe[y][3] for y in ys)
    print(f"{n}y {ys[0]}-{ys[-1]}: capex-end {mc:.1f}  DA-end {md:.1f}  band {min(mc,md):.1f}..{max(mc,md):.1f}  yield {100*min(mc,md)/cap:.2f}%..{100*max(mc,md)/cap:.2f}%  mean capex {st.mean(v(y,'Capex') for y in ys):.1f} mean DA {st.mean(v(y,'DA') for y in ys):.1f}")
# level shift check: early vs recent half of 9 yr OCF series
