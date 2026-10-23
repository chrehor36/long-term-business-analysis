# Q7 arithmetic for ES, equity-only basis central (regulated utility), all-equity beside. USD millions.
Y=[2021,2022,2023,2024,2025]
OCF={2021:1962.6,2022:2401.3,2023:1646.2,2024:2159.7,2025:4113.6}
SBC={2021:28.2,2022:33.4,2023:27.8,2024:30.0,2025:33.6}
PREF={y:7.5 for y in Y}
CAPEX={2021:3175.1,2022:3441.9,2023:4336.8,2024:4480.5,2025:4158.7}
FLP={2021:4.1,2022:3.9,2023:3.9,2024:5.2,2025:5.7}
DEP={2021:1103.0,2022:1194.2,2023:1305.8,2024:1433.5,2025:1568.6}
LTDI={2021:3230.0,2022:4045.0,2023:5198.3,2024:4501.6,2025:2942.4}
LTDR={2021:1142.5,2022:1175.0,2023:2008.5,2024:1950.0,2025:1400.3}
RRB={y:43.2 for y in Y}
TAXP={2021:121.6,2022:77.9,2023:39.2,2024:-69.6,2025:-48.4}
INTP={2021:568.7,2022:636.2,2023:783.2,2024:1014.4,2025:1182.6}
SALES={2021:9863.1,2022:12289.3,2023:11910.7,2024:11900.8,2025:13547.2}
SH=376.674754  # cover count 2026-07-31
SOV=0.0529; FLOOR=0.10; DS=0.50  # debt share allowed (PSNH 50% equity ratio, 10-K)
# CONVENTION of run: cash tax normalised in 2024-25 to 2021-23 average (offshore-wind loss shelter)
tavg=sum(TAXP[y] for y in (2021,2022,2023))/3
TAXADJ={y:0 for y in Y}; TAXADJ[2024]=-(tavg-TAXP[2024]); TAXADJ[2025]=-(tavg-TAXP[2025])
netLTD={y:LTDI[y]-LTDR[y]-RRB[y] for y in Y}
cap_all=sum(DS*(CAPEX[y]+FLP[y]) for y in Y); raised=sum(netLTD.values())
print(f"net LT debt raised 2021-25 {raised:,.0f}; debt share x all spending {cap_all:,.0f}; credit = {min(raised,cap_all):,.0f}")
rows=[]
for y in Y:
    base=OCF[y]-SBC[y]-PREF[y]+TAXADJ[y]
    allsp=base-(CAPEX[y]+FLP[y])
    M=base-DEP[y]+DS*DEP[y]          # maintenance-only, debt credit on the maintenance spending
    G=(CAPEX[y]+FLP[y]-DEP[y])*(1-DS) # equity-funded growth spending
    allcr=allsp+DS*(CAPEX[y]+FLP[y])
    rows.append((y,base,allsp,allcr,M,G))
    print(f"{y} OCF-SBC-pref+taxadj {base:8.1f} | all-spend {allsp:8.1f} | all-spend+credit {allcr:8.1f} | maint M {M:8.1f} | eq growth spend G {G:8.1f} | taxadj {TAXADJ[y]:6.1f}")
avg=lambda i: sum(r[i] for r in rows)/5
Mavg,Gavg,ALLc,ALL=avg(4),avg(5),avg(3),avg(2)
print(f"5-yr avg: all-spend {ALL:.1f}  all-spend+credit {ALLc:.1f}  M {Mavg:.1f}  G {Gavg:.1f}")
h1=(rows[0][4]+rows[1][4])/2; h2=(rows[3][4]+rows[4][4])/2
gM=(h2/h1)**(1/3)-1
gS=(SALES[2025]/SALES[2021])**(1/4)-1
print(f"M halves {h1:.0f} -> {h2:.0f}: shown growth {gM*100:.1f}%/yr; sales growth 2021-25 {gS*100:.1f}%/yr")
# cap (f): M carried at gM for ten years vs highest share of sales earned
hi=max(r[4]/SALES[r[0]] for r in rows)
need=Mavg*(1+gM)**10/(SALES[2025]*(1+gS)**10)
print(f"highest M/sales in window {hi*100:.1f}%; M at shown growth in yr10 / sales yr10 = {need*100:.1f}%")
g=min(gS,SOV) if need>hi else min(gM,SOV)
print(f"growth carried: {g*100:.2f}% (cut to sales growth, never above the discount rate)")
# adjustments (subsequent events, filed)
AQ_M=44.2+46.8-0.5*46.8   # Aquarion 2025 NI + D&A less debt-funded half of D&A (10-K segment note)
AQ_G=(165.3-46.8)*(1-DS)
ROE_CUT=70.0              # 8-K 2026-03-31: ~$70M after-tax 2026 earnings from the FERC base ROE cut
PROCEEDS=1700.0           # 8-K 2026-07-01: adjusted net equity proceeds ~$1.7B
OSW=409.2                 # 10-Q 2026-06-30 offshore wind contingent liability
REF_LO=62.0               # already recorded
def pv(X0,G0,g,r):
    s=0;
    for t in range(1,11): s+=(X0*(1+g)**t-G0*(1+g)**t)/(1+r)**t
    s+=X0*(1+g)**10/r/(1+r)**10
    return s
