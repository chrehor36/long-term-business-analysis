# Owner earnings, PPG, every input typed from the filed Consolidated Statement of Cash Flows and Income ($M),
# the latest 10-K that shows each year (continuing operations where the statement splits them).
# cols: source, OCF, SBC (CF line), NCI share of continuing income, capex, CF D&A, IS "Depreciation" line,
#       acquisitions paid, disposal proceeds, named cash one-offs inside OCF (shown, not removed)
D={
2012:('FY2014',1410,71,17,330,399,292,122,0,''),
2013:('FY2014',1562,81,23,494,452,333,983,940,''),
2014:('FY2016',1718,71,24,564,450,324,2113,1625,''),
2015:('FY2016',1735,54,21,454,471,339,320,47,'pension contributions $273M'),
2016:('FY2016',1241,39,22,402,462,341,349,1094,'asbestos settlement funding $813M; pension contributions $204M'),
2017:('FY2019',1551,35,21,360,460,331,225,593,''),
2018:('FY2019',1487,37,17,411,497,354,378,0,''),
2019:('FY2019',2084,39,26,413,511,375,643,0,''),
2020:('FY2022',2130,44,15,304,509,371,1169,0,'total OCF; includes the US and Canada stores'),
2021:('FY2022',1562,57,21,371,561,389,2137,47,'total OCF; includes the US and Canada stores'),
2022:('FY2024',1000,34,28,486,502,357,114,117,''),
2023:('FY2025',2294,56,39,516,514,360,109,36,''),
2024:('FY2025',1391,42,33,721,492,360,31,831,''),
2025:('FY2025',1936,46,16,778,528,403,1,43,''),
}
CAP=107.52*222.3  # $M
res={}
print('| FY | 10-K | OCF | SBC | NCI | capex | depreciation (IS line; D&A less acquired amortization) | CF D&A | **OE, c = capex** | **OE, c = depreciation** | acquisitions paid | disposals received | noted inside OCF |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for y,(s,ocf,sbc,nci,capex,da,dep,acq,dis,note) in D.items():
    base=ocf-sbc-nci
    lo=base-max(capex,dep); hi=base-min(capex,dep)
    res[y]=(lo,hi,acq,dis)
    print(f'| {y} | {s} | {ocf:,} | {sbc} | {nci} | {capex} | {dep} | {da} | **{lo:,}** | **{hi:,}** | {acq:,} | {dis:,} | {note} |')
print()
print(f'Cap ${CAP:,.1f}M')
print('| window | years | OE mean, c = capex | OE mean, c = depreciation | yield on cap | acquisitions paid a year | disposals a year |')
print('|---|---|---|---|---|---|---|')
W=[('3y',2023,2025),('4y, clean perimeter (US stores out)',2022,2025),('5y, the default [E2-42]',2021,2025),('6y',2020,2025),('7y',2019,2025),('8y',2018,2025),('9y (pure coatings since glass left)',2017,2025),('10y',2016,2025),('11y',2015,2025),('12y',2014,2025),('13y',2013,2025),('14y, every filed year read',2012,2025),('5y 2016-2020',2016,2020),('5y 2012-2016',2012,2016)]
for n,a,b in W:
    ys=range(a,b+1); k=len(ys)
    lo=sum(res[y][0] for y in ys)/k; hi=sum(res[y][1] for y in ys)/k
    aq=sum(res[y][2] for y in ys)/k; dv=sum(res[y][3] for y in ys)/k
    print(f'| {n} | {a}-{b} | ${lo:,.0f}M | ${hi:,.0f}M | {lo/CAP*100:.2f}%..{hi/CAP*100:.2f}% | ${aq:,.0f}M | ${dv:,.0f}M |')
