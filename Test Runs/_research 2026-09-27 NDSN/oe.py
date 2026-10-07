import json
# Filed cash-flow statements, $M (ocf, sbc, capex, dep_plus_intangible_amort, acquisitions_paid).
# FY2000-2002: 10-K FY2002 (0000950152-03-000680); FY2003-2005: 10-K FY2005 (0000950152-06-000197); FY2006-2008: 10-K FY2008 (0000950152-08-010466);
# FY2009-2011: 10-K FY2011 (0001193125-11-343516). Goodwill amortization (FY2000 $5.110M, FY2001 $15.446M, pre-ASC 350) removed from the D&A end.
# FY2003-FY2005: no stock-compensation line in the statement (APB 25 era); FY2000-FY2002 likewise. Recorded as a gap, not filled.
# FY2012-FY2025 from companyfacts (xb_rows.json), cross-checked to the filed FY2014 (0001193125-14-442368), FY2022 (0000072331-22-000185) and FY2025 (0000072331-25-000144) statements.
# The acquisition line from FY2023 is "Sale (acquisition) of businesses, net of cash acquired"; companyfacts carries FY2023/FY2024 as NEGATIVE payments. Used here as cash PAID (sign corrected);
# FY2025's +28.107 is a divestiture inflow and is shown as -28.1 in the acquisitions column.
DEP={2000:24.276,2001:24.909,2002:27.995,2003:27.296,2004:24.083,2005:22.632,2006:22.284,2007:23.784,2008:26.440,2009:26.310,2010:22.625,2011:20.758}
F={2000:(84.976,0.0,23.645,24.276+6.049-5.110,0.0),2001:(73.429,0.0,23.147,24.909+16.946-15.446,280.351),2002:(130.394,0.0,11.397,27.995+1.492,1.223),
2003:(87.547,0.0,7.563,27.296+1.944,-0.544),2004:(112.923,0.0,11.437,24.083+2.793,4.013),2005:(118.831,0.0,15.389,22.632+3.051,0.557),
2006:(120.024,7.121,13.610,22.284+1.026,0.0),2007:(124.248,8.217,31.017,23.784+4.149,325.245),2008:(114.042,9.247,26.386,26.440+5.797,4.699+3.191),
2009:(168.677,-0.814,12.514,26.310+5.100,0.0),2010:(140.186,7.633,14.317,22.625+6.263,18.576),2011:(246.727,8.845,20.239,20.758+8.018,292.980)}
R=json.load(open('xb_rows.json'))
g=lambda n,y:(R[n].get(str(y)) or 0)/1e6
for y in range(2012,2026):
    acq=g('Acq',y)
    if y in (2023,2024): acq=-acq
    if y==2025: acq=-28.107
    F[y]=(g('OCF',y),g('SBC',y),g('Capex',y),g('Dep',y)+g('Amort',y),acq); DEP[y]=g('Dep',y)
# TTM to 2026-07-31: FY2025 + 9M FY2026 - 9M FY2025 (10-Q 0000072331-26-000054)
TTMDEP=None
ttm=(719.175+570.473-516.264, 18.944+17.512-13.255, 58.060+40.313-49.002, 150.523+109.446-112.454, -28.107+11.643)
CAP=18145.182
rows={}
print('FY    OCF    SBC   capex   dep  dep+amort   acq   OE_capex  OE_dep  OE_dep+amort  OE_capex-acq  SBC/OCF')
for y in sorted(F):
    o,s,c,d,a=F[y]; dp=DEP[y]; rows[y]=(o-s-c,o-s-dp,o-s-c-a,o-s-d)
    print('%d %6.1f %5.1f %6.1f %5.1f %6.1f %7.1f %8.1f %8.1f %8.1f %9.1f %6.1f%%'%(y,o,s,c,dp,d,a,rows[y][0],rows[y][1],rows[y][3],rows[y][2],100*s/o))
o,s,c,d,a=ttm; dp=71.259+ (109.446-58.320) - (112.454-59.099)
t=(o-s-c,o-s-dp,o-s-c-a,o-s-d)
print('TTM  %6.1f %5.1f %6.1f %5.1f %6.1f %7.1f %8.1f %8.1f %8.1f %9.1f'%(o,s,c,dp,d,a,t[0],t[1],t[3],t[2]))
print('\nWindows ending FY2025 (means), yields on cap $%.1fM:'%CAP)
allv=[]
for n in range(1,27):
    ys=list(range(2026-n,2026))
    mc=sum(rows[y][0] for y in ys)/n; md=sum(rows[y][1] for y in ys)/n; ma=sum(rows[y][2] for y in ys)/n; mm=sum(rows[y][3] for y in ys)/n
    allv+=[mc,md]
    print('%2dy FY%d-FY2025  capex end %6.1f (%.2f%%)  dep end %6.1f (%.2f%%)  [dep+amort %6.1f]  capex+acq %7.1f (%.2f%%)'%(n,2026-n,mc,100*mc/CAP,md,100*md/CAP,mm,ma,100*ma/CAP))
print('every window 1-26y, both (c) ends: $%.1fM to $%.1fM, %.2f%% to %.2f%%'%(min(allv),max(allv),100*min(allv)/CAP,100*max(allv)/CAP))
print('TTM capex end %.1f (%.2f%%), dep end %.1f (%.2f%%), capex+acq %.1f'%(t[0],100*t[0]/CAP,t[1],100*t[1]/CAP,t[2]))
acq=[(y,F[y][4]) for y in sorted(F)]
print('acquisitions FY2000-FY2025 sum %.1f; FY2016-FY2025 %.1f; FY2021-FY2025 %.1f'%(sum(a for y,a in acq),sum(a for y,a in acq if y>=2016),sum(a for y,a in acq if y>=2021)))
print('OE capex end FY2000-2025 sum %.1f; FY2016-2025 %.1f; FY2021-2025 %.1f'%(sum(rows[y][0] for y in rows),sum(rows[y][0] for y in rows if y>=2016),sum(rows[y][0] for y in rows if y>=2021)))
json.dump({str(k):v for k,v in rows.items()},open('oe_rows.json','w'))
