# AIG run 2026-09-19 - all Stage 0 / Q3 / Q4 / Q5 arithmetic. Every input hand-read from a filed statement.
# FY2025 10-K 0000005272-26-000023; FY2023 10-K 0000005272-24-000023; FY2021 10-K 0001104659-22-024701;
# FY2018 10-K 0000005272-19-000023; Q2 2026 10-Q 0000005272-26-000076; DEF 14A 0000005272-26-000039.
import sys, os, json, datetime
sys.path.insert(0, os.path.abspath('tools')); import sources
P = 75.33; SH = 522_893_169; CAP = P * SH / 1e6          # price 2026-09-18 (aggregator, flagged); 10-Q cover 2026-07-31
SOV = 5.34
print('CAP $M %.0f' % CAP)
# --- Stage 0(b) CONVENTION 4 float
fl = {2024: 69168 + 17232 - 29026 - 10463 - 2065, 2025: 70666 + 17991 - 28871 - 10441 - 2106}
inv = {2024: 93613, 2025: 92999}; eq = {2024: 42521, 2025: 41139}
for y in fl: print('float %d %d  f/inv %.1f%%  inv/eq %.2fx  f/eq %.2fx' % (y, fl[y], 100*fl[y]/inv[y], inv[y]/eq[y], fl[y]/eq[y]))
print('equity check 2025', 161254 - 120092 - 23, ' 6/30/26', 163464 - 122838 - 20, ' BVPS', round(41139/538.2, 2))
# --- Q4 cost of float, net-loss-reserve proxy (rollforwards) and GI underwriting income (APTI basis)
nr = {2015: 60603, 2016: 61545, 2017: 51685, 2018: 51949, 2019: 47423, 2020: 43289, 2021: 43813, 2022: 43065, 2023: 40104, 2024: 40142, 2025: 41795}
uw = {2016: -5605, 2017: -4481, 2018: -3137, 2019: 89, 2020: -1024, 2021: 1055, 2022: 2048, 2023: 2349, 2024: 1917, 2025: 2332}
tot_uw = tot_avg = 0
for y in range(2016, 2026):
    a = (nr[y-1] + nr[y]) / 2; c = -uw[y] / a * 100; tot_uw += uw[y]; tot_avg += a
    print('cost of float %d  uw %6d  avg net reserves %6.0f  cost %+.2f%%' % (y, uw[y], a, c))
print('10-yr cumulative UW %d; cost %+.2f%%/yr' % (tot_uw, -tot_uw / tot_avg * 100))
u5 = sum(uw[y] for y in range(2021, 2026)); a5 = sum((nr[y-1]+nr[y])/2 for y in range(2021, 2026))
print('5-yr 2021-25 UW %d; cost %+.2f%%/yr' % (u5, -u5 / a5 * 100))
print('CONVENTION-4 2025 cost %+.2f%%' % (-2332 / ((fl[2024] + fl[2025]) / 2) * 100))
# --- Q3 primary test [E2-01]
print('ROE GAAP 2023 8.6 / 2024 -3.2 / 2025 7.5 mean %.1f ; core operating 9.6/9.1/11.1 mean %.1f' % ((8.6-3.2+7.5)/3, (9.6+9.1+11.1)/3))
# --- Q3 buybacks vs book
bb = [('2024', 6600, 89, 70.16, 61.75), ('2025', 5800, 73, 76.44, 69.12), ('H1 2026', 1200, 15, 77.39, 74.43)]
for y, d, n, bv, cbv in bb: print('buyback %s $%dM / %dM sh = $%.2f avg; %.2fx year-end BVPS, %.2fx core operating BVPS' % (y, d, n, d/n, d/n/bv, d/n/cbv))
print('shares 12/31/23 688.8M -> 7/31/26 522.9M: %.1f%%' % ((522.893/688.8 - 1) * 100))
# --- Q3 retention test [E3-54], 12/31/20 -> 12/31/25
r = sources._chart('AIG', '10y'); ts = r['timestamp']; cl = r['indicators']['quote'][0]['close']
d = {datetime.datetime.utcfromtimestamp(t).strftime('%Y-%m-%d'): c for t, c in zip(ts, cl) if c}
def close(iso): k = max(x for x in d if x <= iso); return k, d[k]
k0, p0 = close('2020-12-31'); k1, p1 = close('2025-12-31')
mc0 = p0 * 861.6; mc1 = p1 * 538.2
ni = {2021: 10338, 2022: 10198, 2023: 3614, 2024: -1426, 2025: 3096}
dv = {2021: 1083, 2022: 982, 2023: 997, 2024: 1002, 2025: 976}
buy = {2021: 2643, 2022: 5149, 2023: 3014, 2024: 6713, 2025: 5875}
ret = sum(ni.values()) - sum(dv.values())
print('close %s %.2f (aggregator, split-free, close not adjclose) cap %.0f; close %s %.2f cap %.0f' % (k0, p0, mc0, k1, p1, mc1))
print('NI to common 2021-25 %d, dividends %d, retained %d; buybacks %d' % (sum(ni.values()), sum(dv.values()), ret, sum(buy.values())))
print('[E3-54] mkt value change per $1 retained: %.2f ; counting buybacks as distributions: %.2f' % ((mc1 - mc0) / ret, (mc1 - mc0) / (ret - sum(buy.values()))))
print('BVPS 12/31/20 76.46 -> 12/31/25 76.44 ; price %.2f -> %.2f (%+.1f%%/yr)' % (p0, p1, ((p1/p0)**(1/5)-1)*100))
# --- Q5 COMPUTATION, NOT A CLEARANCE
c1 = 92999 + 1274 - (9035 + 156) - 3038 - (1385 + 352)
print('component 1 gross-of-float %d  ($%.2f/sh);  less float %d -> %d ($%.2f/sh)' % (c1, c1/SH*1e6, fl[2025], c1 - fl[2025], (c1 - fl[2025])/SH*1e6))
apti = {2023: 4321, 2024: 4324, 2025: 5344}; nii = {2023: 3022+190, 2024: 3060+434, 2025: 3433+349}
restr = {2023: 356+6+71+22, 2024: 745+39+0+18, 2025: 439+136+15+16}
for y in apti:
    c2 = apti[y] - nii[y]; print('component 2 %d: APTI-basis %d ; after restructuring/integration/pension/regulatory %d' % (y, c2, c2 - restr[y]))
gaap = {2023: 2867, 2024: 3870, 2025: 3879}
print('yields on cap: APTI 2025 %.2f%%; APTI less restructuring etc 2025 %.2f%%; GAAP pre-tax cont ops 2025 %.2f%%, 3-yr mean %.2f%%' % (5344/CAP*100, (5344-606)/CAP*100, 3879/CAP*100, sum(gaap.values())/3/CAP*100))
print('P/B 6/30/26 %.3f ; P/core op BV %.3f ; P/adj tangible BV %.3f' % (P/77.39, P/74.43, P/72.18))
