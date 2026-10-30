# Owner cash by year (USD millions), from the filed cash-flow statements.
# 2014-2016: 10-K FY2016 0000085961-17-000013 (OCF there excludes collections on direct finance leases, which sat in investing;
#            they are added back here so the series matches the later presentation, where collections on sales-type leases are in OCF).
# 2017-2019: 10-K FY2019 0000085961-20-000089 (restated for ASC 842). 2020-2022: 10-K FY2022 0000085961-23-000031. 2023-2025: 10-K FY2025 0000085961-26-000007.
# SBC: us-gaap AllocatedShareBasedCompensationExpense (latest filed).
Y=list(range(2014,2026))
OCF ={2014:1382.8,2015:1441.8,2016:1601.0,2017:1628.1,2018:1718.0,2019:2140.5,2020:2181,2021:2175,2022:2310,2023:2353,2024:2265,2025:2594}
LEASECOLL={2014:64.3,2015:71.0,2016:76.5}
SBC ={2014:20.9,2015:21.2,2016:18.7,2017:19.0,2018:25.0,2019:25.8,2020:30,2021:47,2022:46,2023:44,2024:42,2025:39}
PREE={2014:493.5,2015:423.6,2016:414.2,2017:376.7,2018:379.7,2019:465.7,2020:539,2021:748,2022:1182,2023:764,2024:532,2025:468}
POPE={2014:3.5,2015:3.9,2016:7.1,2017:52.3,2018:16.6,2019:52.3,2020:13,2021:74,2022:53,2023:63,2024:19,2025:18}
CAPX={2014:2259.2,2015:2668.0,2016:1905.2,2017:1860.4,2018:3050.4,2019:3735.2,2020:1146,2021:1941,2022:2631,2023:3234,2024:2683,2025:2135}
ACQ ={2014:10.0,2015:0,2016:0,2017:7.2,2018:167.4,2019:0,2020:0,2021:325,2022:458,2023:250,2024:314,2025:1}
DEP ={2014:1047.0,2015:1122.0,2016:1187.1,2017:1257.7,2018:1388.6,2019:1878.9,2020:2027,2021:1786,2022:1713,2023:1712,2024:1694,2025:1703}
UVS ={2014:-116.1,2015:-99.9,2016:-1.0,2017:17.0,2018:22.3,2019:58.7,2020:0,2021:-257,2022:-450,2023:-196,2024:-72,2025:-22}  # OCF adjustment line; negative = gain
INT ={2014:144.7,2015:150.4,2016:147.8,2017:141.9,2018:180.5,2019:241.4,2020:261,2021:214,2022:228,2023:296,2024:386,2025:404}
REV ={2014:6638.8,2015:6571.9,2016:6758.1,2017:7280.1,2018:8413.9,2019:8925.8,2020:8420,2021:9663,2022:12011,2023:11783,2024:12636,2025:12665}
TAX=0.25  # CONVENTION of this run: interest added back after tax at 25% (the comparable tax rate 2023-2025 was 26.1%, 25.7%, 26.0%)
oc={};od={};ocA={};odA={}
print("year | OCF | SBC | sale proceeds | purchases | owner cash (all spending) | acquisitions | after acq | dep | UVS gain | owner cash (dep basis) | int after tax | all-equity (all spending) | all-equity (dep basis)")
for y in Y:
    o=OCF[y]+LEASECOLL.get(y,0)
    oc[y]=o-SBC[y]+PREE[y]+POPE[y]-CAPX[y]
    od[y]=o-SBC[y]-DEP[y]-UVS[y]
    ia=INT[y]*(1-TAX)
    ocA[y]=oc[y]+ia; odA[y]=od[y]+ia
    print(f"{y} | {o:.0f} | {SBC[y]:.0f} | {PREE[y]+POPE[y]:.0f} | {CAPX[y]:.0f} | {oc[y]:.0f} | {ACQ[y]:.0f} | {oc[y]-ACQ[y]:.0f} | {DEP[y]:.0f} | {-UVS[y]:.0f} | {od[y]:.0f} | {ia:.0f} | {ocA[y]:.0f} | {odA[y]:.0f}")
def avg(d,ys): return sum(d[y] for y in ys)/len(ys)
for name,ys in [("2021-2025 (literal window)",range(2021,2026)),("2016-2025 (ten years)",range(2016,2026)),("2014-2025 (twelve years)",range(2014,2026)),("2016-2020",range(2016,2021))]:
    print(f"{name}: owner cash all-spending {avg(oc,ys):.0f}; after acquisitions {avg({y:oc[y]-ACQ[y] for y in Y},ys):.0f}; dep basis {avg(od,ys):.0f}; all-equity all-spending {avg(ocA,ys):.0f}; all-equity after acq {avg({y:ocA[y]-ACQ[y] for y in Y},ys):.0f}; all-equity dep basis {avg(odA,ys):.0f}; dep basis after acq all-equity {avg({y:odA[y]-ACQ[y] for y in Y},ys):.0f}")
