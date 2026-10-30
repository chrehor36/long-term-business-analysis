# Owner cash after rent, PENN, from the filed cash-flow statements (USD millions).
# OCF, SBC, ESPN warrant expense, finance-lease principal (FLp), financing-obligation principal (FOp), capex, SLB proceeds, maintenance capex
data = {
 # yr: (OCF, SBC, W, FLp, FOp, capex, slb, maint, maint_source)
 2019: (703.9, 14.9, 0.0, 6.2, 51.6, 190.6, 0.0, 165.5, "XBRL PaymentsForCapitalImprovements, 10-K FY2019 vintage"),
 2021: (896.1, 35.1, 0.0, 8.5, 36.0, 244.1, 0.0, None, "not split in 10-K FY2021"),
 2022: (878.2, 58.1, 0.0, 110.5, 63.2, 263.4, 0.0, 263.4-17.1-26.0, "10-K FY2022: capex less York/Morgantown 17.1 and insured hurricane rebuild 26.0"),
 2023: (455.9, 85.9, 12.5, 47.1, 39.2, 360.0, 0.0, None, "not split in 10-K FY2023"),
 2024: (359.3, 52.9, 67.9, 50.3, 40.8, 482.7, 0.0, 229.4, "10-K FY2024"),
 2025: (508.2, 60.9, 57.1, 53.4, 43.5, 647.7, 280.0, 239.3, "10-K FY2025"),
}
known=[v[7] for v in data.values() if v[7] is not None and v is not data[2019]]
known=[data[y][7] for y in (2022,2024,2025)]
imp=sum(known)/len(known)
print("imputed maintenance for 2021, 2023 (mean of 2022, 2024, 2025):",round(imp,1))
rows={}
for y,(ocf,sbc,w,flp,fop,cap,slb,mnt,src) in data.items():
    pre=ocf-sbc-w-flp-fop
    m = mnt if mnt is not None else imp
    allc = pre-(cap-slb)
    rows[y]=(pre,allc,pre-m)
    print(y,"pre-capex",round(pre,1),"all-capex(net SLB)",round(allc,1),"maint",round(pre-m,1),"(maint",round(m,1),")")
five=[2021,2022,2023,2024,2025]
a_all=sum(rows[y][1] for y in five)/5; a_m=sum(rows[y][2] for y in five)/5
whole=[2019,2021,2022,2023,2024,2025]; a_w=sum(rows[y][2] for y in whole)/6
gross25 = rows[2025][0]-647.7
a_gross=(sum(rows[y][1] for y in [2021,2022,2023,2024])+gross25)/5
print("5yr avg all-capex net SLB",round(a_all,1),"gross capex",round(a_gross,1),"maintenance",round(a_m,1),"whole-cycle(2019,21-25) maint",round(a_w,1))
# TTM: H2 2025 + H1 2026
h1_25 = 220.1-31.7-28.5-26.7-21.5
h1_26 = 363.1-31.5-0-27.6-22.6
ttm_pre = (rows[2025][0]-h1_25)+h1_26
print("H1 2025 pre",round(h1_25,1),"H1 2026 pre",round(h1_26,1),"TTM pre",round(ttm_pre,1),"TTM less 220 maint",round(ttm_pre-220,1))
sh=134.17; r=0.0563
def ng(x,rate): return x/rate/sh
for name,x in [("all-capex",a_all),("gross",a_gross),("maint",a_m),("whole",a_w),("runrate",ttm_pre-220)]:
    print(name, round(x,1), "no-growth @5.63%: $",round(ng(x,r),2), " @10%: $",round(ng(x,0.10),2), " yield at $15.10:",round(100*x/(15.10*sh),1),"%")
# shown growth, maintenance basis, first to last
g=(rows[2025][2]/rows[2021][2])**(1/4)-1
print("shown growth maint 2021->2025",round(100*g,1),"%")
pv=0; c=rows[2025][2]
for t in range(1,11):
    c*= (1+g); pv+= c/(1+r)**t
pv+= c/r/(1+r)**10
print("shown-growth end, maint basis: PV",round(pv,1),"per share",round(pv/sh,2))
# depreciation variant 2023-2025 (D&A less finance-lease ROU amortization)
da={2023:435.1-87.5,2024:433.6-89.8,2025:446.9-91.0}
dv={y:rows[y][0]-da[y] for y in da}
print("depreciation variant",{y:round(v,1) for y,v in dv.items()},"avg",round(sum(dv.values())/3,1))
