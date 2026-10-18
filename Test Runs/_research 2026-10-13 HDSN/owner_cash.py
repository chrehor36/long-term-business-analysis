# Owner cash by year, USD millions, from the XBRL cash-flow lines (transcription; checked against the filed
# statements for FY2025, FY2024, FY2018 in the run file). COMPUTATION only.
OCF  = {2016:9.35,2017:18.37,2018:36.33,2019:33.82,2020:11.69,2021:-1.23,2022:62.81,2023:58.55,2024:91.81,2025:-3.16}
SBC  = {2016:0.71,2017:1.50,2018:1.40,2019:1.83,2020:0.66,2021:0.51,2022:0.92,2023:2.31,2024:0.84,2025:1.10}
CAPEX= {2016:1.73,2017:1.02,2018:1.09,2019:1.01,2020:1.47,2021:1.92,2022:3.66,2023:3.58,2024:5.30,2025:5.05}
DA   = {2016:2.23,2017:2.27,2018:4.16,2019:4.18,2020:3.23,2021:3.39,2022:3.18,2023:2.99,2024:3.00,2025:2.69}  # depreciation only (DepreciationDepletionAndAmortization tag carries PP&E depreciation; intangible amortization separate)
ACQ  = {2016:0,2017:208.97,2018:0,2019:0,2020:0,2021:0,2022:0,2023:0,2024:20.67,2025:2.24}
INTPAID={2016:0.96,2017:2.03,2018:13.60,2019:15.16,2020:11.38,2021:10.16,2022:11.70,2023:4.47,2024:0.69,2025:0.52}
NETINTINC={2024:0.48,2025:2.53}   # net interest income, FY2024-25 (InterestIncomeExpenseNonoperatingNet)
TAX={y:(0.35 if y<=2017 else (0.0 if y in (2018,2019,2020) else 0.21)) for y in OCF}  # 2018-20 valuation allowance: no shield
SALES={2015:79.72,2016:105.48,2017:140.38,2018:166.53,2019:162.06,2020:147.60,2021:192.75,2022:325.23,2023:289.02,2024:237.12,2025:246.6}
rows={}
for y in sorted(OCF):
    eq = OCF[y]-SBC[y]-CAPEX[y]            # equity-only, all capital spending, before acquisitions
    eqA= eq-ACQ[y]                          # acquisitions deducted
    adj= INTPAID[y]*(1-TAX[y]) if y<=2023 else -NETINTINC.get(y,0)*(1-TAX[y])
    allq=eqA+adj                            # all-equity basis (before interest, after tax), acquisitions deducted
    allq_noacq=eq+adj
    rows[y]=(eq,eqA,allq,allq_noacq)
    print(y, 'eq %.2f  eq-acq %.2f  allEq-acq %.2f  allEq(noacq) %.2f  ocf/sales %.1f%%' % (eq,eqA,allq,allq_noacq, 100*(OCF[y]-SBC[y]-CAPEX[y])/SALES[y]))
def avg(ys,k): return sum(rows[y][k] for y in ys)/len(ys)
W=range(2021,2026)
print('literal window FY2021-25: eq %.2f eq-acq %.2f allEq-acq %.2f allEq-noacq %.2f'%tuple(avg(W,k) for k in range(4)))
print('ten years FY2016-25: eq %.2f eq-acq %.2f allEq-acq %.2f allEq-noacq %.2f'%tuple(avg(range(2016,2026),k) for k in range(4)))
for a,b in ((2018,2024),(2019,2024),(2020,2025),(2021,2024),(2022,2025),(2016,2020),(2017,2021)):
    ys=range(a,b+1); print('cycle %d-%d: allEq-acq %.2f allEq-noacq %.2f eq-acq %.2f'%(a,b,avg(ys,2),avg(ys,3),avg(ys,1)))
