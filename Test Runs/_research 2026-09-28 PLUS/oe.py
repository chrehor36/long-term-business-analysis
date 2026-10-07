# continuing operations only (the business on offer). $M. Source: 10-K FY2026 cash-flow statement (FY2024-FY2026),
# 8-K 2026-01-26 EX-99.1 recast (FY2023), 10-Q Q1 FY2027 (TTM). Amortization of purchased intangibles from the
# intangibles notes (FY2026 10-K: 20.6, 19.9, 15.2; FY2024 10-K: 9.3 for FY2023).
cap=2361.4
yrs={
 'FY2023':dict(ocf=16.766,sbc=7.580,capex=8.086,da=15.280,amort=9.3,acq=13.288,fp=-10.708),
 'FY2024':dict(ocf=246.063,sbc=9.471,capex=7.664,da=22.499,amort=15.2,acq=54.182,fp=-47.441),
 'FY2025':dict(ocf=323.918,sbc=10.502,capex=5.271,da=27.183,amort=19.9,acq=124.926,fp=-15.577),
 'FY2026':dict(ocf=-117.447,sbc=12.134,capex=4.429,da=27.615,amort=20.6,acq=0.0,fp=30.166),
}
print('year      OCF     SBC  capex  dep(ex-amort)  OE_capex  OE_dep   acq   floorplan  OE_capex+fp')
oe={}
for y,d in yrs.items():
    dep=d['da']-d['amort']
    a=d['ocf']-d['sbc']-d['capex']; b=d['ocf']-d['sbc']-dep
    oe[y]=(a,b,d['acq'],d['fp'])
    print(f"{y}  {d['ocf']:8.1f} {d['sbc']:6.1f} {d['capex']:6.1f} {dep:8.1f}   {a:9.1f} {b:8.1f} {d['acq']:6.1f} {d['fp']:8.1f} {a+d['fp']:9.1f}")
ttm_ocf=-117.447+76.477-(-106.003); ttm_sbc=12.134+3.121-2.663; ttm_cap=4.429+0.853-0.835
print('TTM to 2026-06-30: OCF %.1f SBC %.1f capex %.1f OE %.1f yield %.2f%%'%(ttm_ocf,ttm_sbc,ttm_cap,ttm_ocf-ttm_sbc-ttm_cap,100*(ttm_ocf-ttm_sbc-ttm_cap)/cap))
ys=list(yrs)
for n in (1,2,3,4):
    w=ys[-n:]
    lo=sum(min(oe[y][0],oe[y][1]) for y in w)/n; hi=sum(max(oe[y][0],oe[y][1]) for y in w)/n
    acq=sum(oe[y][2] for y in w)/n; fp=sum(oe[y][3] for y in w)/n
    print(f'{n}y {w[0]}-{w[-1]}: OE {lo:7.1f} to {hi:7.1f}  yield {100*lo/cap:5.2f}% to {100*hi/cap:5.2f}%  | after acquisitions {lo-acq:7.1f} ({100*(lo-acq)/cap:5.2f}%) | floor plan counted as payables {lo+fp:7.1f} to {hi+fp:7.1f}')
# operating working capital (continuing), from the balance sheets
wc26=(667.831+38.896+200.888+77.748+31.602)-(264.605+119.693+48.590+168.127+37.128+83.010)
wc25=(508.272+19.382+120.440+66.769+31.437)-(323.890+89.527+42.722+154.067+22.463+81.759)
print('operating working capital 2025-03-31 %.1f, 2026-03-31 %.1f, change %.1f'%(wc25,wc26,wc26-wc25))
