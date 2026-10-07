import json, sys
from datetime import date
sys.stdout.reconfigure(encoding='utf-8')
# Owner earnings, every window ending 2025 and the TTM to 2026-06-30, at both (c) ends.
# OE = operating cash (as filed, newest vintage across the total and continuing tags; no discontinued
# operations exist in any year read) - stock compensation in full [E5-06] - (c).
# (c) capex end = capital expenditures; (c) depreciation end = the filed "Depreciation" line, which
# excludes the separate "Amortization" line of acquired intangibles [E3-44, E2-41].
g = json.load(open('cache/facts.json'))['facts']['us-gaap']
def ann(tags):
    out = {}
    for tag in tags:
        if tag not in g: continue
        for u, v in g[tag]['units'].items():
            for x in v:
                if x.get('form') not in ('10-K', '10-K/A') or 'start' not in x: continue
                d = (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days
                if not 340 <= d <= 380: continue
                y = int(x['end'][:4])
                if y not in out or x['filed'] > out[y][1]: out[y] = (x['val'] / 1e6, x['filed'], tag)
    return out
ocf = ann(['NetCashProvidedByUsedInOperatingActivities', 'NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'])
sbc = ann(['ShareBasedCompensation']); cap = ann(['PaymentsToAcquirePropertyPlantAndEquipment'])
dep = ann(['Depreciation']); amo = ann(['AmortizationOfIntangibleAssets']); acq = ann(['PaymentsToAcquireBusinessesNetOfCashAcquired'])
ni = ann(['ProfitLoss'])
Y = [y for y in range(2008, 2026) if y in ocf and y in sbc and y in cap and y in dep]
print('year | OCF | SBC | capex | depreciation | acquired-intangible amortization | OE capex end | OE depreciation end | capex/depreciation | net income | acquisitions')
oec, oed = {}, {}
for y in Y:
    oec[y] = ocf[y][0] - sbc[y][0] - cap[y][0]; oed[y] = ocf[y][0] - sbc[y][0] - dep[y][0]
    print(y, '| %.1f | %.1f | %.1f | %.1f | %s | %.1f | %.1f | %.2f | %s | %s' % (ocf[y][0], sbc[y][0], cap[y][0], dep[y][0], ('%.1f' % amo[y][0]) if y in amo else '-', oec[y], oed[y], cap[y][0] / dep[y][0], ('%.1f' % ni[y][0]) if y in ni else '-', ('%.1f' % acq[y][0]) if y in acq else '-'))
# TTM to 2026-06-30 from the 10-Q (six months 2026 and 2025), filed figures:
t_ocf = ocf[2025][0] + 222.180 - 208.700; t_sbc = sbc[2025][0] + 24.072 - 27.208
t_cap = cap[2025][0] + 122.959 - 120.287; t_dep = dep[2025][0] + 132.792 - 113.720
print('TTM 2026-06 | %.1f | %.1f | %.1f | %.1f | | %.1f | %.1f' % (t_ocf, t_sbc, t_cap, t_dep, t_ocf - t_sbc - t_cap, t_ocf - t_sbc - t_dep))
CAP = 123.87 * 63581129 / 1e6
print('\ncap $%.1fM' % CAP)
print('window ending 2025 | years | OE capex end | OE depreciation end | yield capex end | yield depreciation end')
for n in (1, 2, 3, 4, 5, 7, 10, 15, len(Y)):
    ys = [y for y in Y if y > 2025 - n]
    if len(ys) != n: continue
    a = sum(oec[y] for y in ys) / n; b = sum(oed[y] for y in ys) / n
    print('%d-%d | %d | %.1f | %.1f | %.2f%% | %.2f%%' % (ys[0], ys[-1], n, a, b, 100 * a / CAP, 100 * b / CAP))
print('TTM | 1 | %.1f | %.1f | %.2f%% | %.2f%%' % (t_ocf - t_sbc - t_cap, t_ocf - t_sbc - t_dep, 100 * (t_ocf - t_sbc - t_cap) / CAP, 100 * (t_ocf - t_sbc - t_dep) / CAP))
# the screen's construction check: 3y and 5y at both capex ends
for n in (3, 5):
    ys = list(range(2026 - n, 2026))
    print('screen check %dy' % n, round(sum(oec[y] for y in ys) / n, 1), round(sum(oed[y] for y in ys) / n, 1))
