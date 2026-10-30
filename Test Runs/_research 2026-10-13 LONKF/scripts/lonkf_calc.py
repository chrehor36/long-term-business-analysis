# LONKF run 2026-10-13: arithmetic from the filed statements (RMB million). Sources: annual reports on HKEXnews,
# each year's figures from the latest report that prints it (AR2025: 2024-25; AR2023: 2022-23; AR2021: 2020-21;
# AR2019: 2018-19; AR2017: 2016-17; AR2015: 2014-15; AR2013: 2012-13; AR2012: 2011; AR2010: 2009-10).
# Cash flow: CGO = cash generated from operations (after working capital, before interest and tax);
# tax = income tax paid; capex = purchases of PPE (2009-10: acquisition of and deposits paid for PPE).
CF = {  # year: (CGO, tax paid, capex, interest received, interest paid)
 2009:(858.131,83.114,741.370,19.075,61.869), 2010:(66.355,297.420,509.292,10.058,75.594),
 2011:(1663.025,392.355,1055.078,27.992,227.628), 2012:(1221.211,179.937,558.763,37.377,278.553),
 2013:(1683.299,126.379,241.727,19.287,230.703), 2014:(2111.066,183.022,105.462,32.611,176.098),
 2015:(1752.816,70.480,69.824,39.390,117.776), 2016:(2032.266,94.158,26.604,22.116+61.084,82.658),
 2017:(1843.999,279.544,170.105,27.358+217.157,49.964), 2018:(1132.446,410.332,348.986,88.963+21.818,46.161),
 2019:(1737.657,300.433,197.445,133.899,43.442), 2020:(1207.189,257.130,289.568,120.467,17.282),
 2021:(595.218,317.026,382.399,141.492,11.432), 2022:(1824.173,70.130,239.267,102.684,18.818),
 2023:(2022.409,138.344,186.592,100.094,43.436), 2024:(1424.749,177.007,83.455,117.845,21.449),
 2025:(1247.662,128.715,61.538,125.610,3.004)}
REV = {2009:6901.0,2010:12019.9,2011:12721.2,2012:7896.0,2013:8157.5,2014:7427.2,2015:4829.3,2016:5146.4,2017:8994.1,
       2018:11868.3,2019:11743.8,2020:12880.4,2021:13690.5,2022:11150.2,2023:10522.9,2024:10213.6,2025:11215.2}
NP = {2011:1729.5,2012:151.5,2013:480.0,2014:416.9,2015:116.6,2016:461.8,2017:1045.6,2018:1143.9,2019:1643.4,2020:1959.2,
      2021:1275.4,2022:400.5,2023:645.4,2024:1018.4,2025:1300.5}
SEG = {2014:724.2,2015:83.5,2016:307.8,2017:1228.0,2018:1431.1,2019:1483.1,2020:1647.3,2021:1183.4,2022:627.2,
       2023:800.2,2024:1041.9,2025:1308.6}   # machinery segment result, pre-tax, before interest income
DEP = {2014:391.8,2015:390.4,2016:379.8,2017:353.5,2022:270.6,2023:269.2,2024:253.2,2025:233.5}  # depreciation of PPE
# balance sheet: cash, pledged, time deposits, financial investments (FVTPL/AFS/loans at FV/ equity at FVTPL), borrowings, total equity
BS = {
 2014:(1088.5,2358.3,0,300.0,4281.2,7029.3), 2015:(1146.3,2424.2,0,496.5+138.8+830.5,4365.3,6624.1),
 2016:(1130.5,2467.8,0,527.5+108.2+211.0,2150.5,6719.7), 2017:(1633.7,1465.5,0,2079.1+94.3+221.9,1502.9,7730.2),
 2018:(2565.0,1067.4,0,1424.0,1286.9,8207.2), 2019:(2501.8,673.2,0,2336.8,709.3,9077.0),
 2020:(2780.6,837.5,0,2346.6,663.5,10094.3), 2021:(2025.0,784.2,0,2486.2,648.3,10204.8),
 2022:(2032.0,1656.3,0,2132.1,708.2,9751.2), 2023:(3470.8,708.2,743.7,1997.9,726.6,9981.5),
 2024:(1218.0,598.7,1059.3,4253.5,0.0,10704.1), 2025:(4364.8,255.8,2473.7,919.4,20.0,11482.0)}
