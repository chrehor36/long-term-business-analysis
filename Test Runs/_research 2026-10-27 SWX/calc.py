# SWX run 2026-10-27: arithmetic from the filed statements of Southwest Gas Corporation (the utility)
# USD millions. Sources: 10-K FY2025 (0001692115-26-000062) for 2023-2025; FY2022 annual report exhibit
# (0001692115-23-000056, swx-20221231_d2.htm) for 2020-2022; FY2020 exhibit (0001692115-21-000008) for 2018-2019.
Y=[2018,2019,2020,2021,2022,2023,2024,2025]
OCF ={2018:382.502,2019:367.794,2020:424.061,2021:25.245,2022:284.403,2023:391.545,2024:1252.982,2025:618.815}
CAPEX={2018:682.869,2019:778.748,2020:692.216,2021:601.983,2022:683.131,2023:762.081,2024:846.590,2025:807.866}
SBC={2018:5.355,2019:5.146,2020:5.294,2021:6.392,2022:5.776,2023:4.877,2024:10.022,2025:12.989}
DA ={2018:191.816,2019:215.620,2020:235.295,2021:253.398,2022:263.043,2023:295.462,2024:303.095,2025:330.724}
NI ={2018:138.842,2019:163.171,2020:159.118,2021:187.135,2022:154.380,2023:228.412,2024:262.096,2025:300.308}
INT={2018:81.740,2019:95.026,2020:101.148,2021:97.560,2022:115.880,2023:149.830,2024:162.257,2025:181.677}
REV={2018:1357.728,2019:1368.939,2020:1350.585,2021:1521.790,2022:1935.069,2023:2494.220,2024:2482.990,2025:1942.480}
COG={2018:419.388,2019:385.164,2020:342.837,2021:430.907,2022:789.216,2023:1251.367,2024:1157.364,2025:497.636}
# working-capital lines inside OCF (changes in current assets and liabilities), as filed
WC ={2021:-22.806-2.5-343.728+57.764+7.753-70.271,
     2022:-64.414-3.2-158.975+243.276+21.754-188.737,
     2023:-35.114-4.9+188.226-253.239-8.964+2.130+19.859,
     2024:68.348-3.6+714.958-19.735+1.393-67.791,
     2025:30.322-5.0+65.277+11.086-6.043-105.550-97.340}
INTERCO={2025:105.550}   # receivable from parent: a loan inside the group, added back
EQ={2016:1667.880,2017:1609.999,2018:1782.460,2019:2005.152,2020:2233.468,2021:2527.937,2022:2569.175,2023:3183.615,2024:3235.486,2025:3524.966}
W=[2021,2022,2023,2024,2025]
avg=lambda d,ys=W: sum(d[y] for y in ys)/len(ys)
print("year  OCF   capex  SBC   D&A   OC_all  OC_maint  OCexWC_maint  NI/endEq  opmargin")
for y in Y:
    oc_all=OCF[y]+INTERCO.get(y,0)-CAPEX[y]-SBC[y]
    oc_m=OCF[y]+INTERCO.get(y,0)-SBC[y]-DA[y]
    exwc = (OCF[y]-WC[y]-SBC[y]-DA[y]) if y in WC else float('nan')
    print(y, round(OCF[y],1), round(CAPEX[y],1), round(SBC[y],1), round(DA[y],1), round(oc_all,1), round(oc_m,1), round(exwc,1), f"{NI[y]/EQ[y]:.1%}", round(REV[y]-COG[y],1))
ocf_w=avg(OCF)+sum(INTERCO.values())/5
print("window avg OCF (interco added back)", round(ocf_w,1), " avg capex",round(avg(CAPEX),1)," avg SBC",round(avg(SBC),1)," avg D&A",round(avg(DA),1))
print("avg WC lines", round(avg(WC),1), " avg OCF ex WC", round(avg({y:OCF[y]-WC[y] for y in W}),1))
CORP_AT = 6.0*(1-0.21)   # holding-company costs, CONVENTION of the run
oc_maint = ocf_w-avg(SBC)-avg(DA)-CORP_AT
oc_all   = ocf_w-avg(SBC)-avg(CAPEX)-CORP_AT
print("owner cash, maintenance (equity-only, after corp)", round(oc_maint,1), "  all-spending", round(oc_all,1))
growth_sp = avg(CAPEX)-avg(DA)
print("growth spending avg", round(growth_sp,1))
# debt credit: LT debt incl current maturities, end 2020 -> end 2025
lt0=2438.206+0.0; lt5=3433.012+75.0
credit=(lt5-lt0)/5
cap_share=(53*51.5+35*50+12*50)/100/100
print("LT debt end2020",lt0," end2025",lt5," credit/yr",round(credit,1)," cap share",round(cap_share,4)," cap",round(cap_share*growth_sp,1))
credit=min(credit,cap_share*growth_sp)
net_gs=growth_sp-credit
# growth rates
exwc_series={y:OCF[y]-WC[y]-SBC[y]-DA[y] for y in W}
g_shown=(exwc_series[2025]/exwc_series[2021])**(1/4)-1
g_sales=(REV[2025]/REV[2021])**(1/4)-1
g_margin=((REV[2025]-COG[2025])/(REV[2021]-COG[2021]))**(1/4)-1
print("shown growth (ex-WC maint series, 2021->2025)", f"{g_shown:.1%}", " sales", f"{g_sales:.1%}", " op margin", f"{g_margin:.1%}")
r=0.0531
g=min(g_sales,r)
def value(base, gs_net, g, r, years=10):
    v=0
    for t in range(1,years+1):
        v+=(base*(1+g)**t - gs_net*(1+g)**t)/(1+r)**t
    term=base*(1+g)**years/r/(1+r)**years
    return v+term
