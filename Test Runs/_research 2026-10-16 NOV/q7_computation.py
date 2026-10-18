# COMPUTATION, NOT A CLEARANCE. NOV value range and fair price under Q7's range convention, beneath the Q2 STOP.
# Inputs: first-filed XBRL values from each 10-K (USD millions), transcribed in facts.py output; see run file for accessions.
Y = list(range(2008, 2026))
OCF  = dict(zip(Y,[2294,2095,1542,2143,620,3397,2614,1332,960,832,521,714,926,291,-179,143,1304,1251]))
SBC  = dict(zip(Y,[67,68,66,73,80,92,101,109,107,124,110,130,105,78,67,66,70,67]))
CAPEX= dict(zip(Y,[379,250,232,483,583,669,699,453,284,192,244,233,226,201,214,283,351,375]))
FLP  = {2017:6,2018:8,2019:32,2020:31,2021:26,2022:24,2023:23,2024:28,2025:28}
ACQ  = dict(zip(Y,[3008,573,556,1038,2880,2397,291,86,230,86,280,180,14,52,49,22,298,0]))
DIV  = {2024:176}
INTP = {2014:102,2015:103,2016:101,2017:97,2018:90,2019:85,2020:83,2021:76,2022:75,2023:85,2024:86,2025:85}
INTI = {2014:18,2015:14,2016:15,2017:25,2018:25,2019:20,2020:7,2021:9,2022:19,2023:28,2024:38,2025:51}
DEP  = dict(zip(Y,[222,249,262,279,323,392,413,391,370,359,349,355,302,264,250,260,294,300]))
SALES= dict(zip(Y,[13431,12712,12156,14658,20041,22869,21440,14757,7251,7304,8453,8479,6090,5524,7237,8583,8870,8744]))
T = 0.21   # CONVENTION of this run: interest tax shield at the US federal statutory rate
def oc(y, acq=True, alleq=True, dep=False):
    v = OCF[y] - SBC[y] - (DEP[y] if dep else CAPEX[y]) - FLP.get(y,0)
    if acq: v += -ACQ[y] + DIV.get(y,0)
    if alleq: v += (INTP.get(y,0) - INTI.get(y,0)) * (1-T)
    return v
avg = lambda ys, **k: sum(oc(y, **k) for y in ys)/len(ys)
r, floor = 0.0543, 0.10
shares, netdebt, price = 356.478125, 1706-1164, 18.64
mcap = price*shares; ev = mcap + netdebt
def value(cf, g, rate, n=10):
    v, c = 0.0, cf
    for t in range(1, n+1):
        c *= (1+g); v += c/(1+rate)**t
    return v + c/rate/(1+rate)**n
print('owner cash by year (all-equity, acquisitions net deducted):')
for y in Y: print(' ', y, round(oc(y)), ' before acq', round(oc(y, acq=False)), ' equity-only', round(oc(y, alleq=False)), ' depreciation basis', round(oc(y, dep=True)), f' share of sales {100*oc(y,acq=False)/SALES[y]:.1f}%')
cyc  = list(range(2015, 2025)); prev = list(range(2008, 2015)); win = list(range(2021, 2026))
B   = avg(cyc); Bo = avg(cyc, acq=False); Be = avg(cyc, alleq=False); Bd = avg(cyc, dep=True); Bw = avg(win); Bwe = avg(win, alleq=False)
P   = avg(prev); Po = avg(prev, acq=False)
sg = (sum(SALES[y] for y in cyc)/len(cyc) / (sum(SALES[y] for y in prev)/len(prev)))**(1/8.5) - 1
og = (Bo/Po)**(1/8.5) - 1
dg = (B/P)**(1/8.5) - 1 if P > 0 else float('nan')
print(f'\ncycle base 2015-2024 all-equity {B:.1f}; before acq {Bo:.1f}; equity-only {Be:.1f}; depreciation basis {Bd:.1f}')
print(f'prior cycle 2008-2014 all-equity {P:.1f}; before acq {Po:.1f}')
print(f'literal window 2021-2025 all-equity {Bw:.1f}; equity-only {Bwe:.1f}')
print(f'growth between cycle averages (midpoints 2011 to 2019.5, 8.5 years): default pair {dg*100:.1f}%/yr; organic pair {og*100:.1f}%/yr; sales {sg*100:.1f}%/yr')
acq_share = sum(ACQ[y]-DIV.get(y,0) for y in cyc)/sum(oc(y,acq=False,alleq=False) for y in cyc)
print(f'net purchases / owner cash before purchases, cycle 2015-2024: {acq_share*100:.0f}% (serial-acquirer test at one half)')
hi = max(oc(y,acq=False)/SALES[y] for y in Y)
print(f'default-pair growth carried 10y needs owner cash/sales {B*(1+dg)**10/ (sum(SALES[y] for y in cyc)/len(cyc))*100:.0f}% vs highest filed {hi*100:.1f}% -> cap (f) cuts to sales growth {sg*100:.1f}%')
def row(name, cf, g, nd=None):
    nd = netdebt if nd is None else nd
    v = value(cf, g, r); v10 = value(cf, g, floor)
    print(f'  {name:46s} cf {cf:7.1f} g {g*100:6.1f}%  value@5.43% {v:8.0f}  per share {(v-nd)/shares:7.2f}   value@10% {v10:7.0f} per share {(v10-nd)/shares:6.2f}')
    return v, v10
print(f'\nprice {price}, shares {shares}M, mcap {mcap:.0f}, net debt 2026-06-30 {netdebt} (debt 1,706 less cash 1,164; operating leases left out), EV {ev:.0f}')
print('CENTRAL (cycle base, all-equity, acquisitions deducted, cap applied):')
top = row('top: no growth', B, 0.0); bot = row('bottom: decline at sales growth between cycles', B, sg)
fair = ((top[1]+bot[1])/2 - netdebt)/shares
print(f'  RANGE per share {(bot[0]-netdebt)/shares:.2f} to {(top[0]-netdebt)/shares:.2f}; width {top[0]/bot[0]:.2f} to 1 (whole-business)')
print(f'  FAIR PRICE all-equity (each end at 10%, averaged, less net debt): {fair:.2f}')
print('EQUITY-ONLY beside (owner cash after interest, against market value, no net debt deducted):')
te = row('top: no growth, equity-only', Be, 0.0, 0); be = row('bottom: decline, equity-only', Be, sg, 0)
print(f'  equity-only range per share {be[0]/shares:.2f} to {te[0]/shares:.2f}; fair {((te[1]+be[1])/2)/shares:.2f}')
print('BESIDE:')
row('organic pair top: before acquisitions, no growth', Bo, 0.0); row('organic pair bottom: organic decline', Bo, og)
row('literal window 2021-2025, no growth', Bw, 0.0)
row('depreciation basis, cycle base, no growth', Bd, 0.0)
print('FLOOR TEST: expected return at the price on each case (no growth = cf/EV):')
for nm, cf in [('cycle base', B), ('cycle base before acquisitions', Bo), ('literal window', Bw), ('2024-2025 average (not a case of the range; shown for the evidence for)', (oc(2024)+oc(2025))/2)]:
    print(f'  {nm:70s} {cf:7.1f} / EV {ev:.0f} = {100*cf/ev:.1f}%')
