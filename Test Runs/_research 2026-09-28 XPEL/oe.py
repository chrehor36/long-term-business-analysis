# Owner earnings [E2-23], OCF construction (framework CONVENTION): OCF - SBC - (c). $M, filed cash-flow statements
Y=list(range(2017,2026))
ocf={2017:3.02,2018:6.80,2019:10.97,2020:18.47,2021:18.27,2022:12.06,2023:37.38,2024:47.82,2025:66.94}
sbc={2017:0,2018:0,2019:0,2020:0,2021:0.17,2022:0.52,2023:1.64,2024:3.20,2025:2.75}
cap={2017:1.50,2018:2.03,2019:1.57,2020:1.78,2021:6.73,2022:7.94,2023:6.36,2024:6.71,2025:4.01}
dev={2017:0.21,2018:0.39,2019:0.67,2020:0.37,2021:0.96,2022:1.62,2023:1.29,2024:1.88,2025:1.55}
dep={2017:0.59,2018:0.74,2019:0.92,2020:1.27,2021:1.89,2022:3.43,2023:4.53,2024:5.82,2025:6.26}
amo={2017:0.54,2018:0.64,2019:0.78,2020:0.96,2021:2.50,2022:4.40,2023:5.06,2024:5.88,2025:6.99}
inv={2017:-2.55,2018:0.01,2019:-4.25,2020:-6.76,2021:-26.94,2022:-28.57,2023:-24.84,2024:-4.79,2025:11.48}
acq={2017:0.66,2018:0.83,2019:0.13,2020:2.57,2021:49.18,2022:4.67,2023:18.74,2024:9.86,2025:26.17}
buy={2025:3.00}
cap_end={y:ocf[y]-sbc[y]-cap[y]-dev[y] for y in Y}
da_end ={y:ocf[y]-sbc[y]-dep[y]-amo[y] for y in Y}
CAP=1198.8; SOV=5.49
print('FY | OCF | SBC | capex | dev.intang | dep | amort | inventory line | OE capex end | OE D&A end | acquisitions')
for y in Y: print(y,'|',ocf[y],'|',sbc[y],'|',cap[y],'|',dev[y],'|',dep[y],'|',amo[y],'|',inv[y],'|',round(cap_end[y],2),'|',round(da_end[y],2),'|',acq[y])
def m(d,ys): return sum(d[y] for y in ys)/len(ys)
print('\nwindow | capex end (yield) | D&A end (yield)')
for n in (1,3,5,7,9):
    ys=Y[-n:]
    a,b=m(cap_end,ys),m(da_end,ys)
    print(f'{n}y FY{ys[0]}-{ys[-1]} | ${a:.1f}M ({a/CAP*100:.2f}%) | ${b:.1f}M ({b/CAP*100:.2f}%)')
# TTM to 2026-06-30
t_ocf=66.94+38.17-31.12; t_sbc=2.75+2.22-1.70; t_cap=4.01+74.82-1.95; t_dev=1.55+0.88-0.79; t_dep=6.26+3.40-3.09; t_amo=6.99+4.22-3.06
bld=60.4
print(f'\nTTM OCF {t_ocf:.2f} SBC {t_sbc:.2f} capex {t_cap:.2f} dev {t_dev:.2f} dep {t_dep:.2f} amort {t_amo:.2f}')
a=t_ocf-t_sbc-t_cap-t_dev; a2=a+bld; b=t_ocf-t_sbc-t_dep-t_amo
print(f'TTM capex end as filed ${a:.1f}M ({a/CAP*100:.2f}%); ex the $60.4M San Antonio buildings ${a2:.1f}M ({a2/CAP*100:.2f}%); D&A end ${b:.1f}M ({b/CAP*100:.2f}%)')
# growth-adjusted display: add back the inventory build (a disclosed guess that the build was growth, not maintenance)
print('\ninventory build added back (display only, a disclosed guess):')
for n in (3,5,9):
    ys=Y[-n:]
    a=m({y:cap_end[y]-inv[y] for y in Y},ys); b=m({y:da_end[y]-inv[y] for y in Y},ys)
    print(f'{n}y: capex end ${a:.1f}M ({a/CAP*100:.2f}%), D&A end ${b:.1f}M ({b/CAP*100:.2f}%)')
print('\nsum acquisitions FY2017-25', round(sum(acq.values()),2), 'FY2021-25', round(sum(acq[y] for y in range(2021,2026)),2))
print('sum OE capex end FY2017-25', round(sum(cap_end.values()),2), 'FY2021-25', round(sum(cap_end[y] for y in range(2021,2026)),2))
print('SBC/OCF 2025', round(2.75/66.94*100,1))
