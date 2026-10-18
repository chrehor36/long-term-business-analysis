"""SCHYY (Sands China Ltd., HKEX 1928) arithmetic for the run of 2026-10-14.
Every input is typed by hand from the filed statements (the run tools refuse a non-SEC filer).
Sources per line: AR = annual report on HKEXnews; 20-F XBRL = SEC companyfacts CIK 1755281.
US$ millions. Arithmetic only; no verdict.
"""
# year: CFO, capex (PP&E + investment property + intangibles), disposal proceeds,
#       lease repayments, gaming-licence + franchise liability payments, SBC, operating profit
D = {
 2016: (2346, 1151, 1,  4,  0, 15, 1352),   # 20-F XBRL / AR2016 (finance lease payments)
 2017: (2626,  477, 13, 5,  0, 12, 1773),   # 20-F XBRL
 2018: (3049,  532, 5, 15,  0, 13, 2154),   # 20-F XBRL
 2019: (2812,  754, 1, 13,  0, 14, 2275),   # AR2020 cash flow statement p.122; 20-F XBRL
 2020: (-816, 1038, 1, 11,  0, 15, -1239),  # AR2020 cash flow statement p.122
 2021: (  88,  640, 3, 12,  0, 10, -537),   # 20-F XBRL (FY2022 20-F, acc 0001755281-23-000018)
 2022: (-473,  241, 9,  9,  0, 35, -1163),  # 20-F XBRL (FY2022 20-F)
 2023: (2293,  231, 1,  7, 29,  5, 1225),   # AR2024 cash flow statement, changes in equity
 2024: (2072,  871, 0, 13, 32,  9, 1366),   # AR2025 cash flow statement p.108
 2025: (2105,  553, 0, 23, 35,  9, 1231),   # AR2025 cash flow statement p.108 (licence 33 + franchise 2)
}
REV = {2012:6511,2013:8908,2014:9505,2015:6820,2016:6653,2017:7586,2018:8665,2019:8808,2020:1687,
       2021:2874,2022:1605,2023:6534,2024:7080,2025:7443}  # AR2016 and AR2025 five-year summaries;
# note AR2020 restates 2016 at 6,543 under IFRS 15; the IFRS-15 figure is used in the growth lines below.
REV[2016] = 6543
STAT = 0.12   # Macao complementary tax flat rate (AR2025 note 8(a))
TAXPAID = {2016:6,2017:6,2018:6,2019:6,2020:5,2021:5,2022:7,2023:0,2024:11,2025:12}

def oc(y, statutory=False):
    cfo, capex, disp, lease, lic, sbc, op = D[y]
    v = cfo - capex + disp - lease - lic - sbc
    if statutory and op > 0:
        v -= max(0.0, STAT*op - TAXPAID[y])
    return v

print("year  owner cash (all-equity, after capex, leases, licence fee, SBC)  | at statutory 12% tax")
for y in D:
    print(y, round(oc(y)), round(oc(y, True)), " rev", REV[y], " margin", round(oc(y)/REV[y]*100,1) if REV[y] else "")

def avg(ys, st=False): return sum(oc(y, st) for y in ys)/len(ys)
lit = list(range(2021, 2026))
print("literal window 2021-25 avg:", round(avg(lit)), "statutory:", round(avg(lit, True)))
pre = [2016,2017,2018,2019]; post=[2023,2024,2025]
print("pre-COVID 2016-19 avg:", round(avg(pre)), round(avg(pre,True)))
print("post 2023-25 avg:", round(avg(post)), round(avg(post,True)))
ten = list(range(2016,2026))
print("ten-year 2016-25 avg (cycle incl. 2020-22 trough):", round(avg(ten)), round(avg(ten,True)))

# Valuation helpers
def pv(cash0, g, r, years=10):
    """cash grows at g for 10 years, then flat (zero nominal growth) forever; discounted at r."""
    v = 0.0; c = cash0
    for t in range(1, years+1):
        c = c*(1+g); v += c/(1+r)**t
    v += (c/r)/(1+r)**years
    return v

def pv_finite(cash0, g, r, years):
    v=0.0; c=cash0
    for t in range(1, years+1):
        c=c*(1+g); v+= c/(1+r)**t
    return v

