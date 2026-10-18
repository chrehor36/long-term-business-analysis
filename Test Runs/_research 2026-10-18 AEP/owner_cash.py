"""AEP owner cash by year, typed from the filed consolidated statements of cash flows (USD millions).
Sources: FY2016 10-K 0000004904-17-000019 (2016); FY2019 10-K 0000004904-20-000007 (2017-2019);
FY2022 10-K 0000004904-23-000011 (2020-2022); FY2025 10-K 0000004904-26-000013 (2023-2025).
Interest paid: XBRL InterestPaidNet (supplementary cash flow note). SBC: Note on stock-based compensation
(expensed + capitalized), 2020-2025 only. Run: python -I owner_cash.py"""
Y=list(range(2016,2026))
OCF ={2016:4521.8,2017:4270.4,2018:5223.2,2019:4270.1,2020:3832.9,2021:3839.9,2022:5288.0,2023:5012,2024:6804,2025:6944}
CONS={2016:4781.1,2017:5691.3,2018:6310.9,2019:6051.4,2020:6246.3,2021:5659.6,2022:6671.7,2023:7378,2024:7631,2025:8453}
NUCF={2016:128.5,2017:108.0,2018:46.1,2019:92.3,2020:69.7,2021:104.5,2022:100.7,2023:128,2024:140,2025:130}
# acquisitions of businesses/generation facilities, gross
ACQ ={2016:107.9,2017:0,2018:0,2019:918.4,2020:0,2021:114.4+652.8,2022:1207.3,2023:155,2024:399,2025:3453}
# proceeds from sales of assets/businesses (2017: merchant generation sale; 2024 incl. equity-method sale 114)
SALE={2016:0,2017:2159.6,2018:0,2019:0,2020:71.1,2021:118.9,2022:218.0,2023:1341,2024:362+114,2025:25}
DA  ={2016:1962.3,2017:1997.2,2018:2286.6,2019:2514.5,2020:2682.8,2021:2825.7,2022:3202.8,2023:3090,2024:3290,2025:3380}
DEFUEL={2016:-65.5,2017:84.4,2018:189.7,2019:85.2,2020:-31.8,2021:-1647.9,2022:-319.2,2023:893,2024:277,2025:133}
SBC ={2020:53.8+20.4,2021:61.1+16.9,2022:63.3+16.0,2023:51+15,2024:53+14,2025:53+17}
FLP ={2016:106.6,2017:67.3,2018:65.1,2019:70.7,2020:61.7,2021:64.0,2022:309.5,2023:68,2024:65,2025:51}
NCID={2023:8,2024:6,2025:108}
INTP={2016:848,2017:858,2018:939,2019:1022,2020:1029,2021:1137,2022:1286,2023:1674,2024:1838,2025:1894}
REV ={2016:16380,2017:15425,2018:16196,2019:15561,2020:14918,2021:16792,2022:19640,2023:18982,2024:19721,2025:21876}
T=0.21  # CONVENTION of the run: interest shield at the federal statutory rate
rows=[]
print("year   OCF  SBC  constr  nucF netAcq  D&A  defFuel | OC_all(eq)  OC_maint(eq)  OC_maint_exfuel(eq) | +int(1-t) => OC_maint(all-equity)  OC_all(all-equity)")
for y in Y:
    sbc=SBC.get(y,float('nan')) if y>=2020 else 0.0
    other=FLP[y]+NCID.get(y,0)
    allsp=OCF[y]-sbc-CONS[y]-NUCF[y]-(ACQ[y]-SALE[y])-other
    maint=OCF[y]-sbc-DA[y]-NUCF[y]-other
    maintx=maint-DEFUEL[y]
    ai=INTP[y]*(1-T)
    rows.append((y,allsp,maint,maintx,ai))
    print(f"{y} {OCF[y]:6.0f} {sbc:4.0f} {CONS[y]:6.0f} {NUCF[y]:4.0f} {ACQ[y]-SALE[y]:6.0f} {DA[y]:5.0f} {DEFUEL[y]:6.0f} | {allsp:8.0f} {maint:10.0f} {maintx:12.0f} | {maint+ai:10.0f} {allsp+ai:10.0f}")
w=[r for r in rows if r[0]>=2021]
avg=lambda i:sum(r[i] for r in w)/len(w)
avgai=sum(r[4] for r in w)/5
print(f"\n5-yr 2021-2025 averages (equity basis): all-spending {avg(1):.0f}; maintenance-only {avg(2):.0f}; maintenance ex deferred fuel {avg(3):.0f}")
print(f"after-tax interest avg {avgai:.0f}; all-equity: maintenance {avg(2)+avgai:.0f}; all-spending {avg(1)+avgai:.0f}")
f=[r[3] for r in rows if 2021<=r[0]<=2025]
print("maintenance ex fuel series 2021-25:",[round(x) for x in f])
h1=sum(f[:2])/2; h2=sum(f[3:])/2
g_half=(h2/h1)**(1/3)-1
g_end=(f[-1]/f[0])**(1/4)-1
print(f"growth end-to-end {g_end*100:.1f}%/yr; between halves (2021-22 avg {h1:.0f} vs 2024-25 avg {h2:.0f}, 3 yrs apart) {g_half*100:.1f}%/yr")
gs=(REV[2025]/REV[2021])**(1/4)-1
print(f"sales growth 2021-2025 {gs*100:.1f}%/yr; 2016-2025 {((REV[2025]/REV[2016])**(1/9)-1)*100:.1f}%/yr")
print("owner cash (maint, eq) / revenue by year:",{r[0]:round(r[2]/REV[r[0]]*100,1) for r in rows})
gsp=[CONS[y]+NUCF[y]+ACQ[y]-SALE[y]-DA[y]-NUCF[y] for y in range(2021,2026)]
print("growth spending (all capital spending less D&A and nuclear fuel), 2021-25:",[round(x) for x in gsp]," avg",round(sum(gsp)/5))
