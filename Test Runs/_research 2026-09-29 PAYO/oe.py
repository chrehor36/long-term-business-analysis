# Owner earnings, the corpus's way [E2-23], every window [E4-25]. $M from filed statements:
# S-4/A 0001213900-21-028959 (2018-2020), 10-K FY2022 (2021-2022), FY2024 (2023-2024), FY2025, 10-Q June 2026.
# OE = OCF - SBC in full - (c).  (c) capex end = PPE + capitalized internal-use software;
# (c) depreciation end = D&A less acquired-intangible amortization (known 2022-2025; 2018-2021 D&A as filed).
# No net-income proxy anywhere (operator rule 5).
d = {  # ocf, sbc, ppe, sw, da, acq_amort, ca_net, int_cust
 2018: (-5.988, 6.919, 4.538, 6.325, 7.874, 0.0, 5.883-22.639, None),
 2019: (-14.312, 9.535, 9.149, 8.140, 10.341, 0.0, 128.125-171.105, None),
 2020: (9.526, 11.074, 4.992, 9.045, 17.095, 0.0, 259.790-266.149, None),
 2021: (20.015, 37.012, 6.891, 14.008, 17.997, 0.0, 342.930-330.510, None),
 2022: (83.960, 52.149, 10.504, 18.329, 20.858, 5.509-4.022, 237.834-223.819, None),
 2023: (159.489, 65.767, 8.459, 39.333, 27.814, 8.846-5.509, 290.801-299.139, 230.634),
 2024: (176.925, 64.787, 8.189, 52.203, 47.296, 13.111-8.846+0.267, 318.763-329.512, 256.846),
 2025: (233.489, 73.104, 26.874, 60.855, 65.625, 17.650-13.111+0.910-0.267, 325.841-313.264, 231.614),
}
h26 = (113.010, 37.999, 21.116, 34.742, 40.140)
h25 = (124.401, 38.814, 7.304, 29.993, 29.943)
CAP = 7.14*338.850836
oe = {}
print('FY   OCF    SBC   capex   depr   OE_capex  OE_depr  CA_net')
for y,(o,s,p,w,da,aa,ca,ic) in d.items():
    lo = o-s-(p+w); hi = o-s-(da-aa)
    oe[y] = (lo, hi)
    print(y, f'{o:7.1f} {s:6.1f} {p+w:6.1f} {da-aa:6.1f} {lo:8.1f} {hi:8.1f} {ca:7.1f}')
# TTM to June 2026
o = d[2025][0]+h26[0]-h25[0]; s = d[2025][1]+h26[1]-h25[1]; c = d[2025][2]+d[2025][3]+h26[2]+h26[3]-h25[2]-h25[3]; da = d[2025][4]+h26[4]-h25[4]
print(f'TTM Jun-2026 OCF {o:.1f} SBC {s:.1f} capex {c:.1f} D&A(as filed) {da:.1f} OE {o-s-c:.1f} .. {o-s-da:.1f}  yield {100*(o-s-c)/CAP:.2f}%..{100*(o-s-da)/CAP:.2f}%')
ys = sorted(oe)
print('\nTrailing windows ending FY2025 (capex end / depreciation end), yield on cap', round(CAP,1))
for n in range(1, len(ys)+1):
    w = ys[-n:]
    lo = sum(oe[y][0] for y in w)/n; hi = sum(oe[y][1] for y in w)/n
    print(f'{n}y {w[0]}-{w[-1]}: {lo:6.1f} / {hi:6.1f}   {100*lo/CAP:5.2f}% / {100*hi/CAP:5.2f}%')
print('\nRolling five-year windows')
for i in range(len(ys)-4):
    w = ys[i:i+5]
    print(w[0], w[-1], round(sum(oe[y][0] for y in w)/5,1), round(sum(oe[y][1] for y in w)/5,1))
print('\nTwo-year carry test on the five-year window FY2021-25')
w = ys[-5:]
for k in (0,1):
    tot = sum(oe[y][k] for y in w)
    shares = {y: round(100*oe[y][k]/tot,1) for y in w}
    best2 = sorted((oe[y][k] for y in w), reverse=True)[:2]
    print(['capex','depr'][k], 'sum', round(tot,1), shares, 'best two', round(sum(best2),1), 'exceed sum?', sum(best2) > tot)
print('\nThree-year window FY2023-25 two-year test')
w = ys[-3:]
for k in (0,1):
    tot = sum(oe[y][k] for y in w); print(['capex','depr'][k], {y: round(100*oe[y][k]/tot,1) for y in w})
print('\nInterest on customer balances inside OE (pre-tax), 2023-2025:', [d[y][7] for y in (2023,2024,2025)])
for y in (2023,2024,2025):
    print(y, 'OE capex end less interest on customer balances', round(oe[y][0]-d[y][7],1), 'depr end', round(oe[y][1]-d[y][7],1))
print('\nSBC share of OCF', {y: round(100*d[y][1]/d[y][0],0) for y in d if d[y][0]>0})
