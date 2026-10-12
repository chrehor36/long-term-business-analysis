# COMPUTATION, NOT A CLEARANCE. Reporting figures for the BLTH run (the file closed at Q1).
# Inputs transcribed from the filed statements (accessions in the run file).
ocf  = {2021:-392445, 2022:-910709, 2023:-2278206, 2024:-750311, 2025:-499416}
sbc  = {2021:6296, 2022:62080, 2023:275465, 2024:67586, 2025:838358}
capx = {2021:100000, 2022:0, 2023:106000, 2024:0, 2025:0}   # mineral-claim purchases/staking (investing outflows)
cint = {2021:0, 2022:60976, 2023:0, 2024:0, 2025:0}         # cash interest paid where tagged
iexp = {2021:760663, 2022:595124, 2023:203287, 2024:446278, 2025:719979}
yrs = sorted(ocf)
oc_eq_only = {y: ocf[y]-sbc[y]-capx[y] - (iexp[y]-cint[y]) for y in yrs}   # after all interest (accrued, settled in principal/shares)
oc_all     = {y: ocf[y]-sbc[y]-capx[y] + cint[y] for y in yrs}            # before interest
oc_lit     = {y: ocf[y]-sbc[y]-capx[y] for y in yrs}
for y in yrs: print(y, 'owner cash (OCF-SBC-capex)', oc_lit[y], 'before interest', oc_all[y], 'after all interest', oc_eq_only[y])
avg = lambda d,ys: sum(d[y] for y in ys)/len(ys)
A = avg(oc_all, yrs); E = avg(oc_eq_only, yrs); L = avg(oc_lit, yrs)
A4 = avg(oc_all, yrs[1:])
print('5yr avg literal', round(L), 'all-equity', round(A), 'equity-only', round(E), '| 2022-25 all-equity', round(A4))
sov = 0.056
net_debt = 11187330 + 1483617 - 5704   # 8-K 2026-08-25 principal after the 30 Sep step-up + accrued interest 30 Jun 2026 - cash 30 Jun 2026
net_debt_s1 = 16750554 + (946531+790991) - 5704  # S-1/A: convertible notes incl. interest at 11 Aug 2026, plus promissory notes 30 Jun 2026
sh_now = 3789585; sh_after = 3789585 + 612476
price = 4.00
print('net debt central', net_debt, 'alt (S-1/A)', net_debt_s1)
for sh in (sh_after, sh_now):
    print('--- shares', sh, 'market cap', sh*price)
    v_all = A/sov - net_debt; v_eq = E/sov
    f_all = A/0.10 - net_debt; f_eq = E/0.10
    print(' value range (no-growth case alone) all-equity per share', round(v_all/sh,2), ' equity-only', round(v_eq/sh,2))
    print(' fair price all-equity', round(f_all/sh,2), ' equity-only', round(f_eq/sh,2))
    print(' 2022-25 base all-equity value', round((A4/sov-net_debt)/sh,2), 'fair', round((A4/0.10-net_debt)/sh,2))
    print(' alt net debt (S-1/A) all-equity value', round((A/sov-net_debt_s1)/sh,2), 'fair', round((A/0.10-net_debt_s1)/sh,2))
