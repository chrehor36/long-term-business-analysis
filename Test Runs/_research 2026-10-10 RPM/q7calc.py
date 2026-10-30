"""Q7 COMPUTATION, NOT A CLEARANCE (the file closed at Q5). Arithmetic only; inputs from the filed cash-flow
statements (10-Ks FY2017 to FY2026) and the 10-Q of 2026-08-31, USD millions. See the run file, Q7 computation."""
FY   = [2022, 2023, 2024, 2025, 2026]
OCF  = [178.7, 577.1, 1122.3, 768.2, 898.7]
SBC  = [40.1, 28.7, 25.9, 27.0, 32.8]
CAPX = [222.4, 254.4, 214.0, 229.9, 223.5]
DEP  = [104.3, 108.4, 129.8, 146.3, 165.4]
ACQ  = [127.5, 47.5, 15.5, 595.8, 202.4]
SALE = [76.6, 58.3, 6.9, 0.0, 23.2]          # proceeds from sales of assets and businesses (one line as filed)
INT  = [87.9, 119.0, 118.0, 96.5, 111.5]
TAX  = [114.3, 169.7, 198.4, 102.4, 207.9]; PRE = [606.8, 649.4, 787.8, 792.8, 870.3]
# prior block FY2017-FY2021 (no sale line filed in those years)
OC_P  = [227.5, 250.4, 124.9, 382.3, 568.1]; ACQ_P = [254.2, 112.4, 168.2, 65.1, 165.2]
REV_P = [4958.2, 5321.6, 5564.6, 5507.0, 6106.3]; REV = [6707.7, 7256.4, 7335.3, 7372.6, 7863.4]
ORG = [8.9, 10.1, 1.3, 0.8, 2.0]             # consolidated organic growth as the filer reports it, %
NETDEBT = 407.497 + 1999.028 - 312.842       # 10-Q 2026-08-31: current + long-term debt less cash
SH = 127.533690; PRICE = 97.73; SOV = 0.056
m = lambda x: sum(x) / len(x)
oc_all = [o - s - c for o, s, c in zip(OCF, SBC, CAPX)]
oc_mnt = [o - s - d for o, s, d in zip(OCF, SBC, DEP)]
acqnet = [a - s for a, s in zip(ACQ, SALE)]
oc_acq = [x - a for x, a in zip(oc_all, acqnet)]
taxr = sum(TAX) / sum(PRE); iat = m(INT) * (1 - taxr)
print('owner cash, all capex      ', [round(x, 1) for x in oc_all], 'mean', round(m(oc_all), 1))
print('owner cash, maintenance    ', [round(x, 1) for x in oc_mnt], 'mean', round(m(oc_mnt), 1))
print('acquisitions net of sales  ', [round(x, 1) for x in acqnet], 'mean', round(m(acqnet), 1))
print('owner cash after purchases ', [round(x, 1) for x in oc_acq], 'mean', round(m(oc_acq), 1))
print(f'tax rate of the window {taxr:.3f}; interest mean {m(INT):.1f}; after tax {iat:.1f}; net debt {NETDEBT:.1f}')
oc_acq_p = [o - a for o, a in zip(OC_P, ACQ_P)]
g_tot = (m(oc_acq) / m(oc_acq_p)) ** 0.2 - 1
g_all = (m(oc_all) / m(OC_P)) ** 0.2 - 1
g_rev = (m(REV) / m(REV_P)) ** 0.2 - 1
g_org = 1.0
for o in ORG: g_org *= 1 + o / 100
g_org = g_org ** 0.2 - 1
print(f'prior block after purchases mean {m(oc_acq_p):.1f}; growth after purchases {g_tot:.4f}; all-capex {g_all:.4f}; sales {g_rev:.4f}; organic {g_org:.4f}')
def val(base_in, base_term, g, r):
    """ten years of base_in grown at g (year 1 = base*(1+g)), then base_term grown ten years, held flat, at r"""
    pv = sum(base_in * (1 + g) ** t / (1 + r) ** t for t in range(1, 11))
    return pv + base_term * (1 + g) ** 10 / r / (1 + r) ** 10
def ps(v, equity_only=False):
    return v / SH if equity_only else (v - NETDEBT) / SH
cases = {}
for basis, add, eo in (('all-equity', iat, False), ('equity-only', 0.0, True)):
    for r, lab in ((SOV, 'sovereign'), (0.10, 'ten percent')):
        lo = val(m(oc_mnt) + add, m(oc_mnt) + add, 0.0, r)                     # maintenance-only, no growth
        hi = val(m(oc_acq) + add, m(oc_all) + add, g_rev, r)                   # all spending, growth capped at sales growth
        hu = val(m(oc_acq) + add, m(oc_all) + add, g_tot, r)                   # beside: shown growth uncapped
        na = val(m(oc_all) + add, m(oc_all) + add, 0.0, r)                     # beside: all-capex, no growth
        og = val(m(oc_all) + add, m(oc_all) + add, g_org, r)                   # beside: organic pair
        cases[(basis, lab)] = (ps(lo, eo), ps(hi, eo))
        print(f'{basis:11s} {lab:11s}  no-growth maint {ps(lo,eo):7.2f} | growth capped {g_rev:.3%} {ps(hi,eo):7.2f} | '
              f'uncapped {g_tot:.3%} {ps(hu,eo):7.2f} | all-capex no-growth {ps(na,eo):7.2f} | organic {g_org:.3%} {ps(og,eo):7.2f}')
for basis in ('all-equity', 'equity-only'):
    lo, hi = cases[(basis, 'ten percent')]
    print(f'FAIR PRICE {basis}: ({lo:.2f} + {hi:.2f}) / 2 = {(lo + hi) / 2:.2f}')
# expected return at the price on each end (IRR-like: rate at which value = price), all-equity
def solve(base_in, base_term, g):
    a, b = 0.01, 0.30
    for _ in range(100):
        r = (a + b) / 2
        if ps(val(base_in, base_term, g, r)) > PRICE: a = r
        else: b = r
    return r
print('return at the price, all-equity: no-growth maint %.2f%%; growth capped %.2f%%; uncapped %.2f%%' % (
    100 * solve(m(oc_mnt) + iat, m(oc_mnt) + iat, 0), 100 * solve(m(oc_acq) + iat, m(oc_all) + iat, g_rev),
    100 * solve(m(oc_acq) + iat, m(oc_all) + iat, g_tot)))
