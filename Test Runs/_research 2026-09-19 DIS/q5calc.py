CAP   = 177279.0      # 1,726,686,902 x $102.67
PX    = 102.67
SH    = 1726.686902   # millions
SOV   = 5.34
FLOOR = 10.0

OCF  = {2017:12343,2018:14295,2019:5984,2020:7616,2021:5566,2022:6002,2023:9866,2024:13971,2025:18101}
DEP  = {2017:2586,2018:2758,2019:2844,2020:3140,2021:3068,2022:3183,2023:3626,2024:3434,2025:3859}
CAPX = {2017:3623,2018:4465,2019:4876,2020:4022,2021:3578,2022:4943,2023:4969,2024:5412,2025:8024}
SBC  = {2017:364,2018:393,2019:711,2020:525,2021:600,2022:977,2023:1143,2024:1366,2025:1363}
SHD  = {2017:1578,2018:1507,2019:1666,2020:1808,2021:1828,2022:1827,2023:1830,2024:1831,2025:1811}

print('OWNER EARNINGS PER SHARE, at the D&A end of (c) (the optimistic end), by year')
print(' yr    OCF   -SBC   -dep  =  OE      diluted sh    OE/share')
for y in sorted(OCF):
    oe = OCF[y]-SBC[y]-DEP[y]
    print(f' {y} {OCF[y]:6,} {SBC[y]:6,} {DEP[y]:6,}  {oe:7,}   {SHD[y]:9,}   ${oe/SHD[y]:6.2f}')
a, b = 2018, 2025
oa = (OCF[a]-SBC[a]-DEP[a])/SHD[a]; ob = (OCF[b]-SBC[b]-DEP[b])/SHD[b]
print(f'\n FY{a} ${oa:.2f}/sh -> FY{b} ${ob:.2f}/sh = {(ob/oa)**(1/(b-a))-1:+.2%} a year over {b-a} years')
print(f' and at the CAPEX end: FY{a} ${(OCF[a]-SBC[a]-CAPX[a])/SHD[a]:.2f} -> FY{b} '
      f'${(OCF[b]-SBC[b]-CAPX[b])/SHD[b]:.2f}')
print()
print('WHAT THE BUSINESS HAS ACTUALLY DONE, compound, off the filed statements')
for lab, x0, y0, x1, y1 in [('revenue', 69607, 2019, 94425, 2025),
                            ('revenue (from pre-TFCF)', 59434, 2018, 94425, 2025),
                            ('net income attributable', 12598, 2018, 12404, 2025),
                            ('operating cash flow', 14295, 2018, 18101, 2025),
                            ('segment operating income', 12863, 2023, 17551, 2025)]:
    print(f'  {lab:28} FY{y0} {x0:,} -> FY{y1} {x1:,} = {(x1/x0)**(1/(y1-y0))-1:+.2%} a year')
print()
RANGES = {
 'FY2021-25 default':            (3655, 6177),
 'FY2021-25 at CENTRAL (c)':     (4920, 5491),
 'FY2019-23 earlier five':       (1294, 3043),
 'FY2019-25 seven years':        (3077, 5324),
 'FY2022-25 pandemic excluded':  (4370, 7247),
 'FY2023-25 current shape':      (6096, 9049),
 'TTM to 2026-06-27':            (6774, 11370),
 'FY2026 on company guidance':   (8481, 13381),
}
print('1. THE YIELD -- owner earnings / market cap, beside the sovereign of %.2f%%' % SOV)
for k,(lo,hi) in RANGES.items():
    print(f'  {k:30} ${lo:6,}-${hi:6,}M  =  {lo/CAP*100:5.2f}% - {hi/CAP*100:5.2f}%'
          f'   {"CLEARS bond at top" if hi/CAP*100>SOV else "below the bond at BOTH ends"}')
print()
print('2. WHAT THE PRICE ALREADY ASSUMES -- perpetual growth needed, OE/(r-g) = cap')
for k,(lo,hi) in RANGES.items():
    out=[]
    for r in (FLOOR, SOV):
        for v in (lo, hi):
            g = r/100 - v/CAP
            out.append(f'{g*100:+6.2f}%')
    print(f'  {k:30} at 10% floor: {out[0]} (cons) {out[1]} (opt) | at bond: {out[2]} {out[3]}')
print()
print('3. WHAT YOU ARE PAID -- points over the sovereign')
for k,(lo,hi) in RANGES.items():
    print(f'  {k:30} {lo/CAP*100-SOV:+6.2f} to {hi/CAP*100-SOV:+6.2f} points')
print()
print('THE VALUE AS A ROUND-NUMBER RANGE')
for r,lab in ((FLOOR,'at the ~10% floor [E4-28]'), (SOV,'at the sovereign %.2f%% [E4-21]'%SOV)):
    lo = 3655/(r/100); hi = 13381/(r/100)
    print(f'  {lab:34} ${lo:7,.0f}M to ${hi:7,.0f}M  =  ${lo/SH:5.0f} to ${hi/SH:5.0f} a share'
          f'   (price ${PX})')
print()
print('FLOOR TEST: honest pre-tax expectancy at this price, no growth')
for k,(lo,hi) in RANGES.items():
    print(f'  {k:30} {lo/CAP*100:5.2f}% - {hi/CAP*100:5.2f}%   vs ~10%  -> QUIT ON')