shares=72.445853
price=92.02
parent_cash=270.518-58.872
ng=oc_maint/r
gc=value(oc_maint,net_gs,g,r)
print("growth carried", f"{g:.2%}", " net growth spending yr1", round(net_gs*(1+g),1)," yr10",round(net_gs*(1+g)**10,1), " gross yr1",round(growth_sp*(1+g),1)," yr10",round(growth_sp*(1+g)**10,1))
print("EQUITY-ONLY  no-growth", round(ng,1), " growth", round(gc,1))
for lab,v in (("no-growth",ng),("growth",gc)):
    print(f"  {lab}: ${(v+parent_cash)/shares:.2f}/sh (with holding-co cash {parent_cash:.1f})  ex-cash ${v/shares:.2f}")
mc=price*shares
print("market cap", round(mc,1), " yield at price (maint)", f"{oc_maint/mc:.2%}")
# IRR at price for growth case
def npv(rate, base, gsn, g, mcap):
    return value(base,gsn,g,rate)-mcap
lo,hi=0.0001,0.5
for _ in range(100):
    mid=(lo+hi)/2
    if npv(mid,oc_maint,net_gs,g,mc-parent_cash)>0: lo=mid
    else: hi=mid
print("expected return at price, growth case", f"{mid:.2%}", "; no-growth", f"{oc_maint/(mc-parent_cash):.2%}")
# fair price: each end at 10%
f_ng=oc_maint/0.10; f_g=value(oc_maint,net_gs,g,0.10)
fair=((f_ng+f_g)/2+parent_cash)/shares
print("FAIR (equity-only) ends at 10%:", round(f_ng,1), round(f_g,1), " fair/sh", round(fair,2))
# beside: PGA-adjusted base (remove net PGA balance build over window: end2020 net -52.583, end2025 net -304.871)
pga_adj=(304.871-52.583)/5
b2=oc_maint-pga_adj
print("beside: PGA-adjusted base", round(b2,1), " no-growth $", round((b2/r+parent_cash)/shares,2), " growth $", round((value(b2,net_gs,g,r)+parent_cash)/shares,2))
# beside: deferred taxes out
dt={2021:53.237,2022:42.387,2023:71.874,2024:68.954,2025:172.454}
b3=oc_maint-avg(dt)
print("beside: deferred taxes removed, base", round(b3,1), " no-growth $", round((b3/r+parent_cash)/shares,2))
# literal window, all spending, no maintenance split
print("literal window all-spending owner cash", round(oc_all,1))
# ALL-EQUITY beside: add after-tax interest, against EV; all capex growth spending no credit
int_at=avg(INT)*(1-0.21)
ae_base=oc_maint+int_at
netdebt=3409.859+100.0-270.518
ae_ng=ae_base/r; ae_g=value(ae_base,growth_sp,g,r)
print("ALL-EQUITY base",round(ae_base,1)," net debt",round(netdebt,1)," no-growth $",round((ae_ng-netdebt)/shares,2)," growth $",round((ae_g-netdebt)/shares,2))
ae_fair=((ae_base/0.10+value(ae_base,growth_sp,g,0.10))/2-netdebt)/shares
print("ALL-EQUITY fair/sh", round(ae_fair,2))
# --- central range under specific (b): no-growth alone
print("CENTRAL no-growth alone: value/sh", round((ng+parent_cash)/shares,2), " fair (at 10%) /sh", round((oc_maint/0.10+parent_cash)/shares,2))
print("ALL-EQUITY no-growth alone fair/sh", round((ae_base/0.10-netdebt)/shares,2))
# recast series halves (literal, with WC)
lit={y:OCF[y]+INTERCO.get(y,0)-SBC[y]-DA[y] for y in W}
print("halves literal:", round((lit[2021]+lit[2022])/2,1), round((lit[2024]+lit[2025])/2,1))
# highest share of sales test for the shown 28.7%
print("2025 owner cash/sales", f"{exwc_series[2025]/REV[2025]:.1%}", " carried 10y at shown:", round(exwc_series[2025]*(1+g_shown)**10,1), " vs sales at 6.3%:", round(REV[2025]*(1+g_sales)**10,1))
print("interest cover 2025 utility (pretax+interest)/interest", round((353.131+181.677)/181.677,2))
print("own LT debt share of LT capital 2025", f"{3508.012/(3508.012+3524.966):.1%}")
