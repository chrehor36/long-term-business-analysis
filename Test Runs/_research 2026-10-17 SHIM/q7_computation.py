# COMPUTATION, NOT A CLEARANCE: Q7 range and fair price for SHIM (run of 2026-10-17). USD millions.
ocf   = {2021:-53.975, 2022:-3.084, 2023:-88.100, 2024:-21.259, 2025:-65.114}
sbc   = {2021:1.185, 2022:2.295, 2023:2.1, 2024:6.130, 2025:5.237}
capex = {2021:2.935, 2022:10.443, 2023:7.042, 2024:10.477, 2025:6.371}
da    = {2021:14.929, 2022:15.979, 2023:17.3, 2024:15.132, 2025:12.998}
# cash interest paid; 2023 not found, taken at the upper bound of FY2023 other expense, net (2.721)
intp  = {2021:0.072, 2022:0.164, 2023:2.721, 2024:2.0, 2025:2.0}
yrs = sorted(ocf)
oc_capex = {y: ocf[y]-sbc[y]-capex[y] for y in yrs}
oc_da    = {y: ocf[y]-sbc[y]-da[y] for y in yrs}
avg = lambda d: sum(d.values())/len(d)
eq_capex, eq_da = avg(oc_capex), avg(oc_da)
add = avg(intp)
ae_capex, ae_da = eq_capex+add, eq_da+add
debt = 61.318+3.527+10.149     # face, 10-Q debt table 2026-07-03
cash = 16.875                  # unrestricted, 2026-07-03
nd = debt-cash
sh = 41.335823
sov = 0.0543
def nogrowth(x, r):  # ten years flat then zero growth = perpetuity at zero growth
    return x/r
for name,x in (('capex basis',ae_capex),('D&A basis',ae_da)):
    v = nogrowth(x,sov)-nd
    f = nogrowth(x,0.10)-nd
    print(f'{name}: owner cash before interest {x:.1f}; value at sovereign {v:.0f} -> {v/sh:.2f}/sh; at 10% {f:.0f} -> {f/sh:.2f}/sh')
for name,x in (('capex basis',eq_capex),('D&A basis',eq_da)):
    print(f'equity-only {name}: {x:.1f}; at sovereign {x/sov/sh:.2f}/sh; at 10% {x/0.10/sh:.2f}/sh')
print('series capex', {y:round(v,1) for y,v in oc_capex.items()}, 'avg', round(eq_capex,1))
print('series D&A  ', {y:round(v,1) for y,v in oc_da.items()}, 'avg', round(eq_da,1))
print('halves', round((oc_capex[2021]+oc_capex[2022])/2,1), round((oc_capex[2024]+oc_capex[2025])/2,1))
print('net debt', round(nd,1), 'interest add-back avg', round(add,2))
