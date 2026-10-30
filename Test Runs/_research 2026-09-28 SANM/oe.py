import json, statistics
from datetime import date
f = json.load(open('cache/facts.json'))['facts']['us-gaap']
def ann(tags):
    out = {}
    for t in tags:
        if t not in f: continue
        for u, arr in f[t]['units'].items():
            for x in arr:
                if x.get('form') not in ('10-K','10-K/A') or x.get('fp') != 'FY' or 'start' not in x: continue
                d = (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days
                if 350 <= d <= 380:
                    y = int(x['end'][:4]) if x['end'][5:7] >= '06' else int(x['end'][:4]) - 1
                    out.setdefault(y, x['val']/1e6) if False else None
                    out[y] = x['val']/1e6
    return out
ocf = ann(['NetCashProvidedByUsedInOperatingActivitiesContinuingOperations']); ocf.update(ann(['NetCashProvidedByUsedInOperatingActivities']))
sbc = ann(['ShareBasedCompensation']); cap = ann(['PaymentsToAcquirePropertyPlantAndEquipment']); da = ann(['DepreciationDepletionAndAmortization'])
psale = ann(['ProceedsFromSaleOfPropertyPlantAndEquipment'])
ni_all = ann(['ProfitLoss']); ni = ann(['NetIncomeLoss'])
years = [y for y in range(2009, 2026) if y in ocf]
CAP = 12047.1
print('FY  OCF  SBC  capex  D&A  OEcap  OEda  NCI')
rows = {}
for y in years:
    nci = (ni_all.get(y, 0) - ni.get(y, 0)) if y in ni_all else 0.0
    a = ocf[y] - sbc[y] - cap[y]; b = ocf[y] - sbc[y] - da[y]
    rows[y] = (a, b, nci)
    print(y, f"{ocf[y]:.1f} {sbc[y]:.1f} {cap[y]:.1f} {da[y]:.1f} {a:.1f} {b:.1f} {nci:.1f} (PPE sale proceeds {psale.get(y,0):.1f})")
# TTM to 2026-06-27 from the 10-Q
t_ocf = ocf[2025] + 701.977 - 421.578; t_sbc = sbc[2025] + 72.502 - 47.163; t_cap = cap[2025] + 244.441 - 84.890; t_da = da[2025] + 134.817 - 89.813
print('TTM', f"{t_ocf:.1f} {t_sbc:.1f} {t_cap:.1f} {t_da:.1f} {t_ocf-t_sbc-t_cap:.1f} {t_ocf-t_sbc-t_da:.1f}")
print('9M FY2026 alone', f"{701.977-72.502-244.441:.1f} {701.977-72.502-134.817:.1f}")
print('\nwindow ending FY2025 | capex end | D&A end (mean $M, yield on $%.1fM)' % CAP)
allv = []
for n in range(1, len(years)+1):
    ys = years[-n:]
    a = statistics.mean(rows[y][0] for y in ys); b = statistics.mean(rows[y][1] for y in ys)
    allv += [a, b]
    print(f"{n:2d}y FY{ys[0]}-{ys[-1]} | {a:.1f} ({100*a/CAP:.2f}%) | {b:.1f} ({100*b/CAP:.2f}%)")
print('range all windows', round(min(allv),1), round(max(allv),1), f"{100*min(allv)/CAP:.2f}%-{100*max(allv)/CAP:.2f}%")
print('sum capex/sum D&A 17y', round(sum(cap[y] for y in years)/sum(da[y] for y in years),2), ' 5y', round(sum(cap[y] for y in years[-5:])/sum(da[y] for y in years[-5:]),2))
