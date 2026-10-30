# Owner cash arithmetic for the TURV run (COMPUTATION, NOT A CLEARANCE). Figures in $ thousands, from the filed
# cash-flow statements: FY2016 10-K (0001302946-17-000019) for 2015-2016, FY2018 10-K (0001493152-19-005266) for 2017-2018.
yrs = {
 # year: (net cash from operations, capital spending, stock pay non-cash, cash interest paid)
 2015: (-3161, 96+352+5430, 204, 1177),
 2016: (-2729, 192+691+2597, 477, 1460),
 2017: (-2898, 506, 1287, 621),
 2018: (-1060, 140, 1668+1355, 203),
}
r_gov, r_floor = 0.0537, 0.10
shares = 87145.235          # thousands, 10-Q cover 2019-11-22
net_debt = 9329 + 868 - 401  # notes current + non-current less cash, 2019-09-30 10-Q
pref_payable = 4988
oc = {}
for y,(ocf,capex,sbc,intr) in yrs.items():
    oc[y] = ocf - capex - sbc
    print(y, 'owner cash after interest', oc[y], ' before interest', oc[y]+intr)
avg_eq = sum(oc.values())/len(oc)
avg_all = sum(v+yrs[y][3] for y,v in oc.items())/len(oc)
print('avg equity-only', round(avg_eq,1), ' avg all-equity', round(avg_all,1))
ocf5 = [-4372,-3161,-2729,-2898,-1060]
print('OCF 2014-2018 avg', sum(ocf5)/5)
for lab,r in (('gov',r_gov),('floor',r_floor)):
    all_eq = (avg_all/r - net_debt)/shares
    eq = (avg_eq/r)/shares
    print(lab, 'all-equity per share', round(all_eq,2), ' equity-only per share', round(eq,2))
print('net debt', net_debt, 'preferred distributions payable beside', pref_payable)
