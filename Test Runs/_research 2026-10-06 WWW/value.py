r=0.0566; sh=82.066; price=18.94; tax=0.169; netdebt=601.1-158.5; intr=32.8
oc={2016:296.3-22.8-55.3,2017:202.7-25.4-32.4,2018:97.5-31.2-21.7,2019:222.6-24.5-34.4,2020:309.1-28.9-10.3,
    2021:86.8-38.1-17.6,2022:-178.9-33.4-36.5,2023:121.8-15.2-14.6,2024:180.1-19.1-20.2,2025:140.0-24.4-14.5}
ocda={2021:86.8-38.1-33.2,2022:-178.9-33.4-34.6,2023:121.8-15.2-35.1,2024:180.1-19.1-26.2,2025:140.0-24.4-25.9}
for y,v in oc.items(): print(y, round(v,1))
def pv(c,g,yrs=10):
    s=0;x=c
    for t in range(1,yrs+1):
        x=c*(1+g)**t; s+=x/(1+r)**t
    return s + x/r/(1+r)**yrs
five=sum(oc[y] for y in range(2021,2026))/5; ten=sum(oc.values())/10; three=sum(oc[y] for y in (2023,2024,2025))/3
fiveda=sum(ocda.values())/5
g3=(oc[2025]/oc[2023])**0.5-1
print("5yr capex basis",round(five,1)," 5yr D&A basis",round(fiveda,1)," 10yr",round(ten,1)," 3yr",round(three,1)," g 2023-25",round(g3*100,2))
for name,c in [("5yr",five),("10yr whole-cycle",ten),("3yr current perimeter",three)]:
    lo=pv(c,0); hi=pv(c,g3)
    print(f"{name}: C={c:.1f} low ${lo:.0f}M ${lo/sh:.2f}/sh  high ${hi:.0f}M ${hi/sh:.2f}/sh  ratio {hi/lo:.2f}")
# fair price: central case clears 10% pretax on equity (no growth): pre-tax owner cash /0.10
for name,c in [("10yr central",ten),("3yr",three),("5yr",five)]:
    pre=c/(1-tax); eq=pre/0.10
    ev_after=c+intr*(1-tax); ev=ev_after/(1-tax)/0.10 - netdebt
    print(f"fair {name}: equity basis ${eq:.0f}M = ${eq/sh:.2f}/sh ; EV basis ${ev:.0f}M = ${ev/sh:.2f}/sh ; yield at price pre-tax {pre/(price*sh)*100:.1f}%")
print("mcap", price*sh)
# cheap: low case (5yr avg, no growth) clears 10% pretax
print("cheap", five/(1-tax)/0.10/sh)
g10=(oc[2025]/oc[2016])**(1/9)-1
print("10yr shown growth on aggregate owner cash", round(g10*100,2))
lo=pv(ten,g10); print(f"10yr whole-cycle low ${lo:.0f}M ${lo/sh:.2f}/sh ; ratio {pv(ten,0)/lo:.2f}")
g21=(oc[2025]/oc[2021])**(1/4)-1; print("2021-25 endpoint growth", round(g21*100,1))
print("interest coverage 2025 pretax/interest", (121.5+32.8)/32.8)
