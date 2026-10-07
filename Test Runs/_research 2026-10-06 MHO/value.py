r=0.0566; sh=25.283031; price=132.00; t=0.235
def V(C,g):
    pv=sum(C*(1+g)**k/(1+r)**k for k in range(1,11))
    return pv+(C*(1+g)**10/r)/(1+r)**10
ttm=4417.8-2138.685+1983.965
print("TTM revenue",round(ttm,1))
gr=(4417.8/3745.9)**(1/4)-1; print("revenue CAGR 2021-25 %.2f%%"%(gr*100))
for lab,C in [("5yr strict",152.7),("5yr wh-adj",163.0)]:
    print(lab,"no-growth $%.1f  shown-growth $%.1f"%(V(C,0)/sh,V(C,gr)/sh))
inv06=1092.739/3901; inv25=3383.941/8921
infl=(inv25-inv06)*8921; vol=(8921-3901)*inv06
print("inv/home 2006 %.1fK 2025 %.1fK; inflation part %.0f volume part %.0f"%(inv06*1000,inv25*1000,infl,vol))
NI20=2733.9; REV20=41402.6; OC20s=411.5; OC20w=658.5
b1s=OC20s/REV20*ttm; b1w=OC20w/REV20*ttm; b2=(NI20-infl)/REV20*ttm; b3=NI20/REV20*ttm
for lab,C in [("B1 strict",b1s),("B1 wh",b1w),("B2 maint-adj",b2),("B3 all NI",b3)]:
    print(lab,"C=%.1f  value/sh no-growth $%.1f   pre-tax C=%.1f fair(10%%) $%.1f  pre-tax yield at price %.2f%%"%(C,V(C,0)/sh,C/(1-t),C/(1-t)/0.10/sh,C/(1-t)/(price*sh)*100))
for lab,C in [("5yr strict",152.7),("5yr wh-adj",163.0)]:
    pt=C+141.3
    print(lab,"pre-tax OC (adding back avg cash taxes) %.1f fair $%.1f yield at price %.2f%%"%(pt,pt/0.10/sh,pt/(price*sh)*100))
print("mkt cap %.0f"%(price*sh))
print("BV/share 6/30/26 %.2f"%(3227.420/25.237686))
