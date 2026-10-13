# Q7 COMPUTATION, NOT A CLEARANCE. Yen billions. Arithmetic only; conventions as stated in the run file.
import sys
sys.stdout.reconfigure(encoding='utf-8')
r=0.04136; shares=3662.694127; price=4596
nd_june=3939.8; aethon=5.2*158.063; nd=nd_june+aethon
rev21,rev25=17264.828,18915.995
g_sales=(rev25/rev21)**0.25-1
oc21,oc25=401.7,1121.2
g_shown=(oc25/oc21)**0.25-1
def val(B,g,rate,years=10):
    pv=0;c=B
    for t in range(1,years+1):
        c*=1+g; pv+=c/(1+rate)**t
    return pv + c/rate/(1+rate)**years   # zero nominal growth after year ten
print(f"sales growth {g_sales:.4f}; shown owner-cash growth {g_shown:.4f}; net debt {nd:.1f} (June {nd_june} + Aethon {aethon:.1f})")
print(f"cap check: shown growth carried ten years -> {950.0*(1+g_shown)**10:.0f} vs highest owner-cash/sales {1323.9/18617.6:.3f}")
for label,B,deduct in (('all-equity, before purchases (central)',950.0,True),('all-equity, after net divestments',1047.3,True),('ten-year base all-equity before purchases',700.1,True)):
    lo=val(B,0,r); hi=val(B,g_sales,r)
    lo_s=(lo-nd)/shares*1000; hi_s=(hi-nd)/shares*1000
    f_lo=(val(B,0,0.10)-nd); f_hi=(val(B,g_sales,0.10)-nd)
    fair=(f_lo+f_hi)/2/shares*1000
    print(f"{label}: EV {lo:.0f}-{hi:.0f}; per share {lo_s:.0f}-{hi_s:.0f} (width {hi_s/lo_s:.2f}x); fair {fair:.0f}")
for label,B in (('equity-only before purchases',847.9),('equity-only after net divestments',945.2)):
    lo=val(B,0,r)/shares*1000; hi=val(B,g_sales,r)/shares*1000
    fair=(val(B,0,0.10)+val(B,g_sales,0.10))/2/shares*1000
    print(f"{label}: per share {lo:.0f}-{hi:.0f}; fair {fair:.0f}")
# implied return at the price, all-equity, no-growth and growth: solve rate
ev_mkt=price*shares/1000+nd
def solve(B,g):
    lo_,hi_=0.0001,0.5
    for _ in range(100):
        m=(lo_+hi_)/2
        if val(B,g,m)>ev_mkt: lo_=m
        else: hi_=m
    return m
print(f"market EV {ev_mkt:.0f}; implied return no-growth {solve(950.0,0):.4f}, growth {solve(950.0,g_sales):.4f}; after-divestment growth {solve(1047.3,g_sales):.4f}")
print(f"Aethon credited at cost beside: fair central +{aethon/shares*1000:.0f}/share")
