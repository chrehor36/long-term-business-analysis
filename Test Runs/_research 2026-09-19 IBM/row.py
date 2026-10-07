"""Competitor row arithmetic for the IBM run. All inputs are filed figures printed by peers.py."""
D = {
  # ticker: (fy2020_rev, fy2025_rev, fy2025_cogs_or_None, fy2020_cogs_or_None,
  #          fy2025_rd_or_None, fy2025_ocf, fy2025_sbc, fy2025_capex, label)
  'IBM':   (55179.0, 67535.0, 28239.0, 24314.0, 8316.0, 13193.0, 1715.0, 1091.0, 'FY2020->FY2025'),
  'MSFT':  (143015.0, 331839.0, 106374.0, 46078.0, 35562.0, 182935.0, 12405.0, 115948.0, 'FY2020(Jun)->FY2026(Jun)'),
  'GOOGL': (182527.0, 402836.0, 162535.0, 84732.0, 61087.0, 164713.0, 24953.0, 91447.0, 'FY2020->FY2025'),
  'AMZN':  (386064.0, 716924.0, 356414.0, 233307.0, None, 139514.0, 19467.0, 131819.0, 'FY2020->FY2025'),
  'ORCL':  (39068.0, 67357.0, None, None, 10272.0, 31977.0, 4811.0, 55663.0, 'FY2020(May)->FY2026(May)'),
  'ACN':   (44327.0, 69673.0, 47437.6, 30350.9, 817.3, None, None, 600.0, 'FY2020(Aug)->FY2025(Aug)'),
  'DELL':  (86670.0, 113538.0, 90831.0, 66530.0, 3142.0, 11185.0, 723.0, 2633.0, 'FY2021(Jan)->FY2026(Jan)'),
  'HPE':   (26982.0, 34296.0, None, None, 2518.0, 2919.0, 643.0, 2292.0, 'FY2020(Oct)->FY2025(Oct)'),
  'AVGO':  (23888.0, 63887.0, 20593.0, 10372.0, 10977.0, 27537.0, 7568.0, 623.0, 'FY2020(Nov)->FY2025(Nov)'),
  'NOW':   (4519.0, 13278.0, 2983.0, 987.0, 2960.0, 5444.0, 1955.0, 868.0, 'FY2020->FY2025'),
}
ACN_OCF = 9975.0  # placeholder, filled below if known
print('%-6s %10s %10s %7s %8s %8s %7s %7s' % ('tkr','rev0','rev1','CAGR%','GM25%','dGM pts','R&D%','SBC/OCF%'))
for t,(r0,r1,c1,c0,rd,ocf,sbc,capex,lab) in D.items():
    cagr = ((r1/r0)**(1/5.0)-1)*100
    gm1 = (1-c1/r1)*100 if c1 else None
    gm0 = (1-c0/r0)*100 if c0 else None
    dgm = (gm1-gm0) if (gm1 is not None and gm0 is not None) else None
    rdp = (rd/r1*100) if rd else None
    so  = (sbc/ocf*100) if (sbc and ocf) else None
    f = lambda v, n=1: ('%.*f'%(n,v)) if v is not None else '  n/a'
    print('%-6s %10.0f %10.0f %7s %8s %8s %7s %7s   %s' % (t,r0,r1,f(cagr,2),f(gm1),f(dgm),f(rdp),f(so),lab))

print()
print('--- IBM internal: acquisition cash vs revenue added, FY2021-FY2025')
acq = [3293.0, 2348.0, 5082.0, 3289.0, 8294.0]
print('acquisition cash FY2021-25 = %.0f' % sum(acq))
print('revenue added FY2020->FY2025 = %.0f' % (67535.0-55179.0))
print('ratio cash per $1 of added annual revenue = %.2f' % (sum(acq)/(67535.0-55179.0)))
print('R&D FY2025 %.0f = %.2f%% of revenue; R&D+mean acq = %.0f = %.1f%% of revenue'
      % (8316.0, 8316.0/67535.0*100, 8316.0+sum(acq)/5, (8316.0+sum(acq)/5)/67535.0*100))
print()
print('--- IBM goodwill wedge [E2-43], FY2025')
ta, gw, ia, tl, eq = 151880.0, 67717.0, 11391.0, 119139.0, 32740.0
print('total equity %.0f ; goodwill %.0f ; other intangibles %.0f ; TANGIBLE equity %.0f'
      % (eq, gw, ia, eq-gw-ia))
print('tangible assets %.0f' % (ta-gw-ia))
