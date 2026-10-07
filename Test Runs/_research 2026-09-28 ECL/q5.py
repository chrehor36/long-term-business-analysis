import sys; sys.stdout.reconfigure(encoding='utf-8')
sh=280.328603; cap=78349.0; price=279.49
cases={'5y capex':1462.3,'5y dep':1667.5,'8y capex':1356.7,'8y dep':1522.5,'TTM capex':1738.7,'TTM dep':2212.0}
# organic sales change (filer's acquisition-adjusted / organic fixed-currency line), FY2018-FY2025
org={2018:6,2019:4,2020:-7,2021:5,2022:13,2023:9,2024:4,2025:3}
g_org=sum(org.values())/len(org); print('mean organic sales change FY2018-25: %.2f%%'%g_org)
oe18={'capex':1140.2,'dep':1383.0}; oe25={'capex':1767.7,'dep':2143.4}
for k in oe18: print('OE CAGR FY2018-25 %s end: %.2f%%'%(k,100*((oe25[k]/oe18[k])**(1/7)-1)))
acq={2018:229.8,2019:391.4,2020:487.0,2021:3923.7,2022:7.2,2023:180.4,2024:312.9,2025:1621.3}
print('acquisition cash FY2018-25: %.1f'%sum(acq.values()))
for g in (0.0,0.046,0.05,0.065):
    for k,v in cases.items():
        for r in (0.10,0.0549):
            if g>=r: continue
            val=v*(1+g)/(r-g)/sh
            print(f'g={g:.3f} {k:9s} r={r:.4f}: ${val:.0f}')
print('\nexpectancy = yield + g_org:')
for k,v in cases.items(): print(f'{k}: yield {100*v/cap:.2f}% + {g_org:.1f}% = {100*v/cap+g_org:.2f}%')
