"""[E3-28] competitor row for the HESM run, 2026-09-20.

Metric: operating income / (net PP&E + net intangibles + equity-method investments),
FY2021-FY2025, mean of numerator over mean of denominator. Every cell from the peer's
own SEC XBRL company facts, 10-K facts only, newest value per year.

The dual PP&E tag list is deliberate: PAA/PAGP stopped tagging
PropertyPlantAndEquipmentNet after FY2020 and moved to the finance-lease-inclusive
element, which silently drops the filer from any screen keyed to the first tag.
HESM itself tags the first element continuously FY2018-FY2025, so the trap is
filer-specific, not industry-wide.

Reproduces PAGP's cross-run figure for HESM at 25.56% against its published 25.5%.
Run from inside `Test Runs/_research 2026-09-20 HESM/` after fetch.py has populated
companyfacts.json and peers/.
"""
import json
import glob
import os

YEARS = ['2021', '2022', '2023', '2024', '2025']
PPE = ['PropertyPlantAndEquipmentNet',
       'PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfter'
       'AccumulatedDepreciationAndAmortization']
INT = ['FiniteLivedIntangibleAssetsNet', 'IntangibleAssetsNetExcludingGoodwill']
EMI = ['EquityMethodInvestments']


def series(us, tags, duration):
    """Newest 10-K value per fiscal year. duration=True for flow tags, False for stocks."""
    out = {}
    for tag in tags:
        if tag not in us:
            continue
        for _unit, rows in us[tag]['units'].items():
            for r in rows:
                if r.get('form') not in ('10-K', '10-K/A'):
                    continue
                end, start = r['end'], r.get('start')
                if duration:
                    if not start or start[:4] != end[:4] or start[5:7] != '01' or end[5:7] != '12':
                        continue
                elif start or end[5:7] != '12':
                    continue
                if end[:4] in YEARS:
                    out.setdefault(end[:4], {}).setdefault(tag, r['val'])
    return out


def calc(name, path):
    us = json.load(open(path))['facts']['us-gaap']
    oi = series(us, ['OperatingIncomeLoss'], True)
    ppe, intan, emi = series(us, PPE, False), series(us, INT, False), series(us, EMI, False)
    nums, dens = [], []
    for y in YEARS:
        o = oi.get(y, {}).get('OperatingIncomeLoss')
        p = next((ppe[y][t] for t in PPE if y in ppe and t in ppe[y]), None)
        i = next((intan[y][t] for t in INT if y in intan and t in intan[y]), 0)
        e = emi.get(y, {}).get('EquityMethodInvestments', 0)
        if o is None or p is None:
            print(f'  {name} {y}: MISSING operating income or PP&E, year dropped')
            continue
        nums.append(o)
        dens.append(p + i + e)
    if not nums:
        print(f'{name}: NO DATA')
        return
    r = (sum(nums) / len(nums)) / (sum(dens) / len(dens))
    print(f'{name:6s} {r * 100:6.1f}%  n={len(nums)}  '
          f'opinc_mean={sum(nums) / len(nums) / 1e6:9.1f}M  '
          f'cap_mean={sum(dens) / len(dens) / 1e6:10.1f}M')


if __name__ == '__main__':
    calc('HESM', 'companyfacts.json')
    for f in sorted(glob.glob('peers/*_companyfacts.json')):
        calc(os.path.basename(f).split('_')[0], f)
