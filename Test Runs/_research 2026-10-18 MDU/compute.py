# MDU run 2026-10-18: arithmetic only. Every input is transcribed from the filings named in notes.md.
# USD millions unless stated.
import json
yrs=[2021,2022,2023,2024,2025]
# continuing-operations (pure utility) cash flow lines.
# 2022-2025: as restated in 10-K FY2024 (0000067716-25-000016) and FY2025 (0000067716-26-000014).
# 2021: CONVENTION of this run: MDU FY2023 10-K (0000067716-24-000017) continuing ops (which still held Everus)
#       less Everus's own FY2021 statements in its Form 10 (0001628280-24-042608, Ex. 99.1).
ocf  ={2021:298.947-85.449, 2022:321.615, 2023:305.333, 2024:411.813, 2025:474.090}
sbc  ={2021:12.857-1.711,   2022:7.913,   2023:5.505,   2024:8.423,   2025:6.556}
capex={2021:485.197-27.284, 2022:442.582, 2023:484.136, 2024:522.824, 2025:770.394}
remov={2021:-11.363,        2022:-11.779, 2023:1.170,   2024:-5.539,  2025:-11.283}  # cost of removal net of salvage (investing)
da   ={2021:198.240-20.270, 2022:188.560, 2023:190.450, 2024:200.078, 2025:206.708}
intx ={2021:70.709+0.130,   2022:80.683,  2023:104.624, 2024:108.347, 2025:107.749}  # interest expense, continuing
# check of the 2021 method on 2022 (same subtraction from FY2023 10-K vs restated FY2024 10-K):
chk={"ocf":(307.653-(-25.495),321.615),"capex":(478.425-35.844,442.582),"da":(210.028-21.469,188.560),"sbc":(8.982-1.068,7.913)}
T=0.21  # CONVENTION: interest added back at the 21% federal statutory rate
oc_all={y:ocf[y]-sbc[y]-capex[y]+remov[y] for y in yrs}
oc_da ={y:ocf[y]-sbc[y]-da[y] for y in yrs}
ae_da ={y:oc_da[y]+intx[y]*(1-T) for y in yrs}
ae_all={y:oc_all[y]+intx[y]*(1-T) for y in yrs}
gcap  ={y:capex[y]-remov[y]-da[y] for y in yrs}   # spending above depreciation
mean=lambda d:sum(d.values())/len(d)
print("method check 2022 (built vs restated):",{k:(round(a,1),b) for k,(a,b) in chk.items()})
print("year  OCF   SBC  capex  D&A  int | OC_all OC_DA | AE_all AE_DA | growth spend")
for y in yrs: print(y,*[round(v,1) for v in (ocf[y],sbc[y],capex[y],da[y],intx[y],oc_all[y],oc_da[y],ae_all[y],ae_da[y],gcap[y])])
print("means OC_all %.1f OC_DA %.1f AE_all %.1f AE_DA %.1f growth spend %.1f"%(mean(oc_all),mean(oc_da),mean(ae_all),mean(ae_da),mean(gcap)))
# working-capital-neutral series (OCF before changes in current assets and liabilities), shown beside
pre_wc={2021:None,2022:117.252+225.8,2023:330.117+3.3,2024:181.073+190.2,2025:191.407+204.9}
for y in [2022,2023,2024,2025]:
    print(" WC-neutral AE_DA",y, round(pre_wc[y]-sbc[y]-da[y]+intx[y]*(1-T),1))
# price, shares, net debt
price=19.00; sh=210.349456
debt=2572.457+4.700; cash=46.269; nd=debt-cash      # 10-Q 2026-06-30, 0000067716-26-000072
ev=price*sh+nd
print("mcap %.1f  net debt %.1f  EV %.1f"%(price*sh,nd,ev))
# incremental return: change in WC-neutral all-equity owner cash 2022->2025 over growth spending 2022-2024
d_oc=(pre_wc[2025]-sbc[2025]-da[2025]+intx[2025]*(1-T))-(pre_wc[2022]-sbc[2022]-da[2022]+intx[2022]*(1-T))
g_sum=gcap[2022]+gcap[2023]+gcap[2024]
r_inc=d_oc/g_sum
print("incremental cash return on growth spending: %.1f / %.1f = %.2f%%"%(d_oc,g_sum,100*r_inc))
def pv(stream,term,r):
    v=sum(c/(1+r)**(t+1) for t,c in enumerate(stream))
    return v+term/r/(1+r)**len(stream)
B=mean(ae_da); G=mean(gcap)
def caseA(r): return pv([B]*10,B,r)
def caseB(r,rinc=r_inc):
    s=[]; inc=0
    for t in range(10):
        s.append(B+inc-G); inc+=rinc*G
    return pv(s,B+inc,r)   # after year 10: no growth, growth spending stops
for lab,r in (("sovereign 5.43%",0.0543),("ten percent",0.10)):
    a,b=caseA(r),caseB(r)
    print(lab,"caseA EV %.0f -> per share %.2f | caseB EV %.0f -> per share %.2f"%(a,(a-nd)/sh,b,(b-nd)/sh))
# equity-only beside: owner cash after interest (OC_DA), against market cap
Be=mean(oc_da)
for lab,r in (("sovereign",0.0543),("ten",0.10)):
    print(" equity-only caseA",lab,"%.2f"%(Be/r/sh))
# expected return at the price (IRR) of each case, all-equity
def irr(f):
    lo,hi=0.001,0.5
    for _ in range(200):
        m=(lo+hi)/2
        if f(m)>ev: lo=m
        else: hi=m
    return m
print("expected return at the price: caseA %.2f%%  caseB %.2f%%"%(100*B/ev,100*irr(lambda r:caseB(r))))
print("caseB with r_inc = 9.5%% (allowed ROE, generous): EV at 10%% %.0f, IRR %.2f%%"%(caseB(0.10,0.095),100*irr(lambda r:caseB(r,0.095))))
# FSA beside: 7.4M shares for $139.6M (10-Q)
print("with FSA settled, caseA at sovereign per share %.2f"%((caseA(0.0543)-nd+139.6)/(sh+7.4)))
# equity-only case B beside: owner cash after interest, incremental return measured on the same equity basis
d_oc_e=(pre_wc[2025]-sbc[2025]-da[2025])-(pre_wc[2022]-sbc[2022]-da[2022])
r_inc_e=d_oc_e/g_sum
def caseBe(r):
    s=[]; inc=0
    for t in range(10):
        s.append(Be+inc-G); inc+=r_inc_e*G
    return pv(s,Be+inc,r)
print("equity-only incremental return %.2f%%"%(100*r_inc_e))
for lab,r in (("sovereign",0.0543),("ten",0.10)):
    print(" equity-only caseB",lab,"%.2f"%(caseBe(r)/sh))
fair_ae=((caseA(0.10)-nd)/sh+(caseB(0.10)-nd)/sh)/2
fair_eq=(Be/0.10/sh+caseBe(0.10)/sh)/2
print("FAIR PRICE all-equity %.2f  equity-only %.2f"%(fair_ae,fair_eq))
print("RANGE all-equity at sovereign: %.2f to %.2f ; equity-only %.2f to %.2f"%((caseA(0.0543)-nd)/sh,(caseB(0.0543)-nd)/sh,min(Be/0.0543,caseBe(0.0543))/sh,max(Be/0.0543,caseBe(0.0543))/sh))
