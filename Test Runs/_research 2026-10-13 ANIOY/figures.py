# ANIOY / Acerinox run 2026-10-13: figures transcribed by hand from the filed statements (EUR thousands -> millions).
# Sources (consolidated statements, IFRS-EU, in-house English translations; Spanish original prevails):
#  FY2025+FY2024: 2025 Acerinox Group Annual Accounts (authorised 2026-02-25)
#  FY2024+FY2023: 2024 Acerinox Group Annual Accounts
#  FY2023+FY2022: 2023 Consolidated Annual Accounts and Integrated Annual Report
#  FY2022+FY2021: Management Report Business Year 2022 and Explanatory Notes to the Annual Financial Report (IFRS statements)
#  FY2020: 2021 Business Year Results Report (company format, not the IFRS statement; flagged)
#  FY2019+FY2018: CNMV AUDITA 2019/18351_en (PwC audit report and consolidated annual accounts, signed 2020-02-27)
#  FY2017+FY2016: CNMV AUDITA 2017/17363_en
#  H1 2026: Condensed consolidated interim financial statements, six months to 2026-06-30 (PwC limited review)
# Arithmetic only. No judgment here.

Y = list(range(2016, 2026))
rev   = dict(zip(Y,[3968.1,4626.9,5010.8,4753.9,4668,6705.7,8688.5,6608.0,5413.1,5780.5]))
ebit  = dict(zip(Y,[157.4,318.0,312.1,22.6,163,809.7,875.8,374.2,348.1,153.2]))   # operating income as filed (2020: company EBIT)
impair= dict(zip(Y,[0,0,0,165.5,0,0,203.9,156.2,-3.1,0]))                         # impairment of assets in operating income
gain  = dict(zip(Y,[0,0,0,0,0,0,0,0,146.1,0]))                                    # gain on sale of shares (Bahru) 2024
da    = dict(zip(Y,[169.8,169.7,166.2,175.3,179,179.1,192.9,171.1,159.9,195.5]))
cfo   = dict(zip(Y,[268.8,365.9,326.4,358.7,421,387.8,544.1,481.5,293.7,455.5]))  # after interest and tax paid; 2020 company 'operating cash flow'
capex = dict(zip(Y,[163.0,185.6,146.1,145.7,99,102.1,136.7,174.9,204.8,309.8]))  # PPE + intangibles; 2020 'payments due to investment' (net)
dispo = dict(zip(Y,[5.7,1.0,1.4,15.2,0,12.7,2.0,1.0,0.6,0.2]))                   # proceeds from PPE disposals (2020 inside the net figure)
intpd = dict(zip(Y,[40.7,36.7,32.1,33.4,36,43.0,50.1,82.5,101.1,88.2]))         # interest paid (2020: company 'finance costs')
intrc = dict(zip(Y,[6.0,8.5,16.6,18.8,0,2.7,24.9,79.0,90.7,41.2]))              # interest received (2020 net in the 36)
taxpd = dict(zip(Y,[55.8,82.0,81.1,115.7,99,136.9,238.2,233.3,131.2,161.3]))
acq   = dict(zip(Y,[0,0,10.5,0,313+85,0,0,0,709.3,0]))                           # 2018 minority buy-out; 2020 VDM cash + debt assumed; 2024 Haynes net of cash
divest= dict(zip(Y,[0,0,0,0,0,0,0,0,16.8,68.3]))                                  # other receipts for divestments (Bahru)
# balance sheet at 31 Dec
equity= dict(zip(Y,[2168.7,1970.3,2119.3,1929.0,1615.0,2214.9,2547.7,2463.1,2575.1,2097.6]))
borrow= dict(zip(Y,[124.1+1.7+812.7+280.0, 74.4+51.6+862.3+241.5, 74.5+1.6+951.8+374.3, 74.6+1.6+977.2+318.2,
                    1410+280, 74.8+1.6+1293.5+483.3, 74.9+1.6+1319.2+592.9, 76.6+1291.2+767.1, 1464.3+918.7, 1321.5+837.0]))
