# All figures USD millions, from the filed cash-flow statements (accessions in owner_cash.md)
Y=[2021,2022,2023,2024,2025]
OCF={2021:275.679,2022:373.867,2023:480.666,2024:541.839,2025:601.771}
SBC={2021:25.323,2022:22.397,2023:22.468,2024:14.880,2025:21.876}
CAPEX={2021:203.308,2022:391.423,2023:337.463,2024:306.055,2025:382.388}
UNPAID={2020:7.869,2021:13.936,2022:24.221,2023:35.867,2024:56.123,2025:65.892}
FLADD={2021:22.959,2022:1.335,2023:32.101,2024:17.871,2025:31.392}
NCI={2021:1.070,2022:2.000,2023:2.500,2024:5.600,2025:6.967}
DA={2021:258.053,2022:351.178,2023:382.783,2024:365.334,2025:381.927}
AMORT={2021:46.5,2022:40.0,2023:32.6,2024:22.3,2025:20.3}
FLROU={2021:0,2022:0,2023:5.938,2024:11.100,2025:15.342}
ACQ={2021:1620.320,2022:19.017,2023:19.687,2024:9.536,2025:42.378}
WC={2021:-29.694-14.920+2.731-83.383,2022:-0.209-6.300-13.143-57.131,2023:-28.862+15.531-20.305+40.955,2024:-26.217-28.065+27.325+33.832,2025:30.986-11.491-61.071+139.272}
oc={};od={}
print('| FY | OCF | SBC | cash capex | change in unpaid equipment | finance-lease equipment | NCI distributions | OWNER CASH (capex basis) | depreciation basis | working-capital change inside OCF | cash acquisitions |')
print('|---|---|---|---|---|---|---|---|---|---|---|')
for y in Y:
    du=UNPAID[y]-UNPAID[y-1]
    oc[y]=OCF[y]-SBC[y]-CAPEX[y]-du-FLADD[y]-NCI[y]
    dep=DA[y]-AMORT[y]+FLROU[y]
    od[y]=OCF[y]-SBC[y]-dep-NCI[y]
    print(f'| {y} | {OCF[y]:.1f} | {SBC[y]:.1f} | {CAPEX[y]:.1f} | {du:.1f} | {FLADD[y]:.1f} | {NCI[y]:.1f} | **{oc[y]:.1f}** | {od[y]:.1f} | {WC[y]:+.1f} | {ACQ[y]:.1f} |')
a5=sum(oc.values())/5; d5=sum(od.values())/5; a3=sum(oc[y] for y in (2023,2024,2025))/3; d3=sum(od[y] for y in (2023,2024,2025))/3
print(f'\nfive-year mean, capex basis {a5:.1f}; depreciation basis {d5:.1f}; three-year (2023-25) capex basis {a3:.1f}; depreciation basis {d3:.1f}')
print(f'capital put in 2021-25 (capex+unpaid change+finance-lease equipment) {sum(CAPEX[y]+UNPAID[y]-UNPAID[y-1]+FLADD[y] for y in Y):.1f}; depreciation ex-amortization incl. finance-lease ROU {sum(DA[y]-AMORT[y]+FLROU[y] for y in Y):.1f}; cash acquisitions {sum(ACQ.values()):.1f}; owner cash sum {sum(oc.values()):.1f}')
# H1 2026
h=239.024-12.089-287.456-(81.667-65.892)-3.286-2.349
print(f'H1 2026 owner cash, capex basis: {h:.1f}; cash acquisitions H1 2026 127.4')
r=0.0563
def pv(base,g,yrs=10):
    v=0;cf=base
    for t in range(1,yrs+1):
        cf=cf*(1+g); v+=cf/(1+r)**t
    tv=cf/r/(1+r)**yrs
    return v+tv
sh=136.344+12.406
TRA=265.7-26.846; DIAB=235.0
print('\nshares, common plus preferred as converted', sh)
for lab,base in (('5yr capex',a5),('5yr dep',d5),('3yr capex',a3),('3yr dep',d3)):
    for g in (0.0,0.017):
        ev=pv(base,g); eq=ev-TRA+DIAB
        print(f'{lab:10s} g={g:.3f}  PV {ev:7.1f}  equity {eq:7.1f}  per share {eq/sh:6.2f}')
# fair price: price at which owner cash yield >= 10% pre-tax -> owner cash is after tax; pre-tax equivalent
