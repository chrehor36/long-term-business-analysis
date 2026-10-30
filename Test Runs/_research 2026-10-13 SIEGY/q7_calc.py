# Q7 arithmetic for the SIEGY run (2026-10-13). Figures in EUR millions from the filed reports cited in the run file.
# Same number sooner: every input is a filed figure; the method is Q7's range convention.
yrs = [2021, 2022, 2023, 2024, 2025]
fcf_cont = [8379, 8304, 10146, 9726, 11004]   # Free cash flow, continuing ops (FY2025 five-year summary; FY2021 from AR2021)
sbc      = [294, 376, 444, 530, 535]          # share-based payment expense credited to capital reserve (notes 19/20)
nci      = [537, 669, 579, 691, 767]          # net income attributable to non-controlling interests
intpaid  = [704, 824, 1208, 1462, 1733]       # interest paid (financing activities)
sfs_fcf  = [820, 985, 852, 785, 747]          # SFS segment free cash flow (note 29)
acq      = [14391, 2207, 407, 413, 14236]     # acquisitions of businesses, net of cash acquired
disp     = [2+1698, 2078, 368+281, 60, 553+3216]  # disposals of businesses (continuing + discontinued investing where a business sale)
oc  = [f - s - n for f, s, n in zip(fcf_cont, sbc, nci)]
r = 0.0378        # ECB AAA 30Y, 2026-10-09
floor = 0.10
price = 272.10    # Xetra close 2026-10-09 (aggregator, flagged)
shares = 768.1    # millions, derived in Step 0
mc = price * shares
netdebt_before_securities = 8600 + 41324 - 10930 + 1233   # Jun 30 2026 debt less cash, plus buyback cash paid Jul 1 to Oct 9 2026
securities = 12420   # Level 1 equity instruments at FVOCI, Half-year report Note 8, Mar 31 2026 (latest filing that states them)
netdebt = netdebt_before_securities - securities
def pv(c0, g, rate, n=10):
    v = 0; c = c0
    for t in range(1, n + 1):
        c *= (1 + g); v += c / (1 + rate) ** t
    return v + c / rate / (1 + rate) ** n
def report(label, base, g, nd, sh=shares):
    lo_g, hi_g = (0.0, g) if g >= 0 else (g, 0.0)
    v_lo, v_hi = pv(base, lo_g, r), pv(base, hi_g, r)
    f_lo, f_hi = pv(base, lo_g, floor), pv(base, hi_g, floor)
    ev = mc + nd
    print(f"--- {label}: base {base:,.0f}, growth {g*100:.2f}%")
    print(f"  range at {r*100:.2f}%: EUR {(v_lo-nd)/sh:,.2f} to {(v_hi-nd)/sh:,.2f} a share (whole {v_lo:,.0f} to {v_hi:,.0f}); width {(v_hi-nd)/(v_lo-nd):.2f}x")
    print(f"  at 10%: whole {f_lo:,.0f} to {f_hi:,.0f} vs price EV {ev:,.0f}; floor met by any case: {max(f_lo,f_hi) >= ev}")
    print(f"  fair price: EUR {((f_lo+f_hi)/2 - nd)/sh:,.2f} a share (ADS {((f_lo+f_hi)/2 - nd)/sh/2:,.2f})")
avg = lambda x: sum(x) / len(x)
print("owner cash by year", oc, "avg", avg(oc))
g_shown = (oc[-1] / oc[0]) ** 0.25 - 1
g_org = (1.08 * 1.11 * 1.03 * 1.05) ** 0.25 - 1
netp = sum(acq) - sum(disp)
print(f"net purchases {netp:,} vs owner cash before purchases {sum(oc):,} ratio {netp/sum(oc):.2f}")
print(f"market cap {mc:,.0f}; net debt {netdebt:,}; EV {mc+netdebt:,.0f}; price/ADS ${price*2:.0f}eq")
report("CENTRAL all-equity, organic pair (serial acquirer)", avg(oc), g_org, netdebt)
# equity-only beside
oc_eq = [o - i for o, i in zip(oc, intpaid)]
print("equity-only owner cash", oc_eq, "avg", avg(oc_eq))
report("beside: equity-only, organic pair (securities added to equity value)", avg(oc_eq), g_org, -securities)
report("beside: all-equity, securities NOT deducted", avg(oc), g_org, netdebt_before_securities)
# industrial basis beside: SFS out of owner cash and out of net debt, SFS added at its net assets
oc_ind = [o - s for o, s in zip(oc, sfs_fcf)]
nd_ind = netdebt - 28898 - (33365 - 28898)
report("beside: industrial basis (SFS FCF out, SFS debt out, SFS net assets added)", avg(oc_ind), g_org, nd_ind)
# literal window shown beside (no cycle adjustment needed; same window)
# default pair, corrected for specific (c): purchases deducted in years 1-10 while total growth is credited;
# after year ten growth and purchases stop, terminal on owner cash before purchases. The no-growth end buys no growth, spends nothing.
def pv_default(pre0, purch0, g, rate):
    v = 0; pre = pre0; pu = purch0
    for t in range(1, 11):
        pre *= (1 + g); pu *= (1 + g); v += (pre - pu) / (1 + rate) ** t
    return v + pre / rate / (1 + rate) ** 10
pre0, pu0 = avg(oc), netp / 5
for rate in (r, floor):
    lo = pv(pre0, 0.0, rate); hi = pv_default(pre0, pu0, g_shown, rate)
    print(f"default pair at {rate*100:.2f}%: no-growth {lo:,.0f}, total-growth-with-purchases {hi:,.0f}; per share {(lo-netdebt)/shares:,.2f} / {(hi-netdebt)/shares:,.2f}")
lo10 = pv(pre0, 0.0, floor); hi10 = pv_default(pre0, pu0, g_shown, floor)
print(f"default pair fair price EUR {((lo10+hi10)/2-netdebt)/shares:,.2f}")
