# DIS owner earnings. All figures $M, from the filed statements (see run file for accessions).
OCF  = {2017:12343,2018:14295,2019:5984,2020:7616,2021:5566,2022:6002,2023:9866,2024:13971,2025:18101}
CAPX = {2017:3623,2018:4465,2019:4876,2020:4022,2021:3578,2022:4943,2023:4969,2024:5412,2025:8024}
DEP  = {2017:2586,2018:2758,2019:2844,2020:3140,2021:3068,2022:3183,2023:3626,2024:3434,2025:3859}
DA   = {2017:2782,2018:3011,2019:4167,2020:5345,2021:5111,2022:5163,2023:5369,2024:4990,2025:5326}
SBCc = {2019:711,2020:525,2021:600,2022:977,2023:1143,2024:1366,2025:1363}      # charge, net of capitalised
SBCcap={2023:145,2024:201,2025:194}                                              # capitalised, per footnote
# [E3-70] grant-date fair value of the year's grants: RSU units x WAGDFV + ~2M options x WAGDFV
RSUn = {2019:4,2020:6,2021:6,2022:13,2023:18,2024:18,2025:16}
RSUv = {2019:112.73,2020:142.77,2021:179.44,2022:136.36,2023:89.66,2024:93.90,2025:108.55}
OPTv = {2019:28.76,2020:36.19,2021:57.05,2022:46.76,2023:33.18,2024:32.09,2025:37.66}
SBCg = {y: round(RSUn[y]*RSUv[y] + 2*OPTv[y]) for y in RSUn}

CONTENT_SPEND = {2024:23435,2025:22709}
CONTENT_AMORT = {2024:24481,2025:23286}

TTM = dict(OCF=18101-13627+12515, CAPX=8024-6108+6780, SBCc=1363-1004+1160)

def mean(d, yrs): return sum(d[y] for y in yrs)/len(yrs)

WINDOWS = {
 'FY2021-25 (5y, the corpus default)': range(2021,2026),
 'FY2019-23 (5y, the earlier five)':   range(2019,2024),
 'FY2019-25 (7y, every filed year since the TFCF perimeter)': range(2019,2026),
 'FY2022-25 (4y, pandemic years excluded)': range(2022,2026),
 'FY2023-25 (3y, the current shape)': range(2023,2026),
 'FY2017-19 (3y, pre-TFCF, pre-streaming)': range(2017,2020),
}

print('SBC: charge vs [E3-70] grant value')
print(' yr  charge  capitalised  grant-value  grant/charge')
for y in sorted(SBCc):
    print(f' {y}  {SBCc[y]:6}  {SBCcap.get(y,0):11}  {SBCg[y]:11}  {SBCg[y]/SBCc[y]:11.2f}x')
print()
print('CONTENT: cash spend vs amortisation (content capital is INSIDE OCF)')
for y in sorted(CONTENT_SPEND):
    print(f' {y}  spend {CONTENT_SPEND[y]}  amort {CONTENT_AMORT[y]}  spend-less-amort {CONTENT_SPEND[y]-CONTENT_AMORT[y]:+}')
print()
print('OWNER EARNINGS = OCF - SBC - (c).  Two SBC measures, three (c) constructions.')
print()
hdr = ('window', 'OCF', 'SBCchg', 'SBCgrant', 'dep', 'capex',
       'OE@dep,chg', 'OE@dep,grant', 'OE@capex,chg', 'OE@capex,grant')
print(' | '.join(h.rjust(11) for h in hdr))
rows = {}
for name, yrs in WINDOWS.items():
    yrs = list(yrs)
    o, sc, sg, dp, cx = mean(OCF,yrs), mean(SBCc,yrs) if all(y in SBCc for y in yrs) else None, \
        mean(SBCg,yrs) if all(y in SBCg for y in yrs) else None, mean(DEP,yrs), mean(CAPX,yrs)
    if sc is None:
        sc = sg = 400.0   # FY2017-18 charge 364/393 -> use charge; grant not published
    vals = [o - sc - dp, o - sg - dp, o - sc - cx, o - sg - cx]
    rows[name] = vals
    print(' | '.join([name[:11].rjust(11)] + [f'{v:11.0f}' for v in [o,sc,sg,dp,cx]+vals]))
print()
for name, yrs in WINDOWS.items():
    v = rows[name]
    print(f'{name}')
    print(f'   OE range {min(v):,.0f} to {max(v):,.0f}')
print()
print('TTM to 2026-06-27:', TTM, ' capex TTM', TTM['CAPX'])
print('FY2026 company guidance: OCF at least 19,000 ; capex approximately 9,000')
print('  -> guided OCF less guided capex less TTM SBC charge =', 19000-9000-TTM['SBCc'])
print('  -> guided OCF less ~4,100 depreciation less TTM SBC charge =', 19000-4100-TTM['SBCc'])
CAP = 177279.0
print()
print('YIELDS on market cap $%.0fM (1,726,686,902 x $102.67)' % CAP)
for name in WINDOWS:
    v = rows[name]
    print(f'  {name[:48]:48} {min(v)/CAP*100:5.2f}% to {max(v)/CAP*100:5.2f}%')
