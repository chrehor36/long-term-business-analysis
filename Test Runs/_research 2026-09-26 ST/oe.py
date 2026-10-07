import json
# $M, from the filed cash-flow statements (cfgrep_out.txt); FY2008-2009 from the FY2010 10-K; OCF FY2008 continuing operations
ocf={2008:61.9,2009:187.6,2010:300.0,2011:305.9,2012:397.3,2013:395.8,2014:382.6,2015:533.1,2016:521.5,2017:557.6,2018:620.6,2019:619.6,2020:559.8,2021:554.2,2022:460.6,2023:456.7,2024:551.5,2025:621.5}
sbc={2008:2.1,2009:2.2,2010:25.4,2011:8.0,2012:14.7,2013:9.0,2014:13.0,2015:15.3,2016:17.4,2017:19.8,2018:23.8,2019:18.8,2020:19.1,2021:25.7,2022:31.8,2023:30.0,2024:38.5,2025:25.0}
capex={2008:41.0,2009:15.0,2010:52.9,2011:89.8,2012:54.8,2013:82.8,2014:144.2,2015:177.2,2016:130.2,2017:144.6,2018:159.8,2019:161.3,2020:106.7,2021:144.4,2022:150.1,2023:184.6,2024:158.6,2025:131.2}
dep={2008:51.4,2009:48.4,2010:38.6,2011:44.4,2012:54.7,2013:50.9,2014:65.8,2015:96.1,2016:106.9,2017:109.3,2018:106.0,2019:115.9,2020:125.7,2021:125.0,2022:127.2,2023:133.1,2024:167.1,2025:176.2}
# finance/capital lease principal: separately filed FY2008-2010 (cash-flow line) and FY2019-2025 (tag FinanceLeasePrincipalPayments); FY2011-2018 inside "Payments on debt", not separately filed
fl={2008:1.2,2009:4.2,2010:4.6,2019:1.9,2020:0.9,2021:1.8,2022:2.4,2023:1.5,2024:1.9,2025:2.2}
cap_m=6140.16; sov=5.49
rows={}
for y in range(2008,2026):
    f=fl.get(y,0.0)
    a=ocf[y]-sbc[y]-capex[y]-f
    b=ocf[y]-sbc[y]-dep[y]-f
    rows[y]=(a,b)
out=[]
out.append('FY | OCF | SBC | capex | dep | fin lease | OE capex end | OE dep end')
for y in range(2008,2026):
    out.append(f'{y} | {ocf[y]:.1f} | {sbc[y]:.1f} | {capex[y]:.1f} | {dep[y]:.1f} | {fl.get(y,0):.1f} | {rows[y][0]:.1f} | {rows[y][1]:.1f}')
# TTM to 2026-06-30: FY2025 + H1 2026 - H1 2025 (10-Q)
t_ocf=621.5+332.5-260.1; t_sbc=25.0+14.0-11.4; t_cap=131.2+41.5-58.0; t_dep=176.2+67.6-74.3
out.append(f'TTM | {t_ocf:.1f} | {t_sbc:.1f} | {t_cap:.1f} | {t_dep:.1f} | ~2.2 | {t_ocf-t_sbc-t_cap-2.2:.1f} | {t_ocf-t_sbc-t_dep-2.2:.1f}')
out.append('')
out.append('window | capex end | dep end | yield capex | yield dep | capex/dep')
allv=[]
for n in range(3,19):
    ys=list(range(2026-n,2026))
    a=sum(rows[y][0] for y in ys)/n; b=sum(rows[y][1] for y in ys)/n
    r=sum(capex[y] for y in ys)/sum(dep[y] for y in ys)
    allv+= [a,b]
    out.append(f'{n}y FY{ys[0]}-{ys[-1]} | {a:.1f} | {b:.1f} | {a/cap_m*100:.2f}% | {b/cap_m*100:.2f}% | {r:.2f}')
out.append(f'RANGE {min(allv):.1f} to {max(allv):.1f} ; {min(allv)/cap_m*100:.2f}% to {max(allv)/cap_m*100:.2f}%')
open('oe_out.txt','w').write('\n'.join(out)); print('\n'.join(out))
json.dump({'rows':rows},open('oe_series.json','w'))
