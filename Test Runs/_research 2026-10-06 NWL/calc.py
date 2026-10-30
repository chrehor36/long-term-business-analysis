# COMPUTATION - NOT A CLEARANCE. Figures USD millions from the 10-K cash flow statements (XBRL, cross-checked 2023-2025 to 0000814453-26-000008).
ocf={2019:1044,2020:1432,2021:884,2022:-272,2023:930,2024:496,2025:264}
sbc={2019:42,2020:41,2021:52,2022:12,2023:50,2024:74,2025:68}
capex={2019:265,2020:259,2021:289,2022:312,2023:284,2024:259,2025:247}
da={2019:446,2020:357,2021:325,2022:296,2023:334,2024:323,2025:311}
tax={2019:156,2020:106,2021:165,2022:172,2023:103,2024:173,2025:137}
intp={2019:304,2020:281,2021:271,2022:244,2023:298,2024:319,2025:354}
sales={2019:9715,2020:9385,2021:10589,2022:9459,2023:8133,2024:7582,2025:7204}
oc={y:ocf[y]-sbc[y]-capex[y] for y in ocf}
ocd={y:ocf[y]-sbc[y]-da[y] for y in ocf}
for y in ocf: print(y,'owner cash (capex)',oc[y],'(D&A)',ocd[y])
def avg(d,ys): return sum(d[y] for y in ys)/len(ys)
W5=range(2021,2026); W7=range(2019,2026)
r=0.0566; px=5.48; sh=425.9; netdebt=4673-203
for name,W in (('5yr',W5),('7yr whole-cycle',W7)):
    a=avg(oc,W); ad=avg(ocd,W); t=avg(tax,W); i=avg(intp,W)
    pre_eq=a+t; pre_ev=a+t+i
    print(f'\n{name}: owner cash {a:.1f} (D&A basis {ad:.1f}); cash tax {t:.1f}; cash interest {i:.1f}')
    print(f'  no-growth value equity {a/r:.0f} = ${a/r/sh:.2f}/sh')
    g=(sales[2025]/sales[2021])**(1/4)-1
    pv=sum(a*(1+g)**k/(1+r)**k for k in range(1,11)); term=a*(1+g)**10/r/(1+r)**10
    print(f'  shown-growth case (sales CAGR 2021-25 {g:.2%}) equity {pv+term:.0f} = ${(pv+term)/sh:.2f}/sh')
    print(f'  pre-tax yield on equity at ${px}: {pre_eq/(px*sh):.2%}; pre-tax pre-interest yield on EV: {pre_ev/(px*sh+netdebt):.2%}')
    print(f'  fair (10% pre-tax) equity basis ${pre_eq/0.10/sh:.2f}; EV basis ${(pre_ev/0.10-netdebt)/sh:.2f}')
    print(f'  cheap (20% pre-tax) equity basis ${pre_eq/0.20/sh:.2f}; EV basis ${(pre_ev/0.20-netdebt)/sh:.2f}')
print('\nmarket cap',px*sh,'EV',px*sh+netdebt)
