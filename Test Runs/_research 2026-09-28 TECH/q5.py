# Q5 arithmetic (engine only; casts no vote). $M; 156,818,238 cover shares; net cash 64.7; r = the ~10% floor [E4-28]
SH=156.818238; NC=64.7; CAP=11370.9; SOV=0.0556
def gordon(oe,g,r=0.10): return oe*(1+g)/(r-g)
def two(oe,g1,n,g2,r=0.10):
    v=0; x=oe
    for t in range(1,n+1): x*=1+g1; v+=x/(1+r)**t
    tv=x*(1+g2)/(r-g2)/(1+r)**n
    return v+tv
for oe in (210.2,219.3):
    print(f'OE {oe}: yield {100*oe/CAP:.2f}%  vs bond {100*(oe/CAP-SOV):+.2f} pts')
    print('  perpetual growth the price needs at 10pct: %.2f%%; at the bond 5.56pct: %.2f%%'%(100*(0.10*CAP-oe)/(CAP+oe),100*(SOV*CAP-oe)/(CAP+oe)))
    for g in (0,0.03,0.044,0.05):
        v=(gordon(oe,g) if g else oe/0.10)+NC; print(f'  g {g:.3f}: ${v/SH:6.2f}/share (equity {v:7.1f})')
    for g1 in (0.065,0.08,0.10):
        v=two(oe,g1,10,0.05)+NC; print(f'  two-stage {g1:.3f} x10y then 5%: ${v/SH:6.2f}')
# year-1 growth (ten years then 5%) that the quote needs at 10%
import math
for oe in (210.2,219.3):
    lo,hi=0.0,0.5
    for _ in range(80):
        m=(lo+hi)/2
        if two(oe,m,10,0.05)+NC<CAP: lo=m
        else: hi=m
    print(f'OE {oe}: ten-year growth then 5% needed at 10%: {100*lo:.1f}%')
# expectancy at the quote: yield + growth (record 4.4%/yr per share, 4.8% OE FY2010-FY2026, 6.5% FY2016-FY2026)
for oe in (210.2,219.3):
    for g in (0.044,0.048,0.065):
        print(f'  expectancy OE {oe} g {g}: {100*(oe/CAP*(1+g)+g):.2f}%')
# deal arithmetic: spread
print('spread', 73-72.51, 100*(73/72.51-1))
