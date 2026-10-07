"""Owner earnings for OTTR, every valid window, both (c) ends, with and without the
plastics boom. All inputs are filed lines; sources in the run file."""
import sys
sys.stdout.reconfigure(encoding='utf-8')

# filed annual lines, $ thousands
OCF = {2019: 185037, 2020: 211921, 2021: 231243, 2022: 389309, 2023: 404499, 2024: 452731, 2025: 385985}
CAPEX = {2019: 207365, 2020: 371553, 2021: 171829, 2022: 171134, 2023: 287134, 2024: 358650, 2025: 288068}
SBC = {2019: 5958, 2020: 6284, 2021: 6908, 2022: 6814, 2023: 7753, 2024: 9529, 2025: 9119}
DA = {2019: 78086, 2020: 82037, 2021: 91358, 2022: 92597, 2023: 97954, 2024: 107121, 2025: 118107}

# TTM to 2026-06-30 = FY2025 - H1 2025 + H1 2026
H1_26 = dict(ocf=182711, capex=324755, sbc=8526, da=60789)
H1_25 = dict(ocf=159379, capex=124239, sbc=7396, da=58822)
TTM = {k: OCF[2025] - H1_25['ocf'] + H1_26['ocf'] if k == 'ocf' else
       {'capex': CAPEX[2025] - H1_25['capex'] + H1_26['capex'],
        'sbc': SBC[2025] - H1_25['sbc'] + H1_26['sbc'],
        'da': DA[2025] - H1_25['da'] + H1_26['da']}[k]
       for k in ('ocf', 'capex', 'sbc', 'da')}
ESCROW_PAID_IN_TTM = 73500   # paid into settlement escrow June 2026; NOT deducted from filed OCF
                             # because the statement reconciles cash INCLUDING restricted cash

# the (c) JUDGMENT, built from the filed five-year capital plan (FY2025 10-K, p.39-40)
# Electric 2026-2030: Renewable Gen & Storage 645, Transmission 855, Distribution 268, Other 153
C_ELEC_RENEWAL = (645 + 268 + 153) * 1000 / 5.0    # replacement of retiring plant + distribution + other
C_ELEC_GROWTH = 855 * 1000 / 5.0                   # transmission = rate-base expansion
C_MFG_PLAT = 129 * 1000 / 5.0                      # Manufacturing + Plastics five-year plan
C_JUDGMENT = C_ELEC_RENEWAL + C_MFG_PLAT

print('(c) JUDGMENT, from the filed 2026-2030 capital plan, $ thousands per year')
print('  Electric renewal (Renewable Gen+Storage %d + Distribution %d + Other %d) / 5 = %.0f'
      % (645, 268, 153, C_ELEC_RENEWAL))
print('  Manufacturing Platform 129 / 5                                          = %.0f' % C_MFG_PLAT)
print('  (c) judgment total                                                      = %.0f' % C_JUDGMENT)
print('  Electric growth leg excluded from (c) (Transmission 855/5)              = %.0f' % C_ELEC_GROWTH)
print('  consolidated D&A FY2025 for comparison                                  = %d' % DA[2025])
print('  ratio (c) judgment / D&A = %.2fx   <- [E5-20] the D&A end is INVALID for the utility' %
      (C_JUDGMENT / DA[2025]))
print()


def oe(years, cmode):
    n = len(years)
    ocf = sum(OCF[y] for y in years) / n
    sbc = sum(SBC[y] for y in years) / n
    if cmode == 'capex':
        c = sum(CAPEX[y] for y in years) / n
    elif cmode == 'da':
        c = sum(DA[y] for y in years) / n
    else:
        c = C_JUDGMENT
    return ocf - sbc - c


WINDOWS = {
    '3y 2023-25': [2023, 2024, 2025],
    '4y 2022-25': [2022, 2023, 2024, 2025],
    '5y 2021-25': [2021, 2022, 2023, 2024, 2025],
    '6y 2020-25': [2020, 2021, 2022, 2023, 2024, 2025],
    '7y 2019-25': [2019, 2020, 2021, 2022, 2023, 2024, 2025],
}

CAP = 41985580 * 87.42 / 1000.0   # $ thousands

print('AS FILED — owner earnings = mean OCF less mean SBC less (c)')
print('%-13s %10s %10s %10s' % ('window', 'capex end', 'judgment', 'D&A end*'))
rows = []
for name, ys in WINDOWS.items():
    a, b, d = oe(ys, 'capex'), oe(ys, 'judgment'), oe(ys, 'da')
    rows += [a, b, d]
    print('%-13s %10.0f %10.0f %10.0f   yields %.2f%% / %.2f%% / %.2f%%'
          % (name, a, b, d, 100 * a / CAP, 100 * b / CAP, 100 * d / CAP))

ttm_capex = TTM['ocf'] - TTM['sbc'] - TTM['capex']
ttm_judg = TTM['ocf'] - TTM['sbc'] - C_JUDGMENT
ttm_da = TTM['ocf'] - TTM['sbc'] - TTM['da']
print('%-13s %10.0f %10.0f %10.0f   yields %.2f%% / %.2f%% / %.2f%%'
      % ('TTM 6/30/26', ttm_capex, ttm_judg, ttm_da,
         100 * ttm_capex / CAP, 100 * ttm_judg / CAP, 100 * ttm_da / CAP))