def ends(M,G,g,r):
    a=M/r                      # maintenance-only, no growth
    b=pv(M,G,g,r)              # growth case: growth spending charged, growth stops after yr10 with its spending
    return a,b
for label,(M,G) in {'literal window (no adjustments)':(Mavg,Gavg),'central: less Aquarion, less FERC ROE cut':(Mavg-AQ_M-ROE_CUT,Gavg-AQ_G)}.items():
    adj = 0 if label.startswith('literal') else PROCEEDS-OSW
    a,b=ends(M,G,g,SOV); a10,b10=ends(M,G,g,FLOOR)
    ps=lambda v:(v+adj)/SH
    print(f"\n{label}: M {M:.0f} G {G:.0f}; equity add {adj:.0f}")
    print(f"  at sovereign 5.29%: no-growth {ps(a):.2f}  growth {ps(b):.2f}  -> range {min(ps(a),ps(b)):.2f} to {max(ps(a),ps(b)):.2f}")
    print(f"  at 10% floor:       no-growth {ps(a10):.2f}  growth {ps(b10):.2f}  -> fair (avg) {(ps(a10)+ps(b10))/2:.2f}")
    # implied return at price for each case: solve r where value = price
    price=67.84
    for nm,f in (('no-growth',lambda r:(M/r+adj)/SH),('growth',lambda r:(pv(M,G,g,r)+adj)/SH)):
        lo,hi_=0.01,0.5
        for _ in range(100):
            mid=(lo+hi_)/2
            if f(mid)>price: lo=mid
            else: hi_=mid
        print(f"  expected return at ${price} on the {nm} case: {mid*100:.2f}%")
# beside: maintenance guess from the filer's capex categories (distribution basic+aging share applied to all spending)
share=(2493.6+2632.0+2709.6)/(2931.1+3056.4+3157.5)
Mb=sum(r[1]-(1-DS)*share*(CAPEX[r[0]]+FLP[r[0]]) for r in rows)/5 - AQ_M - ROE_CUT
Gb=sum((1-share)*(CAPEX[y]+FLP[y])*(1-DS) for y in Y)/5 - AQ_G
a10,b10=ends(Mb,Gb,g,FLOOR); a,b=ends(Mb,Gb,g,SOV)
print(f"\nbeside, maintenance = filer's basic+aging share {share*100:.1f}% of spending: M {Mb:.0f} G {Gb:.0f}; sovereign {((a+PROCEEDS-OSW)/SH):.2f}/{((b+PROCEEDS-OSW)/SH):.2f}; at 10% {((a10+PROCEEDS-OSW)/SH):.2f}/{((b10+PROCEEDS-OSW)/SH):.2f}")
# beside: FERC refund high end, after tax at 21% federal (CONVENTION of run)
print(f"FERC refund high end less recorded, after 21%: {(968.4-REF_LO)*0.79:.0f}M = ${(968.4-REF_LO)*0.79/SH:.2f}/share")
# all-equity beside: owner cash before interest (interest paid x (1-21%)), against market value + net debt
ND=393.7+2502.6+43.2+26609.0+259.3-1819.3   # 10-Q 2026-06-30
PREFS=155.6
Mae=sum(r[1]-DEP[r[0]] + 0.79*INTP[r[0]] for r in rows)/5 - (44.2+46.8+30.8*0.79) - ROE_CUT
Gae=sum(CAPEX[y]+FLP[y]-DEP[y] for y in Y)/5-(165.3-46.8)
for r in (SOV,FLOOR):
    a,b=ends(Mae,Gae,g,r)
    print(f"all-equity at {r*100:.2f}%: M {Mae:.0f} G {Gae:.0f} no-growth {(a-ND-PREFS-OSW)/SH:.2f} growth {(b-ND-PREFS-OSW)/SH:.2f}  (net debt {ND:,.0f}, pref {PREFS}, OSW {OSW})")
