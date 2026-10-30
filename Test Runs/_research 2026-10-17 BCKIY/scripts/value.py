# Q7 range, floor test and fair price for BCKIY (GBP m). See run file Q7 for the conventions applied.
r_gov=0.0586; floor=0.10; shares=490.485431; price=9.618
mcap=shares*price
net_debt=329.0+47.4+24.5   # 31 Mar 2026 net debt incl leases + April buyback remainder + FY26 final dividend (both stated in AR2026)
EV=mcap+net_debt
def pv(c0,g,r,yrs=10):
    v=0; c=c0
    for t in range(1,yrs+1):
        c=c*(1+g); v+=c/(1+r)**t
    return v + c/r/(1+r)**yrs           # zero nominal growth after year ten
def irr(c0,g,target):
    lo,hi=0.0001,1.0
    for _ in range(200):
        mid=(lo+hi)/2
        if pv(c0,g,mid)>target: lo=mid
        else: hi=mid
    return mid
oc={"FY22":-205.3,"FY23":65.9,"FY24":148.0,"FY25":139.1,"FY26":244.6}
intr={"FY22":45.0,"FY23":62.2,"FY24":32.2,"FY25":26.8,"FY26":26.6}
growthcapex={"FY22":135.2-74.4,"FY23":86.2-84.9,"FY24":111.8-67.3,"FY25":122.2-78.3,"FY26":107.2-85.2}
pens={"FY22":151.7,"FY23":141.9,"FY24":107.6,"FY25":90.3,"FY26":23.4}
def avg(d,ks): return sum(d[k] for k in ks)/len(ks)
lit=list(oc); cyc=["FY23","FY24","FY25","FY26"]
g_sales=(5177.7/4438.6)**(1/3)-1
print("mcap %.0f  net debt %.1f  EV %.0f  g_sales FY23-26 %.4f  owner-cash CAGR FY23-26 %.3f"%(mcap,net_debt,EV,g_sales,(244.6/65.9)**(1/3)-1))
cases={}
for name,ks in [("literal FY22-26",lit),("cycle base FY23-26",cyc)]:
    eq=avg(oc,ks); ae=eq+0.75*avg(intr,ks); maint=ae+avg(growthcapex,ks); pensv=maint+avg(pens,ks)-20.0
    cases[name]=(eq,ae,maint,pensv)
    print(f"\n== {name}: equity-only {eq:.1f}; all-equity {ae:.1f}; maintenance-only all-equity {maint:.1f}; + pension variant {pensv:.1f}")
for name,(eq,ae,maint,pensv) in cases.items():
    g = 0.0 if name.startswith("literal") else g_sales
    for lab,c in [("all-spending",ae),("maintenance (central)",maint),("pension variant",pensv)]:
        nd = net_debt + (100.0 if lab=="pension variant" else 0)
        lo=pv(c,0.0,r_gov); hi=pv(c,g,r_gov)
        ps=lambda v:(v-nd)/shares*100
        f_lo=pv(c,0.0,floor); f_hi=pv(c,g,floor); fair=((f_lo+f_hi)/2-nd)/shares*100
        tgt=mcap+nd
        print(f"{name:20s} {lab:22s} base {c:6.1f} g {g:.4f} | range {ps(lo):6.0f}p to {ps(hi):6.0f}p (width {ps(hi)/ps(lo) if ps(lo)>0 else float('nan'):.2f}x) | IRR at price: no-growth {irr(c,0,tgt)*100:5.2f}% growth {irr(c,g,tgt)*100:5.2f}% | fair {fair:6.0f}p")
# equity-only fair (owner cash after interest vs market value only)
for name,(eq,ae,maint,pensv) in cases.items():
    g = 0.0 if name.startswith("literal") else g_sales
    c=eq+(avg(growthcapex,cyc if 'cycle' in name else lit))
    f=(pv(c,0,floor)+pv(c,g,floor))/2/shares*100
    print(f"equity-only maintenance {name}: base {c:.1f} fair {f:.0f}p ; IRR growth case vs mcap {irr(c,g,mcap)*100:.2f}%")
