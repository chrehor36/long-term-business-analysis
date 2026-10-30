# Hawkins owner earnings, COMPUTATION - NOT A CLEARANCE (the file closed at Q2).
# OCF, SBC, capex, acquisitions: companyfacts FY2010-FY2026 (xb_out.txt), checked against the filed FY2026
# statement (FY2024-FY2026) and the filed FY2022 statement; FY2004-FY2009 read from the 10-Ks of FY2004-FY2010.
# dep = depreciation of plant only (DepreciationDepletionAndAmortization less AmortizationOfIntangibleAssets;
# the Depreciation tag FY2019-FY2026). amort = amortization of bought intangibles. $M.
D = {
# FY: (ocf, sbc, capex, dep, amort, acq)
2004:(7.41,None,4.90,None,None,0.0),
2005:(12.62,None,5.92,None,None,0.0),
2006:(9.46,None,6.95,None,None,0.0),
2007:(8.73,0.19,4.69,None,None,0.0),
2008:(12.21,0.52,5.78,None,None,None),
2009:(24.43,0.28,14.21,None,None,None),
2010:(38.782,0.659,8.331,None,None,None),
2011:(28.533,1.952,12.421,6.848,0.3,25.5),
2012:(33.682,1.35,20.057,7.858,0.6,1.709),
2013:(35.474,1.621,26.66,9.548,0.7,0.1),
2014:(34.612,1.322,12.261,11.905,0.7,2.416),
2015:(20.664,1.631,14.552,12.115,0.9,10.068),
2016:(36.333,1.706,24.183,13.111,2.4,159.199),
2017:(44.855,2.127,21.616,14.775,6.1,2.199),
2018:(27.349,1.371,19.703,16.69,5.7,0.0),
2019:(47.99,2.01,12.618,16.3,5.5,0.0),
2020:(58.902,2.273,24.549,16.5,5.1,0.0),
2021:(43.793,3.343,20.794,16.8,5.8,51.0),
2022:(42.837,3.818,28.512,17.7,6.5,21.546),
2023:(77.4,3.825,48.321,20.5,6.9,0.0),
2024:(159.499,4.88,40.151,23.3,8.5,83.455),
2025:(111.096,6.498,41.096,27.2,12.8,87.4),
2026:(144.327,8.573,58.239,31.3,21.3,167.108),
}
CAP = 129.03*20875117/1e6
TTM = (144.327+35.152-31.490, 8.573+2.235-2.212, 58.239+11.605-13.544, None, None, 167.108+3.6-151.328)
print('cap %.1f' % CAP)
print('FY   ocf    sbc   capex   dep  amort   acq   OEcapex  OEdep  OEdep-amort  OEcapex-acq')
rows={}
for y in sorted(D):
    o,s,c,d,a,q=D[y]
    s0=s or 0
    oc=o-s0-c
    od=(o-s0-d) if d is not None else None
    oda=(od-a) if (od is not None and a is not None) else None
    oq=(oc-q) if q is not None else None
    rows[y]=(oc,od,oda,oq)
    f=lambda x:('%7.1f'%x) if x is not None else '      -'
    print(y, f(o), f(s), f(c), f(d), f(a), f(q), f(oc), f(od), f(oda), f(oq))
o,s,c,_,_,q=TTM
print('TTM to 2026-06-28: ocf %.1f sbc %.1f capex %.1f acq %.1f OEcapex %.1f' % (o,s,c,q,o-s-c))
def mean(ys,k):
    v=[rows[y][k] for y in ys if rows[y][k] is not None]
    return sum(v)/len(v) if v else None
print()
for n in (1,3,5,10,16):
    ys=list(range(2027-n,2027))
    mc=mean(ys,0); md=mean(ys,1); mda=mean(ys,2); mq=mean(ys,3)
    print(f'{n:2d}y FY{ys[0]}-FY2026: capex end {mc:6.1f} ({mc/CAP*100:.2f}%)  dep end {md:6.1f} ({md/CAP*100:.2f}%)  dep end less amort {mda:6.1f}  after acquisitions {mq:6.1f} ({mq/CAP*100:.2f}%)')
ys=list(range(2004,2027)); print('23y FY2004-FY2026 capex end %.1f (%.2f%%)' % (mean(ys,0), mean(ys,0)/CAP*100))
# screen reproduction attempts
print()
for n in (3,5):
    ys=list(range(2027-n,2027))
    print(n,'y: capex end', round(mean(ys,0),1),' dep+amort end (DDA as c):', round(sum(D[y][0]-D[y][1]-(D[y][3]+D[y][4]) for y in ys)/n,1))
# working capital lines FY2021-FY2026 (receivables, inventories, payables, filed signs as cash effect)
WC={2021:(-21.323,-7.960,2.551),2022:(-30.526,-30.034,25.138),2023:(-6.389,4.717,-11.596),2024:(21.399,19.921,-0.828),2025:(-11.23,-6.572,2.445),2026:(-2.467,10.053,-5.841)}
print()
for y,(r,i,p) in WC.items(): print(y,'recv %.1f inv %.1f pay %.1f sum %.1f ; OCF %.1f' % (r,i,p,r+i+p,D[y][0]))
print('WC sum FY2022-FY2026 %.1f' % sum(sum(WC[y]) for y in range(2022,2027)))
