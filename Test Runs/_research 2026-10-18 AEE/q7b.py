# Q7 growth case under specific (e): growth spending G charged each year for ten years, and credited with the growth it
# buys at the incremental return Q3 measured (rho), so owner cash rises by rho*G a year; no growth and no growth
# spending after year ten. Also the same at rho from 2016-2025.
B_ae=1466.7; B_eq=1050.2; G=2224.8; r=0.0543; netdebt=21796; shares=276.843; mc=29367.5
def pv(B,rho,rate,G=G):
    s=0
    for t in range(1,11):
        s+=(B+rho*G*t-G)/(1+rate)**t
    s+=(B+rho*G*10)/rate/(1+rate)**10
    return s
def irr(B,rho,cost):
    lo,hi=0.0005,1.0
    for _ in range(200):
        m=(lo+hi)/2
        if pv(B,rho,m)>cost: lo=m
        else: hi=m
    return m
for rho in (0.0668,0.0598):
    for lab,B,sub,cost in (('all-equity',B_ae,netdebt,mc+netdebt),('equity-only',B_eq,0,mc)):
        v=pv(B,rho,r); v10=pv(B,rho,0.10)
        print(f"rho {rho*100:.2f}% {lab}: at 5.43% {v:,.0f} -> {(v-sub)/shares:,.2f}/sh; at 10% {v10:,.0f} -> {(v10-sub)/shares:,.2f}/sh; return at price {irr(B,rho,cost)*100:.2f}%; year-10 owner cash {B+rho*G*10:,.0f}")
