# COMPUTATION - NOT A CLEARANCE. Arithmetic only, ASO run 2026-10-06.
r = 0.0566          # 30-yr US Treasury par yield, 2026-10-05 (tools/sources.py)
sh = 61.578891      # cover shares, 10-Q accession 0001817358-26-000149, as of 2026-09-02
px = 51.98          # close 2026-10-05, aggregator (tools/run.py), flagged
# fiscal years FY2021..FY2025 (ended 2022-01-29 .. 2026-01-31), USD M, XBRL from 10-Ks
ocf  = [673.3, 552.0, 535.8, 528.1, 434.8]
sbc  = [39.3, 21.2, 24.4, 26.6, 21.2]
capx = [75.8, 108.3, 207.8, 199.6, 212.7]
da   = [105.3, 106.8, 110.9, 118.1, 122.9]
oe_c = [o-s-c for o,s,c in zip(ocf,sbc,capx)]
oe_d = [o-s-d for o,s,d in zip(ocf,sbc,da)]
avg = lambda x: sum(x)/len(x)
def pv(base, g, rate, yrs=10):
    v=0; c=base
    for t in range(1,yrs+1):
        c*=1+g; v+=c/(1+rate)**t
    return v + (c/rate)/(1+rate)**yrs   # then zero nominal growth
def ps(x): return x/sh
print("owner cash all-capex", [round(x,1) for x in oe_c], "avg", round(avg(oe_c),1))
print("owner cash D&A basis", [round(x,1) for x in oe_d], "avg", round(avg(oe_d),1))
g_c = (oe_c[-1]/oe_c[0])**0.25-1; g_d=(oe_d[-1]/oe_d[0])**0.25-1
print(f"shown growth aggregate, all-capex {g_c:.4f}, D&A {g_d:.4f}")
for nm,b,g in (("window all-capex",avg(oe_c),g_c),("window D&A",avg(oe_d),g_d)):
    lo=pv(b,g,r); hi=b/r
    print(f"{nm}: no-growth ${ps(hi):.2f}  shown-growth ${ps(lo):.2f}  ratio {hi/lo:.2f}")
# whole-cycle variant: op margin FY2015..FY2025
sales = {2015:4646.686,2016:4738.474,2017:4835.582,2018:4783.893,2019:4829.897,2020:5689.233,2021:6773.128,2022:6395.073,2023:6159.291,2024:5933.450,2025:6053.414}
opi   = {2015:252.214,2016:147.279,2017:157.321,2018:128.950,2019:179.421,2020:420.398,2021:907.947,2022:846.549,2023:677.855,2024:538.639,2025:512.184}
m = avg([opi[y]/sales[y] for y in sales]); mpre = avg([opi[y]/sales[y] for y in range(2015,2020)])
print(f"avg op margin FY15-25 {m:.4f}; FY15-19 {mpre:.4f}; FY21-25 {avg([opi[y]/sales[y] for y in range(2021,2026)]):.4f}")
t=0.225; S=sales[2025]; D=122.866; C=212.668; I=36.214
def oc(margin, capex): return S*margin*(1-t) + D - capex - I*(1-t)
wc_c = oc(m,C); wc_d = oc(m,D); pre_c=oc(mpre,C); pre_d=oc(mpre,D)
print(f"whole-cycle owner cash: all-capex {wc_c:.1f}, D&A {wc_d:.1f}; pre-pandemic margin: all-capex {pre_c:.1f}, D&A {pre_d:.1f}")
gs=(S/sales[2015])**0.1-1
print(f"sales CAGR FY15-25 {gs:.4f}")
for nm,b in (("whole-cycle all-capex",wc_c),("whole-cycle D&A",wc_d)):
    print(f"{nm}: no-growth ${ps(b/r):.2f}  shown-growth(sales) ${ps(pv(b,gs,r)):.2f}  ratio {pv(b,gs,r)/(b/r):.2f}")
# fair price: price at which central case returns 10% (discount central stream at 10%)
for nm,b,g in (("central = whole-cycle D&A, no growth",wc_d,0.0),("whole-cycle all-capex + sales growth",wc_c,gs),("whole-cycle all-capex, no growth",wc_c,0.0),("window all-capex no growth",avg(oe_c),0.0)):
    print(f"FAIR {nm}: ${ps(pv(b,g,0.10)):.2f}")
for nm,b in (("pre-pandemic D&A",pre_d),("pre-pandemic all-capex",pre_c)):
    print(f"CHEAP {nm}: ${ps(b/0.10):.2f}")
mc=px*sh
print(f"mkt cap {mc:.0f}; yields: window avg {avg(oe_c)/mc:.4f}, FY25 all-capex {oe_c[-1]/mc:.4f}, FY25 D&A {oe_d[-1]/mc:.4f}, whole-cycle D&A {wc_d/mc:.4f}, whole-cycle capex {wc_c/mc:.4f}")
# buyback prices vs ranges
bb={"FY2021":(411.409,10.566796),"FY2022":(489.475,11.903636),"FY2023":(204.154,3.651231),"FY2024":(368.338,6.544337),"FY2025":(200.784,3.930672),"FY2026H1":(180.505,3.311559)}
tot=0;n=0
for k,(v,s) in bb.items(): print(k, f"avg ${v/s:.2f}"); tot+=v;n+=s
print(f"total ${tot:.0f}M for {n:.2f}M shares avg ${tot/n:.2f}")
# comps compounding
aso=[3.1,-3.4,-5.2,-2.5,-0.7,16.1,18.9,-6.4,-6.5,-5.1,-1.5]; dks=[-0.2,3.5,-0.3,-3.2,3.7,9.9,26.5,-0.5,2.4,5.2,4.5]
import math
f=lambda xs: math.prod(1+x/100 for x in xs)-1
print(f"cum comps FY15-25: ASO {f(aso):.3f} DKS {f(dks):.3f}; FY20-25: ASO {f(aso[5:]):.3f} DKS {f(dks[5:]):.3f}; FY15-19 ASO {f(aso[:5]):.3f} DKS {f(dks[:5]):.3f}")