print('   TTM inputs: OCF %d  SBC %d  capex %d  D&A %d' % (TTM['ocf'], TTM['sbc'], TTM['capex'], TTM['da']))
print('%-13s %10.0f %10.0f %10.0f   <- TTM LESS the $73.5m escrow actually paid'
      % ('TTM adj', ttm_capex - ESCROW_PAID_IN_TTM, ttm_judg - ESCROW_PAID_IN_TTM,
         ttm_da - ESCROW_PAID_IN_TTM))
rows += [ttm_capex, ttm_judg, ttm_da, ttm_capex - ESCROW_PAID_IN_TTM, ttm_da - ESCROW_PAID_IN_TTM]
print()
print('AS-FILED BAND: %.0f to %.0f   (%.2f%% to %.2f%% of a $%.0fm cap)'
      % (min(rows), max(rows), 100 * min(rows) / CAP, 100 * max(rows) / CAP, CAP / 1000))
print()

# ---------- WITHOUT THE PLASTICS BOOM ----------
# Plastics segment operating income and revenue, filed
P_REV = {2017: 185075, 2018: 197840, 2019: 183257, 2020: 205249, 2021: 380229,
         2022: 512527, 2023: 418026, 2024: 463441, 2025: 422755}
P_OP = {2017: 29644, 2018: 32917, 2019: 28439, 2020: 37823, 2021: 132760,
        2022: 264578, 2023: 254402, 2024: 271905, 2025: 231079}
pre = [2017, 2018, 2019, 2020]
pre_margin = sum(P_OP[y] for y in pre) / sum(P_REV[y] for y in pre)
pre_dollars = sum(P_OP[y] for y in pre) / len(pre)
print('PRE-BOOM PLASTICS BASELINE, 2017-2020 (four filed years, none touched by the boom)')
print('  mean operating margin  = %.1f%%' % (100 * pre_margin))
print('  mean operating income  = %.0f' % pre_dollars)
TAXR = 59999 / 230399.0   # Plastics 2025 segment effective tax rate, filed
print('  Plastics segment effective tax rate, FY2025 filed = %.1f%%' % (100 * TAXR))
print()
print('METHOD A - price actual revenue at the pre-boom margin (respects inflation and mix)')
print('METHOD B - hold the pre-boom DOLLAR income, scaled by the pounds index (ignores inflation)')
POUNDS = {2020: 1.000, 2021: 1.017, 2022: 0.824, 2023: 0.708, 2024: 0.900, 2025: 0.972}
adjA, adjB = {}, {}
for y in [2021, 2022, 2023, 2024, 2025]:
    normA = P_REV[y] * pre_margin
    normB = pre_dollars * POUNDS[y]
    adjA[y] = (P_OP[y] - normA) * (1 - TAXR)
    adjB[y] = (P_OP[y] - normB) * (1 - TAXR)
    print('  %d  filed %7.0f  normA %7.0f  normB %7.0f   after-tax excess A %7.0f  B %7.0f'
          % (y, P_OP[y], normA, normB, adjA[y], adjB[y]))
print()


def oe_norm(years, cmode, adj):
    n = len(years)
    ocf = sum(OCF[y] - adj.get(y, 0) for y in years) / n
    sbc = sum(SBC[y] for y in years) / n
    if cmode == 'capex':
        c = sum(CAPEX[y] for y in years) / n
    elif cmode == 'da':
        c = sum(DA[y] for y in years) / n
    else:
        c = C_JUDGMENT
    return ocf - sbc - c


print('WITHOUT THE PLASTICS BOOM — the same windows, boom excess removed after tax')
allnorm = []
for label, adj in (('A', adjA), ('B', adjB)):
    print(' method', label)
    for name, ys in WINDOWS.items():
        a, b, d = oe_norm(ys, 'capex', adj), oe_norm(ys, 'judgment', adj), oe_norm(ys, 'da', adj)
        allnorm += [a, b, d]
        print('   %-13s %10.0f %10.0f %10.0f   yields %.2f%% / %.2f%% / %.2f%%'
              % (name, a, b, d, 100 * a / CAP, 100 * b / CAP, 100 * d / CAP))
print()
print('NORMALISED BAND: %.0f to %.0f   (%.2f%% to %.2f%%)'
      % (min(allnorm), max(allnorm), 100 * min(allnorm) / CAP, 100 * max(allnorm) / CAP))
print()
print('Market cap used: $%.1fm  = 41,985,580 x $87.42' % (CAP / 1000))
print('Sovereign 5.34%%; the [E4-28] floor is ~10%%.')
print()
print('SBC checks: 18 filed years 2008-2025, every year present and non-zero.')
print('  FY2025 charge 9,119; fair value of vested awards 3.6m restricted + 5.5m performance = 9.1m.')
print('  SBC / FY2025 operating cash = %.2f%%' % (100 * 9119 / 385985))
print()
print('Staying power:')
print('  interest paid FY2025 45,701; OCF 385,985; capex 288,068')
print('  [E2-54] coverage: (OCF - capex) / interest paid = %.2fx'
      % ((385985 - 288068) / 45701.0))
print('  [E2-54] on the (c) judgment: (OCF - c) / interest = %.2fx'
      % ((385985 - C_JUDGMENT) / 45701.0))
print('  debt due <1yr 140,000 + interest 47,000 = 187,000 against cash 386,193')
