# CLF owner cash and Q7 COMPUTATION (not a clearance). All $M. Sources: 10-K FY2022 (0000764065-23-000032), FY2025 (0000764065-26-000025), 10-Q Q2 2026 (0000764065-26-000100).
yrs=[2020,2021,2022,2023,2024,2025]
OCF={2020:-258,2021:2785,2022:2423,2023:2267,2024:105,2025:-462}
SBC={2020:17,2021:18,2022:28,2023:41,2024:50,2025:57}
CAPEX={2020:525,2021:705,2022:943,2023:646,2024:695,2025:561}
FLP={2020:15,2021:94,2022:96,2023:92,2024:49,2025:67}
NCI={2020:61,2021:62,2022:74,2023:67,2024:48,2025:76}
INTP={2020:170,2021:299,2022:249,2023:256,2024:255,2025:459}
ACQ={2020:869+658,2021:761-54,2022:31,2023:-35,2024:2512,2025:-53}  # net of businesses sold
REV={2020:5354,2021:20444,2022:22989,2023:21996,2024:19185,2025:18610}
TAX=0.25
oc={y:OCF[y]-SBC[y]-CAPEX[y]-FLP[y]-NCI[y] for y in yrs}
ae={y:oc[y]+INTP[y]*(1-TAX) for y in yrs}
for y in yrs: print(y,'owner cash eq-only before purchases',oc[y],' all-equity',round(ae[y]),' acq',ACQ[y],' OC/rev %.1f%%'%(100*oc[y]/REV[y]))
avg=lambda d,ys: sum(d[y] for y in ys)/len(ys)
W=[2021,2022,2023,2024,2025]; C=[2020,2021,2022,2023,2024,2025]
print('5yr window 2021-25: eq-only %.0f all-equity %.0f; with acquisitions deducted eq %.0f ae %.0f'%(avg(oc,W),avg(ae,W),avg({y:oc[y]-ACQ[y] for y in W},W),avg({y:ae[y]-ACQ[y] for y in W},W)))
print('cycle 2020-25: eq-only %.0f all-equity %.0f; with acq deducted eq %.0f ae %.0f'%(avg(oc,C),avg(ae,C),avg({y:oc[y]-ACQ[y] for y in C},C),avg({y:ae[y]-ACQ[y] for y in C},C)))
print('serial test window: net purchases %d vs half of owner cash before purchases %.0f'%(sum(ACQ[y] for y in W),sum(oc[y] for y in W)/2))
print('halves: first 2021-22 %.0f, second 2024-25 %.0f'%(avg(oc,[2021,2022]),avg(oc,[2024,2025])))
# depreciation variant (OCF - SBC - D&A)
DA={2020:308,2021:897,2022:1034,2023:973,2024:951,2025:1235}
print('D&A variant window eq-only %.0f'%avg({y:OCF[y]-SBC[y]-DA[y]-FLP[y]-NCI[y] for y in W},W))
# net debt at 2026-06-30
debt=7703; fl=402; cash=70
nd=debt+fl-cash; sh=570.540; price=12.86
print('net debt',nd,' market cap %.0f  EV %.0f'%(sh*price, sh*price+nd))
r=0.056
for name,ocv,kind in [('cycle base all-equity',avg(ae,C),'ae'),('literal window all-equity',avg(ae,W),'ae'),('cycle base eq-only',avg(oc,C),'eq'),('literal window eq-only',avg(oc,W),'eq')]:
    v=ocv/r; v10=ocv/0.10
    if kind=='ae': ps=(v-nd)/sh; ps10=(v10-nd)/sh; yld=ocv/(sh*price+nd)
    else: ps=v/sh; ps10=v10/sh; yld=ocv/(sh*price)
    print('%-28s OC %.0f  value@5.6%% $%.2f/sh  value@10%% $%.2f/sh  yield at price %.1f%%'%(name,ocv,ps,ps10,100*yld))
print('owner cash before interest needed for 10%% on EV at the price: %.0f'%(0.10*(sh*price+nd)))
