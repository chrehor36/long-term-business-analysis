# COMPUTATION, NOT A CLEARANCE. Q7 arithmetic for the CPYYY run (the file closed OUT at Q2).
# Sources: statutory Group Cash Flow Statements (AR2022 p.125, AR2023 p.131, AR2025 p.138 printed), lease cash from the leases
# notes, growth spending from the AR2025 CFO report net-investment table (p.20), D&A from the cash-flow statements,
# adjusted net cash at 30 June 2026 (H1 2026 p.2), shares from the RNS of 1 Oct 2026, BoE 30y spot 5.864% (15 Oct 2026).
yrs = [2021, 2022, 2023, 2024, 2025]
ocf      = [1611, 1314, 2752, 1149, 695]     # net cash flow from operating activities (after tax, pension deficit, WC, margin cash)
op_int   = [0, 30, 20, 16, 16]               # operating interest paid (added back on the all-equity basis)
div_jv   = [2, 60, 220, 355, 135]            # dividends received from JVs and associates (mainly the nuclear associate)
capex    = [420-36, 371-11, 335-0, 416-0, 554-12]   # PP&E and intangibles bought, net of sales
dna      = [768, 669, 518, 473, 428]         # depreciation and amortisation (depreciation variant)
acq_net  = [-14+70+2, 12+92-18, -34+55-9, -92+4+0, -22+119-609]  # businesses and JVs bought, net of businesses sold (continuing)
lease    = [103, 162, 105, 108, 104]         # lease cash (capital element 2021-22; capital plus interest 2023-25)
nci      = [0, 273, 17, 0, 0]                # distributions to non-controlling interests (Spirit Energy minority)
int_rec  = [2, 46, 267, 317, 227]
fin_int  = [233, 172, 286, 283, 181]
growth_spend = [0, 0, 0, 104, 387+208+271]   # MAP 2024; Sizewell C, Grain LNG, MAP 2025 (CFO report)
rf=0.05864; floor=0.10
shares=4619.492850; price_p=150.5; netcash=709; fx=1.3253
mcap=shares*price_p/100; ev=mcap-netcash
avg=lambda s: sum(s)/len(s)

def series(basis, maint, dep=False):
    out=[]
    for i in range(5):
        c = capex[i] if not dep else dna[i]
        v = ocf[i]+op_int[i]+div_jv[i]-c+acq_net[i]-lease[i]-nci[i]
        if basis=="eq": v += int_rec[i]-fin_int[i]-op_int[i]
        if maint: v += growth_spend[i]
        out.append(v)
    return out
def growth(s):
    if s[0]>0 and s[-1]>0: return (s[-1]/s[0])**(1/4)-1, "end years"
    a=(s[0]+s[1])/2; b=(s[3]+s[4])/2
    if a>0 and b>0: return (b/a)**(1/3)-1, "halves (series changes sign)"
    return None, "meaningless: no-growth case alone"
def pv(base,g,r,after10_addback=0.0):
    v=0; c=base
    for t in range(1,11):
        c=c*(1+g); v+=c/(1+r)**t
    v+=((c+after10_addback)/r)/(1+r)**10
    return v
def implied(base,g,target,addb=0.0):
    lo,hi=-0.5,2.0
    for _ in range(200):
        mid=(lo+hi)/2
        if pv(base,g,mid,addb)>target: lo=mid
        else: hi=mid
    return mid
cases=[("A all-equity, maintenance only (CENTRAL)","ae",True,False),
       ("B all-equity, all spending (beside)","ae",False,False),
       ("C all-equity, maintenance only, depreciation variant (beside)","ae",True,True),
       ("D equity-only, maintenance only (beside)","eq",True,False),
       ("E equity-only, all spending (beside)","eq",False,False)]
print(f"market cap GBPm {mcap:.0f}; adjusted net cash 30 Jun 2026 {netcash}; EV {ev:.0f}")
for name,basis,maint,dep in cases:
    s=series(basis,maint,dep); b=avg(s); g,how=growth(s)
    addb = -avg(acq_net) if not maint else 0.0   # purchases stop after year ten (all-spending cases)
    gg = g if g is not None else 0.0
    bot_g=min(gg,0.0); top_g=max(gg,0.0)
    adj = netcash if basis=="ae" else 0.0
    target = ev if basis=="ae" else mcap
    pb=pv(b,bot_g,rf,addb); pt=pv(b,top_g,rf,addb)
    b10=pv(b,bot_g,floor,addb); t10=pv(b,top_g,floor,addb)
    ps=lambda v:(v+adj)/shares*100
    fair=ps((b10+t10)/2)
    print(f"\n== {name}\n series {[round(x) for x in s]} avg {b:.0f}; growth {('%.1f%%'%(g*100)) if g is not None else 'n/a'} ({how})")
    print(f" range at {rf*100:.3f}%: whole {pb:.0f} to {pt:.0f}; per share {ps(pb):.1f}p to {ps(pt):.1f}p; width {pt/pb:.2f}x" if pb>0 else f" range: {pb:.0f} to {pt:.0f}")
    print(f" ends at 10%: {b10:.0f} and {t10:.0f}; FAIR PRICE {fair:.1f}p a share = ${fair/100*fx*4:.2f} an ADS")
    print(f" implied return at the price: bottom case {implied(b,bot_g,target,addb)*100:.1f}%, top case {implied(b,top_g,target,addb)*100:.1f}%")
# literal window with the two crisis years left out (a CONVENTION of this run, beside only)
s=series("ae",True,False); x=[s[0],s[3],s[4]]; b=avg(x)
print(f"\n== F beside: central basis, 2022 and 2023 left out, avg of 2021, 2024, 2025 = {b:.0f}; growth 2021->2025 {((s[4]/s[0])**0.25-1)*100:.1f}%")
g=(s[4]/s[0])**0.25-1
pb=pv(b,g,rf); pt=pv(b,0,rf); b10=pv(b,g,floor); t10=pv(b,0,floor)
ps=lambda v:(v+netcash)/shares*100
print(f" range {ps(pb):.1f}p to {ps(pt):.1f}p; fair {ps((b10+t10)/2):.1f}p; implied bottom {implied(b,g,ev)*100:.1f}% top {implied(b,0,ev)*100:.1f}%")
