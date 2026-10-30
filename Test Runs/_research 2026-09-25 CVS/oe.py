# Owner earnings, CVS, built by hand from the filed cash-flow statements (10-K FY2017 EX13, FY2019, FY2022, FY2025)
# OE = OCF - SBC - growth in health-care-costs-payable (float, stripped per the UNH precedent / [E2-61]) - (c)
# (c) low end = depreciation = D&A less amortization of acquired intangibles ([E3-44] default is the depreciation charge)
# (c) high end = total capex (purchases of property and equipment)
Y=list(range(2015,2026))
OCF=[8539,10141,8007,8865,12848,15865,18265,16177,13426,9107,10639]
SBC=[230,222,234,280,453,400,484,447,588,540,535]
FLT=[0,0,0,-311,320,-231,169,1247,394,2757,16]
DA=[2092,2475,2479,2718,4371,4441,4512,4247,4366,4597,4606]
AM=[611,795,817,1006,2436,2341,2259,1808,1905,2025,1976]
CPX=[2367,2224,1918,2037,2457,2437,2520,2727,3031,2781,2832]
rows=[]
for i,y in enumerate(Y):
    dep=DA[i]-AM[i]
    base=OCF[i]-SBC[i]-FLT[i]
    rows.append((y,OCF[i],SBC[i],FLT[i],dep,CPX[i],base-dep,base-CPX[i]))
print('| year | OCF | SBC | float growth stripped | depreciation (D&A - intangible amort.) | capex | OE, (c)=depreciation | OE, (c)=capex |')
print('|---|---|---|---|---|---|---|---|')
for r in rows: print('| %d | %s |'%(r[0],' | '.join(f'{x:,}' for x in r[1:])))
def win(a,b):
    sel=[r for r in rows if a<=r[0]<=b]; n=len(sel)
    return sum(r[6] for r in sel)/n, sum(r[7] for r in sel)/n
print()
for a,b,lab in [(2023,2025,'3y 2023-25'),(2021,2025,'5y 2021-25'),(2019,2025,'7y 2019-25 (post-Aetna perimeter)'),(2016,2025,'10y 2016-25 (crosses the Aetna perimeter)')]:
    d,c=win(a,b); print(f'{lab}: (c)=dep {d:,.0f}  (c)=capex {c:,.0f}')
