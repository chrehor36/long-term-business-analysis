# Q7 arithmetic for EVRG, 2026-10-23. Inputs are filed figures (10-Ks, XBRL as cross-checked; 10-Q 2026-06-30).
r=0.0529; floor=0.10; shares=230.567172; price=84.95; mcap=shares*price
yrs=[2021,2022,2023,2024,2025]
OCF={2021:1351.7,2022:1801.9,2023:1980.2,2024:1983.7,2025:2045.2}
SBC={2021:15.6,2022:18.8,2023:17.7,2024:15.2,2025:20.7}
CAPEX={2021:1972.5,2022:2166.5,2023:2334.0,2024:2336.6,2025:2796.9}
CIAC={2025:170.0,2023:-217.9}   # 2025: nonrefundable contributions in aid of construction (inflow); 2023: Persimmon Creek acquisition, net of cash (outflow, specific (c))
DA={2021:896.4,2022:929.4,2023:1076.5,2024:1114.0,2025:1162.9}
PISA_REG={2020:70.0,2021:98.5,2022:159.1,2023:168.7,2024:238.3,2025:367.1}  # 'Depreciation' regulatory asset (PISA)
LTD_IN={2021:497.3,2022:567.7,2023:2444.8,2024:1414.0,2025:1687.5}
LTD_OUT={2021:432.0,2022:410.9,2023:439.5,2024:811.5,2025:751.1}
INT_PAID={2021:356.9,2022:393.7,2023:500.9,2024:538.5,2025:586.7}
REV={2021:5586.7,2022:5859.1,2023:5508.2,2024:5847.3,2025:5961.6}
NETDEBT=1495.3+2331.0+356.0+12315.7-21.8   # 2026-06-30
DEBT_SHARE=(1495.3+12315.7)/(1495.3+12315.7+10223.0)  # LTD incl current / (LTD + equity), filer's own definition excl. short-term debt
t_stat=0.22  # filer's "statutory rate of approximately 22%" (10-K adjusted-earnings footnote)
def pisa(y): return PISA_REG[y]-PISA_REG[y-1]
def rows(ys):
    out=[]
    for y in ys:
        cap=CAPEX[y]-CIAC.get(y,0)
        maint=DA[y]+pisa(y)
        out.append(dict(y=y,ocf=OCF[y],sbc=SBC[y],cap=cap,maint=maint,netltd=LTD_IN[y]-LTD_OUT[y],
            oc_maint=OCF[y]-SBC[y]-maint, oc_all=OCF[y]-SBC[y]-cap, intpd=INT_PAID[y], rev=REV[y]))
    return out
def pv_case(c0,g,spend,years=10):
    # owner cash c0 grows at g for 10 years (year1=c0*(1+g)), less 'spend' each year for 10 years; then flat, no spend
    pv=0;c=c0
    for t in range(1,years+1):
        c=c*(1+g); pv+=(c-spend)/(1+R)**t
    pv+= c/R/(1+R)**years
    return pv