R = 0.0556  # US Treasury 30-year par yield, 2026-10-13
# 2026-10-15 (resume): net debt = borrowings at face excluding lease liabilities, less cash, interim report note 11 and balance sheet 2026-06-30.
# Face 6,470 less lease liabilities 164 = 6,306; cash 851. Lease liabilities (IFRS 16, all leases) are left out because their
# principal repayments are already deducted inside owner cash (charged once). Restricted bank deposit 125 (non-current) not counted as cash.
# (Until 2026-10-15 this line read 5666 + 767 - 851 = 5,582: carrying amount with leases, net of deferred costs.)
NETDEBT_JUN26 = 6306 - 851
SH = 8093.379566  # million shares
HKD = 7.8406      # interim report illustration rate (HK$ per US$), for per-share HK$ display only
PRICE_HKD = 11.29
cap_usd = SH*PRICE_HKD/HKD
print("market cap US$m", round(cap_usd), " EV", round(cap_usd+NETDEBT_JUN26), " net debt", NETDEBT_JUN26)

# growth shown: cycle-to-cycle (pre-COVID 2016-19 avg to post 2023-25 avg), over ~7 years between midpoints 2017.5 -> 2024
for st in (False, True):
    a, b = avg(pre, st), avg(post, st)
    g_cash = (b/a)**(1/6.5)-1
    rev_g = ((sum(REV[y] for y in post)/3)/(sum(REV[y] for y in pre)/4))**(1/6.5)-1
    base = b
    lo = pv(base, 0.0, R); hi = pv(base, max(g_cash, 0), R)
    lo_f = pv(base,0.0,0.10); hi_f = pv(base,max(g_cash,0),0.10)
    print("\nstatutory tax" if st else "\nas paid (exemption)")
    print(" cycle growth owner cash %.2f%%  revenue %.2f%%" % (g_cash*100, rev_g*100))
    print(" base", round(base), " EV range", round(lo), round(hi), " equity", round(lo-NETDEBT_JUN26), round(hi-NETDEBT_JUN26))
    print(" per share HK$", round((lo-NETDEBT_JUN26)/SH*HKD,2), round((hi-NETDEBT_JUN26)/SH*HKD,2), " width", round(hi/lo,2))
    fair = ((lo_f+hi_f)/2 - NETDEBT_JUN26)/SH*HKD
    print(" fair at 10%% all-equity HK$ %.2f" % fair)
    # implied return at price on the all-equity basis: solve r where avg of PV = EV
    ev = cap_usd+NETDEBT_JUN26
    for case,g in (("no-growth",0.0),("growth",max(g_cash,0))):
        lo_r, hi_r = 0.01, 0.5
        for _ in range(100):
            m=(lo_r+hi_r)/2
            if pv(base,g,m) > ev: lo_r=m
            else: hi_r=m
        print("  implied return", case, "%.2f%%" % (m*100))

# ---------------- Q7 construction for the run (COMPUTATION, NOT A CLEARANCE) ----------------
print("\n================ Q7 CONSTRUCTION ================")
DIV_AFTER = 516     # interim dividend HK$4.05bn (~US$516M) declared 2026-08-14, paid 2026-10-09: interim report note 6 (was 517 until 2026-10-15)
ND = NETDEBT_JUN26 + DIV_AFTER
SHELTER = sum((STAT*1231 - 12)/(1+R)**t for t in (1, 2))   # exemption through tax year 2027: 2026, 2027 at the 2025 level
print("net debt incl. stated interim dividend:", ND, " shelter PV:", round(SHELTER))
def per_share(ev): return (ev + SHELTER - ND)/SH*HKD
def implied(base, g, ev_target):
    lo_r, hi_r = 0.005, 0.6
    for _ in range(200):
        m=(lo_r+hi_r)/2
        if pv(base,g,m)+SHELTER > ev_target: lo_r=m
        else: hi_r=m
    return m
