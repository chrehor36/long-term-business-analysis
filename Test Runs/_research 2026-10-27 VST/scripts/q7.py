# COMPUTATION, Q7 (and the reporting figures). USD millions except per share.
import statistics as st
exec(open(__file__.replace("q7.py","owner_cash.py")).read().split("rows=[]")[0])  # reuse inputs
GROWTH=[None,104,401,440,475,698,800,648]  # MD&A growth and development (FY2020, FY2022, FY2024 10-Ks); 2025 FY2025 Note 21 basis
GROWTH_NEW={2023:205,2024:351,2025:648}   # FY2025 10-K Note 21 basis
oc={}
for i,y in enumerate(Y):
    pre = OCF[i] + INT_PAID[i] + (TAX_PAID[i] or 0)
    spend = CAPEX[i] - ALLOW_NET[i] - NDT_NET[i] - PPE_PROC[i] - INS_PROC[i] - ITC_PROC[i] - OTHER_INV[i]
    ebitx = PRETAX[i] + INTEXP[i] + MTM_COM[i] - PTC_REV[i]   # PTC taken out of the taxed base (transferable credit, priced separately)
    tax = T*ebitx
    ae = pre - SBC[i] - spend - tax - PTC_REV[i]
    eq = ae - INT_PAID[i]*(1-T) - PREF_DIV[i]
    oc[y]=dict(ae=ae,eq=eq,g=GROWTH[i])
for y in Y: print(y, {k:(round(v) if v is not None else None) for k,v in oc[y].items()})
def avg(a,b,k,maint=False,new=False):
    vals=[]
    for y in range(a,b+1):
        v=oc[y][k]
        if maint:
            g = GROWTH_NEW.get(y, oc[y]['g']) if new else oc[y]['g']
            v+= g
        vals.append(v)
    return st.mean(vals)
r=0.0531; SH=335.635; PRICE=141.73
NETDEBT = 17719+1876+300+613-435   # 2026-06-30 10-Q: LTD + current LTD + AR financing + forward repurchase - cash
PREF=2476
ND = NETDEBT+PREF
PTC_AVG = st.mean(PTC_REV[3:])     # window average, 2021-2025
def ann(rate,n): return (1-(1+rate)**-n)/rate
def shelters(rate):
    return PTC_AVG*ann(rate,7) + 1078/(1+rate)**1.5   # PTC 2026-2032; NOL deferred tax asset used over ~3 years (midpoint 1.5)
cases = {
 "central: cycle 2019-2023, maintenance only (old MD&A growth series)": avg(2019,2023,'ae',True),
 "literal window 2021-2025, maintenance only (latest-filing growth basis)": avg(2021,2025,'ae',True,True),
 "literal window 2021-2025, all spending": avg(2021,2025,'ae'),
 "cycle 2019-2023, all spending": avg(2019,2023,'ae'),
 "information only: 2023-2025, maintenance only (latest basis)": avg(2023,2025,'ae',True,True),
}
print(f"\nmarket cap {SH*PRICE:,.0f}; net debt {NETDEBT:,} + preferred {PREF:,} = {ND:,}; EV {SH*PRICE+ND:,.0f}")
print(f"shelters PV at 5.31%: {shelters(r):,.0f}; at 10%: {shelters(0.10):,.0f}  (PTC window avg {PTC_AVG:.0f}/yr)")
print("\nALL-EQUITY, no growth (growth not measurable; specific (b))")
for k,b in cases.items():
    v=b/r+shelters(r); v10=b/0.10+shelters(0.10)
    print(f" {k}\n    base {b:7.0f}/yr  value@5.31% EV {v:8.0f} -> per share {(v-ND)/SH:7.2f}   @10% EV {v10:8.0f} -> per share {(v10-ND)/SH:7.2f}   yield at price {b/(SH*PRICE+ND)*100:4.2f}%")
print("\nEQUITY-ONLY, no growth")
eqc = {
 "central: cycle 2019-2023, maintenance only": avg(2019,2023,'eq',True),
 "literal 2021-2025, maintenance only": avg(2021,2025,'eq',True,True),
 "literal 2021-2025, all spending": avg(2021,2025,'eq'),
 "information only: 2023-2025, maintenance only": avg(2023,2025,'eq',True,True),
}
for k,b in eqc.items():
    v=b/r+shelters(r); v10=b/0.10+shelters(0.10)
    print(f" {k}\n    base {b:7.0f}/yr  @5.31% per share {v/SH:7.2f}   @10% per share {v10/SH:7.2f}   yield at price {b/(SH*PRICE)*100:4.2f}%")
# growth needed for the floor at the price, central base, no growth spending charged (generous)
B=cases[list(cases)[0]]; target=SH*PRICE+ND-shelters(0.10)
def val(g): return sum(B*(1+g)**t/1.1**t for t in range(1,11)) + B*(1+g)**10/0.10/1.1**10
lo,hi=0,1
for _ in range(100):
    m=(lo+hi)/2
    lo,hi=(m,hi) if val(m)<target else (lo,m)
print(f"\ngrowth needed for 10 years (then none) for the central base to earn 10% at the price, with no growth spending charged: {lo*100:.1f}%/yr; year-10 owner cash {B*(1+lo)**10:,.0f}")
# Cogentrix beside (signed, unclosed): no filed earnings -> credited at nothing; financing added
cog_nd = 2300+1500; cog_sh=5.0
v=B/r+shelters(r)
print(f"Cogentrix beside: central per share {(v-ND-cog_nd)/(SH+cog_sh):.2f} (net debt +{cog_nd}, shares +{cog_sh}M, earnings credited at nothing: none filed)")
