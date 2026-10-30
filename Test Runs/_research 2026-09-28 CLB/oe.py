# owner earnings = OCF - SBC (in full) - (c); (c) at two ends: operations capex, D&A. Both CIKs, latest filed vintage. No net-income proxy.
import json, statistics as S
from datetime import date
F=[json.load(open(f'cache/facts_{k}.json'))['facts']['us-gaap'] for k in ('nv','new')]
def dur(t):
    o={}
    for f in F:   # nv first, then new: the newer registrant's vintage wins where both exist
        if t not in f: continue
        for u,a in f[t]['units'].items():
            for x in sorted(a, key=lambda z: z.get('filed','')):
                if x.get('form') in ('10-K','10-K/A') and 'start' in x and 350<=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<=380:
                    o[int(x['end'][:4])]=x['val']/1e6
    return o
ocf=dur('NetCashProvidedByUsedInOperatingActivities'); sbc=dur('ShareBasedCompensation')
cap=dur('PaymentsToAcquirePropertyPlantAndEquipment'); da=dur('DepreciationDepletionAndAmortization')
CAP=476.740; SOV=5.49
Y=list(range(2008,2026))
oe_c={y: ocf[y]-sbc[y]-cap[y] for y in Y}; oe_d={y: ocf[y]-sbc[y]-da[y] for y in Y}
print('FY | OCF | SBC | capex (operations) | D&A | OE capex end | OE D&A end')
for y in Y: print(f'{y} | {ocf[y]:.1f} | {sbc[y]:.1f} | {cap[y]:.1f} | {da[y]:.1f} | {oe_c[y]:.1f} | {oe_d[y]:.1f}')
# TTM to 2026-06-30 from the 10-Q (six months 2026 and 2025, $000 as filed)
t_ocf=37.031+11.774-20.583; t_sbc=7.137+5.934-4.697; t_cap=11.209+8.135-6.259; t_da=14.649+7.589-7.387
print(f'TTM | {t_ocf:.1f} | {t_sbc:.1f} | {t_cap:.1f} | {t_da:.1f} | {t_ocf-t_sbc-t_cap:.1f} | {t_ocf-t_sbc-t_da:.1f}')
print('capex/D&A sums: 18y %.2f, 10y %.2f, 5y %.2f' % tuple(sum(cap[y] for y in Y[-n:])/sum(da[y] for y in Y[-n:]) for n in (18,10,5)))
print('\nTRAILING WINDOWS ending FY2025, cap $%.1fM, sovereign %.2f%%' % (CAP,SOV))
lo=[];hi=[]
for n in range(1,19):
    w=Y[-n:]; c=S.mean(oe_c[y] for y in w); d=S.mean(oe_d[y] for y in w)
    lo.append(min(c,d)); hi.append(max(c,d))
    print(f'{n:2d}y FY{w[0]}-{w[-1]} | capex end {c:.1f} ({100*c/CAP:.2f}%) | D&A end {d:.1f} ({100*d/CAP:.2f}%)')
print('range all trailing windows: %.1f to %.1f (%.2f%% to %.2f%%)' % (min(lo),max(hi),100*min(lo)/CAP,100*max(hi)/CAP))
print('\nROLLING FIVE-YEAR WINDOWS')
R=[]
for s in range(2008,2022):
    w=list(range(s,s+5)); c=S.mean(oe_c[y] for y in w); d=S.mean(oe_d[y] for y in w); R+= [c,d]
    print(f'FY{s}-{s+4} | capex end {c:.1f} ({100*c/CAP:.2f}%) | D&A end {d:.1f} ({100*d/CAP:.2f}%)')
print('rolling five-year range %.1f to %.1f (%.2f%% to %.2f%%)' % (min(R),max(R),100*min(R)/CAP,100*max(R)/CAP))
# largest single-year share in the 3y and 5y capex-end sums
for n in (3,5):
    w=Y[-n:]; tot=sum(oe_c[y] for y in w); mx=max(w,key=lambda y: oe_c[y]); print(f'{n}y capex-end sum {tot:.1f}; largest year FY{mx} {oe_c[mx]:.1f} = {100*oe_c[mx]/tot:.1f}%')
