import sys; sys.stdout.reconfigure(encoding='utf-8')
# $M, from filed cash-flow statements (FY2025 10-K for 2023-25, FY2022 10-K for 2020-22, FY2020 10-K for 2018-20), Q2 2026 10-Q for H1
Y={2018:(-39.0,248.5,13.0,13.9),2019:(-165.2,242.0,13.1,12.3),2020:(-296.6,1270.7,12.2,13.9),2021:(333.9,778.2,12.6,14.9),
   2022:(223.7,564.8,40.0,22.5),2023:(712.2,475.9,15.1,33.4),2024:(1153.9,691.6,12.6,31.6),2025:(2134.5,684.0,33.9,26.1)}
H1_26=(2115.3,466.8,22.0,15.0); H1_25=(849.5,315.3,13.8,13.2)
TTM=tuple(round(a+b-c,1) for a,b,c in zip(Y[2025],H1_26,H1_25))
INT={2023:132.6,2024:196.8,2025:229.2}; INT_TTM=229.2+143.9-106.7
oe_cap={y:round(o-s-c,1) for y,(o,s,c,d) in Y.items()}
oe_da={y:round(o-s-d,1) for y,(o,s,c,d) in Y.items()}
print("year | OCF | SBC | SBC/OCF | capex | D&A | OE@capex | OE@D&A")
for y,(o,s,c,d) in Y.items():
    print(f"{y} | {o} | {s} | {('n/m (OCF<0)' if o<=0 else f'{100*s/o:.1f}%')} | {c} | {d} | {oe_cap[y]} | {oe_da[y]}")
o,s,c,d=TTM; print(f"TTM 6/26 | {o} | {s} | {100*s/o:.1f}% | {c} | {d} | {round(o-s-c,1)} | {round(o-s-d,1)}")
print(f"H1 2026 SBC/OCF {100*H1_26[1]/H1_26[0]:.1f}%  H1 2025 {100*H1_25[1]/H1_25[0]:.1f}%")
print("\nwindows ending 2025 (mean), capex end / D&A end")
for n in range(1,9):
    ys=[y for y in range(2026-n,2026)]
    print(f"{n}y {ys[0]}-25 | {sum(oe_cap[y] for y in ys)/n:.1f} | {sum(oe_da[y] for y in ys)/n:.1f}")
print("\nrecent-business windows: 2023-25 mean capex", round(sum(oe_cap[y] for y in (2023,2024,2025))/3,1), "; 2024-25", round((oe_cap[2024]+oe_cap[2025])/2,1))
print("FY2025 ex-interest", round(oe_cap[2025]-INT[2025],1), " TTM ex-interest", round(o-s-c-INT_TTM,1), "TTM interest", round(INT_TTM,1))
# cap
shares=2403058480; price=167.23; cap=shares*price/1e6
opts=152.2; k=9.98; rsu=41.6; sars=11.3
dil=shares/1e6+opts*(1-k/price)+rsu  # SARs capped; ignore
print(f"\ncap (cover count) {cap:,.0f}M ; diluted-claims cap {dil*price:,.0f}M (adds {dil-shares/1e6:.1f}M shares)")
cash=2030.0+7379.1; ev=cap-cash; print(f"cash+MS 6/30/26 {cash:,.1f}M ; EV {ev:,.0f}M")
sov=5.35
for lbl,oe in [("5y mean D&A (screen bottom)",247.0),("3y mean capex (screen top)",695.8),("FY2025 capex",oe_cap[2025]),("FY2025 ex-interest",oe_cap[2025]-INT[2025]),("TTM capex",round(o-s-c,1)),("TTM ex-interest",round(o-s-c-INT_TTM,1))]:
    print(f"yield {lbl}: {oe:.1f} / {cap:,.0f} = {100*oe/cap:.2f}%  vs sovereign {100*oe/cap-sov:+.2f} pts")
# growth needed: 10y growth g, then 3% terminal, discount 10% floor; PV = EV
def pv(oe0,g,r=0.10,n=10,gt=0.03):
    v=0; x=oe0
    for t in range(1,n+1):
        x*=1+g; v+=x/(1+r)**t
    v+=x*(1+gt)/(r-gt)/(1+r)**n
    return v
def solve_g(oe0,target):
    lo,hi=0.0,3.0
    for _ in range(100):
        m=(lo+hi)/2
        if pv(oe0,m)<target: lo=m
        else: hi=m
    return m
print("\nGROWTH NEEDED for 10 years (then 3%) to justify EV at the 10% floor:")
for lbl,oe in [("5y mean D&A 247",247.0),("3y mean capex 696",695.8),("FY2025 ex-interest",oe_cap[2025]-INT[2025]),("FY2025 capex",oe_cap[2025]),("TTM ex-interest",round(o-s-c-INT_TTM,1)),("TTM capex (cash not credited, full cap)",round(o-s-c,1))]:
    tgt = cap if 'full cap' in lbl else ev
    print(f"  from {lbl}: {100*solve_g(oe,tgt):.1f}%/yr")
# expectancy (IRR) at price for given growth for n years then 3%
def irr(oe0,g,n,target):
    lo,hi=0.0301,3.0
    for _ in range(200):
        m=(lo+hi)/2
        if pv(oe0,g,m,n)>target: lo=m
        else: hi=m
    return m
print("\nEXPECTANCY at $167.23 (EV basis), growth for N years then 3% forever:")
for n in (10,15,20):
    print(f" N={n}y")
    for g in (0.10,0.15,0.20,0.25,0.30,0.40,0.50):
        print(f"   g={int(g*100)}%: from FY25 ex-int {100*irr(oe_cap[2025]-INT[2025],g,n,ev):.2f}%  from FY25 {100*irr(oe_cap[2025],g,n,ev):.2f}%  from TTM {100*irr(round(o-s-c,1),g,n,ev):.2f}%")
# steady state
print(f"\nsteady-state OE for 10% on EV: {0.10*ev:,.0f}M ; FY2025 OE margin {100*oe_cap[2025]/4475.4:.1f}% ; TTM rev {4475.4+3568.0-1887.6:.1f} TTM OE margin {100*(o-s-c)/(4475.4+3568.0-1887.6):.1f}%")
for m in (0.317,0.41,0.50):
    print(f"  at OE margin {m*100:.0f}%: revenue needed {0.10*ev/m:,.0f}M = {0.10*ev/m/4475.4:.1f}x FY2025, {0.10*ev/m/8154:.1f}x FY2026 guidance")
# zero-growth value bands
for lbl,oe in [("FY2025 ex-int",oe_cap[2025]-INT[2025]),("FY2025",oe_cap[2025]),("TTM ex-int",round(o-s-c-INT_TTM,1)),("TTM",round(o-s-c,1))]:
    for r,rl in ((sov/100,'sov'),(0.10,'floor')):
        v=oe/r+cash; print(f"value {lbl} at {rl}: ${v/1000:.1f}bn = ${v/(shares/1e6):.2f}/sh")