EV_MKT = cap_usd + ND
print("market cap", round(cap_usd), " EV at price", round(EV_MKT))
cases = {
 "CENTRAL: cycle base 2016-25 (statutory tax)": (avg(ten, True), avg(pre,True), avg(post,True)),
 "beside: literal window 2021-25 (statutory)": (avg(lit, True), avg(pre,True), avg(post,True)),
 "beside: ex-pandemic base 2023-25 (statutory)": (avg(post, True), avg(pre,True), avg(post,True)),
 "beside: cycle base 2016-25, tax as paid": (avg(ten), avg(pre), avg(post)),
}
for name,(base,a,b) in cases.items():
    g = (b/a)**(1/6.5)-1   # successive cycle averages, midpoints 2017.5 -> 2024
    top = pv(base, 0.0, R); bot = pv(base, g, R)
    f_top = pv(base, 0.0, 0.10); f_bot = pv(base, g, 0.10)
    fair = per_share((f_top+f_bot)/2)
    eq_only_fair = None
    print(f"{name}: base {base:.0f}, g {g*100:.2f}%  range HK$ {per_share(bot):.2f} to {per_share(top):.2f}"
          f"  width {top/bot:.2f}  fair HK$ {fair:.2f}  implied return top {implied(base,0.0,EV_MKT)*100:.2f}% bottom {implied(base,g,EV_MKT)*100:.2f}%")

# equity-only beside the central: owner cash after net interest (interest paid less received) against market value
INT = {2016:(94,3),2017:(128,4),2018:(128,16),2019:(274,40),2020:(209,13),2021:(378,3),2022:(367,16),2023:(437,50),2024:(398,62),2025:(381,41)}
def oc_eq(y, st=True): return oc(y, st) - (INT[y][0]-INT[y][1])
be = sum(oc_eq(y) for y in ten)/10
a = sum(oc_eq(y) for y in pre)/4; b = sum(oc_eq(y) for y in post)/3
g = (b/a)**(1/6.5)-1
f = (pv(be,0,0.10)+pv(be,g,0.10))/2 + SHELTER
print(f"equity-only central: base {be:.0f}, g {g*100:.2f}%  fair HK$ {f/SH*HKD:.2f}; range HK$ {(pv(be,g,R)+SHELTER)/SH*HKD:.2f} to {(pv(be,0,R)+SHELTER)/SH*HKD:.2f}")
# depreciation variant beside (CFO less D&A instead of capex), cycle base
DA = {2016:611,2017:676,2018:655,2019:706,2020:684,2021:733,2022:750,2023:809,2024:754,2025:792}
# concession case beside: cash for 2026-2032 only (7 years), nothing after (gaming assets revert; non-gaming cash not separable from the filing)
for name, base in (("cycle base", avg(ten,True)), ("ex-pandemic base", avg(post,True))):
    v = pv_finite(base, 0.0, R, 7) + SHELTER
    print(f"concession-ends case ({name}): EV {v:.0f}, per share HK$ {(v-ND)/SH*HKD:.2f}")
# sales-share cap check (f): highest owner-cash share of sales in filings read
print("highest owner cash / sales in span:", max(round(oc(y,True)/REV[y]*100,1) for y in D if REV[y]>0), "%")


# ---------------- added 2026-10-15 (resume) ----------------
print()
print("================ BESIDE CASES (2026-10-15) ================")
def halves(st=True):
    a=sum(oc(y,st) for y in range(2016,2021))/5; b=sum(oc(y,st) for y in range(2021,2026))/5
    return a,b,(b/a)**(1/5)-1
a,b,gh=halves()
base=avg(ten,True)
print(f"rule (b) halves of the cycle window 2016-20 {a:.0f} vs 2021-25 {b:.0f}: g {gh*100:.2f}%  bottom HK$ {per_share(pv(base,gh,R)):.2f}  fair(top/bottom avg at 10%) HK$ {per_share((pv(base,0,0.10)+pv(base,gh,0.10))/2):.2f}")
tt=list(range(2016,2025)); bt=avg(tt,True)
print(f"trough-to-trough 2016-24 base {bt:.0f}: top HK$ {per_share(pv(bt,0,R)):.2f}  implied return no growth {implied(bt,0,EV_MKT)*100:.2f}%")
pk=list(range(2018,2024)); bp=avg(pk,True)
print(f"peak-to-peak 2018-23 base {bp:.0f}: top HK$ {per_share(pv(bp,0,R)):.2f}  implied {implied(bp,0,EV_MKT)*100:.2f}%")
for nm,yrs,st in (("pre-closure 2016-19 as paid",pre,False),("pre-closure 2016-19 statutory",pre,True),("2023-25 as paid",post,False)):
    bb=avg(yrs,st); print(f"sensitivity {nm}: base {bb:.0f} no growth: value HK$ {per_share(pv(bb,0,R)):.2f}  implied return at price {implied(bb,0,EV_MKT)*100:.2f}%")
