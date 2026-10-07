# Owner earnings arithmetic, EUR millions, every input from the filed cash-flow statements (sources in the run file).
import json
Y = [2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
OCF   = dict(zip(Y,[101,179,344,573,259,361,46,680,2301,2933]))
SBC   = dict(zip(Y,[53,65,88,122,176,223,381,321,267,247]))
CAPEX = dict(zip(Y,[27,36,125,135,78,85,25,6,17,61]))
LEASE = dict(zip(Y,[0,0,0,17,24,35,43,66,69,73]))     # payments of lease liabilities (financing, IFRS 16 from 2019)
DEP   = dict(zip(Y,[32,46,21,71,86,94,118,110,85,79]))  # incl. right-of-use depreciation from 2019
AMORT = dict(zip(Y,[6,8,11,16,25,33,53,48,36,23]))
# working-capital lines inside OCF: receivables, liabilities, deferred revenue, provisions
WC = {2016:-60+245+77+38, 2017:-112+447+77+8, 2018:-61+291+38-17, 2019:-27+454+59-35, 2020:-187+425+73+6,
      2021:-245+137+67+5, 2022:-84+226+52-3, 2023:-145+501+113-5, 2024:145+183+45+3, 2025:-115+281+60+22}
ACCR_SOC = {2017:87,2018:64,2019:64,2020:169,2021:84,2022:7,2023:57,2024:217,2025:217}  # accrued social costs, options+RSUs, Dec 31
INT_RECV = dict(zip(Y,[5,19,18,14,4,3,37,111,216,242]))
TAX_PAID = dict(zip(Y,[-4,2,-9,4,8,6,43,43,53,86]))
EBIT = dict(zip(Y,[-349,-378,-43,-73,-293,94,-659,-446,1365,2198]))
REV = dict(zip(Y,[2952,4090,5259,6764,7880,9668,11727,13247,15673,17186]))
out = {}
for y in Y:
    dsoc = ACCR_SOC[y]-ACCR_SOC[y-1] if (y in ACCR_SOC and y-1 in ACCR_SOC) else 0
    c_hi = CAPEX[y] + LEASE[y]          # conservative (c): capex plus lease principal
    c_da = DEP[y] + AMORT[y]            # D&A default [E3-44]
    base = OCF[y] - SBC[y]
    out[y] = dict(
        OCF=OCF[y], SBC=SBC[y], c_capex_lease=c_hi, c_DA=c_da, WC=WC[y], dSocAccr=dsoc,
        OE_high = base - min(c_hi, c_da) - dsoc,                 # WC kept, social cost on accrual basis, lower (c)
        OE_DA = base - c_da - dsoc,
        OE_capex = base - c_hi - dsoc,
        OE_low = base - max(c_hi, c_da) - WC[y],                 # WC removed (its change incl. the social accrual), higher (c)
        tax_paid=TAX_PAID[y], int_recv=INT_RECV[y], EBIT=EBIT[y], REV=REV[y])
def mean(ys, k): return sum(out[y][k] for y in ys)/len(ys)
W = {'5y 2021-2025':[2021,2022,2023,2024,2025], '2y 2024-2025':[2024,2025], '3y 2023-2025':[2023,2024,2025], '10y 2016-2025':Y}
summ = {w:{k:round(mean(ys,k)) for k in ['OE_high','OE_DA','OE_capex','OE_low','int_recv','WC','SBC']} for w,ys in W.items()}
for y in Y: print(y, out[y])
for w,v in summ.items(): print(w, v)
# normalised-tax sensitivity: statutory 23.87% on EBIT less cash tax actually paid
for y in [2024,2025]:
    print('tax gap', y, round(0.2387*EBIT[y]-TAX_PAID[y]))
json.dump({'years':out,'windows':summ}, open('oe_out.json','w'), indent=1)
