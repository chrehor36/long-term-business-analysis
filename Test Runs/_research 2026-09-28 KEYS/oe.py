# Owner earnings [E2-23]: OCF - SBC - (c), (c) at two ends: capex (gross PP&E investment) and depreciation [E3-44]; dep+amort end shown for the screen only.
# $M, latest filed vintage (companyfacts cross-checked to the FY2025 face at Step 0). FY2013-FY2014 are carve-out years (Agilent paid the taxes): shown, flagged, excluded from windows.
CAP = 362.15*170244745/1e6
OCF ={2013:566,2014:563,2015:376,2016:420,2017:328,2018:555,2019:998,2020:1016,2021:1322,2022:1144,2023:1408,2024:1052,2025:1409}
SBC ={2013:41,2014:43,2015:55,2016:49,2017:56,2018:59,2019:82,2020:92,2021:103,2022:125,2023:135,2024:137,2025:162}
CPX ={2013:69,2014:70,2015:92,2016:91,2017:72,2018:132,2019:120,2020:117,2021:174,2022:185,2023:197,2024:154,2025:128}
DEP ={2013:65,2014:74,2015:81,2016:85,2017:92,2018:103,2019:96,2020:104,2021:117,2022:117,2023:120,2024:126,2025:131}
AM  ={2013:9,2014:8,2015:15,2016:43,2017:131,2018:204,2019:210,2020:220,2021:174,2022:103,2023:92,2024:144,2025:145}
# TTM to 2026-07-31 = FY2025 + 9M FY2026 - 9M FY2025 (10-Qs 0001601046-26-000036 and 0001601046-25-000091)
TTM = dict(ocf=1409+1379-1184, sbc=162+181-129, cpx=128+97-90, dep=131+116-97, am=145+202-104)
def oe(y, end):
    c = {'capex':CPX,'dep':DEP}[end][y] if end!='depam' else DEP[y]+AM[y]
    return OCF[y]-SBC[y]-c
print('FY    OCF  SBC  capex  dep  amort | OE capex  OE dep  OE dep+am')
for y in sorted(OCF):
    print(y, f"{OCF[y]:5} {SBC[y]:4} {CPX[y]:5} {DEP[y]:4} {AM[y]:5} | {oe(y,'capex'):7} {oe(y,'dep'):7} {oe(y,'depam'):8}", '(carve-out)' if y<2015 else '')
t=TTM; print('TTM ', t, '| capex', t['ocf']-t['sbc']-t['cpx'], 'dep', t['ocf']-t['sbc']-t['dep'], 'dep+am', t['ocf']-t['sbc']-t['dep']-t['am'])
print(f'\nCAP {CAP:,.1f}  trailing windows ending FY2025 (standalone years FY2015-FY2025 only)')
yrs=list(range(2015,2026))
for n in range(1,12):
    w=yrs[-n:]
    m={e: sum(oe(y,e) for y in w)/n for e in ('capex','dep','depam')}
    print(f"{n:2}y {w[0]}-{w[-1]}: capex {m['capex']:7.1f} ({100*m['capex']/CAP:.2f}%)  dep {m['dep']:7.1f} ({100*m['dep']/CAP:.2f}%)  dep+am {m['depam']:7.1f} ({100*m['depam']/CAP:.2f}%)")
print('\nrolling five-year windows')
for s in range(2015,2022):
    w=list(range(s,s+5)); m={e: sum(oe(y,e) for y in w)/5 for e in ('capex','dep')}
    print(f"{w[0]}-{w[-1]}: capex {m['capex']:7.1f} ({100*m['capex']/CAP:.2f}%)  dep {m['dep']:7.1f} ({100*m['dep']/CAP:.2f}%)")
tt={'capex':t['ocf']-t['sbc']-t['cpx'],'dep':t['ocf']-t['sbc']-t['dep']}
print(f"\nTTM: capex {tt['capex']} ({100*tt['capex']/CAP:.2f}%)  dep {tt['dep']} ({100*tt['dep']/CAP:.2f}%)")
# screen reproduction: oe_bottom_m 879, oe_top_m 978
for n in (3,5):
    w=yrs[-n:]; print(n,'y', {e: round(sum(oe(y,e) for y in w)/n,1) for e in ('capex','dep','depam')})
# [E4-41] luck: FY2023 swap-termination proceeds $107M; FY2024 tax receivable -$202M and FY2025 +$105M
print('5y capex end ex FY2023 swap proceeds', (sum(oe(y,'capex') for y in yrs[-5:])-107)/5)
