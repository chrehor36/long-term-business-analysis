# Owner earnings, COMPUTATION - NOT A CLEARANCE. $M. Sources: filed cash-flow statements (cfs_*.txt), the selected-data
# "Net capital expenditures, including assets acquired through notes payable and capital/finance leases" line (netcapex.py) for 2006-2020,
# and for 2021-2025 cash capex "net of financings" + "Equipment financed" (noncash) - "Proceeds from sale of property and equipment".
# OCF: latest filed vintage (companyfacts where tagged, else the filed statement). SBC: filed add-back. D: "Depreciation and amortization"
# (excludes amortization of acquired intangibles from 2012). SW: capitalization of internally developed software (a capital outlay).
import sys
sys.stdout.reconfigure(encoding='utf-8')
cap=2797.5
#      OCF    SBC   D      netcapex SW    acq(+paid/-received)
T={2006:(168.5,4.7,67.7,135.6,4.1,0),2007:(143.1,4.9,77.3,86.1,4.6,0),2008:(105.3,6.1,76.9,42.0,5.3,0),
2009:(11.8,6.2,75.2,43.7,5.2,4.9),2010:(26.3,5.7,71.6,41.9,4.4,0),2011:(100.9,6.5,73.7,76.6,5.3,4.1),
2012:(84.5,6.1,85.5,68.9,7.2,180.0),2013:(93.5,5.5,84.2,24.2,7.7,4.1),2014:(143.8,7.0,81.9,85.9,8.4,2.6),
2015:(149.1,8.0,89.0,152.4,8.5,29.8),2016:(111.9,7.6,98.8,142.8,10.5,24.8),2017:(151.9,7.0,98.5,145.7,9.8,0),
2018:(255.3,8.4,104.1,133.8,10.1,0),2019:(170.4,9.5,108.1,147.2,11.5,0),2020:(206.0,10.5,114.4,91.7,14.2,0),
2021:(323.5,11.4,118.9,104.3,20.1,239.4),2022:(470.8,12.8,127.1,211.0,17.3,-2.3),2023:(322.2,11.4,132.9,244.8,13.0,0),
2024:(285.8,11.4,136.3,288.4,16.9,0),2025:(229.0,10.6,157.5,198.2,13.4,0)}
print('year  OCF  SBC  dep  netcapex+SW  OE_capex  OE_dep  acq')
for y in sorted(T):
    o,s,d,c,w,a=T[y]
    print(y,o,s,d,round(c+w,1),round(o-s-c-w,1),round(o-s-d,1),a)
print()
def win(n,end=2025):
    ys=[y for y in range(end-n+1,end+1)]
    ce=sum(T[y][0]-T[y][1]-T[y][3]-T[y][4] for y in ys)/n
    de=sum(T[y][0]-T[y][1]-T[y][2] for y in ys)/n
    aq=sum(T[y][5] for y in ys)/n
    return ce,de,aq
for n in (1,3,5,10,15,20):
    ce,de,aq=win(n)
    print('%2dy %d-2025: capex end %.1f (%.2f%%)  dep end %.1f (%.2f%%)  after acquisitions (capex end) %.1f'%(n,2026-n,ce,100*ce/cap,de,100*de/cap,ce-aq))
# capex vs depreciation
print('years capex(+SW) > dep:',[y for y in T if T[y][3]+T[y][4]>T[y][2]])