def report(label,ys):
    global R
    rs=rows(ys); n=len(rs)
    avg=lambda k: sum(x[k] for x in rs)/n
    cap_sum=sum(x["cap"] for x in rs); netltd=sum(x["netltd"] for x in rs)
    credit=min(netltd, DEBT_SHARE*cap_sum)
    maint_avg=avg("oc_maint"); all_eq=avg("oc_all")+credit/n
    grow_spend=(cap_sum-sum(x["maint"] for x in rs))/n
    grow_spend_eq=grow_spend-credit/n
    first,last=rs[0]["oc_maint"],rs[-1]["oc_maint"]
    g=(last/first)**(1/(n-1))-1
    sales_g=(rs[-1]["rev"]/rs[0]["rev"])**(1/(n-1))-1
    maxshare=max(x["oc_maint"]/x["rev"] for x in rs)
    g_used=g
    cut=""
    if g>0 and last*(1+g)**10 > maxshare*rs[-1]["rev"]*(1+sales_g)**10:
        g_used=min(sales_g,r); cut=f" (shown {g*100:.1f}% cut by (f) to sales growth {sales_g*100:.1f}%)"
    print(f"\n=== {label}: years {ys[0]}-{ys[-1]}")
    for x in rs: print(f"  {x['y']}: OCF {x['ocf']:.1f} SBC {x['sbc']:.1f} capex(net CIAC) {x['cap']:.1f} maint(D&A+PISA) {x['maint']:.1f} | owner cash after maint {x['oc_maint']:.1f} | after all capex {x['oc_all']:.1f} | net LTD {x['netltd']:.1f}")
    print(f"  avg owner cash after maintenance {maint_avg:.1f}; after all capex {avg('oc_all'):.1f}; net LTD raised {netltd:.1f}; debt-share cap {DEBT_SHARE*100:.1f}% x {cap_sum:.1f} = {DEBT_SHARE*cap_sum:.1f}; credit {credit:.1f}")
    print(f"  equity owner cash, all spending with debt credit: {all_eq:.1f}/yr")
    print(f"  growth spending {grow_spend:.1f}/yr, of which equity after credit {grow_spend_eq:.1f}/yr")
    print(f"  shown growth of owner cash after maintenance {g*100:.2f}%/yr; used {g_used*100:.2f}%{cut}")
    out={}
    for RR,tag in [(r,"sov"),(floor,"10%")]:
        R=RR
        top=maint_avg/R
        grow=pv_case(maint_avg,g_used,grow_spend_eq)
        alleq_ng=all_eq/R
        out[tag]=(top,grow,alleq_ng)
        print(f"  at {tag}: maintenance-only no-growth {top:.0f} (${top/shares:.2f}); growth case w/ equity growth spend {grow:.0f} (${grow/shares:.2f}); all-spending+credit no-growth {alleq_ng:.0f} (${alleq_ng/shares:.2f})")
    # all-equity basis beside
    ia=avg("intpd")*(1-t_stat)
    for RR,tag in [(r,"sov"),(floor,"10%")]:
        R=RR
        a=(maint_avg+ia)/R-NETDEBT; b=(avg("oc_all")+ia)/R-NETDEBT
        print(f"  ALL-EQUITY at {tag}: maint-only {(maint_avg+ia):.1f}/yr -> ${a/shares:.2f}; all-spending {(avg('oc_all')+ia):.1f}/yr -> ${b/shares:.2f}")
    # floor test at price
    print(f"  floor test: maint-only cash yield at price {maint_avg/mcap*100:.2f}%; all-spend+credit {all_eq/mcap*100:.2f}%")
    return out,maint_avg,g_used
print(f"market cap {mcap:.1f}; net debt 2026-06-30 {NETDEBT:.1f}; debt share {DEBT_SHARE*100:.1f}%")
R=r
o1=report("CENTRAL (four clean years, 2021 aberrational)",[2022,2023,2024,2025])
o2=report("LITERAL WINDOW",[2021,2022,2023,2024,2025])
# statutory tax beside (top case): pre-tax income 2025 from the tax note 188.5/0.21
pretax=188.5/0.21; extra=pretax*t_stat-6.1
print(f"\nstatutory-tax restatement beside: extra tax {extra:.1f}/yr; top case {(o1[1]-extra)/r/shares:.2f} at sovereign")
# all-equity growth case (no debt credit): c0 = maint owner cash + after-tax interest; growth spend = full growth spending
print("\nALL-EQUITY growth case (central years):")
for RR,tag in [(r,"sov"),(floor,"10%")]:
    R=RR
    c0=796.8+505.0*(1-t_stat)  # 2022-25 avg interest paid 505.0
    v=pv_case(c0,-0.0260,1282.6)-NETDEBT
    top=c0/R-NETDEBT
    print(f"  {tag}: growth case ${v/shares:.2f}; maint-only no-growth ${top/shares:.2f}; average ${(v+top)/2/shares:.2f}")