print(f"market cap at 67.84: {67.84*SH:,.0f}M")
print("\n--- growth variants on the central figures (M,G less Aquarion and ROE cut; equity add proceeds less OSW) ---")
M,G=Mavg-AQ_M-ROE_CUT,Gavg-AQ_G; adj=PROCEEDS-OSW
for gg,nm in ((gM,'shown, halves of the window'),(gS,'sales growth 2021-25 (= regulated non-GAAP NI growth 2021-25, 8.3%)'),(SOV,'at the discount rate')):
    a,b=ends(M,G,gg,SOV); a10,b10=ends(M,G,gg,FLOOR)
    lo,hi_=0.01,0.5
    for _ in range(100):
        mid=(lo+hi_)/2
        if (pv(M,G,gg,mid)+adj)/SH>67.84: lo=mid
        else: hi_=mid
    print(f"g {gg*100:.2f}% ({nm}): sovereign no-growth {(a+adj)/SH:.2f} growth {(b+adj)/SH:.2f}; at 10% {(a10+adj)/SH:.2f} / {(b10+adj)/SH:.2f}; fair {((a10+b10)/2+adj)/SH:.2f}; return at price on growth case {mid*100:.2f}%")
print("\n--- (a) cycle to cycle: prior five years 2016-2020 (OCF, SBC, depreciation from XBRL as filed; 10-K FY2020 cross-checked for 2018-20) ---")
OCFp={2016:2208.2,2017:1996.2,2018:1830.5,2019:2009.6,2020:1682.6}
SBCp={2016:23.6,2017:19.7,2018:21.4,2019:27.3,2020:33.9}
DEPp={2016:715.5,2017:773.8,2018:819.9,2019:885.3,2020:981.4}
Mp=sum(OCFp[y]-SBCp[y]-7.5-0.5*DEPp[y] for y in OCFp)/5
gc=(Mavg/Mp)**(1/5)-1
print(f"M 2016-20 avg {Mp:.0f} -> 2021-25 avg {Mavg:.0f}: growth {gc*100:.2f}%/yr (includes the 2017 Aquarion and 2020 EGMA purchases, so it overstates organic growth)")
a,b=ends(M,G,gc,SOV); a10,b10=ends(M,G,gc,FLOOR)
lo,hi_=0.01,0.5
for _ in range(100):
    mid=(lo+hi_)/2
    if (pv(M,G,gc,mid)+adj)/SH>67.84: lo=mid
    else: hi_=mid
print(f"g {gc*100:.2f}%: sovereign no-growth {(a+adj)/SH:.2f} growth {(b+adj)/SH:.2f}; at 10% {(a10+adj)/SH:.2f} / {(b10+adj)/SH:.2f}; fair {((a10+b10)/2+adj)/SH:.2f}; return at price on growth case {mid*100:.2f}%")
print("\n--- all-equity beside at the central growth ---")
for r in (SOV,FLOOR):
    a,b=ends(Mae,Gae,gc,r)
    print(f"all-equity at {r*100:.2f}%: no-growth {(a-ND-PREFS-OSW)/SH:.2f} growth {(b-ND-PREFS-OSW)/SH:.2f}")
a,b=ends(Mae,Gae,gc,FLOOR); print(f"all-equity fair (avg at 10%): {((a+b)/2-ND-PREFS-OSW)/SH:.2f}")
print("\n--- beside grid ---")
def show(label,M,G,gg,adj):
    a,b=ends(M,G,gg,SOV); a10,b10=ends(M,G,gg,FLOOR)
    def irr(f):
        lo,hi_=0.01,0.5
        for _ in range(100):
            mid=(lo+hi_)/2
            if f(mid)>67.84: lo=mid
            else: hi_=mid
        return mid
    r1=irr(lambda r:(M/r+adj)/SH); r2=irr(lambda r:(pv(M,G,gg,r)+adj)/SH)
    print(f"{label}: g {gg*100:.2f}% | sovereign {(a+adj)/SH:.2f} / {(b+adj)/SH:.2f} | 10% {(a10+adj)/SH:.2f} / {(b10+adj)/SH:.2f} | fair {((a10+b10)/2+adj)/SH:.2f} | return at price {r1*100:.2f}% / {r2*100:.2f}%")
show('central (adjusted), cycle growth',M,G,gc,adj)
show('literal window, cycle growth',Mavg,Gavg,gc,0)
show('literal window, halves growth',Mavg,Gavg,gM,0)
show('central, halves growth',M,G,gM,adj)
show('central, sales growth',M,G,gS,adj)
show('filer-category maintenance, cycle growth',Mb,Gb,gc,adj)
show('central less FERC refund high end (after 21%)',M,G,gc,adj-(968.4-62.0)*0.79)
# issuance prices
print("issuance prices: 2024", 989.447/15.740294, "2025", 465.389/7.130134, "Q2 2026", 20.2/0.289044)