def oc(y):  # owner cash before interest (all-equity basis)
    c,t,k,ir,ip = CF[y]; return c-t-k
def oc_eq(y):  # equity-only: after net interest
    c,t,k,ir,ip = CF[y]; return c-t-k+ir-ip
print("year  rev    OC_pre  OC_eq   NP     seg   segM%  netM%  ROE%  netfin  opcap  segROC%")
prev=None
for y in sorted(CF):
    line=f"{y} {REV[y]:7.0f} {oc(y):7.1f} {oc_eq(y):7.1f}"
    if y in NP: line+=f" {NP[y]:7.1f}"
    if y in SEG: line+=f" {SEG[y]:6.0f} {100*SEG[y]/REV[y]:5.1f} {100*NP[y]/REV[y]:5.1f}"
    if y in BS and y-1 in BS:
        e0=BS[y-1][5]; e1=BS[y][5]; roe=100*NP[y]/((e0+e1)/2)
        nf=lambda b: b[0]+b[1]+b[2]+b[3]-b[4]
        op0=e0-nf(BS[y-1]); op1=e1-nf(BS[y])
        line+=f" {roe:5.1f} {nf(BS[y]):7.0f} {op1:6.0f} {100*SEG[y]/((op0+op1)/2):6.1f}"
    print(line)
def avg(ys,f): return sum(f(y) for y in ys)/len(ys)
W=range(2021,2026); print("\nliteral window 2021-25 OC_pre avg", round(avg(W,oc),1), " OC_eq avg", round(avg(W,oc_eq),1))
H1=range(2016,2021); print("halves 2016-20 OC_pre avg", round(avg(H1,oc),1), "; 2021-25", round(avg(W,oc),1),
  " growth/yr", round(100*((avg(W,oc)/avg(H1,oc))**(1/5)-1),2))
C=range(2010,2021); print("owner-cash trough-to-trough cycle 2010-2020 avg", round(avg(C,oc),1))
C2=range(2015,2023); print("profit trough-to-trough 2015-2022 OC_pre avg", round(avg(C2,oc),1))
print("10y 2016-25 OC_pre avg", round(avg(range(2016,2026),oc),1), " OC_eq", round(avg(range(2016,2026),oc_eq),1))
print("sales growth 2016-20 avg vs 2021-25 avg /yr", round(100*((avg(W,lambda y:REV[y])/avg(H1,lambda y:REV[y]))**(1/5)-1),2))
print("max OC/sales", max((oc(y)/REV[y],y) for y in CF))

# ---------------- Q7 COMPUTATION, NOT A CLEARANCE ----------------
DEPALL={2009:134.9,2010:203.9,2011:283.5,2012:329.4,2013:356.7,2014:391.8,2015:390.4,2016:379.8,2017:353.5,2018:347.1,
        2019:343.6,2020:334.8,2021:285.8,2022:270.6,2023:269.2,2024:253.2,2025:233.5}
cyc=range(2010,2021)
print("\ncycle 2010-20: capex sum", round(sum(CF[y][2] for y in cyc),1), " depreciation sum", round(sum(DEPALL[y] for y in cyc),1))
print("window 2021-25: capex sum", round(sum(CF[y][2] for y in W),1), " depreciation sum", round(sum(DEPALL[y] for y in W),1))
oc_dep=lambda y: oc(y)+CF[y][2]-DEPALL[y]
print("depreciation-variant OC: cycle avg", round(avg(cyc,oc_dep),1), " window avg", round(avg(W,oc_dep),1))
SOV=0.02069   # ChinaBond government bond yield curve, 30-year, 2026-10-13
SH=4280.1     # million shares, monthly return to 30 Sep 2026, no treasury shares
PX_HKD=3.04; FX=0.85753  # HKD close 2026-10-13 (aggregator); CFETS/PBOC central parity HKD/CNY 2026-10-13
PX=PX_HKD*FX; MC=PX*SH
# net cash at 30 June 2026 (interim report): cash 3724.179 + time deposits 3092.776+459.677 + FVTPL 207.654+693.132
# less dividends payable 743.496 (paid by 31 July 2026, before the price date); borrowings nil; pledged deposits 457.305 left out (they secure bills payable)
NETCASH=3724.179+3092.776+459.677+207.654+693.132-743.496
def pv(B,g,r,n=10):
    v=0; c=B
    for t in range(1,n+1):
        c=B*(1+g)**t; v+=c/(1+r)**t
    return v + (c/r)/(1+r)**n
