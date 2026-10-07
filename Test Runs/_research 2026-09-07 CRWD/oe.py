import statistics, sys
sys.path.insert(0,'tools')
# (fy, OCF, SBC, ppe_capex, cap_software_cash, DA_ppe, amort_intang)   $ thousands -> millions
R=[(2019,-22995,20505,35851,6794,14815,583),
   (2020,99943,79940,80198,7289,23026,487),
   (2021,356566,149675,52799,10864,38710,1448),
   (2022,574784,309952,112143,20866,55908,12902),
   (2023,941007,526504,235019,29095,77245,16565),
   (2024,1166207,648665,176529,49457,126838,18416),
   (2025,1381727,861391,254852,58969,187952,26004),
   (2026,1612349,1096679,302108,68751,250218,31233)]
rows=[]
for fy,ocf,sbc,ppe,cs,da,ai in R:
    cash=(ocf-sbc)/1000.0
    capex=(ppe+cs)/1000.0
    dna=(da+ai)/1000.0
    rows.append(dict(fy=fy,ocf=ocf/1000,sbc=sbc/1000,cash=cash,capex=capex,dna=dna,
                     oe_da=cash-dna, oe_cx=cash-capex, sbc_ocf=sbc/ocf if ocf>0 else None))
print(f"{'FY':>5} {'OCF':>9} {'SBC':>9} {'SBC/OCF':>8} {'OCF-SBC':>9} {'capex':>8} {'D&A':>8} {'OE@D&A':>9} {'OE@capex':>9}")
for r in rows:
    s=f"{r['sbc_ocf']*100:7.1f}%" if r['sbc_ocf'] else "      na"
    print(f"{r['fy']:>5} {r['ocf']:>9,.1f} {r['sbc']:>9,.1f} {s} {r['cash']:>9,.1f} {r['capex']:>8,.1f} {r['dna']:>8,.1f} {r['oe_da']:>9,.1f} {r['oe_cx']:>9,.1f}")
print()
def win(n,label):
    sel=rows[-n:]
    a=statistics.fmean(x['oe_da'] for x in sel); b=statistics.fmean(x['oe_cx'] for x in sel)
    print(f"  {label:<28} FY{sel[0]['fy']}-{sel[-1]['fy']}  OE@D&A {a:>8,.1f}   OE@capex {b:>8,.1f}")
    return a,b
res=[win(n,l) for n,l in [(3,'3-year'),(4,'4-year'),(5,'5-year (corpus default)'),(6,'6-year'),(7,'7-year'),(8,'8-year (all filed)')]]
lo=min(min(x) for x in res); hi=max(max(x) for x in res)
print(f"\n  FULL RANGE across six windows and both capex ends: {lo:,.1f} .. {hi:,.1f}  ({hi/lo:.2f}x width)")
CAP=213.10*1023934842/1e6
print(f"\n  Market cap = $213.10 x 1,023,934,842 = ${CAP:,.0f}M")
SOV=5.24
for nm,v in [('range low',lo),('range high',hi),('judged 250',250.0)]:
    print(f"    {nm:<12} OE ${v:,.1f}M -> yield {v/CAP*100:.4f}%   vs sovereign {SOV}%  = {v/CAP*100-SOV:+.2f} pts")
    print(f"                 zero-growth value @sov = ${v/(SOV/100):,.0f}M = ${v/(SOV/100)/1023.934842:,.2f}/sh ; @10% floor = ${v/0.10:,.0f}M = ${v/0.10/1023.934842:,.2f}/sh")
def implied_growth(cap, base, rate, tgr=0.025, yrs=10):
    if base<=0 or rate<=tgr: return None
    def pv(g1):
        v,oe=0.0,base
        for t in range(1,yrs+1):
            g=g1+(tgr-g1)*(t-1)/(yrs-1); oe*=(1+g); v+=oe/(1+rate)**t
        return v + (oe*(1+tgr)/(rate-tgr))/(1+rate)**yrs
    lo_,hi_=-0.5,3.0
    for _ in range(300):
        m=(lo_+hi_)/2
        if pv(m)<cap: lo_=m
        else: hi_=m
    return (lo_+hi_)/2
print()
for nm,v in [('range low',lo),('judged 250',250.0),('range high',hi),('best single yr FY2024 D&A',372.2)]:
    g10=implied_growth(CAP,v,0.10); gs=implied_growth(CAP,v,SOV/100)
    print(f"    {nm:<26} growth needed for the 10% FLOOR: {g10*100:6.2f}%/yr yr-1 fading to 2.5% ; to match the sovereign: {gs*100:6.2f}%")
