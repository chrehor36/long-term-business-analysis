# Q7 arithmetic for the AQN run (COMPUTATION). Figures in $ millions from the filed statements; see run file for sources.
SH = 769.901895      # common shares issued and outstanding at 2026-08-06 (Q2 2026 MD&A, Equity)
PX = 5.42            # close 2026-10-27, Yahoo (aggregator, flagged)
RF = 0.0530          # UST 30y par, 2026-10-27
FLOOR = 0.10
NETDEBT = 6635.7 - 55.0   # LTD incl current, CP and bank lines, less cash, 2026-06-30
PREF = 184.3
CAP = 6635.7/(6635.7+4977.2)  # own LTD share of LT capital, 2026-06-30
SECURITIZATION = 305.5  # Empire securitized utility tariff bonds issued 2024-01-30 (note 6(a)), left out with their charge
DEBT_INC = ((6532.9-337.0-4.5-78.5) - (4538.47-223.507-152.338-122.0) - SECURITIZATION)/5  # LTD ex CP/revolvers/bank lines and securitization, end-2020 to end-2025, per year
TAXSHIELD = 0.25
bases = {
 'central: avg FY2024 continuing + FY2025': dict(ocf=(360.4+593.6)/2, sus=(617.1+505.0)/2, gro=(146.7+103.8)/2, da=(395.7+400.3)/2, intpd=(377.3+312.1)/2),
 'FY2025':                                  dict(ocf=593.6, sus=505.0, gro=103.8, da=400.3, intpd=312.1),
 'TTM to 2026-06-30':                       dict(ocf=589.3, sus=488.6, gro=123.6, da=412.2, intpd=299.1),
 'FY2024 continuing':                       dict(ocf=360.4, sus=617.1, gro=146.7, da=395.7, intpd=377.3),
}
PREFDIV = 10.5
def pv(m0, gspend, credit, g, r, n=10):
    v = 0.0
    for t in range(1, n+1):
        v += (m0*(1+g)**t - (gspend - credit)*(1+g)**t) / (1+r)**t
    v += (m0*(1+g)**n / r) / (1+r)**n   # zero nominal growth after year 10; growth spending and credit stop
    return v
def run(name, b, maint, g, basis):
    total = b['sus'] + b['gro']
    m = b['sus'] if maint == 'sustaining' else b['da']
    gs = max(total - m, 0.0)
    if basis == 'equity':
        m0 = b['ocf'] - m - PREFDIV
        credit = min(DEBT_INC, CAP*gs)
        adj = 0.0
    else:  # all-equity: before interest (after tax shield), preferred treated as a claim
        m0 = b['ocf'] - m + b['intpd']*(1-TAXSHIELD)
        credit = 0.0
        adj = NETDEBT + PREF
    out = {}
    for lab, r in (('rf', RF), ('10%', FLOOR)):
        ng = m0 / r - adj
        gr = pv(m0, gs, credit, g, r) - adj
        out[lab] = (ng/SH, gr/SH)
    return m0, gs, credit, out
if __name__ == '__main__':
    print(f"cap {CAP:.3f}  debt increase/yr {DEBT_INC:.1f}  net debt {NETDEBT:.1f}  mkt cap {PX*SH:.0f}")
    for g in (0.035, 0.062):
        for basis in ('equity', 'all-equity'):
            for maint in ('sustaining', 'D&A'):
                for name, b in bases.items():
                    m0, gs, cr, o = run(name, b, maint, g, basis)
                    lo, hi = sorted(o['rf']); f = sum(o['10%'])/2
                    clears = max(o['10%']) >= PX
                    print(f"g={g:.3f} {basis:10s} maint={maint:10s} {name:42s} m0={m0:7.1f} growth-spend={gs:6.1f} credit={cr:6.1f} | range rf ${o['rf'][0]:6.2f} (no-growth) ${o['rf'][1]:6.2f} (growth) | at10% ${o['10%'][0]:6.2f} ${o['10%'][1]:6.2f} fair ${f:6.2f} | floor cleared at price: {clears}")