# depreciation variant: CFO - D&A in place of capex (statutory), cycle base
def oc_da(y):
    cfo,capex,disp,lease,lic,sbc,op=D[y]; v=cfo-DA[y]-lease-lic-sbc
    if op>0: v-=max(0.0,STAT*op-TAXPAID[y])
    return v
bd=sum(oc_da(y) for y in ten)/10
print(f"depreciation variant cycle base {bd:.0f}: top HK$ {per_share(pv(bd,0,R)):.2f}  implied {implied(bd,0,EV_MKT)*100:.2f}%")
print("capex avg 2016-25", sum(D[y][1] for y in ten)/10, " D&A avg", sum(DA[y] for y in ten)/10)
# per ADS and US$
def ads(hk): return hk*10, hk*10/HKD
base=avg(ten,True); g=(avg(post,True)/avg(pre,True))**(1/6.5)-1
lo_,hi_=per_share(pv(base,g,R)),per_share(pv(base,0,R)); fair=per_share((pv(base,0,0.10)+pv(base,g,0.10))/2)
print(f"CENTRAL per share HK$ {lo_:.2f}-{hi_:.2f}; per ADS HK$ {ads(lo_)[0]:.2f}-{ads(hi_)[0]:.2f} = US$ {ads(lo_)[1]:.2f}-{ads(hi_)[1]:.2f}; fair HK$ {fair:.2f} = ADS HK$ {ads(fair)[0]:.2f} US$ {ads(fair)[1]:.2f}")
be = sum(oc_eq(y) for y in ten)/10; ge=(sum(oc_eq(y) for y in post)/3/(sum(oc_eq(y) for y in pre)/4))**(1/6.5)-1
fe=((pv(be,0,0.10)+pv(be,ge,0.10))/2+SHELTER)/SH*HKD
print(f"EQUITY-ONLY fair HK$ {fe:.2f} = ADS HK$ {fe*10:.2f} US$ {fe*10/HKD:.2f}; implied return on market cap (no growth) {(lambda: next(r/1000 for r in range(5,600) if pv(be,0,r/1000)+SHELTER < cap_usd))()*100:.1f}%")
print(f"price per ADS implied by HK$ price: US$ {PRICE_HKD*10/HKD:.2f} (quoted US$14.28)")

# ---------------- rivals, Macao segments, from their own filings (US$M) ----------------
# Sands China: adjusted property EBITDA (2016 'adjusted EBITDA'): AR2016, SCL 20-F FY2018, AR2020, AR2022, AR2024, AR2025.
# Wynn Macau Operations (Adjusted Property EBITDAR): 10-K FY2019 0001174922-20-000024, FY2022 0001174922-23-000048, FY2025 0001174922-26-000013.
# MGM China (segment Adjusted Property EBITDAR): 10-K FY2019 0001564590-20-007393, FY2022 0000789570-23-000008, FY2025 0000789570-26-000018.
# Melco Macau properties (Adjusted Property EBITDA, Mocha + Altira + City of Dreams + Studio City): 20-F FY2019 0001193125-20-091982,
#   FY2022 0001193125-23-086859, FY2025 0001193125-26-105023.
RIV = {
 "Sands China": {2017:(7586,2611),2018:(8665,3079),2019:(8808,3193),2020:(1687,-428),2021:(2874,341),2022:(1605,-323),2023:(6534,2225),2024:(7080,2329),2025:(7443,2312)},
 "Wynn Macau":  {2017:(4367.2,1288.3),2018:(5052.1,1577.1),2019:(4613.7,1378.4),2020:(980.1,-236.8),2021:(1509.0,95.9),2022:(721.5,-220.6),2023:(3100.4,953.9),2024:(3682.3,1175.6),2025:(3718.0,1085.0)},
 "MGM China":   {2017:(1858.2,535.5),2018:(2450.0,574.3),2019:(2905.4,734.7),2020:(656.7,-193.8),2021:(1210.8,25.4),2022:(673.6,-203.1),2023:(3153.6,866.9),2024:(4022.4,1087.1),2025:(4461.7,1203.2)},
 "Melco Macau": {2017:(4597.1,1187.8),2018:(4496.8,1208.7),2019:(4988.3,1412.6),2020:(1426.3,-135.5),2021:(1660.4,144.5),2022:(844.7,-170.1),2023:(3117.4,809.1),2024:(3920.3,987.9),2025:(4429.2,1234.0)},
}
print()
print("================ RIVALS (Macao segments) ================")
for n,d in RIV.items():
    r17_19=sum(d[y][0] for y in (2017,2018,2019)); e17_19=sum(d[y][1] for y in (2017,2018,2019))
    r23_25=sum(d[y][0] for y in (2023,2024,2025)); e23_25=sum(d[y][1] for y in (2023,2024,2025))
    e20_22=sum(d[y][1] for y in (2020,2021,2022)); e9=sum(d[y][1] for y in d); r9=sum(d[y][0] for y in d)
    print(f"{n:12s} rev 17-19 {r17_19:7.0f} 23-25 {r23_25:7.0f} chg {100*(r23_25/r17_19-1):6.1f}% | margin 17-19 {100*e17_19/r17_19:5.1f}% 23-25 {100*e23_25/r23_25:5.1f}% | EBITDA 20-22 {e20_22:6.0f} | 9-yr margin {100*e9/r9:5.1f}%")
