# Owner earnings, OPXS, $K. OCF, SBC, depreciation and capex from the filed cash-flow statements (FY2010-FY2025; FY2013-2015 read
# from the 10-Ks, which carry no operating-cash tag). (c) at two ends: depreciation excluding acquired-intangible amortization, and
# total purchases of property and equipment. No net-income proxy. FY2015 capex includes the Applied Optics Center purchase (flagged).
Y=list(range(2010,2026))
OCF=[-876,1114,848,-1538,1671,-1218,-539,16,1039,160,3911,481,2042,-296,1781,6931]
SBC=[97,87,152,128,105,140,192,220,153,113,197,228,162,247,425,383]
DEP=[66,66,165,69,80,334,345,337,327,340,248,263,307,345,387,359]
CAPEX=[116,31,96,121,40,2100,34,149,167,143,152,274,257,376,681,494]
CAP=10.42*6959873/1000
lo=[o-s-c for o,s,c in zip(OCF,SBC,CAPEX)]; hi=[o-s-d for o,s,d in zip(OCF,SBC,DEP)]
print('cap $K',round(CAP))
print('FY   OCF  SBC  DEP CAPEX  OE_capex OE_dep  SBC/OCF')
for i,y in enumerate(Y):
    print(y,OCF[i],SBC[i],DEP[i],CAPEX[i],lo[i],hi[i], f"{SBC[i]/OCF[i]:.0%}" if OCF[i]>0 else 'n/a')
def w(n):
    a=lo[-n:];b=hi[-n:]; ml=sum(a)/n; mh=sum(b)/n
    return ml,mh
for n in [1,2,3,4,5,7,10,16]:
    ml,mh=w(n); print(f"{n:2d}y ending FY2025: ${ml:,.0f}K to ${mh:,.0f}K  yield {ml/CAP:.2%} to {mh/CAP:.2%}")
# 16-year with FY2015 AOC purchase removed from capex (acquired fixed assets $2,064.7K at fair value)
lo2=lo[:]; lo2[5]=lo[5]+2065
print('16y capex end ex AOC fixed assets:', round(sum(lo2)/16), f"{sum(lo2)/16/CAP:.2%}")
# rolling 5-year windows
for e in range(2014,2026):
    i=Y.index(e); a=lo[i-4:i+1]; b=hi[i-4:i+1]
    print('5y to',e, round(sum(a)/5), round(sum(b)/5))
# TTM to 2026-06-28
ocf=6931-5368+989; sbc=383-247+738; capex=494-453+1056; dep=359-(386-117)+294
print('TTM OCF',ocf,'SBC',sbc,'capex',capex,'dep(est)',dep,'OE',ocf-sbc-capex,ocf-sbc-dep, f"{(ocf-sbc-capex)/CAP:.2%} {(ocf-sbc-dep)/CAP:.2%}")
print('cumulative FY2010-2025 OCF',sum(OCF),'SBC',sum(SBC),'capex',sum(CAPEX),'dep',sum(DEP))
