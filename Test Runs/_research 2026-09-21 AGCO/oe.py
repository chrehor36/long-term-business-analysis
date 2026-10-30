# All figures hand-transcribed from the filed Consolidated Statements of Cash Flows.
# Sources: FY2025 10-K (0000880266-26-000010) years 2023-25; FY2022 10-K
# (0000880266-23-000010) years 2020-22; FY2019 10-K (0000880266-20-000006) years 2017-19;
# FY2016 10-K (0000880266-17-000005) years 2014-16.
rows = [
 # yr, OCF, depreciation, amort_intang, SBC, capex, equity_earn_net_of_cash_recd
 (2014, 438.4, 239.4, 41.0, -10.8, 301.5, -25.4),
 (2015, 524.2, 217.4, 42.7,  12.2, 211.4, -19.0),
 (2016, 369.5, 223.4, 51.2,  18.1, 201.0,  -1.4),
 (2017, 577.6, 222.8, 57.0,  38.2, 203.9,  41.2),
 (2018, 595.9, 225.2, 64.7,  46.3, 203.3,  -3.2),
 (2019, 695.9, 210.9, 61.1,  41.3, 273.4,   0.0),
 (2020, 896.5, 212.5, 59.5,  37.6, 269.9, -43.7),
 (2021, 660.2, 220.7, 61.1,  27.4, 269.8,  -1.9),
 (2022, 838.2, 209.5, 60.1,  34.0, 388.3, -40.8),
 (2023,1103.1, 230.4, 57.7,  46.4, 518.1, -36.4),
 (2024, 689.9, 251.2, 81.0,  18.4, 393.3, -29.4),
 (2025, 988.1, 256.5, 71.1,  28.4, 247.9, -20.6),
]
print(f"{'yr':>5}{'OCF':>9}{'SBC':>8}{'undist':>8}{'dep':>8}{'capex':>9}{'OE_dep':>9}{'OE_capex':>10}")
out={}
for yr,ocf,dep,am,sbc,capex,eq in rows:
    undist = -eq if eq < 0 else 0.0   # add back the share NOT received in cash [E3-04]
    base = ocf - sbc + undist
    oe_dep   = base - dep            # (c) = depreciation, the [E3-44] default
    oe_capex = base - capex          # (c) = total capex, the [E5-20] conservative end
    out[yr]=(oe_dep,oe_capex)
    print(f"{yr:>5}{ocf:>9.1f}{sbc:>8.1f}{undist:>8.1f}{dep:>8.1f}{capex:>9.1f}{oe_dep:>9.1f}{oe_capex:>10.1f}")
def mean(ys,i):
    v=[out[y][i] for y in ys]; return sum(v)/len(v)
for label,ys in [("12y 2014-25",range(2014,2026)),("10y 2016-25",range(2016,2026)),
                 ("5y 2021-25",range(2021,2026)),("5y 2016-20",range(2016,2021)),
                 ("3y 2023-25",range(2023,2026)),("post-perimeter 2025 only",[2025])]:
    ys=list(ys)
    print(f"{label:>26}  D&A-end mean {mean(ys,0):8.1f}   capex-end mean {mean(ys,1):8.1f}")

print()
dep=[r[2] for r in rows]; cap=[r[5] for r in rows]
base={r[0]: r[1]-r[4]+(-r[6] if r[6]<0 else 0.0) for r in rows}
import statistics as st
print("mean depreciation 2014-25 %.1f ; mean capex %.1f ; ratio %.2f" % (st.mean(dep), st.mean(cap), st.mean(cap)/st.mean(dep)))
print("mean base (OCF - SBC + undistributed affiliate) 12y  %.1f" % st.mean(base.values()))
print("mean base 10y 2016-25 %.1f" % st.mean([base[y] for y in range(2016,2026)]))
print("mean base  5y 2021-25 %.1f" % st.mean([base[y] for y in range(2021,2026)]))
for c,lab in [(228.4,'(c)=mean depreciation 228.4'),(256.5,'(c)=2025 depreciation 256.5'),(290.4,'(c)=mean capex 290.4'),(350.0,'(c)=350 judged up')]:
    print("  %-32s  12y OE %7.1f   10y OE %7.1f   5y OE %7.1f" % (lab,
        st.mean(base.values())-c, st.mean([base[y] for y in range(2016,2026)])-c, st.mean([base[y] for y in range(2021,2026)])-c))
wc=[(2014,None)]
print()
print("working-capital contribution to OCF, filed detail lines:")
wcs={2020:194.8,2021:-451.2,2022:-293.5,2023:-112.7,2024:29.5,2025:495.6}
print("  ", wcs, " sum 2020-25 = %.1f" % sum(wcs.values()))
