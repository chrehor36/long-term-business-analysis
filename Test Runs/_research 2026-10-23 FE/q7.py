"""FE Q7 arithmetic (COMPUTATION). Figures in USD millions from the filed cash-flow statements:
2021-2022 from the FY2023 10-K (0001031296-24-000008), 2023-2025 from the FY2025 10-K (0001031296-26-000046);
stock plan issuance from the equity statements of the same 10-Ks; depreciation from the FY2021, FY2023 and FY2025 10-Ks."""
yrs=[2021,2022,2023,2024,2025]
ocf   =[2811,2683,1387,2891,3700]
ohio  =[0,0,0,0,275]          # Ohio restitution accrued in 2025 OCF, paid 2026 (charged in its year)
sbc   =[50,98,89,74,60]       # stock issued under share-based plans (equity statements)
capex =[2487,2848,3356,4030,4705]
remov =[226,213,274,305,376]  # asset removal costs (investing)
nci   =[0,21,72,86,100]       # distributions to FET minority interest
ltd_i =[2100,700,3150,2100,5925]
ltd_r =[532,3005,537,2760,3129]
intp  =[1085,1021,1002,1062,999]  # cash interest paid, net of capitalized
dep   =[1302,1375,1461,1581,1664]
ALLOWED_DEBT=0.488   # PUCO order 2025-11-19, hypothetical capital structure, the only allowed share the 10-K states
TAX=0.21
SOV=0.0529; FLOOR=0.10
SH=578.639932; PRICE=46.49
NETDEBT=505+1376+27102-63   # 2026-06-30: current LTD + short-term + LTD and other long-term obligations - cash
n=len(yrs)
net_ltd=[a-b for a,b in zip(ltd_i,ltd_r)]
spend=[c+r for c,r in zip(capex,remov)]
cap=[ALLOWED_DEBT*s for s in spend]
tot_net_ltd=sum(net_ltd); tot_cap=sum(cap)
credit_total=min(tot_net_ltd,tot_cap)
print("net LTD raised by year",net_ltd,"total",tot_net_ltd,"; cap (48.8 pct x spending) total %.0f"%tot_cap,"-> credit",credit_total)
pre=[o-h-s-sp-nc for o,h,s,sp,nc in zip(ocf,ohio,sbc,spend,nci)]
eq_year=[p+l for p,l in zip(pre,net_ltd)]
print("equity-only owner cash by year (net LTD credited in its year):",eq_year)
eq_mean=(sum(pre)+credit_total)/n
print("CENTRAL equity-only mean: %.0f  per share %.2f  yield at price %.2f%%"%(eq_mean,eq_mean/SH,100*eq_mean/(SH*PRICE)))
# variant A: credit at the cap (assets funded at the allowed debt share)
capvar=[p+c for p,c in zip(pre,cap)]
cv_mean=sum(capvar)/n
print("variant, credit at the allowed share each year:",[round(x) for x in capvar],"mean %.0f per share %.2f yield %.2f%%"%(cv_mean,cv_mean/SH,100*cv_mean/(SH*PRICE)))
# variant B: depreciation in place of all spending, no debt credit
dv=[o-h-s-d-nc for o,h,s,d,nc in zip(ocf,ohio,sbc,dep,nci)]
dv_mean=sum(dv)/n
print("variant, depreciation for spending:",dv,"mean %.0f per share %.2f yield %.2f%%"%(dv_mean,dv_mean/SH,100*dv_mean/(SH*PRICE)))
h1=(dv[0]+dv[1])/2; h2=(dv[3]+dv[4])/2; g=(h2/h1)**(1/3)-1
print("  halves (2021-22 vs 2024-25): %.0f -> %.0f, growth %.2f%%/yr"%(h1,h2,100*g))
def val(cash,g,r,yrs=10):
    v=0;c=cash
    for t in range(1,yrs+1):
        c*=1+g; v+=c/(1+r)**t
    v+=c/r/(1+r)**yrs   # zero nominal growth after year ten
    return v
for name,base,g_ in [("central equity-only",eq_mean,0.0),("cap variant",cv_mean,0.0),("dep variant no growth",dv_mean,0.0),("dep variant halves growth",dv_mean,g)]:
    print("%-28s value at sovereign %.2f/sh ; at 10%% %.2f/sh ; return at price (perp+g approx) %.2f%%"%(name,val(base,g_,SOV)/SH,val(base,g_,FLOOR)/SH,100*(base/(SH*PRICE))*(1+g_)+100*g_))
# all-equity basis beside
un=[p+i*(1-TAX) for p,i in zip(pre,intp)]
un_mean=sum(un)/n
print("all-equity unlevered owner cash by year",[round(x) for x in un],"mean %.0f"%un_mean)
print("net debt 2026-06-30 %.0f"%NETDEBT)
print("all-equity: value at sovereign %.2f/sh ; fair at 10%% %.2f/sh"%((val(un_mean,0,SOV)-NETDEBT)/SH,(val(un_mean,0,FLOOR)-NETDEBT)/SH))
print("equity-only fair price at 10%% (central): %.2f/sh"%(val(eq_mean,0,FLOOR)/SH))
print("owner cash needed for 10%% at the price: %.0f/yr"%(0.10*SH*PRICE))
