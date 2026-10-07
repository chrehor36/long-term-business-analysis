import json
# Filed cash-flow statements, $M. FY2003-FY2011 read from the 10-Ks for FY2005, FY2008 and FY2011 (text in k/);
# FY2012-FY2025 from SEC companyfacts (xb_rows.json), cross-checked to the filed FY2021 and FY2025 statements.
# (ocf, sbc, capex, dep_plus_amort, acquisitions)
F={2003:(46.365,0.0,19.127,24.963,0.0),2004:(47.144,0.0,21.644,24.068,12.668),2005:(52.644,0.0,21.632,24.262,16.088),
2006:(54.965,1.586,19.739,24.608,26.264),2007:(57.843,1.740,22.765,27.008,52.747),2008:(54.897,1.851,22.781,27.470,0.0),
2009:(80.633,1.716,27.190,27.753,0.0),2010:(68.008,1.248,33.531,29.852,25.185),2011:(80.456,0.918,29.124,30.234,8.806)}
R=json.load(open('xb_rows.json'))
g=lambda n,y:(R[n].get(str(y)) or 0)/1e6
for y in range(2012,2026):
    F[y]=(g('OCF',y),g('SBC',y),g('Capex',y),g('Dep',y)+g('Amort',y),g('Acq',y))
# TTM to 2026-06-27: FY2025 + 9M FY2026 - 9M FY2025 (10-Q to 2026-06-27, 0001437749-26-026302)
ttm=(165.126+100.443-98.697, 6.320+4.684-4.580, 82.873+53.263-61.264, (66.018+52.167-48.296)+(7.314+4.218-5.871), 0.0)
CAP=1448.011
rows={}
print('FY    OCF    SBC   capex   D&A    acq   OE_capex  OE_D&A  OE_capex+acq')
for y in sorted(F):
    o,s,c,d,a=F[y]
    rows[y]=(o-s-c,o-s-d,o-s-c-a)
    print('%d %6.1f %5.1f %6.1f %6.1f %6.1f %8.1f %8.1f %8.1f'%(y,o,s,c,d,a,*rows[y]))
o,s,c,d,a=ttm; t=(o-s-c,o-s-d,o-s-c-a)
print('TTM  %6.1f %5.1f %6.1f %6.1f %6.1f %8.1f %8.1f'%(o,s,c,d,a,t[0],t[1]))
print('\nWindows ending FY2025 (means), yields on cap $%.1fM:'%CAP)
lo=hi=None; allv=[]
for n in range(1,24):
    ys=[y for y in range(2026-n,2026)]
    mc=sum(rows[y][0] for y in ys)/n; md=sum(rows[y][1] for y in ys)/n; ma=sum(rows[y][2] for y in ys)/n
    allv+= [mc,md]
    print('%2dy FY%d-FY2025  capex end %6.1f (%.2f%%)  D&A end %6.1f (%.2f%%)  capex+acq %6.1f (%.2f%%)'%(n,2026-n,mc,100*mc/CAP,md,100*md/CAP,ma,100*ma/CAP))
print('every window 1-23y, both (c) ends: $%.1fM to $%.1fM, %.2f%% to %.2f%%'%(min(allv),max(allv),100*min(allv)/CAP,100*max(allv)/CAP))
print('TTM capex end %.1f (%.2f%%), D&A end %.1f (%.2f%%)'%(t[0],100*t[0]/CAP,t[1],100*t[1]/CAP))
sb=[F[y][1]/F[y][0]*100 for y in range(2006,2026)]
print('SBC share of OCF FY2006-FY2025: %.1f%% to %.1f%%'%(min(sb),max(sb)))
json.dump({str(k):v for k,v in rows.items()},open('oe_rows.json','w'))
