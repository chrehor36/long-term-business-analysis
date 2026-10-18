# Arithmetic for the VUOC run, 2026-10-17. Every input is transcribed from the filed statements
# named in the run file (accessions there). Shares before the 1-for-20 reverse split of 2011-11-23
# are divided by 20 for comparability (k2011 / k2012 Item 5 state the split).
bs = {  # year: cash, total assets, total liabilities, equity incl NCI, accumulated deficit, shares (as filed)
 2006:(289795, 300145, 344403, 300145-344403, -45422233, 47430683, True),
 2007:(1014512,3324167, 624666, 2699501, -48530613, 64663517, True),
 2008:(2486609,3390351, 606303, 2784048, -58386684, 85691892, True),
 2009:(366303, 1873026,4054926,1873026-4054926, -65873319, 86152246, True),
 2010:(119619, 1768929, 729895, 1039034, -70499569,104992350, True),
 2011:(10992,   437629,5093045, 437629-5093045, -79581191, 5568253, False),
 2012:(328188,  489410,5712367, 489410-5712367, -83406639, 7130226, False),
 2013:(92795,   313414,6227053,-5913639, -88426616,10576097, False),
 2014:(1903,    207864,6874392,-6666528, -91416708,12950384, False),
 '2015Q1':(2432,196032,6515320,-6319288,-92339080,13973093, False),
}
print("year | cash | total assets | total liabilities | equity | accumulated deficit | shares (post-split basis)")
for y,(c,ta,tl,eq,ad,sh,pre) in bs.items():
    s = sh/20 if pre else sh
    print(f"{y} | {c:,} | {ta:,} | {tl:,} | {eq:,} | {ad:,} | {s:,.0f}")
# cash flows: OCF, capex+building deposits, SBC & stock/warrants issued for services, revenue, cash interest paid
cf = {
 2007:(-1675723,-201381, 579136+320275+761973, 0, None),
 2008:(-4636469,-747985,1878508+633038+1678739+41621+467232, 0, None),
 2009:(-4635318,-457502, 444920+48735+266459, 0, 3995),
 2010:(-3529351,-417383, 881691+6722+19125+150000, 0, 206001),
 2011:(-5780066,-264147,1006807+339924, 7816, 2203),
 2012:(-1568781, 0, 134349+455290, 0, 25000),
 2013:(-1716606, -34015,1109367, 0, 0),
 2014:(-1081190,-157052, 497032, 0, 14619),
}
print("\nyear | OCF | capex | OCF-capex | stock pay | owner cash after stock pay | revenue")
oc={}
for y,(o,k,sbc,rev,ip) in cf.items():
    oc[y]=o+k-sbc
    print(f"{y} | {o:,} | {k:,} | {o+k:,} | {sbc:,} | {o+k-sbc:,} | {rev:,}")
w=[2010,2011,2012,2013,2014]
a1=sum(cf[y][0]+cf[y][1] for y in w)/5; a2=sum(oc[y] for y in w)/5
ip=sum((cf[y][4] or 0) for y in w)/5
print(f"\nfive-year average FY2010-FY2014: OCF-capex {a1:,.0f}; owner cash after stock pay {a2:,.0f}; cash interest paid avg {ip:,.0f}; before interest {a2+ip:,.0f}")
tot=sum(oc.values()); print(f"eight-year sum FY2007-FY2014 owner cash after stock pay {tot:,}")
# net debt at 2015-03-31 (latest filed): borrowings = convertible debentures + judgment payable + loan payable; cash
nd = 2788300+1295920+0-2432
print(f"net debt 2015-03-31 (debentures 2,788,300 + judgments 1,295,920 - cash 2,432) = {nd:,}; total liabilities 6,515,320")
print(f"last filed close 0.62 (2015-04-15) x 14,273,093 shares (2015-05-12) = {0.62*14273093:,.0f}")

# COMPUTATION, NOT A CLEARANCE: the Q7 construction applied after the Q1 stop.
sh=14273093; nd=4081788; r=0.0543
base_eq=a2            # owner cash after interest (equity-only)
base_ae=a2+ip         # owner cash before cash interest (all-equity basis)
for lab,b,dr in (("no-growth, all-equity, at the long rate",base_ae,r),("no-growth, all-equity, at 10% (fair price)",base_ae,0.10)):
    whole=b/dr; eq=whole-nd
    print(f"{lab}: whole business {whole:,.0f}; less net debt {eq:,.0f}; per share {eq/sh:,.2f}")
print(f"equity-only at 10%: {base_eq/0.10:,.0f}; per share {base_eq/0.10/sh:,.2f}")
print(f"liquidation reading 2015-03-31: assets 196,032 less liabilities 6,515,320 = {196032-6515320:,}; per share {(196032-6515320)/sh:,.2f}")
