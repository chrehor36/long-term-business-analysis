# $ millions. XBRL-sourced screening series (companyfacts, CIK 0000006845), cross-checked
# against the filed CONSOLIDATED STATEMENTS OF CASH FLOWS in the FY2026 and FY2021 10-Ks.
# fy_label : (OCF, capex_PPE, D&A, SBC, NetIncome, acquisitions)
D={
2010:( 97.2,  9.8, 29.6, 6.1,  31.7,   0.0),
2011:( -8.0,  9.1, 28.2, 5.2, -10.3,  20.6),
2012:( 24.6,  9.7, 27.2, 4.4,   4.6,   0.1),
2013:( 40.5, 34.7, 26.5, 4.4,  19.1,   0.0),
2014:( 52.9, 41.9, 26.6, 4.7,  28.0,  53.3),
2015:( 71.8, 27.2, 29.4, 4.8,  50.5,   0.0),
2016:(128.9, 42.0, 31.2, 4.9,  65.3,   0.0),
2017:(124.0, 68.1, 35.6, 6.0,  85.8, 137.9),
2018:(127.5, 53.2, 54.8, 6.2,  79.5, 182.8),
2019:( 96.4, 60.7, 49.8, 6.3,  45.7,   0.0),
2020:(107.3, 51.4, 46.8, 6.6,  61.9,   0.0),
2021:(141.9, 26.2, 51.4, 8.6,  15.4,   0.0),
2022:(100.5, 21.8, 50.0, 6.3,   3.5,   0.0),
2023:(102.7, 45.2, 42.4, 8.7, 104.1,   0.0),
2024:(204.2, 43.2, 41.6, 9.7,  99.6,   0.0),
2025:(125.2, 35.6, 44.6,10.7,  85.1, 232.2),
2026:(122.5, 27.3, 50.0, 8.2,  54.1,   0.0),
}
print(f"{'FY':>5} {'OCF':>7} {'capex':>7} {'D&A':>7} {'SBC':>6} | {'OE c=D&A':>9} {'OE c=capex':>11}  {'NI':>7} {'acq':>7}")
R={}
for fy,(ocf,cx,da,sbc,ni,acq) in D.items():
    a=round(ocf-sbc-da,1); b=round(ocf-sbc-cx,1)
    R[fy]=(a,b,ocf,cx,da,sbc,ni)
    print(f"{fy:>5} {ocf:>7.1f} {cx:>7.1f} {da:>7.1f} {sbc:>6.1f} | {a:>9.1f} {b:>11.1f}  {ni:>7.1f} {acq:>7.1f}")
def mean(a,b,i):
    v=[R[f][i] for f in range(a,b+1)]; return sum(v)/len(v)
print()
for (a,b) in [(2022,2026),(2018,2026),(2010,2026),(2012,2026),(2017,2026),(2024,2026),(2013,2017),(2018,2022)]:
    print(f"  {a}-{b} ({b-a+1}y): OE c=D&A {mean(a,b,0):7.1f}M | OE c=capex {mean(a,b,1):7.1f}M | OCF {mean(a,b,2):7.1f}M | capex {mean(a,b,3):6.1f}M | D&A {mean(a,b,4):6.1f}M")
CAP=767.95
print()
print(f"  cap (hand-struck) ${CAP:.1f}M   sovereign 5.34%")
for (a,b) in [(2022,2026),(2018,2026),(2010,2026)]:
    lo=min(mean(a,b,0),mean(a,b,1)); hi=max(mean(a,b,0),mean(a,b,1))
    print(f"  {a}-{b}: yield {lo/CAP*100:5.2f}% to {hi/CAP*100:5.2f}%")
