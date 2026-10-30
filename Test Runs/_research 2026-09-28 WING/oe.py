import json, sys
from datetime import date
sys.stdout.reconfigure(encoding='utf-8')
F = json.load(open('cache/facts.json', encoding='utf-8'))['facts']
def ann(ns, t):
    out = {}
    if t not in F.get(ns, {}): return out
    for u, arr in F[ns][t]['units'].items():
        for x in arr:
            if x.get('form') in ('10-K', '10-K/A') and 'start' in x:
                d = (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days
                if 350 <= d <= 380: out[int(x['end'][:4])] = x['val'] / 1e6   # latest filed wins
    return out
print([k for k in F.get('wing', {}).keys() if 'Acqui' in k or 'Restaurant' in k][:20])
ocf = ann('us-gaap', 'NetCashProvidedByUsedInOperatingActivities'); sbc = ann('us-gaap', 'ShareBasedCompensation')
cap = ann('us-gaap', 'PaymentsToAcquirePropertyPlantAndEquipment'); da = ann('us-gaap', 'DepreciationDepletionAndAmortization')
acq = {}
for t in F.get('wing', {}):
    if 'Acqui' in t and 'Restaurant' in t: acq = ann('wing', t); print('acq tag', t)
yrs = sorted(ocf)
oe_c = {y: ocf[y] - sbc[y] - cap[y] for y in yrs}; oe_d = {y: ocf[y] - sbc[y] - da[y] for y in yrs}
print('FY   OCF   SBC  capex   D&A  OEcap  OEda  acq')
for y in yrs: print(y, '%6.1f %5.1f %6.1f %5.1f %6.1f %6.1f %5s' % (ocf[y], sbc[y], cap[y], da[y], oe_c[y], oe_d[y], ('%.1f' % acq[y]) if y in acq else ''))
CAP = 99.07 * 27242546 / 1e6
print('cap', round(CAP, 1))
for n in range(1, len(yrs) + 1):
    w = yrs[-n:]; c = sum(oe_c[y] for y in w) / n; d = sum(oe_d[y] for y in w) / n
    print('%2dy %d-%d  capex end %6.1f (%.2f%%)  D&A end %6.1f (%.2f%%)' % (n, w[0], w[-1], c, c / CAP * 100, d, d / CAP * 100))
t_ocf = 153.065 + 68.301 - 31.876; t_sbc = 24.878 + 8.716 - 11.529; t_cap = 47.441 + 35.936 - 22.381; t_da = 25.068 + 14.053 - 12.448
print('TTM OCF %.1f SBC %.1f capex %.1f D&A %.1f  OE cap %.1f (%.2f%%) OE da %.1f (%.2f%%)' % (t_ocf, t_sbc, t_cap, t_da, t_ocf - t_sbc - t_cap, (t_ocf - t_sbc - t_cap) / CAP * 100, t_ocf - t_sbc - t_da, (t_ocf - t_sbc - t_da) / CAP * 100))
