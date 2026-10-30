# Owner cash and Q7 arithmetic for the MAR run, from the filed cash-flow statements (USD millions).
# Sources: 10-K FY2019 (0001628280-20-002376) for 2017-2019; FY2022 (0001628280-23-003485) for 2020-2022;
# FY2025 (0001048286-26-000007) for 2023-2025. Acquisitions inside capex from the 10-K notes/MD&A.
Y = [2017,2018,2019,2020,2021,2022,2023,2024,2025]
OCF   = dict(zip(Y,[2227,2357,1685,1639,1177,2363,3170,2749,3212]))
SBC   = dict(zip(Y,[181,184,187,201,182,192,205,237,236]))
CAPEX = dict(zip(Y,[240,556,653,135,183,332,452,750,604]))
ACQ_IN_CAPEX = dict(zip(Y,[0,255,334,0,0,0,0,200,0]))   # Sheraton Phoenix 2018; W Union Sq 206 + Elegant 128 in 2019; Sheraton Grand Chicago ~200 in 2024
ACQ_LINE = dict(zip(Y,[0,0,0,0,0,0,101,26,350]))        # "Asset acquisitions" line (City Express 2023, citizenM 2025)
ACQ_IN_OCF = dict(zip(Y,[0,0,0,0,0,0,0,300,0]))        # 2024 guarantee settlement for the Sheraton Grand Chicago purchase
DISP  = dict(zip(Y,[1418,479,395,260,12,1,71,16,9]))
LADV  = dict(zip(Y,[93,13,30,41,13,11,77,10,35]))
LCOL  = dict(zip(Y,[187,48,51,8,40,14,61,36,22]))
OTHI  = dict(zip(Y,[-61,-10,-47,-57,-43,31,33,0,10]))
INTX  = dict(zip(Y,[288,340,394,445,420,403,565,695,809]))
INTI  = dict(zip(Y,[38,22,26,27,28,26,30,40,42]))
LOY   = dict(zip(Y,[298,520,257,535,-28,-119,301,514,473]))
FEES  = dict(zip(Y,[3295,3638,3823,1683,2694,4078,4824,5170,5438]))  # gross fee revenues
TAX = 0.24   # CONVENTION of the run: after-tax interest at the 2024-2025 effective rate (776/3151, 793/3394)
MAINT = 250  # filer's own maintenance guidance: ~200 (2020), ~220 (2021), ~250 (2022), ~300 (2023), ~250 (2024)
oc, ocu, npur, capex_org, ocu_x = {}, {}, {}, {}, {}
for y in Y:
    capex_org[y] = CAPEX[y]-ACQ_IN_CAPEX[y]
    oc[y] = OCF[y]+ACQ_IN_OCF[y]-SBC[y]-capex_org[y]-(LADV[y]-LCOL[y])+OTHI[y]
    ocu[y] = oc[y] + (INTX[y]-INTI[y])*(1-TAX)
    ocu_x[y] = ocu[y]-LOY[y]
    npur[y] = ACQ_IN_CAPEX[y]+ACQ_LINE[y]+ACQ_IN_OCF[y]-DISP[y]
print("year  OCF  ownercash(lev)  unlevered  ex-loyalty  netpurch  capex_org  fees  OCu/fees")
for y in Y: print(y, OCF[y], oc[y], round(ocu[y]), round(ocu_x[y]), npur[y], capex_org[y], FEES[y], f"{ocu[y]/FEES[y]:.0%}")
avg = lambda d, ys: sum(d[y] for y in ys)/len(ys)
cyc = [2019,2020,2021,2022,2023,2024,2025]; win=[2021,2022,2023,2024,2025]
b_cyc, b_win = avg(ocu,cyc), avg(ocu,win)
print(f"cycle 2019-25 unlevered avg {b_cyc:.0f}; literal window 2021-25 {b_win:.0f}; levered cycle {avg(oc,cyc):.0f}; window levered {avg(oc,win):.0f}")
print(f"ex-loyalty cycle {avg(ocu_x,cyc):.0f}; net purchases/yr cycle {avg(npur,cyc):.0f}, window {avg(npur,win):.0f}; capex_org cycle {avg(capex_org,cyc):.0f}")
pre, post = avg(ocu,[2017,2018,2019]), avg(ocu,[2023,2024,2025])
g = (post/pre)**(1/6)-1
gf = (avg(FEES,[2023,2024,2025])/avg(FEES,[2017,2018,2019]))**(1/6)-1
print(f"pre 2017-19 {pre:.0f}, post 2023-25 {post:.0f}, growth between them {g:.2%}; fee growth same halves {gf:.2%}")
g_win = (ocu[2025]/ocu[2021])**(1/4)-1
print(f"literal end-year growth 2021-25 {g_win:.2%} (meaningless: 2021 trough)")
r = 0.0556
def val(base, g, r, yrs=10, purch=0.0):
    # years 1-10: (base - purch) grown at g; after year ten growth and purchases stop (spec (c)): base grown, flat
    pv=0
    for t in range(1,yrs+1):
        pv+=(base-purch)*(1+g)**t/(1+r)**t
    return pv + base*(1+g)**yrs/r/(1+r)**yrs
