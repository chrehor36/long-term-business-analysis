"""Owner cash arithmetic for MARUY from the audited consolidated cash flow statements (JPY bn).
Each fiscal year FYn ends March 31 of n+1. Figures transcribed from the current-year column of
each year's English Consolidated Financial Statements (cache/fs_*.pdf); FY2015 from the FY2016 file's comparative."""
D = {  # OCF, ICF, PPE purchase, PPE sale, sub acq, sub sale, inv purch, inv sale, lease principal, hybrid dist, int paid, int recd, dep&amort, net profit to owners
 2015: (359.1,-174.6,259.3,26.5,13.8,52.1,111.7,117.0, 0.0,0.0,34.5,15.1,111.7, 62.3),
 2016: (324.3,  46.5,131.0,89.7,10.7,56.6, 89.8,105.8, 0.0,2.0,33.4,13.4,121.5,155.4),
 2017: (253.4, -49.7,103.2,15.6,23.0,51.7, 74.5, 63.4, 0.0,4.0,35.1, 9.6,120.3,211.3),
 2018: (284.9,  22.5, 93.2, 6.0,-7.2,12.0, 52.2,123.3, 0.0,4.0,44.2,11.4,113.5,230.9),
 2019: (327.0,-209.8,109.9, 8.7,15.4,15.8,199.2, 66.4,55.8,3.9,48.9,11.7,166.9,-197.5),
 2020: (397.1,-116.3,124.1, 7.1,18.8, 8.8, 70.1, 79.4,55.5,3.9,24.3, 9.0,144.4,223.3),
 2021: (311.9, -79.7,101.8,14.1, 7.8, 9.1, 57.6, 69.8,56.2,3.1,21.6, 8.9,143.0,424.3),
 2022: (606.3, 156.8,104.3,18.0, 8.1,330.1,100.7,44.1,59.6,2.6,54.0,22.0,156.5,543.0),
 2023: (442.5,-334.4,153.4,21.7,56.1, 1.0,215.3, 72.0,74.7,1.3,74.5,27.4,177.7,471.4),
 2024: (597.9,-395.3,177.6,12.8,50.2,12.2,322.7,127.7,79.3,0.0,81.3,22.9,199.3,503.0),
 2025: (535.4,-118.0,153.5,24.3,80.1,77.7,154.4,138.4,75.6,0.0,79.3,23.7,209.1,543.9),
}
T = 0.3062  # CONVENTION of this run: Japanese statutory effective rate used to put net interest after tax
rows = {}
print("FY   OCF   ICF  netPPE netBuy  lease  OwnerEq  OwnerOrg  NetIntAT  OwnerAllEq OrgAllEq  NP")
for y, (ocf, icf, pp, ps, sa, ss, ip, isl, ls, hy, ipd, ir, da, np) in D.items():
    netppe = pp - ps
    netbuy = sa - ss + ip - isl
    eq = ocf + icf - ls - hy                 # acquisitions deducted, all investing deducted
    org = eq + netbuy                        # before net purchases of businesses
    nit = (ipd - ir) * (1 - T)
    rows[y] = dict(eq=eq, org=org, ae=eq + nit, aorg=org + nit, netbuy=netbuy, np=np)
    print(f"{y} {ocf:6.1f} {icf:6.1f} {netppe:6.1f} {netbuy:6.1f} {ls:5.1f} {eq:8.1f} {org:8.1f} {nit:8.1f} {eq+nit:9.1f} {org+nit:8.1f} {np:6.1f}")
def avg(k, ys): return sum(rows[y][k] for y in ys) / len(ys)
w = range(2021, 2026); w10 = range(2016, 2026)
for k in ("eq", "org", "ae", "aorg", "np"):
    print(f"{k}: 5yr avg {avg(k,w):7.1f}  FY2016-25 avg {avg(k,w10):7.1f}  FY2016-20 {avg(k,range(2016,2021)):7.1f}  FY2021-25 {avg(k,range(2021,2026)):7.1f}")
print("net purchases FY2021-25:", round(sum(rows[y]['netbuy'] for y in w), 1),
      " half of owner cash before purchases:", round(sum(rows[y]['org'] for y in w) / 2, 1))
