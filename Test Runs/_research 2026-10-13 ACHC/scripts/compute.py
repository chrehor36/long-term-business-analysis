# COMPUTATION, NOT A CLEARANCE. Figures in USD millions from the filed cash-flow statements
# (10-K FY2021 0001564590-22-007930, FY2023 0000950170-24-022057, FY2025 0001193125-26-078266) and XBRL transcription.
yrs=[2021,2022,2023,2024,2025]
ocf ={2021:374.2,2022:380.6,2023:462.3,2024:129.7,2025:131.9}   # continuing ops
sbc ={2021:37.5,2022:29.6,2023:32.3,2024:37.1,2025:31.7}
capex={2021:244.8,2022:296.1,2023:424.1,2024:690.4,2025:571.8}
maint={2021:41.8,2022:60.5,2023:99.6,2024:104.0,2025:104.4}
acq ={2021:139.0,2022:9.5,2023:0.3,2024:53.5,2025:8.2}
ppe_sale={2021:3.5,2022:7.1,2023:29.4,2024:10.4,2025:23.8}
nci ={2021:1.6,2022:5.1,2023:5.1,2024:3.0,2025:3.9}
intpaid={2021:93.7,2022:65.7,2023:80.7,2024:113.4,2025:124.7}
rev ={2021:2314.4,2022:2610.4,2023:2928.7,2024:3154.0,2025:3312.8}
T=0.21
def series(kind, basis):
    out={}
    for y in yrs:
        base=ocf[y]-sbc[y]-nci[y]
        if kind=='all': base-= capex[y]-ppe_sale[y]+acq[y]
        else: base-= maint[y]
        if basis=='ae': base+= intpaid[y]*(1-T)
        out[y]=base
    return out
def pv(cf, g, r, n=10):
    # cf = year-0 base; grows at g for 10 yrs, then flat (zero nominal growth) forever, discounted at r
    v=0; c=cf
    for t in range(1,n+1):
        c*= (1+g); v+= c/(1+r)**t
    v+= c/r/(1+r)**n
    return v
for kind in ('maint','all'):
    for basis in ('ae','eq'):
        s=series(kind,basis); avg=sum(s.values())/5
        h1=(s[2021]+s[2022])/2; h2=(s[2024]+s[2025])/2
        print(kind,basis,' '.join('%d:%.1f'%(y,s[y]) for y in yrs),' avg %.1f  first-half %.1f  last-half %.1f'%(avg,h1,h2))
print('rev growth 2021-25 CAGR %.2f%%'%(((rev[2025]/rev[2021])**0.25-1)*100))
import sys
# central: maintenance case, all-equity
NETDEBT=2270.1; SH_COVER=93.100275; SH_BS=90.868250; PRICE=30.20
for kind in ('maint','all'):
    s_ae=series(kind,'ae'); s_eq=series(kind,'eq')
    a_ae=sum(s_ae.values())/5; a_eq=sum(s_eq.values())/5
    for r in (0.056,0.10):
        v_ae=pv(a_ae,0.0,r); v_eq=pv(a_eq,0.0,r)
        print('%s r=%.3f  all-equity EV %.0f -> per share (cover) %.2f (bs) %.2f | equity-only %.0f -> %.2f'%(kind,r,v_ae,(v_ae-NETDEBT)/SH_COVER,(v_ae-NETDEBT)/SH_BS,v_eq,v_eq/SH_COVER))
mcap=PRICE*SH_COVER; ev=mcap+NETDEBT
print('mcap %.1f  EV %.1f'%(mcap,ev))
for kind in ('maint','all'):
    a_ae=sum(series(kind,'ae').values())/5; a_eq=sum(series(kind,'eq').values())/5
    print(kind,'yield on EV %.2f%%  yield on mcap (eq-only) %.2f%%'%(a_ae/ev*100,a_eq/mcap*100))
print('--- decline case (maintenance, shown growth between end years)')
for basis in ('ae','eq'):
    s=series('maint',basis); a=sum(s.values())/5
    g=(s[2025]/s[2021])**0.25-1 if s[2025]>0 else None
    print(basis,'end-year g', g)
    if g is not None:
        for r in (0.056,0.10):
            v=pv(a,g,r); print('  r=%.3f EV/val %.0f per share %.2f'%(r,v,((v-NETDEBT) if basis=='ae' else v)/SH_COVER))
    # halves
    h1=(s[2021]+s[2022])/2; h2=(s[2024]+s[2025])/2
    if h1>0 and h2>0:
        gh=(h2/h1)**(1/3)-1; print('  halves g %.4f'%gh)
        for r in (0.056,0.10):
            v=pv(a,gh,r); print('  halves r=%.3f val %.0f per share %.2f'%(r,v,((v-NETDEBT) if basis=='ae' else v)/SH_COVER))
print('--- beside: legal settlement payments added back after tax (2024 400.0, 2025 147.5)')
for basis in ('ae','eq'):
    s=series('maint',basis); s[2024]+=400*(1-T); s[2025]+=147.5*(1-T); a=sum(s.values())/5
    for r in (0.056,0.10):
        v=pv(a,0,r); print(basis,'avg %.1f r=%.3f val %.0f per share %.2f'%(a,r,v,((v-NETDEBT) if basis=='ae' else v)/SH_COVER))
    print(basis,'yield at price %.2f%%'%(a/(ev if basis=='ae' else mcap)*100))