cash  = dict(zip(Y,[598.5,620.5,850.1,876.9,917,1274.9,1548.0,1793.7,1262.8,969.9]))
inv   = dict(zip(Y,[887.4,990.5,1018.7,1016.3,1182,1776.6,2155.5,1860.5,2061.6,1678.6]))
recv  = dict(zip(Y,[572.2,601.6,578.1,523.1,532,839.6,637.8,626.3,619.1,546.7]))
pay   = dict(zip(Y,[804.0,941.5,860.4,857.8,879,1446.7,1181.4,951.1,817.2,775.2]))
ppe   = dict(zip(Y,[2068.2,1868.4,1890.9,1793.7,None,1820.3,1649.6,1471.9,1852.6,1882.3]))
gw    = dict(zip(Y,[69.1+2.8,69.1+2.5,69.1+2.2,1.2+3.2,None,51.1+46.6,51.1+43.4,51.1+41.3,181.5+136.4,164.5+118.0]))
assets= dict(zip(Y,[4455.0,4404.0,4607.6,4396.8,4733,5984.2,6318.1,6098.8,6469.3,5620.5]))
# subsidiary contributions to consolidated profit (Note 'reserves and results by company'); None where not read
nas   = dict(zip(Y,[63.4,165.0,199.7,268.4,None,None,697.5,579.4,345.7,306.9]))
europa= dict(zip(Y,[20.4,55.0,27.2,-57.7,None,None,-46.8,-189.9,-251.2,-239.4]))
bahru = dict(zip(Y,[-39.8,-40.5,-51.2,-164.8,None,None,-218.0,-205.2,-23.2,None]))
columbus=dict(zip(Y,[18.4,22.8,7.7,-69.2,None,None,None,None,-32.8,-45.2]))
okmp_roce = dict(zip(Y,[2.6,11.3,7.0,0.8,-1.4,17.6,22.6,-2.1,-1.2,-3.2]))       # Outokumpu own annual reports (2020 AR; 2025 AR, 2021 restated)

def oc_equity(y):  # owner cash after interest and tax: CFO - capex + disposal proceeds
    return cfo[y] - capex[y] + dispo[y]
def oc_allequity(y):  # before net interest (added back gross), after the company's tax as paid
    return oc_equity(y) + (intpd[y] - intrc[y])
def netdebt(y): return borrow[y] - cash[y]

if __name__ == "__main__":
    print("year  rev   EBIT  EBITx  D&A  CFO  capex  OCeq  OCall  netint acq-div  ND    CE    ROCE%  OKMP%  NAS   Europa")
    for y in Y:
        exi = ebit[y] + impair[y] - gain[y]
        ce = equity[y] + netdebt(y)
        print(f"{y} {rev[y]:6.0f} {ebit[y]:6.1f} {exi:6.1f} {da[y]:5.1f} {cfo[y]:5.1f} {capex[y]:5.1f} {oc_equity(y):6.1f} {oc_allequity(y):6.1f} {intpd[y]-intrc[y]:5.1f} {acq[y]-divest[y]:6.1f} {netdebt(y):6.1f} {ce:6.0f} {100*ebit[y]/ce:5.1f} {okmp_roce[y]:5.1f} {nas[y] if nas[y] is not None else '':>6} {europa[y] if europa[y] is not None else '':>6}")
    import statistics as st
    for a,b,lab in [(2016,2025,'10y'),(2021,2025,'5y'),(2016,2020,'first5')]:
        ys=[y for y in Y if a<=y<=b]
        print(lab, "avg OCeq", round(sum(oc_equity(y) for y in ys)/len(ys),1), "avg OCall", round(sum(oc_allequity(y) for y in ys)/len(ys),1),
              "net acq", round(sum(acq[y]-divest[y] for y in ys),1), "avg EBIT", round(sum(ebit[y] for y in ys)/len(ys),1),
              "avg EBIT ex", round(sum(ebit[y]+impair[y]-gain[y] for y in ys)/len(ys),1),
              "avg ROCE", round(sum(100*ebit[y]/(equity[y]+netdebt(y)) for y in ys)/len(ys),1), "OKMP avg", round(sum(okmp_roce[y] for y in ys)/len(ys),1),
              "avg rev", round(sum(rev[y] for y in ys)/len(ys),0))
