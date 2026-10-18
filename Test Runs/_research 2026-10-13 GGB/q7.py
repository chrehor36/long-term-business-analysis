import json
R = {int(k):v for k,v in json.load(open("owner_cash.json")).items()}
T=0.34
INT = {2015:(946041,153631),2016:(1240165,107980),2017:(1330116,75387),2018:(1162364,49745),2019:(945027,72784),
       2020:(1079981,99359),2021:(1100826,170671),2022:(968851,309782),2023:(858301,481624),2024:(946936,274291),2025:(1461147,166307)}
LEASEPRIN={2019:161824,2020:247914,2021:275854,2022:310226,2023:388202,2024:459504,2025:487784}
# purchases of businesses and JV capital, gross of disposals (R$k): disposals not counted as owner cash (CONVENTION of this run)
PURCH={2015:61453,2016:0,2017:178670,2018:375456,2019:74343,2020:485324,2021:-113595,2022:72904,2023:477179,2024:647630,2025:790554}
def oc(y, basis, case):
    r=R[y]
    if case=="all":   v=r["oc_eq"]                       # CFOx - capex - intangibles - lease principal
    else:             v=r["cfo_x"]-r["da"]                # maintenance proxy: D&A incl. right-of-use depreciation stands for maintenance and lease cost
    v -= PURCH[y]
    if basis=="un":   v += (INT[y][0]-INT[y][1])*(1-T)
    return v/1e3   # R$ millions
SOV=0.1257; FLOOR=0.10
NETDEBT=8117.6+451.3   # 30 Jun 2026 borrowings+debentures less cash and short-term investments (leases excluded), plus the R$451.3m dividend the interim filing states as a subsequent event
SH=1963.180639   # shares in circulation 30 Jun 2026, both classes (millions)
P_PN=25.98; P_ON=22.12; FX=5.0096
MCAP=717.010819*P_ON+1246.169820*P_PN
print("market value R$m %.1f  US$m %.1f ; EV all-equity %.1f" % (MCAP, MCAP/FX, MCAP+NETDEBT))
def pv(c0,g,r,yrs=10):
    v=0;c=c0
    for t in range(1,yrs+1):
        c*=1+g; v+=c/(1+r)**t
    return v + c/r/(1+r)**yrs
def show(label, years, g=0.0):
    out={}
    for basis in ("un","eq"):
        for case in ("all","maint"):
            out[(basis,case)]=sum(oc(y,basis,case) for y in years)/len(years)
    print(label, {k:round(v) for k,v in out.items()})
    return out
cyc=show("cycle 2017-2025", range(2017,2026))
lit=show("literal 2021-2025", range(2021,2026))
for nm,base in (("CYCLE",cyc),):
    for basis,lab in (("un","ALL-EQUITY"),("eq","EQUITY-ONLY")):
        lo=base[(basis,"all")]; hi=base[(basis,"maint")]
        vlo=pv(lo,0,SOV); vhi=pv(hi,0,SOV)
        f10lo=pv(lo,0,FLOOR); f10hi=pv(hi,0,FLOOR)
        if basis=="un":
            vlo-=NETDEBT; vhi-=NETDEBT; f10lo-=NETDEBT; f10hi-=NETDEBT
            yld_lo=lo/(MCAP+NETDEBT); yld_hi=hi/(MCAP+NETDEBT)
        else:
            yld_lo=lo/MCAP; yld_hi=hi/MCAP
        fair=(f10lo+f10hi)/2/SH
        print(f"{nm} {lab}: OC {lo:,.0f}-{hi:,.0f}  range R$ {vlo/SH:.2f}-{vhi/SH:.2f}/sh (US$ {vlo/SH/FX:.2f}-{vhi/SH/FX:.2f}); width {vhi/vlo:.2f}:1; "
              f"yield at price {100*yld_lo:.1f}%-{100*yld_hi:.1f}%; fair R$ {fair:.2f} (US$ {fair/FX:.2f}); ends at 10% {f10lo/SH:.2f} / {f10hi/SH:.2f}")
# literal window: growth shown between end years (maintenance and all-spending), carried as decline
import math
for basis in ("un","eq"):
    for case in ("all","maint"):
        a=oc(2021,basis,case); b=oc(2025,basis,case)
        g=(b/a)**(1/4)-1 if a>0 and b>0 else float('nan')
        base=lit[(basis,case)]
        v0=pv(base,0,SOV); vg=pv(base,g,SOV) if not math.isnan(g) else float('nan')
        nd = NETDEBT if basis=="un" else 0
        print(f"LITERAL {basis} {case}: 2021 {a:,.0f} 2025 {b:,.0f} g {100*g:.1f}%/yr; base {base:,.0f}; no-growth R$ {(v0-nd)/SH:.2f}/sh; decline case R$ {(vg-nd)/SH:.2f}/sh")
# sales growth for reference
print("sales cagr 2017-2025 %.1f%%; 2021-2025 %.1f%%" % (100*((R[2025]['rev']/R[2017]['rev'])**(1/8)-1), 100*((R[2025]['rev']/R[2021]['rev'])**(1/4)-1)))
