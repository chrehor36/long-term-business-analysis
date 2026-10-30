# COMPUTATION - NOT A CLEARANCE. Filed figures in $M (10-K cash flow statements; SBC from equity statements)
ocf={2022:78.1,2023:90.8,2024:93.3,2025:69.6,2026:89.9}
sbc={2022:11.2,2023:11.7,2024:9.8,2025:8.7,2026:8.8}
cap={2022:22.0,2023:24.2,2024:20.3,2025:28.3,2026:25.2}
dep={2022:18.0,2023:18.2,2024:18.6,2025:19.2,2026:20.3}
intx={2022:5.9,2023:5.4,2024:4.5,2025:23.9,2026:30.7}
t=0.21
lev={y:ocf[y]-sbc[y]-cap[y] for y in ocf}
levd={y:ocf[y]-sbc[y]-dep[y] for y in ocf}
unl={y:lev[y]+intx[y]*(1-t) for y in ocf}
for y in ocf: print(y,'levered',round(lev[y],1),'dep-variant',round(levd[y],1),'unlevered',round(unl[y],1))
avg=lambda d:sum(d.values())/len(d)
A_l,A_u,A_d=avg(lev),avg(unl),avg(levd)
print('avg levered',round(A_l,1),'avg unlev',round(A_u,1),'avg dep variant',round(A_d,1))
g_u=(unl[2026]/unl[2022])**(1/4)-1; g_l=(lev[2026]/lev[2022])**(1/4)-1
print('growth unlev %.1f%% lev %.1f%%'%(100*g_u,100*g_l))
shares=12.119465; price=289.91
netdebt=517.95-178.734+64.0  # LT debt - cash + NCI purchase obligation paid July 2026
print('net debt incl NCI obligation',round(netdebt,1))
def pv(c,g,r,n=10):
    v=0;x=c
    for i in range(1,n+1):
        x*=1+g; v+=x/(1+r)**i
    return v + x/r/(1+r)**n
r=0.0563
bot=(pv(A_u,0,r)-netdebt)/shares
top=(pv(A_u,g_u,r)-netdebt)/shares
topl=(pv(A_u,g_l,r)-netdebt)/shares
print('BOTTOM no-growth %.1f  TOP shown unlev growth %.1f (ratio %.2f)  alt top at levered growth %.1f'%(bot,top,top/bot,topl))
# Q3-capped top: organic record ~1.6%/yr nominal FY2017-FY2026
print('Q3-capped top at 1.6%%: %.1f'%((pv(A_u,0.016,r)-netdebt)/shares))
# what growth does price imply, at sovereign, base A_u
import math
lo,hi=0,0.5
for _ in range(100):
    m=(lo+hi)/2
    if (pv(A_u,m,r)-netdebt)/shares<price: lo=m
    else: hi=m
print('growth for 10 yrs the price implies at sovereign on 5-yr avg base: %.1f%%'%(100*lo))
# central case for fair price
base_c=70.0; g_c=0.05; r_f=0.07
fair=(pv(base_c,g_c,r_f)-netdebt)/shares
print('FAIR (central %.0f, %.0f%% x10y, at 7%% after-tax): %.1f'%(base_c,100*g_c,fair))
fair10=(pv(base_c,g_c,0.10)-netdebt)/shares
print('fair if 10%% applied to after-tax owner cash: %.1f'%fair10)
cheap=(A_u/0.10-netdebt)/shares
print('CHEAP (5y avg unlev, no growth, 10%% after tax): %.1f'%cheap)
# expected return at price, central case: solve r
lo,hi=0.0,0.5
for _ in range(100):
    m=(lo+hi)/2
    if (pv(base_c,g_c,m)-netdebt)/shares>price: lo=m
    else: hi=m
print('expected after-tax return at price on central case: %.2f%%'%(100*lo))
print('mkt cap',round(price*shares,1),'EV',round(price*shares+netdebt,1),'unlev yield on EV %.2f%%'%(100*A_u/(price*shares+netdebt)))