B=avg(cyc,oc); Bw=avg(W,oc)
g_sh=(Bw/B)**(1/8)-1   # full-cycle average (midpoint 2015) to the latest five-year average (midpoint 2023)
g_h=(avg(W,oc)/avg(H1,oc))**(1/5)-1
print(f"\nprice RMB {PX:.4f}/sh, mkt cap RMB {MC:.1f}m; net cash {NETCASH:.1f}m; EV at price {MC-NETCASH:.1f}m")
print(f"base (cycle 2010-20) {B:.1f}; literal window {Bw:.1f}; growth cycle->window {100*g_sh:.2f}%/yr; halves {100*g_h:.2f}%/yr")
def show(label,Bx,gs,r,addcash=True):
    out=[]
    for g in gs:
        ev=pv(Bx,g,r); eq=ev+(NETCASH if addcash else 0); out.append((g,ev,eq,eq/SH,eq/SH/FX))
    for g,ev,eq,ps,ph in out: print(f"  {label} g={100*g:+.2f}% r={100*r:.3f}%: EV {ev:,.0f} equity {eq:,.0f} -> RMB {ps:.2f} / HKD {ph:.2f} a share")
    return out
print("VALUE RANGE at the sovereign (all-equity, central):")
R=show("cycle base",B,[0.0,g_sh],SOV)
print("  width top/bottom", round(max(x[2] for x in R)/min(x[2] for x in R),3))
show("literal window",Bw,[0.0,g_h],SOV)
show("cycle base, halves decline as bottom",B,[g_h],SOV)
print("expected return at price (all-equity): cycle base / EV =", round(100*B/(MC-NETCASH),1),"%;  window:", round(100*Bw/(MC-NETCASH),1),"%")
print("FAIR PRICE (each end at 10%, averaged), all-equity:")
F=show("fair",B,[0.0,g_sh],0.10); fp=sum(x[3] for x in F)/2
print(f"  FAIR PRICE all-equity RMB {fp:.2f} / HKD {fp/FX:.2f}")
Beq=avg(cyc,oc_eq); Beqw=avg(W,oc_eq); geq=(Beqw/Beq)**(1/8)-1
print(f"equity-only base (after net interest) cycle {Beq:.1f}, window {Beqw:.1f}, growth {100*geq:.2f}%")
E=show("equity-only fair",Beq,[0.0,geq],0.10,addcash=False); fe=sum(x[3] for x in E)/2
print(f"  FAIR PRICE equity-only RMB {fe:.2f} / HKD {fe/FX:.2f}")
print("equity-only expected return at price:", round(100*Beq/MC,1), "% (cycle);", round(100*Beqw/MC,1),"% (window)")
# beside: bills payable (31 Dec 2025 split, 2131.569) less pledged deposits (457.305) counted as debt
bills=2131.569-457.305
print(f"beside: bills payable net of pledged deposits as debt ({bills:.0f}m): fair all-equity RMB {fp-bills/SH:.2f} / HKD {(fp-bills/SH)/FX:.2f}")
Fw=show("fair, literal window",Bw,[0.0,g_h],0.10); print("  literal-window fair RMB %.2f / HKD %.2f"%(sum(x[3] for x in Fw)/2, sum(x[3] for x in Fw)/2/FX))
