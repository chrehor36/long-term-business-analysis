# Owner earnings, [E2-23] form: OCF (filed, companyfacts cross-checked at Step 0) - SBC (noncash compensation) - (c)
# (c) two ends: capex (Purchases of property and equipment, gross of sale proceeds) and D&A excluding goodwill impairment.
import json
from datetime import date
f=json.load(open('cache/facts.json'))['facts']['us-gaap']
def dur(t):
    o={}
    if t not in f: return o
    for u,a in f[t]['units'].items():
        for x in a:
            if x.get('form') in ('10-K','10-K/A') and 'start' in x and 350<=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<=380:
                o[int(x['end'][:4])]=x['val']/1e6
    return o
ocf=dur('NetCashProvidedByUsedInOperatingActivities'); sbc=dur('ShareBasedCompensation'); cap=dur('PaymentsToAcquirePropertyPlantAndEquipment')
da_all=dur('DepreciationAndAmortization'); dda=dur('DepreciationDepletionAndAmortization'); dep=dur('Depreciation'); am=dur('AmortizationOfIntangibleAssets')
da={}
for y in range(2008,2026):
    if y<=2016: da[y]=da_all[y]; src='DepreciationAndAmortization'
    elif y<=2020: da[y]=dep[y]+am[y]   # face line 2018-2020 includes goodwill impairment ($76M 2018, $15M 2019, 2020 face 528.9)
    elif y==2021: da[y]=da_all[y]
    else: da[y]=dda[y]
# TTM to 2026-06-30 from the 10-Q (six months 2026 and 2025): OCF (3.912) (3.531); SBC 10.458 7.381; capex 40.585 56.360; D&A 54.600 49.848
ttm={'ocf':ocf[2025]-3.912+3.531,'sbc':sbc[2025]+10.458-7.381,'cap':cap[2025]+40.585-56.360,'da':da[2025]+54.600-49.848}
print('FY | OCF | SBC | capex | D&A (ex goodwill impairment) | OE capex end | OE D&A end')
rows={}
for y in range(2008,2026):
    a=ocf[y]-sbc[y]-cap[y]; b=ocf[y]-sbc[y]-da[y]; rows[y]=(a,b)
    print(f'{y} | {ocf[y]:.1f} | {sbc[y]:.1f} | {cap[y]:.1f} | {da[y]:.1f} | {a:.1f} | {b:.1f}')
ta=ttm['ocf']-ttm['sbc']-ttm['cap']; tb=ttm['ocf']-ttm['sbc']-ttm['da']
print(f"TTM 2026-06 | {ttm['ocf']:.1f} | {ttm['sbc']:.1f} | {ttm['cap']:.1f} | {ttm['da']:.1f} | {ta:.1f} | {tb:.1f}")
cap_m=46.26*99529645/1e6
print('\ncap', round(cap_m,1))
print('\nTRAILING WINDOWS ENDING FY2025 (every length):')
for n in range(1,19):
    ys=range(2026-n,2026); a=sum(rows[y][0] for y in ys)/n; b=sum(rows[y][1] for y in ys)/n
    print(f'{n:2d}y FY{2026-n}-25 | capex end {a:.1f} ({100*a/cap_m:.2f}%) | D&A end {b:.1f} ({100*b/cap_m:.2f}%)')
print('\nROLLING FIVE-YEAR WINDOWS (every end year):')
for e in range(2012,2026):
    ys=range(e-4,e+1); a=sum(rows[y][0] for y in ys)/5; b=sum(rows[y][1] for y in ys)/5
    print(f'FY{e-4}-{e} | capex end {a:.1f} ({100*a/cap_m:.2f}%) | D&A end {b:.1f} ({100*b/cap_m:.2f}%)')
allv=[v for y in rows for v in rows[y]]
print('\ncapex/D&A sums: 18y', round(sum(cap.values())/sum(da.values()),2), '10y', round(sum(cap[y] for y in range(2016,2026))/sum(da[y] for y in range(2016,2026)),2), '5y', round(sum(cap[y] for y in range(2021,2026))/sum(da[y] for y in range(2021,2026)),2))
print('check 2018 face 293.590-76 =',293.590-76,' 2019 face 263.427-15 =',263.427-15)
