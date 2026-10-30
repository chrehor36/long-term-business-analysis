"""CENT run 2026-10-05. COMPUTATION - NOT A CLEARANCE. Arithmetic on filed figures (USD millions)."""
# Filed figures, 10-K cash-flow statements (accessions in the run file)
ocf  = {2016:151.4,2017:114.3,2018:114.1,2019:205.0,2020:264.3,2021:250.8,2022:-34.0,2023:381.6,2024:394.9,2025:332.5}
sbc  = {2016:8.4,2017:11.1,2018:11.6,2019:14.7,2020:19.0,2021:23.1,2022:25.8,2023:28.0,2024:20.6,2025:21.1}
capx = {2016:27.6,2017:44.7,2018:37.8,2019:31.6,2020:43.1,2021:80.3,2022:115.2,2023:54.0,2024:43.1,2025:41.4}
da   = {2016:40.0,2017:42.7,2018:47.2,2019:50.8,2020:55.4,2021:74.7,2022:80.9,2023:87.7,2024:90.8,2025:84.9}
acq  = {2016:69.0,2017:103.9,2018:91.2,2019:41.2,2020:0.0,2021:820.5,2022:0.0,2023:0.0,2024:60.2,2025:3.3}
buyb = {2016:10.9,2017:27.6,2018:13.8,2019:63.0,2020:59.1,2021:27.9,2022:62.3,2023:37.2,2024:24.1,2025:155.1}
oc = {y: ocf[y]-sbc[y]-capx[y] for y in ocf}
ocd = {y: ocf[y]-sbc[y]-da[y] for y in ocf}
print("owner cash (OCF-SBC-capex):", {y: round(v,1) for y,v in oc.items()})
print("owner cash (OCF-SBC-D&A):  ", {y: round(v,1) for y,v in ocd.items()})
m5 = sum(oc[y] for y in range(2021,2026))/5; m5d = sum(ocd[y] for y in range(2021,2026))/5
m10 = sum(oc.values())/10; m5a = sum(oc[y] for y in range(2016,2021))/5
print(f"5y mean capex basis {m5:.1f}; D&A basis {m5d:.1f}; 10y mean {m10:.1f}; FY16-20 mean {m5a:.1f}")
print(f"10y sum owner cash {sum(oc.values()):.1f}; acquisitions {sum(acq.values()):.1f}; buybacks {sum(buyb.values()):.1f}")
print(f"10y capex {sum(capx.values()):.1f} vs D&A {sum(da.values()):.1f}")
# working-capital-neutral FY2023-25 (CONVENTION of this run): OCF less the filed changes in working capital lines (lease line excluded)
wc = {2023: 43.980+86.980+8.813-19.962+6.766+9.595, 2024: 11.857+84.306+11.944+18.373+17.152-12.631, 2025: 0.629+31.278-2.740+20.107+1.348+0.986}
ocn = {y: ocf[y]-wc[y]-sbc[y]-capx[y] for y in wc}
print("WC changes", {y: round(v,1) for y,v in wc.items()}, "WC-neutral owner cash", {y: round(v,1) for y,v in ocn.items()}, "mean", round(sum(ocn.values())/3,1))

r = 0.0566
def pv(c, g, rate, years=10):
    v = 0.0; cf = c
    for t in range(1, years+1):
        cf = cf*(1+g); v += cf/(1+rate)**t
    v += cf/rate/(1+rate)**years   # zero nominal growth after year ten
    return v
SH = 62.592598  # cover count, 10-Q filed 2026-08-06, all three classes
P_CENT, P_CENTA = 39.70, 34.20
cap_mixed = 9.650221*P_CENT + 51.340003*P_CENTA + 1.602374*P_CENT
print(f"market cap: mixed classes {cap_mixed:.0f}; all at CENT {SH*P_CENT:.0f}; all at CENTA {SH*P_CENTA:.0f}")
g_shown = 0.048   # filer's five-year average GAAP operating income growth (10-K FY2025 line 189), includes acquisitions
for base, lab in [(m5,"5y mean"), (sum(ocn.values())/3, "WC-neutral 3y"), (m10, "10y mean")]:
    lo = pv(base, 0.0, r); hi = pv(base, g_shown, r)
    print(f"{lab:14s} base {base:6.1f}: range {lo:7.0f} - {hi:7.0f}  per share {lo/SH:6.2f} - {hi/SH:6.2f}  width {hi/lo:.2f}x")
# fair price: PV at 10% of PRE-TAX owner cash (gross-up at FY2025 effective rate 24.4%), central case = growth at half the shown rate
t = 0.244
for base, lab in [(m5,"5y mean"), (sum(ocn.values())/3, "WC-neutral 3y")]:
    pre = base/(1-t)
    for g, gl in [(0.0,"no growth"), (g_shown/2,"half shown (central)"), (g_shown,"shown")]:
        f = pv(pre, g, 0.10)
        print(f"fair @10% pre-tax, {lab}, {gl:22s}: {f:7.0f}M  ${f/SH:6.2f}/sh")
lo5 = pv(m5, 0.0, r)
print(f"cheap (half the bottom of the 5y range): ${lo5/SH/2:.2f}")
# yields at the two prices
for p in (P_CENT, P_CENTA):
    print(f"price {p}: owner-cash yield 5y mean {m5/(SH*p):.2%}, pre-tax {m5/(1-t)/(SH*p):.2%}")
# segment margins (filed segment tables)
seg = {  # year: (pet sales, pet OI, garden sales, garden OI)
2006:(819.2,104.5,802.4,57.5),2007:(893.2,94.3,778.0,45.6),2009:(833.2,102.2,781.1,68.9),2010:(840.6,97.9,683.1,53.0),
2011:(851.3,77.6,777.3,50.0),2012:(930.8,87.7,769.3,40.4),2013:(888.2,95.5,765.4,8.3),2014:(845.5,88.1,758.9,41.0),
2015:(894.5,98.8,756.2,60.1),2016:(1081.9,119.9,747.2,70.3),2017:(1246.4,131.6,808.1,87.3),2018:(1340.9,140.4,874.5,95.6),
2019:(1384.7,122.7,998.3,102.2),2020:(1678.0,171.4,1017.5,115.4),2021:(1894.9,208.2,1408.8,138.8),2022:(1878.1,208.9,1460.5,154.0),
2023:(1877.2,198.0,1432.9,123.5),2024:(1832.7,203.4,1367.7,81.9),2025:(1801.9,215.7,1327.1,142.4)}
for y,(ps,po,gs,go) in seg.items():
    print(y, f"pet {po/ps:5.1%}  garden {go/gs:5.1%}")
cons = {2006:(1621.5,136.8),2007:(1671.1,99.4),2008:(1705.4,-324.4),2009:(1614.3,126.0),2010:(1523.6,109.1),2011:(1628.7,85.2),
2012:(1700.0,74.4),2013:(1653.6,40.2),2014:(1604.4,56.2),2015:(1650.7,91.4),2016:(1829.0,129.4),2017:(2054.5,156.1),2018:(2215.4,167.3),
2019:(2383.0,152.1),2020:(2695.5,198.0),2021:(3303.7,254.5),2022:(3338.6,260.0),2023:(3310.1,210.6),2024:(3200.5,185.4),2025:(3129.1,250.0)}
print("consolidated op margin", {y: f"{o/s:.1%}" for y,(s,o) in cons.items()})
