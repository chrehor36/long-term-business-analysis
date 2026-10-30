# Q7 arithmetic for the WEC run of 2026-10-27. All inputs from the filed statements (accessions in the run file).
yrs=[2021,2022,2023,2024,2025]
OCF=[2032.7,2060.7,3018.4,3211.8,3379.4]
SBC=[15.7,34.8,9.7,39.3,48.2]
DA=[1074.3,1122.6,1264.2,1354.5,1478.5]
INV=[2330.5,2657.8,3558.2,3802.5,4874.7]   # net cash used in investing, rabbi-trust securities lines removed
WECI=[119.9,382.0,699.9,893.7,406.1]       # WECI acquisitions of contracted (non-regulated) renewables, inside INV
PTC=[81.3,107.6,168.2,200.1,261.3]         # PTCs per the tax-rate reconciliations
INT=[473.8,485.2,653.4,785.7,858.5]        # interest paid
REV=[8316.0,9597.4,8893.0,8599.9,9800.1]
SOV=0.0531; FLOOR=0.10; TAX=0.27
SH=325.849383; PRICE=111.12
NETDEBT=19216.3+1413.5+415.8+1934.1-50.0
LTD20=11672.8+785.8+55.3; LTD25=18498.1+1519.4+372.0-(67.4+9.3)
CAP=0.47
avg=lambda x:sum(x)/len(x)
ocm_lit=[o-s-d for o,s,d in zip(OCF,SBC,DA)]
ocm=[o-p for o,p in zip(ocm_lit,PTC)]
oca=[o-s-i for o,s,i in zip(OCF,SBC,INV)]
gs=[i-d for i,d in zip(INV,DA)]
gs_reg=[g-w for g,w in zip(gs,WECI)]
print("owner cash after maintenance (D&A), literal :",[round(x,1) for x in ocm_lit],"avg",round(avg(ocm_lit),1))
print("owner cash after maintenance, PTC removed  :",[round(x,1) for x in ocm],"avg",round(avg(ocm),1))
print("owner cash after ALL spending              :",[round(x,1) for x in oca],"avg",round(avg(oca),1))
print("growth spending (all spending less D&A)    :",[round(x,1) for x in gs],"avg",round(avg(gs),1))
print("growth spending ex WECI acquisitions       :",[round(x,1) for x in gs_reg],"avg",round(avg(gs_reg),1))
ltd_inc=(LTD25-LTD20)/5
credit=min(ltd_inc,CAP*avg(gs_reg))
print("LTD end-2020",round(LTD20,1),"end-2025 ex securitization",round(LTD25,1),"increase/yr",round(ltd_inc,1),"cap",round(CAP*avg(gs_reg),1),"credit",round(credit,1))
g_shown=(ocm[-1]/ocm[0])**0.25-1; g_sales=(REV[-1]/REV[0])**0.25-1
print("shown growth (PTC-out series) %.2f%%  literal %.2f%%  sales growth %.2f%%"%(100*g_shown,100*((ocm_lit[-1]/ocm_lit[0])**0.25-1),100*g_sales))
share=[o/r for o,r in zip(ocm,REV)]; print("owner cash / sales by year",[round(100*s,1) for s in share])
base=avg(ocm); yr10=base*(1+g_shown)**10; print("shown rate carried ten years: owner cash yr10",round(yr10),"vs sales yr10 at sales growth",round(REV[-1]*(1+g_sales)**10),"share %.1f%%"%(100*yr10/(REV[-1]*(1+g_sales)**10)))
ptc=avg(PTC)
def ann(r,n=10): return (1-(1+r)**-n)/r
def shelter(r): return ptc*ann(r)
def nogrowth(oc,r): return oc/r
def growth(oc,gsnet,g,r):
    pv=sum((oc-gsnet)*(1+g)**t/(1+r)**t for t in range(1,11))
    term=oc*(1+g)**10/r/(1+r)**10
    return pv+term
gsnet=avg(gs)-credit
print("growth spending charged to equity: yr1 %.1f yr10 %.1f (gross yr1 %.1f, credit yr1 %.1f)"%(gsnet*(1+g_sales),gsnet*(1+g_sales)**10,avg(gs)*(1+g_sales),credit*(1+g_sales)))
def report(label,oc,gsn,g,extra=0,debt=0):
    out={}
    for r in (SOV,FLOOR):
        a=nogrowth(oc,r)+shelter(r)-debt; b=growth(oc,gsn,g,r)+shelter(r)-debt
        out[r]=(a,b)
        print(f"  {label} @{r:.4f}: no-growth {a:,.0f} (${a/SH:.2f})  growth {b:,.0f} (${b/SH:.2f})")
    fair=(out[FLOOR][0]+out[FLOOR][1])/2
    print(f"  {label} FAIR (avg of ends at 10%): {fair:,.0f}  ${fair/SH:.2f}/share; range at sovereign ${min(out[SOV])/SH:.2f} to ${max(out[SOV])/SH:.2f}")
    return out
print("CENTRAL equity-only, PTC at statutory + shelter, growth cut to sales growth:")
report("central",base,gsnet,g_sales)
print("BESIDE: literal window (PTC left in owner cash, no shelter):")
for r in (SOV,FLOOR):
    a=avg(ocm_lit)/r; b=growth(avg(ocm_lit),gsnet,g_sales,r); print(f"  literal @{r}: no-growth ${a/SH:.2f} growth ${b/SH:.2f}")
print("BESIDE: base without aberrational 2021 (2022-2025):")
b2=avg(ocm[1:]); print("  base",round(b2,1)); report("ex2021",b2,gsnet,g_sales)
print("BESIDE: all-equity (owner cash before after-tax interest; growth spending with no debt credit; less net debt %.1f):"%NETDEBT)
oce=base+avg(INT)*(1-TAX); print("  owner cash before interest",round(oce,1))
report("all-equity",oce,avg(gs),g_sales,debt=NETDEBT)
print("BESIDE: debt credit on all growth spending incl. WECI (cap on %.1f):"%avg(gs))
c2=min(ltd_inc,CAP*avg(gs)); report("credit-incl-WECI",base,avg(gs)-c2,g_sales)
mc=PRICE*SH; print("market cap %.0f; owner cash yield at price: central %.2f%%, literal %.2f%%, 2023-25 literal %.2f%%"%(mc,100*base/mc,100*avg(ocm_lit)/mc,100*avg(ocm_lit[2:])/mc))
print("forward shares (unsettled) 6.392021M; diluted count",round(SH+6.392021,3))
print("retained 2021-2025: NI-div",round(sum([1300.3,1408.1,1331.7,1527.2,1557.5])-sum([854.8,917.9,984.2,1056.2,1147.8]),1))