tot={y:sum(RIV[n][y][0] for n in RIV) for y in RIV['Sands China']}
print("Sands China share of the four's Macao revenue:", {y:round(100*RIV['Sands China'][y][0]/tot[y],1) for y in tot})

# ---------------- CENTRAL as written in the run (2026-10-15) ----------------
# Q7 (a): window 2021-25 opens on an aberrational year (closures) -> base = cycle average 2016-25 (statutory tax, shelter added).
# Only one cycle of owner cash was read, so "between successive cycles" cannot be measured; the series changes sign, so by
# Q7 (b) growth is measured between the halves of the window, 2016-20 against 2021-25; negative -> bottom; no growth -> top.
print()
print("================ CENTRAL AS WRITTEN (halves growth) ================")
base = avg(ten, True); a, b, gh = halves(True)
top, bot = pv(base, 0, R), pv(base, gh, R)
fair = per_share((pv(base, 0, 0.10) + pv(base, gh, 0.10)) / 2)
print(f"all-equity: base {base:.0f} g {gh*100:.2f}%  range HK$ {per_share(bot):.2f} to {per_share(top):.2f} (ADS HK$ {per_share(bot)*10:.2f}-{per_share(top)*10:.2f}, US$ {per_share(bot)*10/HKD:.2f}-{per_share(top)*10/HKD:.2f})  width {per_share(top)/per_share(bot):.1f} on equity, {top/bot:.2f} on the business")
print(f"  implied return at price: top {implied(base,0,EV_MKT)*100:.2f}%  bottom {implied(base,gh,EV_MKT)*100:.2f}%")
print(f"  FAIR all-equity HK$ {fair:.2f}  ADS HK$ {fair*10:.2f}  US$ {fair*10/HKD:.2f}")
ae = sum(oc_eq(y) for y in range(2016,2021))/5; be2 = sum(oc_eq(y) for y in range(2021,2026))/5
print(f"  equity-only halves {ae:.0f} vs {be2:.0f}")
be = sum(oc_eq(y) for y in ten)/10
ge = (be2/ae)**(1/5)-1 if ae>0 and be2>0 else None
print(f"  equity-only base {be:.0f}, halves growth {'n/a (sign)' if ge is None else '%.2f%%'%(ge*100)}")
if ge is None:
    fe = (pv(be,0,0.10)+SHELTER)/SH*HKD; rng=(pv(be,0,R)+SHELTER)/SH*HKD
    print(f"  EQUITY-ONLY (no-growth case alone): value HK$ {rng:.2f}; fair HK$ {fe:.2f} ADS HK$ {fe*10:.2f} US$ {fe*10/HKD:.2f}")
else:
    fe = ((pv(be,0,0.10)+pv(be,ge,0.10))/2+SHELTER)/SH*HKD
    print(f"  EQUITY-ONLY range HK$ {(pv(be,ge,R)+SHELTER)/SH*HKD:.2f} to {(pv(be,0,R)+SHELTER)/SH*HKD:.2f}; fair HK$ {fe:.2f} ADS HK$ {fe*10:.2f} US$ {fe*10/HKD:.2f}")
print(f"  market cap US$ {cap_usd:.0f}M; net debt {ND}; EV {EV_MKT:.0f}; shelter {SHELTER:.0f}")
