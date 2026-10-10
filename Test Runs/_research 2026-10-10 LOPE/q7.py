# COMPUTATION, NOT A CLEARANCE. Owner cash (USD m) from filed cash-flow statements (XBRL transcription, checked FY2025 OCF 273,491 against the filed statement).
ocf ={2021:313.1,2022:220.8,2023:243.7,2024:290.0,2025:273.5}
sbc ={2021:11.5,2022:12.6,2023:13.2,2024:14.2,2025:13.6}
capx={2021:28.9,2022:35.2,2023:44.5,2024:37.2,2025:34.8}
pre ={2021:331.3,2022:240.1,2023:259.7,2024:291.3,2025:279.9}
opi ={2021:282.2,2022:237.5,2023:249.3,2024:275.4,2025:265.9}
tax ={2021:70.9,2022:55.4,2023:54.7,2024:65.1,2025:63.7}
r=0.056; floor=0.10; netcash=171.060+103.466; sh=26.065037
yrs=sorted(ocf)
oc={};inv={}
for y in yrs:
    t=tax[y]/pre[y]; i=pre[y]-opi[y]; inv[y]=i*(1-t)
    oc[y]=ocf[y]-sbc[y]-capx[y]-inv[y]
    print(y,f"eff tax {t*100:.1f}%  invest inc pre {i:.1f} after {inv[y]:.1f}  owner cash all-equity {oc[y]:.1f}  equity-only {oc[y]+inv[y]:.1f}")
def val(c0,g,rate,n=10):
    v=0;c=c0
    for t in range(1,n+1):
        c=c*(1+g); v+=c/(1+rate)**t
    return v + c/rate/(1+rate)**n
def report(label,ser,add_cash=True):
    c0=sum(ser.values())/len(ser)
    g_end=(ser[2025]/ser[2021])**(1/4)-1
    g_half=(((ser[2024]+ser[2025])/2)/((ser[2021]+ser[2022])/2))**(1/3)-1
    for gl,g in (('end-to-end',g_end),('halves',g_half)):
        a=val(c0,0.0,r); b=val(c0,g,r)
        lo,hi=sorted([a,b]); gm=g/2
        mid=val(c0,gm,r)
        fair=val(c0,gm,floor)
        cash=netcash if add_cash else 0
        ps=lambda v:(v+cash)/sh
        print(f"{label:28s} base {c0:6.1f} growth[{gl}] {g*100:5.2f}%  range ${ps(lo):6.2f}-${ps(hi):6.2f}  width {hi/lo:4.2f}x  mid(at r) ${ps(mid):6.2f}  FAIR(mid at 10%) ${ps(fair):6.2f}  price-implied yr1 yield {c0/(159.80*sh-cash)*100 if add_cash else c0/(159.80*sh)*100:4.2f}%")
report('ALL-EQUITY literal',oc)
report('EQUITY-ONLY literal',{y:oc[y]+inv[y] for y in yrs},add_cash=False)
ex=dict(oc); ex[2025]=oc[2025]+33.4
report('ALL-EQUITY ex-settlement',ex)
