# ROKU owner earnings - all filed years, both (c) ends, multiple windows
# All figures in $ thousands, from the filed Consolidated Statements of Cash Flows
# of the 10-Ks named in the run file. Cross-checked to the dollar for FY2023-25.
OCF={2016:-32463,2017:37292,2018:13922,2019:13707,2020:148192,2021:228081,2022:11795,2023:255856,2024:218045,2025:483718}
SBC={2016:8206,2017:10953,2018:37674,2019:85175,2020:134076,2021:187532,2022:359931,2023:370130,2024:384662,2025:354169}
DA ={2016:5302,2017:5336,2018:8389,2019:15669,2020:36206,2021:42621,2022:48651,2023:70447,2024:62714,2025:68904}
CAP={2016:8596,2017:9229,2018:18327,2019:77180,2020:82382,2021:40041,2022:161696,2023:82619,2024:5061,2025:5280}
dDR={2016:19786,2017:29976,2018:10063,2019:-10597,2020:21517,2021:-7224,2022:41402,2023:10841,2024:4039,2025:-4987}
yrs=sorted(OCF)
print("FY   OCF       SBC      SBC/OCF   D&A     capex    OE(c=capex)  OE(c=D&A)   dDefRev  dDR/OCF")
for y in yrs:
    r=SBC[y]/OCF[y]*100 if OCF[y] else float('nan')
    print(f"{y} {OCF[y]:>9,} {SBC[y]:>8,} {r:>8.1f}% {DA[y]:>8,} {CAP[y]:>8,} {OCF[y]-SBC[y]-CAP[y]:>11,} {OCF[y]-SBC[y]-DA[y]:>11,} {dDR[y]:>8,} {dDR[y]/OCF[y]*100 if OCF[y] else 0:>7.1f}%")
print()
def win(a,b,label):
    ys=[y for y in yrs if a<=y<=b]
    n=len(ys)
    o=sum(OCF[y] for y in ys)/n; s=sum(SBC[y] for y in ys)/n
    d=sum(DA[y] for y in ys)/n; c=sum(CAP[y] for y in ys)/n
    print(f"{label:<16} n={n}  meanOCF {o:>10,.0f}  meanSBC {s:>10,.0f}  SBC/OCF {s/o*100 if o else 0:>7.1f}%  OE(c=capex) {o-s-c:>11,.0f}  OE(c=D&A) {o-s-d:>11,.0f}")
for a,b,l in [(2016,2025,'11yr 2016-25'),(2021,2025,'5yr 2021-25'),(2023,2025,'3yr 2023-25'),(2020,2024,'5yr 2020-24'),(2016,2020,'early 2016-20'),(2024,2025,'2yr 2024-25'),(2025,2025,'1yr 2025')]:
    win(a,b,l)
print()
print("cumulative 2016-2025: OCF",f"{sum(OCF.values()):,}","SBC",f"{sum(SBC.values()):,}","ratio",f"{sum(SBC.values())/sum(OCF.values())*100:.1f}%")
print("cumulative 2021-2025: OCF",f"{sum(OCF[y] for y in range(2021,2026)):,}","SBC",f"{sum(SBC[y] for y in range(2021,2026)):,}","ratio",f"{sum(SBC[y] for y in range(2021,2026))/sum(OCF[y] for y in range(2021,2026))*100:.1f}%")
print("cumulative 2023-2025: ratio",f"{sum(SBC[y] for y in range(2023,2026))/sum(OCF[y] for y in range(2023,2026))*100:.1f}%")
print()
print("FY2022 contract-liability flag: dDR 41,402 / OCF 11,795 =",f"{41402/11795*100:.1f}%")
print("FY2022 OCF without the deferred-revenue increment:",f"{11795-41402:,}")
print()
shares=148418969; px=154.93; cap=shares*px/1e6
print(f"shares {shares:,} price {px} cap ${cap:,.0f}M")
print("deal value at FOXA 65.94:",96.00+0.9693*65.94)
