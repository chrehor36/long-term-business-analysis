# expected return at the price for the midpoint streams; equity-only uncut default pair
from q7 import *
X=rows(); prev=[2012,2013,2014,2015,2016,2017,2018]; cyc=[2019,2020,2021,2022,2023,2024,2025]
ND=37556-(3172+235)
def irr(base,g,target):
    lo,hi=0.0,0.5
    for _ in range(200):
        m=(lo+hi)/2
        if value(base,g,m)>target: lo=m
        else: hi=m
    return (lo+hi)/2
for lab,key,nd in (("all-equity","u_acq",ND),("equity-only","oc_acq",0)):
    pb=mean([X[y][key] for y in prev]); cb=mean([X[y][key] for y in cyc]); g=cagr(pb,cb,7)
    v0=value(cb,0); v1=value(cb,g); vm=(v0+v1)/2; gm=solve_g_for_value(cb,vm); fair=value(cb,gm,FLOOR)
    target=PRICE*SH+nd
    print(f"{lab}: base {cb:,.0f} g {100*g:.2f}% range/sh {(v0-nd)/SH:.2f}..{(v1-nd)/SH:.2f} width {(v1-nd)/(v0-nd):.2f}x mid {(vm-nd)/SH:.2f} fair {(fair-nd)/SH:.2f}; expected return at $186 on the midpoint stream {100*irr(cb,gm,target):.2f}%; on the top stream {100*irr(cb,g,target):.2f}%; on no growth {100*cb/target:.2f}%")
