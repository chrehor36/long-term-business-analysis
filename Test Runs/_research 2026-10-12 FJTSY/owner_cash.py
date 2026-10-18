# Owner cash for Fujitsu, years ended March 2022-2026, billions of yen, from the filed cash-flow statements
# (Financial Sections 2022, 2024, 2026). Device Solutions (discontinued) removed by estimate; see run file.
Y=[2022,2023,2024,2025,2026]
OCF =[248.347,220.329,309.221,303.882,338.130]
INTR=[1.049,2.658,5.717,6.498,8.525]
DIVR=[7.402,7.081,12.147,9.851,10.551]
INTP=[2.994,3.984,5.270,8.068,6.192]
CAPX=[143.251,168.098,195.839,160.898,108.977]
PPEP=[0.0,15.580,4.769,9.991,30.893]   # FY2022 not shown separately (inside "Other, net")
LEAS=[62.328,58.566,52.609,46.307,46.585]
ACQ =[0.0,9.824,43.311,0.903,45.764]
SALE=[16.322,88.049,-29.535,42.398,298.718]
# Device Solutions owner cash, estimate: adj. OP x 0.7 + D&A - capex (2022-2024, segment notes); 2025 actual
# discontinued OCF 53.816 + investing -52.801; 2026 taken as ~0 (OCF 9.132, capex for ~10 weeks not disclosed)
DEV =[78.319*0.7+34.799-44.001, 77.415*0.7+39.020-73.501, 18.324*0.7+31.823-79.573, 53.816-52.801, 0.0]
SBC =[0,0,0,4.337,6.276]  # stock pay expense, Note 33 (2025, 2026); earlier years not read
REV =[3586.839,3713.767,3476.985,3550.116,3502.971]  # as filed in five-year summary (2022-23 incl. Device)
def show(name,s): print(f"{name:34s}"+" ".join(f"{v:8.1f}" for v in s)+f"  avg {sum(s)/5:7.1f}")
eq_lit=[OCF[i]-CAPX[i]+PPEP[i]-LEAS[i]-ACQ[i]+SALE[i] for i in range(5)]
eq_cons=[OCF[i]-CAPX[i]+PPEP[i]-LEAS[i]-ACQ[i] for i in range(5)]
eq=[eq_cons[i]-DEV[i]-SBC[i] for i in range(5)]
unlev=[eq[i]+INTP[i]-INTR[i]-DIVR[i] for i in range(5)]
org=[eq[i]+ACQ[i] for i in range(5)]
org_un=[unlev[i]+ACQ[i] for i in range(5)]
show("Device owner cash est",DEV)
show("literal (sales of subs credited)",eq_lit)
show("consolidated, sales excluded",eq_cons)
show("CONTINUING equity basis",eq)
show("CONTINUING all-equity (pre-int)",unlev)
show("organic (acq left out) equity",org)
show("organic all-equity",org_un)
import math
for nm,s in [("equity",eq),("all-equity",unlev),("organic all-eq",org_un)]:
    a=s; g=(a[4]/a[0])**(1/4)-1 if a[0]>0 and a[4]>0 else None
    h1=sum(a[:2])/2; h2=sum(a[3:])/2
    print(nm,"end-to-end CAGR",None if g is None else round(g*100,2),"halves",round(h1,1),round(h2,1),"half-growth/yr",round(((h2/h1)**(1/3)-1)*100,2) if h1>0 else None)
