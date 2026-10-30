# DEER owner cash and COMPUTATION, NOT A CLEARANCE. Figures in USD as filed (translated from RMB by the filer).
# Sources: FY2011 10-K 0001185185-12-000545 (2009-2011 cash flows), FY2009 10-K/A 0001144204-10-034192 (2008),
# FY2008 10-K 0001144204-09-017240 (2007), 10-Q Q2 2012 0001185185-12-001666 (H1 2012, balance sheet 2012-06-30).
ocf = {2007: 432890, 2008: 3037566, 2009: 384221, 2010: 11076019, 2011: 5968640}
# all capital spending as filed: PP&E, intangibles (land use rights), construction in progress, land deposits,
# equipment advances, less the land deposit refunded in 2011 (restricted cash and short-term investments excluded)
spend = {
 2007: 2191640 + 162263 - 111835,
 2008: 3627873 + 8319 + 559651,
 2009: 1474527 + 2829702,
 2010: 10095861 + 36441355 + 4601917 + 4969627,
 2011: 10444879 + 4325011 + 17587593 + 826923 + 824307 - 10513006,
}
da = {2007: 795531 + 18509, 2008: 1199578 + 18723, 2009: 1449186, 2010: 1640882, 2011: 2965616}
ni = {2007: 3421592, 2008: 3356784, 2009: 12369062, 2010: 30349037, 2011: 39805629}
rev = {2007: 33476259, 2008: 43784935, 2009: 81342680, 2010: 175846887, 2011: 226748885}
oc = {y: ocf[y] - spend[y] for y in ocf}
dv = {y: ocf[y] - da[y] for y in ocf}
for y in ocf:
    print(y, f"OCF {ocf[y]/1e6:8.3f}  spend {spend[y]/1e6:8.3f}  owner cash {oc[y]/1e6:8.3f}  "
          f"OCF-D&A {dv[y]/1e6:7.3f}  net income {ni[y]/1e6:7.3f}  revenue {rev[y]/1e6:8.3f}")
avg = sum(oc.values())/5; avgd = sum(dv.values())/5
print(f"5y sum owner cash {sum(oc.values())/1e6:.3f}  avg {avg/1e6:.3f}; 5y sum net income {sum(ni.values())/1e6:.3f}; 5y sum OCF {sum(ocf.values())/1e6:.3f}")
print(f"depreciation variant avg {avgd/1e6:.4f}")
h1 = -2404632 - (10570 + 52299 + 26620)
print(f"H1 2012 owner cash {h1/1e6:.3f} (net income H1 2012 13.552)")
shares = 33592562; price = 0.0002; netcash = 9401816 + 474316  # 2012-06-30, no borrowings (notes payable nil)
r = 0.0206
print(f"market cap ${shares*price:,.2f}; net cash {netcash/1e6:.3f}M; EV {(shares*price-netcash)/1e6:.3f}M")
def pv(c0, g, rate, yrs=10):
    v = 0; c = c0
    for t in range(1, yrs+1):
        c *= (1+g); v += c/(1+rate)**t
    v += c/rate/(1+rate)**yrs   # zero nominal growth after year ten
    return v
for label, c0 in (("central, all spending", avg), ("depreciation variant", avgd)):
    for rate in (r, 0.10):
        v0 = pv(c0, 0, rate)
        print(f"{label} no-growth @ {rate:.4f}: business {v0/1e6:9.3f}M  per share {(v0+netcash)/shares:8.4f}")
    vg = pv(avgd, r, r) if label.startswith("dep") else None
    if vg is not None:
        print(f"  growth case capped at the discount rate 2.06% @2.06%: per share {(vg+netcash)/shares:.4f}; "
              f"@10%: {(pv(avgd, r, 0.10)+netcash)/shares:.4f}")
        fp = ((pv(avgd,0,0.10)+netcash)/shares + (pv(avgd,r,0.10)+netcash)/shares)/2
        print(f"  variant fair price (average of the two ends at 10%) {fp:.4f}")
print(f"revenue CAGR 2007-2011 {((rev[2011]/rev[2007])**0.25-1)*100:.1f}%")
