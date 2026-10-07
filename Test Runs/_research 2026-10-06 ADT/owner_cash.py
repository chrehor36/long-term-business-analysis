# Arithmetic only. Every input is a filed cash-flow line (USD millions), accession in the run file.
Y = {
 # year: OCF, SBC, dealer accts, subscriber system, PP&E, finance lease pmts, cash taxes, cash interest, D&A
 2017: (1591.930, 11.276, 653.222, 582.723, 130.624, 0.0, 19.433, 661.250, 1863.299),
 2018: (1787.607,135.012, 693.525, 576.290, 126.799, 0.0,  6.346, 688.121, 1930.929),
 2019: (1873.117, 85.626, 669.683, 542.305, 158.846, 0.0, -1.001, 545.206, 1989.082),
 2020: (1366.749, 96.013, 380.716, 418.355, 157.191,27.956,25.802, 510.185, 1913.767),
 2021: (1649.723, 61.237, 675.118, 694.684, 168.238,32.123, 1.877, 512.628, 1914.779),
 2022: (1887.920, 66.566, 621.695, 734.639, 176.660,44.978,22.654, 470.947, 1693.575),
 2023: (1657.726, 51.137, 588.638, 630.535, 176.353,43.733,60.296, 522.775, 1388.671),
 2024: (1884.899, 48.613, 585.809, 523.146, 163.805,29.023,21.700, 372.036, 1344.696),
 2025: (1884.163, 54.553, 596.483, 395.986, 175.747,30.209,142.168,409.415, 1367.234),
}
rows={}
print(f"{'yr':>5} {'OCF':>8} {'SBC':>6} {'dealer':>7} {'subsys':>7} {'PPE':>6} {'lease':>6} {'OWNER':>7} {'+tax=PRE':>8} {'+int=EV':>8} {'D&Avar':>7}")
for y,(ocf,sbc,dl,ss,pp,fl,tx,it,da) in Y.items():
    oc = ocf-sbc-dl-ss-pp-fl
    pre = oc+tx
    ev = pre+it
    dav = ocf-sbc-da
    rows[y]=(oc,pre,ev,dav)
    print(f"{y:>5} {ocf:8.1f} {sbc:6.1f} {dl:7.1f} {ss:7.1f} {pp:6.1f} {fl:6.1f} {oc:7.1f} {pre:8.1f} {ev:8.1f} {dav:7.1f}")
avg=lambda ys,i: sum(rows[y][i] for y in ys)/len(ys)
W5=[2021,2022,2023,2024,2025]; W9=list(range(2017,2026)); W2=[2024,2025]
for nm,ys in [("5yr 2021-25",W5),("whole span 2017-25",W9),("2024-25",W2)]:
    print(nm, "owner %.1f  pre-tax %.1f  pre-int(EV) %.1f  D&A var %.1f"%(avg(ys,0),avg(ys,1),avg(ys,2),avg(ys,3)))
r=0.0566
SH=730.559248  # cover 10-Q 2026-06-30: 675,814,723 + 54,744,525 Class B
P=6.21
ND=7775.286-28.037  # debt principal 6/30/2026 less cash+restricted cash 6/30/2026
def pv(c,g,r=r,n=10):
    v=0; x=c
    for t in range(1,n+1):
        x*=1+g; v+=x/(1+r)**t
    return v + x/r/(1+r)**n   # then zero nominal growth
print("market cap", round(P*SH,1), " net debt", round(ND,1))
for nm,ys in [("5yr",W5),("whole",W9),("2024-25",W2)]:
    c=avg(ys,0)
    lo=pv(c,0.0); hi=pv(c,0.008)
    print(f"{nm}: C={c:.1f} no-growth {lo:.0f} (${lo/SH:.2f}) | g=0.8% {hi:.0f} (${hi/SH:.2f})  ratio {hi/lo:.2f}  yield at price {c/(P*SH)*100:.1f}% pre-tax yield {avg(ys,1)/(P*SH)*100:.1f}%")
    fair_eq = avg(ys,1)/0.10/SH
    fair_ev = (avg(ys,2)/0.10-ND)/SH
    print(f"   FAIR (10% pre-tax on equity) ${fair_eq:.2f} ;  FAIR (10% pre-tax, pre-interest, on equity+net debt) ${fair_ev:.2f}")