ND, SH, P = 16834, 260.766, 371.50
maint_base = b_cyc + (avg(capex_org,cyc)-MAINT)
grow_base = b_cyc; P_C = avg(npur,cyc)
cap_ok = ((grow_base)*(1+g)**10)/(FEES[2025]*(1+gf)**10)
print(f"cap check: yr10 owner cash / yr10 fees = {cap_ok:.0%} vs highest share {max(ocu[y]/FEES[y] for y in Y):.0%}")
lo = val(maint_base,0,r); hi = val(grow_base,g,r,purch=P_C)
lo_all = val(b_cyc,0,r)
print(f"bottom (maint-only, no growth) EV {lo:.0f}; all-spending no growth {lo_all:.0f}; top (growth {g:.2%}) EV {hi:.0f}")
for nm,v in [("bottom",lo),("top",hi),("all-spend no-growth",lo_all)]: print(nm, f"per share {(v-ND)/SH:.2f}")
print(f"width {(hi-ND)/(lo-ND):.2f}x on equity; {hi/lo:.2f}x on EV")
EV = P*SH+ND
print(f"market cap {P*SH:.0f}, EV {EV:.0f}; yield on EV of cycle base {b_cyc/EV:.2%}, of 2025 {ocu[2025]/EV:.2%}")
# implied return of the top case at the price
def irr(base,g,target):
    lo_r,hi_r=0.0001,0.5
    for _ in range(100):
        m=(lo_r+hi_r)/2
        if val(base,g,m)>target: lo_r=m
        else: hi_r=m
    return m
print(f"expected return at price: top case {irr(grow_base,g,EV):.2%} (purchases ignored, generous), bottom case {irr(maint_base,0,EV):.2%}")
# fair price: each end valued at 10%, averaged, less net debt
f_lo, f_hi = val(maint_base,0,0.10), val(grow_base,g,0.10,purch=P_C)
fair = ((f_lo+f_hi)/2-ND)/SH
print(f"fair all-equity: lo {f_lo:.0f} hi {f_hi:.0f} -> {fair:.2f}/sh")
# equity-only: owner cash after interest (levered cycle), against market value
lev_m = avg(oc,cyc) + (avg(capex_org,cyc)-MAINT); lev_g = avg(oc,cyc)
fe = ((val(lev_m,0,0.10)+val(lev_g,g,0.10,purch=P_C))/2)/SH
print(f"fair equity-only {fe:.2f}/sh; equity-only range {val(lev_m,0,r)/SH:.2f} to {val(lev_g,g,r,purch=P_C)/SH:.2f}")
# literal window beside
lw_lo = val(b_win+(avg(capex_org,win)-MAINT),0,r); lw_hi = val(b_win,g,r,purch=avg(npur,win))
print(f"literal window range per share {(lw_lo-ND)/SH:.2f} to {(lw_hi-ND)/SH:.2f}")
# ex-loyalty-float beside
xl_lo = val(avg(ocu_x,cyc)+(avg(capex_org,cyc)-MAINT),0,r); xl_hi=val(avg(ocu_x,cyc),g,r,purch=P_C)
print(f"ex-loyalty-float range per share {(xl_lo-ND)/SH:.2f} to {(xl_hi-ND)/SH:.2f}")
# what growth would the top case need to earn 10% at the price? search g
def need_g(base,target,r=0.10):
    a,b=0.0,0.6
    for _ in range(100):
        m=(a+b)/2
        if val(base,m,r)<target: a=m
        else: b=m
    return m
print(f"growth needed for 10 years (then flat) to earn 10% at the price: {need_g(grow_base,EV):.2%}")

# no-growth all-spending at 10% and the bottom/top at 10% for the record
print(f"at 10%: bottom EV {f_lo:.0f} ({(f_lo-ND)/SH:.2f}/sh), top EV {f_hi:.0f} ({(f_hi-ND)/SH:.2f}/sh)")
print(f"net debt used {ND}; shares {SH}M; price {P}")
print(f"equity-only basis: levered cycle owner cash {avg(oc,cyc):.0f}, maintenance-adjusted {lev_m:.0f}; market cap {P*SH:.0f}; yield {avg(oc,cyc)/(P*SH):.2%}")
