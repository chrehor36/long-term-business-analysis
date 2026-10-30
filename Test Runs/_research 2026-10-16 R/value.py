# COMPUTATION, NOT A CLEARANCE. Q7 range construction for Ryder, all figures $M unless per share.
import importlib.util,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
R=0.0543            # US Treasury 30-year par yield, 2026-10-15
FLOOR=0.10          # CONVENTION of the framework (Q7 floor)
SH=38.346868        # shares, 10-Q Q2 2026 cover
ND=7457-219         # net debt at 2026-06-30 (10-Q): total debt incl. finance leases less cash
PRICE=240.38
def pv(base,g,r,years=10):
    v=0;c=base
    for t in range(1,years+1):
        c=base*(1+g)**t; v+=c/(1+r)**t
    term=c/r/(1+r)**years   # zero nominal growth after year ten
    return v+term
def ps(ev): return (ev-ND)/SH
def irr(base,g,price_ev):
    lo,hi=0.0005,1.0
    for _ in range(200):
        mid=(lo+hi)/2
        if pv(base,g,mid)>price_ev: lo=mid
        else: hi=mid
    return mid
EV=PRICE*SH+ND
print(f"market value {PRICE*SH:.1f}; net debt {ND}; EV {EV:.1f}")
cases={
 'CENTRAL all-equity, all spending, acquisitions deducted, cycle base 2016-2025':(297.1,0.0543),
 'literal window 2021-2025 all-equity after acq':(515.0,-0.037),
 'depreciation-as-maintenance, all-equity after acq, cycle base':(561.0,0.0543),
 'depreciation-as-maintenance, literal window':(733.0,0.0543),
}
for name,(b,g) in cases.items():
    lo=min(pv(b,0,R),pv(b,g,R)); hi=max(pv(b,0,R),pv(b,g,R))
    flo=min(pv(b,0,FLOOR),pv(b,g,FLOOR)); fhi=max(pv(b,0,FLOOR),pv(b,g,FLOOR))
    print(f"\n{name}: base {b}, growth {g*100:.2f}%")
    print(f"  range at {R*100:.2f}%: EV {lo:.0f} to {hi:.0f}; per share {ps(lo):.2f} to {ps(hi):.2f}")
    print(f"  ends at 10%: EV {flo:.0f} and {fhi:.0f}; per share {ps(flo):.2f} and {ps(fhi):.2f}; FAIR (average) {(ps(flo)+ps(fhi))/2:.2f}")
    print(f"  expected return at the price (EV {EV:.0f}): no-growth {irr(b,0,EV)*100:.2f}%  growth case {irr(b,g,EV)*100:.2f}%")
# equity-only beside: owner cash after interest (not all-equity), acquisitions deducted, against market value
MV=PRICE*SH
for name,(b,g) in {'EQUITY-ONLY cycle base 2016-2025 after acq':(110.0,0.0543),'EQUITY-ONLY literal window after acq':(286.0,0.0)}.items():
    a,c=pv(b,0,FLOOR)/SH,pv(b,g,FLOOR)/SH
    print(f"\n{name}: base {b}: range at R per share {pv(b,0,R)/SH:.2f} to {pv(b,g,R)/SH:.2f}; FAIR {(a+c)/2:.2f}; return at price no-growth {irr(b,0,MV)*100:.2f}% growth {irr(b,g,MV)*100:.2f}%")
