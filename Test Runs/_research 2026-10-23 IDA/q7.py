# Q7 arithmetic for IDA, figures from the filed cash flow statements (USD millions)
# 2021-2022: 10-K FY2022 acc 0001057877-23-000007; 2023-2025: 10-K FY2025 acc 0001057877-26-000028
Y   = [2021, 2022, 2023, 2024, 2025]
OCF = [363.264, 351.285, 267.027, 594.417, 601.838]
SBC = [8.583, 10.279, 9.578, 11.708, 12.505]          # statements of equity
CPX = [299.999, 432.589, 611.137, 1009.279, 1179.327]  # additions to PP&E
RMB = [5.876, 17.778, 26.501, 83.708, 151.880]         # transmission joint-funding partner payments
FLP = [0, 0, 0, 0, 3.762]                              # finance lease principal
DA  = [179.444, 173.555, 199.908, 228.091, 258.402]
LTI = [0, 198.0, 872.0, 300.0, 400.0]                  # LTD issued
LTR = [0, 4.360, 225.0, 49.800, 19.885]                # LTD retired
INT = [83.5, 86.0, 97.742, 109.067, 139.277]           # cash interest paid net of capitalized (2021-22 XBRL InterestPaidNet)
REV = [1458.1, 1644.0, 1766.356, 1826.633, 1812.997]
DEBT_SHARE = 0.49   # Idaho 2025 settlement: 7.41% ROR on filed structure ~49% LTD / 51% equity (8-K 2025-05-30)
r, f = 0.0529, 0.10
SH = 57.842043      # cover, 10-Q acc 0001057877-26-000129, as of 2026-07-24
P = 142.06
avg = lambda a: sum(a)/len(a)
netcpx = [c - m for c, m in zip(CPX, RMB)]
oc_all = [o - s - n - l for o, s, n, l in zip(OCF, SBC, netcpx, FLP)]
oc_mnt = [o - s - d - l for o, s, d, l in zip(OCF, SBC, DA, FLP)]
netlt = [i - t for i, t in zip(LTI, LTR)]
cap_win = DEBT_SHARE * sum(netcpx)
credit_win = min(sum(netlt), cap_win)
credit_gross = min(sum(LTI), cap_win)
yearly_credit = [min(n, DEBT_SHARE*c) for n, c in zip(netlt, netcpx)]
print('year      OCF   SBC  netcapex   D&A  OC_all  OC_maint  netLTD  yr-credit  OC_all+yrcredit')
for i, y in enumerate(Y):
    print(y, '%7.1f %5.1f %8.1f %6.1f %7.1f %8.1f %7.1f %9.1f %9.1f' % (OCF[i], SBC[i], netcpx[i], DA[i], oc_all[i], oc_mnt[i], netlt[i], yearly_credit[i], oc_all[i]+yearly_credit[i]))
print('averages: OC_all %.1f  OC_maint %.1f  netcapex %.1f  D&A %.1f' % (avg(oc_all), avg(oc_mnt), avg(netcpx), avg(DA)))
print('window net LTD %.1f, gross LTD %.1f, cap (%.0f%% of net capex %.1f) %.1f' % (sum(netlt), sum(LTI), DEBT_SHARE*100, sum(netcpx), cap_win))
oc_central = avg(oc_all) + credit_win/5
print('central equity-only, all spending less window debt credit: %.1f /yr' % oc_central)
print('  variant gross-debt credit: %.1f ; variant yearly-capped credit: %.1f' % (avg(oc_all)+credit_gross/5, avg(oc_all)+sum(yearly_credit)/5))
def pv(base, g, rate, yrs=10):
    v = 0; c = base
    for t in range(1, yrs+1):
        c *= (1+g); v += c/(1+rate)**t
    return v + (c/rate)/(1+rate)**yrs
for name, base in [('bottom: all spending less debt credit, no growth', oc_central), ('top: maintenance-only (D&A), no growth', avg(oc_mnt))]:
    v = pv(base, 0, r); vf = pv(base, 0, f)
    print('%-52s base %.1f  value@%.2f%% %.0f = $%.2f/sh ; @10%% %.0f = $%.2f/sh' % (name, base, r*100, v, v/SH, vf, vf/SH))
