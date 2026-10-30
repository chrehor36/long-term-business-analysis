# NCTKF (Nabtesco, TSE 6268) arithmetic for the 2026-10-16 run. JPY millions unless stated.
# Every input is transcribed from the filed statements named in the run file (Step 0 and Q4 tables).
Y=list(range(2016,2026))
CFO ={2016:27730,2017:23071,2018:24165,2019:38433,2020:34203,2021:36340,2022:7717,2023:11177,2024:26650,2025:32824}
PPE ={2016:14474,2017:11375,2018:20650,2019:13743,2020:17148,2021:7738,2022:8809,2023:22578,2024:24898,2025:13201}
INT ={2016:920,2017:818,2018:840,2019:1020,2020:1549,2021:1561,2022:2559,2023:3021,2024:3453,2025:2814}
LEASE={2016:0,2017:0,2018:0,2019:2477,2020:2547,2021:2522,2022:2854,2023:3060,2024:3424,2025:3669}
NCI ={2016:14,2017:264,2018:340,2019:674,2020:1215,2021:2928,2022:3101,2023:1563,2024:1249,2025:2610}
ACQ ={2016:778,2017:8203,2018:0,2019:0,2020:0,2021:746,2022:0,2023:11619-1686,2024:0,2025:0}
DA  ={2016:7422,2017:8974,2018:10011,2019:13093,2020:13730,2021:13266,2022:14483,2023:15469,2024:16469,2025:17258}
INTPAID={2016:106,2017:171,2018:112,2019:256,2020:190,2021:165,2022:194,2023:574,2024:736,2025:847}
TAXPAID={2016:4169,2017:9786,2018:7335,2019:7767,2020:7106,2021:12204,2022:23216,2023:16093,2024:6468,2025:5203}
SALES={2016:244968,2017:282422,2018:294626,2019:289808,2020:279358,2021:299641,2022:309123,2023:333367,2024:323384,2025:307912}
OI  ={2016:25982,2017:29468,2018:21889,2019:25320,2020:28533,2021:29669,2022:18654,2023:16660,2024:15012,2025:20956}
NI  ={2016:18606,2017:25146,2018:21029,2019:17931,2020:20505,2021:64771,2022:10415,2023:14226,2024:10188,2025:15255}
EQ  ={2015:138271,2016:147929,2017:167537,2018:178702,2019:187398,2020:198031,2021:241372,2022:251250,2023:262721,2024:272559,2025:273466}
TAXRATE=0.306  # statutory tax rate stated in the FY2025 ASR tax note (30.6%)
oc={y:CFO[y]-PPE[y]-INT[y]-LEASE[y]-NCI[y]-ACQ[y] for y in Y}
mc={y:DA[y]-LEASE[y] for y in Y}   # maintenance capex guess: D&A less right-of-use depreciation, the latter taken = lease principal
om={y:CFO[y]-mc[y]-LEASE[y]-NCI[y] for y in Y}
print("year  CFO  capex(ppe+int)  lease  NCIdiv  acq  OWNERCASH_all  maint_capex  OWNERCASH_maint  OI  OI/sales  ROE")
for y in Y:
    roe=NI[y]/((EQ[y]+EQ[y-1])/2)
    print(y,CFO[y],PPE[y]+INT[y],LEASE[y],NCI[y],ACQ[y],oc[y],mc[y],om[y],OI[y],f"{OI[y]/SALES[y]:.1%}",f"{roe:.1%}")
def avg(d,ys): return sum(d[y] for y in ys)/len(ys)
w5=range(2021,2026); h1=range(2016,2021)
print("owner cash all-spending: ten-year avg",round(avg(oc,Y)),"| literal window 2021-25",round(avg(oc,w5)),"| first half 2016-20",round(avg(oc,h1)))
print("owner cash maintenance:  ten-year avg",round(avg(om,Y)),"| literal window 2021-25",round(avg(om,w5)),"| first half 2016-20",round(avg(om,h1)))
print("acquisitions ten-year",sum(ACQ.values()),"owner cash before purchases ten-year",sum(oc[y]+ACQ[y] for y in Y))
ia=avg(INTPAID,Y)*(1-TAXRATE); print("interest paid after tax, ten-year avg",round(ia))
r=0.0402; floor=0.10
shares=118064699-417022-1861100   # issued less treasury (Jun 30 2026) less buyback Aug-Sep 2026
netcash=99583+3843-43427-8578-4824  # cash + current other financial assets - borrowings - buyback Aug-Sep - interim dividend Aug 31
price=4488
print("shares",shares,"net cash",netcash,"market cap",round(price*shares/1e6))
top_ae=(avg(om,Y)+ia); bot_ae=(avg(oc,Y)+ia)
def ps(v): return v*1e6/shares
print(f"ALL-EQUITY range at {r:.2%}: bottom {ps(bot_ae/r+netcash):.0f} top {ps(top_ae/r+netcash):.0f}  width {(top_ae/r+netcash)/(bot_ae/r+netcash):.2f}x")
print(f"EQUITY-ONLY range at {r:.2%}: bottom {ps(avg(oc,Y)/r):.0f} top {ps(avg(om,Y)/r):.0f}")
ev=price*shares/1e6-netcash
print(f"yield at price on all-equity: top case {top_ae/ev:.2%} bottom case {bot_ae/ev:.2%} (floor 10%)")
fair_ae=(ps(top_ae/floor+netcash)+ps(bot_ae/floor+netcash))/2
fair_eq=(ps(avg(om,Y)/floor)+ps(avg(oc,Y)/floor))/2
print(f"FAIR (all-equity) {fair_ae:.0f}  ends {ps(top_ae/floor+netcash):.0f} / {ps(bot_ae/floor+netcash):.0f} ; FAIR (equity-only) {fair_eq:.0f}")
# variant: HDS-related tax added back (disclosed guess)
hds=(125107-56958)+(-10488+4872)+3485; hdstax=hds*TAXRATE  # 2021 valuation gain less the 56,958 valuation loss in the FY2021 cash flow statement; 2022 net; 2023 gain
print("HDS net gains",hds,"tax guess",round(hdstax),"per year over ten",round(hdstax/10))
print(f"variant top (maint + HDS tax back) {ps((top_ae+hdstax/10)/r+netcash):.0f}; variant bottom {ps((bot_ae+hdstax/10)/r+netcash):.0f}")
# capital: equity and segment
print("equity 2016->2025",EQ[2016],EQ[2025],"OI 2016->2025",OI[2016],OI[2025])
