# Owner earnings, TXRH, $M. Operating cash, SBC, D&A, acquired-intangible amortization and capex from the filed cash-flow statements via
# companyfacts (FY2015-FY2025 NetCashProvidedByUsedInOperatingActivities; FY2009-FY2014 NetCashProvidedByUsedInOperatingActivitiesContinuingOperations,
# latest filing), FY2023-FY2025 cross-checked to the FY2025 10-K statement. (c) at two ends: depreciation EXCLUDING the amortization of
# acquired intangibles (reacquired franchise rights; untagged for FY2009-FY2010, taken as zero and flagged), and total capital expenditures.
# SBC subtracted in full [E5-06]. No net-income proxy (operator rule 5).
Y = list(range(2009, 2026))
OCF = [115.129, 120.056, 136.419, 148.046, 173.836, 191.713, 227.941, 257.065, 286.4, 352.9, 374.3, 230.4, 468.8, 511.7, 564.984, 753.629, 730.067]
SBC = [7.5, 7.7, 10.5, 13.2, 14.7, 14.9, 22.8, 26.1, 26.9, 34.0, 35.5, 29.4, 38.1, 36.7, 34.230, 47.055, 47.765]
DA = [41.8, 41.3, 42.7, 46.7, 51.6, 59.2, 69.7, 83.0, 93.5, 101.2, 115.5, 117.9, 126.8, 137.2, 153.202, 178.157, 206.640]
AMI = [0, 0, 1.1, 1.1, 1.6, 1.7, 1.4, 1.2, 0.9, 0.7, 0.7, 0.6, 0.8, 2.8, 3.0, 2.2, 6.463]
CAPEX = [45.5, 45.1, 79.7, 87.0, 111.5, 125.4, 173.5, 164.7, 161.6, 156.0, 214.3, 154.4, 200.7, 246.1, 347.034, 354.341, 387.996]
ACQ = [0, 0, 0, 4.3, 0, 0, 0, 0, 16.5, 2.2, 1.5, 10.6, 0, 33.1, 39.2, 0, 107.528]
CAP = 159.75 * 65640926 / 1e6
DEP = [d - a for d, a in zip(DA, AMI)]
lo = [o - s - c for o, s, c in zip(OCF, SBC, CAPEX)]
hi = [o - s - d for o, s, d in zip(OCF, SBC, DEP)]
print('cap $M %.1f' % CAP)
print('FY    OCF    SBC   DEP  CAPEX  ACQ   OE_capex  OE_dep  capex/dep  SBC/OCF')
for i, y in enumerate(Y):
    print(y, '%6.1f %5.1f %5.1f %6.1f %5.1f  %7.1f %7.1f   %4.2f   %4.1f%%' % (OCF[i], SBC[i], DEP[i], CAPEX[i], ACQ[i], lo[i], hi[i], CAPEX[i] / DEP[i], SBC[i] / OCF[i] * 100))
for n in range(1, 18):
    ml = sum(lo[-n:]) / n; mh = sum(hi[-n:]) / n
    print('%2dy ending FY2025: $%6.1fM to $%6.1fM  yield %.2f%% to %.2f%%' % (n, ml, mh, ml / CAP * 100, mh / CAP * 100))
print('rolling five-year windows (capex end / depreciation end, $M):')
for e in range(2013, 2026):
    i = Y.index(e); a = lo[i - 4:i + 1]; b = hi[i - 4:i + 1]
    print('  5y to', e, round(sum(a) / 5, 1), round(sum(b) / 5, 1))
# TTM to 2026-06-30 = FY2025 - H1 2025 + H1 2026 (10-Q 0001104659-26-092408 cash-flow statement)
ocf = 730.067 - 365.980 + 439.227; sbc = 47.765 - 23.249 + 26.902; capex = 387.996 - 169.912 + 178.845
da = 206.640 - 99.544 + 115.184; ami = 6.463  # H1 amortization of intangibles not tagged in the 10-Q; FY2025's figure used, flagged
dep = da - ami
print('TTM OCF %.1f SBC %.1f capex %.1f D&A %.1f dep(est) %.1f  OE %.1f to %.1f  yield %.2f%% to %.2f%%' % (ocf, sbc, capex, da, dep, ocf - sbc - capex, ocf - sbc - dep, (ocf - sbc - capex) / CAP * 100, (ocf - sbc - dep) / CAP * 100))
# acquisitions of franchise restaurants spent outside (c), five and ten years
print('franchise acquisitions FY2021-25 $%.1fM, FY2016-25 $%.1fM' % (sum(ACQ[-5:]), sum(ACQ[-10:])))
# a five-year window with the acquisitions counted as capital the owner spent (a display, not (c))
print('5y OE capex end less acquisitions: $%.1fM (%.2f%%)' % (sum(l - a for l, a in zip(lo[-5:], ACQ[-5:])) / 5, sum(l - a for l, a in zip(lo[-5:], ACQ[-5:])) / 5 / CAP * 100))