g_sales = (REV[-1]/REV[0])**(1/4)-1
print('sales growth 2021-2025 %.2f%%' % (g_sales*100))
v = pv(avg(oc_mnt), g_sales, r); print('maintenance-only WITH sales growth (growth spending uncharged, shown only as a bound): $%.2f/sh' % (v/SH))
# halves test on the credited yearly series
s = [a+c for a, c in zip(oc_all, yearly_credit)]
print('halves (yearly-credit series): first %.1f second %.1f' % (avg(s[:2]), avg(s[3:])))
# maintenance-only growth: halves
print('halves (maint series): first %.1f second %.1f ; CAGR 21-25 %.1f%%' % (avg(oc_mnt[:2]), avg(oc_mnt[3:]), ((oc_mnt[-1]/oc_mnt[0])**0.25-1)*100))
print('max share of sales of maint OC: %.1f%%' % (max(o/rv for o, rv in zip(oc_mnt, REV))*100))
mc = SH*P; print('market cap $%.0fM; yield of central %.2f%%, of maint-only %.2f%%' % (mc, oc_central/mc*100, avg(oc_mnt)/mc*100))
# fair price equity-only: average of the two end cases valued at 10%
fb = pv(oc_central, 0, f)/SH; ft = pv(avg(oc_mnt), 0, f)/SH
print('FAIR equity-only: bottom $%.2f top $%.2f -> fair $%.2f' % (fb, ft, (fb+ft)/2))
# all-equity beside: owner cash before interest (after-tax at 21%), all spending, no debt credit; less net debt
ND = 3677.926 + 116.300 + 213.560 - 83.644 - 186.775   # LTD + current + finance lease (noncurrent) - cash - July FSA settlement proceeds; July PCRB repayment nets to zero
ia = avg(INT)*(1-0.21)
ae_bot = avg(oc_all) + ia; ae_top = avg(oc_mnt) + ia
print('net debt %.0f ; interest after tax %.1f' % (ND, ia))
for nm, b in [('all-equity bottom', ae_bot), ('all-equity top', ae_top)]:
    print('%s base %.1f value@r per sh $%.2f ; @10%% per sh $%.2f' % (nm, b, (pv(b,0,r)-ND)/SH, (pv(b,0,f)-ND)/SH))
print('FAIR all-equity: $%.2f' % (((pv(ae_bot,0,f)-ND)/SH + (pv(ae_top,0,f)-ND)/SH)/2))
# literal window (run.py as filed): OE capex 5-yr -270.9

print('\n--- (e) maintenance central: growth case charges equity-funded growth spending against the growth it buys ---')
gsp_all = avg(netcpx) - avg(DA)                 # growth spending, all sources
gsp_eq  = gsp_all - credit_win/5                # less debt credit (equity-funded part)
gsp_eq25 = (netcpx[-1]-DA[-1]) - netlt[-1]      # 2025 level, for the variant
print('growth spending avg %.1f ; equity-funded after window credit %.1f ; 2025 equity-funded level %.1f' % (gsp_all, gsp_eq, gsp_eq25))
def ann(x, rate, yrs=10): return x*(1-(1+rate)**-yrs)/rate
m = avg(oc_mnt)
for rate in (r, f):
    nog = pv(m, 0, rate); gro = pv(m, g_sales, rate) - ann(gsp_eq, rate); gro25 = pv(m, g_sales, rate) - ann(gsp_eq25, rate)
    print('rate %.2f%%: no-growth $%.2f/sh ; growth (avg equity growth spend) $%.2f/sh ; growth (2025 level) $%.2f/sh' % (rate*100, nog/SH, gro/SH, gro25/SH))
nog10 = pv(m,0,f)/SH; gro10 = (pv(m,g_sales,f)-ann(gsp_eq,f))/SH
print('FAIR equity-only (maint central): ($%.2f + $%.2f)/2 = $%.2f' % (nog10, gro10, (nog10+gro10)/2))
# IRR of growth case at the price
lo, hi = 0.0001, 0.2
for _ in range(100):
    mid = (lo+hi)/2
    v = pv(m, g_sales, mid) - ann(gsp_eq, mid)
    if v > SH*P: lo = mid
    else: hi = mid
print('expected return at the price, growth case: %.2f%% ; no-growth case: %.2f%%' % (mid*100, m/(SH*P)*100))
# all-equity beside (no debt credit, before interest after 21%% tax shield)
ae_m = m + ia
for rate in (r, f):
    nog = pv(ae_m, 0, rate) - ND; gro = pv(ae_m, g_sales, rate) - ann(gsp_all, rate) - ND
    print('ALL-EQUITY rate %.2f%%: no-growth $%.2f/sh ; growth $%.2f/sh' % (rate*100, nog/SH, gro/SH))
print('FAIR all-equity: $%.2f' % (((pv(ae_m,0,f)-ND) + (pv(ae_m,g_sales,f)-ann(gsp_all,f)-ND))/2/SH))
