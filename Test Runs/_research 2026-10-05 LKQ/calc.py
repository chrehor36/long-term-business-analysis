# COMPUTATION - NOT A CLEARANCE. Arithmetic for the LKQ run of 2026-10-05.
ocf  ={2016:635.0,2017:518.9,2018:710.7,2019:1064.0,2020:1443.9,2021:1367.0,2022:1250.0,2023:1356.0,2024:1121.0,2025:1063.0}
sbc  ={2016:22.3,2017:22.8,2018:22.8,2019:27.7,2020:29.1,2021:33.7,2022:38.0,2023:40.0,2024:30.0,2025:34.0}
capex={2016:207.1,2017:179.1,2018:250.0,2019:265.7,2020:172.7,2021:293.5,2022:222.0,2023:358.0,2024:311.0,2025:216.0}
da   ={2016:198.3,2017:230.2,2018:294.1,2019:314.4,2020:299.5,2021:284.0,2022:264.0,2023:319.0,2024:406.0,2025:418.0}
fl   ={2016:0,2017:0,2018:9.0,2019:11.7,2020:11.8,2021:13.4,2022:14.0,2023:19.0,2024:28.0,2025:30.0}
rev  ={2016:8584.0,2017:9736.9,2018:11876.7,2019:12506.1,2020:11628.8,2021:13088.5,2022:12794.0,2023:13866.0,2024:14355.0,2025:13651.0}
# Self Service (sold 2025-09-30) free cash flow: 2024 ~40, 2025 ~50 as the 10-K states;
# 2021-2023 estimated (CONVENTION of this run): segment EBITDA less segment capex less 25% tax on (EBITDA - capex)
ss_ebitda={2021:175,2022:83,2023:36}; ss_capex={2021:16,2022:14,2023:36}
ss={y:round((ss_ebitda[y]-ss_capex[y])*0.75) for y in ss_ebitda}; ss[2024]=40; ss[2025]=50
oc={y:ocf[y]-sbc[y]-capex[y]-fl[y] for y in ocf}
ocd={y:ocf[y]-sbc[y]-da[y]-fl[y] for y in ocf}
print("year  OCF   SBC  capex  FL   OC(capex)  OC(D&A)  OC/rev  SS  OC cont")
for y in ocf:
    print(y, ocf[y], sbc[y], capex[y], fl[y], round(oc[y],1), round(ocd[y],1), f"{100*oc[y]/rev[y]:.1f}%", ss.get(y,'-'), round(oc[y]-ss.get(y,0),1) if y>=2021 else '-')
yrs=[2021,2022,2023,2024,2025]
avg=sum(oc[y] for y in yrs)/5; avgd=sum(ocd[y] for y in yrs)/5
cont={y:oc[y]-ss[y] for y in yrs}; avgc=sum(cont.values())/5
print("5yr avg capex basis %.1f  D&A basis %.1f  continuing %.1f"%(avg,avgd,avgc))
g_filed=(oc[2025]/oc[2021])**0.25-1; g_cont=(cont[2025]/cont[2021])**0.25-1
print("shown growth 2021->2025: as filed %.2f%%  continuing %.2f%%"%(100*g_filed,100*g_cont))
ten=sum(oc[y] for y in range(2016,2026))/10
mar=sum(oc[y]/rev[y] for y in range(2016,2026))/10
print("10yr avg OC %.1f ; 10yr avg OC/revenue %.2f%% -> x 2025 revenue = %.1f"%(ten,100*mar,mar*rev[2025]))
# TTM to 2026-06-30
ttm_ocf=1063-293+55; ttm_capex=216-107+91; ttm_sbc=34-17+18; ttm_fl=30
print("TTM owner cash ~ %.0f (OCF %d, capex %d, SBC %d, FL %d)"%(ttm_ocf-ttm_capex-ttm_sbc-ttm_fl,ttm_ocf,ttm_capex,ttm_sbc,ttm_fl))
def pv(x,g,r,n=10):
    s=0; c=x
    for t in range(1,n+1):
        c=c*(1+g); s+=c/(1+r)**t
    return s + c/r/(1+r)**n
shares=253.002; price=22.41; sov=0.0563
print("market cap %.0f"%(shares*price))
for name,x,g in (("continuing, no growth",avgc,0.0),("continuing, shown growth",avgc,g_cont),("as filed, no growth",avg,0.0),("as filed, shown growth",avg,g_filed),("whole-cycle 10yr margin, no growth",mar*rev[2025],0.0),("whole-cycle, shown growth",mar*rev[2025],g_cont),("TTM, no growth",ttm_ocf-ttm_capex-ttm_sbc-ttm_fl,0.0),("TTM, shown growth",ttm_ocf-ttm_capex-ttm_sbc-ttm_fl,g_cont)):
    v=pv(x,g,sov); print("%-36s X=%.0f g=%.2f%%  value %.0f  per share $%.2f"%(name,x,100*g,v,v/shares))
# fair price: central case (midpoint growth) at the floor, after-tax equivalent
t=0.255  # 2025 effective rate on continuing ops: 204 tax on 800 pre-tax (10-K)
r_floor=0.10*(1-t)
gc=g_cont/2
for name,x in (("continuing",avgc),("TTM",ttm_ocf-ttm_capex-ttm_sbc-ttm_fl)):
    fv=pv(x,gc,r_floor); print("FAIR (%s, central g %.2f%%, r=%.2f%% after-tax = 10%% pre-tax at t=%.1f%%): $%.2f"%(name,100*gc,100*r_floor,100*t,fv/shares))
# expected return at price, central case: solve r
def irr(x,g,P):
    lo,hi=0.0001,1.0
    for _ in range(200):
        m=(lo+hi)/2
        if pv(x,g,m)>P: lo=m
        else: hi=m
    return m
for name,x in (("continuing",avgc),("TTM",ttm_ocf-ttm_capex-ttm_sbc-ttm_fl)):
    for g in (0.0,gc,g_cont):
        r=irr(x,g,shares*price); print("expected after-tax return at $%.2f, %s, g=%.2f%%: %.1f%% (pre-tax equiv %.1f%%)"%(price,name,100*g,100*r,100*r/(1-t)))
