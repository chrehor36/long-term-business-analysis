import sys
sys.argv=['x']; exec(open('scripts/owner_cash.py').read().split("print(f\"{'yr'")[0])
# recompute OC dicts silently
OC={};OCpre={}
for y in Y:
    cap=PPE[y]+INT[y]; oc=OCF[y]-SBC[y]-cap-FLP[y]-NCI[y]; OC[y]=oc; OCpre[y]=oc+(IPD[y]-IIN[y])*(1-T)
SOV=0.0206; FLOOR=0.10
SH=3154.059870  # million ordinary shares, 2026-06-30
FX=6.7298       # RMB per USD, PBOC central parity 2026-10-13
PX=44.17        # USD per ADS
CAP=SH/10*PX*FX # RMB m
# net debt at 2026-06-30 (6-K 2026-08-17 balance sheet), subsequent events stated in that filing: US$275m dividend declared, paid Sept 2026
debt=911+3315; finl=62+2931; cash=14249+142+1315
div_after=275*6.7851
ND=debt+finl-cash+div_after
EV=CAP+ND
def pv(base,g,r,yrs=10,terminal_base=None):
    v=0; c=base
    for t in range(1,yrs+1):
        c=base*(1+g)**t; v+=c/(1+r)**t
    tb=(terminal_base if terminal_base is not None else base)*(1+g)**yrs
    v+=tb/r/(1+r)**yrs
    return v
def avg(d,ys): return sum(d[y] for y in ys)/len(ys)
print(f"cap RMB {CAP:,.0f}m  net debt {ND:,.0f}m (debt {debt}, fin leases {finl}, cash+restricted+ST inv {cash}, dividend after {div_after:.0f})  EV {EV:,.0f}m")
def report(label,base,g,base_eq=None):
    lo=pv(base,0,SOV); hi=pv(base,g,SOV)
    lo10=pv(base,0,FLOOR); hi10=pv(base,g,FLOOR)
    ends=sorted([lo,hi]); e10=sorted([lo10,hi10])
    ps=lambda ev:(ev-ND)/SH   # RMB per share
    usd=lambda x:x*10/FX
    print(f"\n{label}: base {base:,.0f}  growth {g*100:.2f}%")
    print(f"  at sovereign {SOV*100:.2f}%: whole {ends[0]:,.0f} to {ends[1]:,.0f}; per share RMB {ps(ends[0]):.2f} to {ps(ends[1]):.2f}; per ADS US$ {usd(ps(ends[0])):.2f} to {usd(ps(ends[1])):.2f}; width {ends[1]/ends[0]:.2f}:1" if ends[0]>0 else "  neg")
    print(f"  at floor 10%: {e10[0]:,.0f} to {e10[1]:,.0f} against EV {EV:,.0f}; earns floor? {'YES' if e10[1]>=EV else 'NO'}; implied return at price on growth case {irr(base,g):.2%}")
    fair=(lo10+hi10)/2; fps=(fair-ND)/SH
    print(f"  fair (all-equity): whole {fair:,.0f}; per share RMB {fps:.2f}; per ADS RMB {fps*10:.2f} = US$ {usd(fps):.2f}; per share US$ {usd(fps)/10:.3f}")
    if base_eq is not None:
        f2=(pv(base_eq,0,FLOOR)+pv(base_eq,g,FLOOR))/2; f2ps=f2/SH
        print(f"  fair (equity-only, base {base_eq:,.0f}): per share RMB {f2ps:.2f}; per ADS US$ {usd(f2ps):.2f}; per share US$ {usd(f2ps)/10:.3f}")
def irr(base,g):
    lo,hi=0.0001,1
    for _ in range(100):
        m=(lo+hi)/2
        if pv(base,g,m)>EV: lo=m
        else: hi=m
    return m
cyc=range(2019,2024)
b=avg(OCpre,cyc); beq=avg(OC,cyc)
g_org=(20535/11212)**(1/6)-1   # legacy Huazhu revenue 2019 -> 2025 (2019: all revenue was legacy Huazhu)
report("CENTRAL: cycle 2019-2023, organic pair (purchases left out), organic growth = legacy Huazhu revenue CAGR 2019-2025",b,g_org,beq)
bacq=b-avg(ACQ,cyc)
print(f"\nDEFAULT PAIR beside: cycle base less purchases {bacq:,.0f}; growth between cycles not measurable; no-growth only: at 10% {bacq/0.1:,.0f}; at sovereign {bacq/SOV:,.0f}")
lit=range(2021,2026)
report("LITERAL WINDOW 2021-2025 beside (sign change; halves meaningless; no-growth alone)",avg(OCpre,lit),0.0,avg(OC,lit))
pc=range(2023,2026); gpc=(OCpre[2025]/OCpre[2023])**0.5-1
report("SENSITIVITY, not a rule case: post-COVID 2023-2025, growth 2023->2025",avg(OCpre,pc),gpc,avg(OC,pc))
report("SENSITIVITY + maintenance-only (growth capex ~RMB 347m/yr added back)",avg(OCpre,pc)+347,gpc)
print("\nhighest OC/revenue in filings read: %.1f%%"%max(100*OC[y]/REV[y] for y in Y))
print("cap check central: OC yr10 %.0f vs revenue yr10 at same growth %.0f -> %.1f%%"%(b*(1+g_org)**10, 20535*(1+g_org)**10, 100*b/20535))
