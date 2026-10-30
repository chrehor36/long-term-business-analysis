# COMPUTATION, NOT A CLEARANCE. BETA run 2026-10-23. Figures in USD millions from the FY2025 10-K
# (0001628280-26-015838) cash-flow statement and the Q2 2026 10-Q (0001628280-26-055982) balance sheet.
ocf  = {2023:-158.015, 2024:-222.661, 2025:-267.798}
sbc  = {2023:8.961, 2024:12.105, 2025:34.761}
warr = {2023:0.0, 2024:0.0, 2025:6.073}          # GE warrant expense, stock pay added back in OCF
capex= {2023:153.240, 2024:73.509, 2025:45.447}
da   = {2023:8.618, 2024:16.464, 2025:22.026}
int_paid = {2023:0.112, 2024:9.185, 2025:10.873}  # cash paid for interest (supplemental)
int_inc  = {2023:12.389, 2024:8.516, 2025:20.147} # interest income (income statement), proxy for cash received
r=0.0529; floor=0.10
shares=233.941060   # 225,439,576 A + 8,501,484 B (10-Q cover, Aug 6 2026); B converts 1:1
price=18.37
cash=1479.470; notes=8.547+175.405   # June 30 2026 balance sheet; notes include sale-leaseback financing
net_debt = notes - cash
yrs=[2023,2024,2025]
def mean(d): return sum(d[y] for y in yrs)/len(yrs)
eq_all  ={y: ocf[y]-sbc[y]-warr[y]-capex[y] for y in yrs}          # equity-only, all spending
eq_da   ={y: ocf[y]-sbc[y]-warr[y]-da[y] for y in yrs}             # equity-only, maintenance guessed at D&A
ae_all  ={y: eq_all[y]+int_paid[y]-int_inc[y] for y in yrs}        # all-equity (before net interest)
ae_da   ={y: eq_da[y]+int_paid[y]-int_inc[y] for y in yrs}
print('market cap', round(price*shares,1), 'net debt', round(net_debt,1))
for name,d,basis in [('all-equity, maintenance (D&A) case',ae_da,'ae'),('all-equity, all spending',ae_all,'ae'),
                     ('equity-only, maintenance (D&A) case',eq_da,'eq'),('equity-only, all spending',eq_all,'eq')]:
    m=mean(d)
    v_sov=m/r; v_fl=m/floor
    if basis=='ae': ps_sov=(v_sov-net_debt)/shares; ps_fl=(v_fl-net_debt)/shares
    else: ps_sov=v_sov/shares; ps_fl=v_fl/shares
    print(f"{name}: by year {[round(d[y],1) for y in yrs]} mean {m:.1f}; no-growth value at sovereign {ps_sov:.2f}/sh; at ten percent (fair) {ps_fl:.2f}/sh")
