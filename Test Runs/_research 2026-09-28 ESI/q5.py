# COMPUTATION — NOT A CLEARANCE until Q1-Q4 close. Arithmetic only.
SH=243690914; P=35.12; CAP=P*SH/1e6; BOND=0.0549; FLOOR=0.10
W={'5y FY2021-25 capex':237.8,'5y FY2021-25 dep':252.2,'7y FY2019-25 capex':222.8,'7y FY2019-25 dep':229.5,'3y FY2023-25 capex':239.6,'3y dep':259.5,'TTM capex':69.2,'TTM dep':104.6}
org={2019:-4,2020:-3,2021:13,2022:5,2023:-5,2024:4,2025:6}
g7=sum(org.values())/7; g6=sum(v for k,v in org.items() if k>=2020)/6
print(f'cap {CAP:.1f}; organic mean FY2019-25 {g7:.2f}%, FY2020-25 {g6:.2f}%')
for k,oe in W.items():
    y=oe/CAP; greq=(FLOOR*CAP-oe)/(CAP+oe)
    ps=lambda v: v/ (SH/1e6)
    out=[f"{k}: OE {oe:.1f} yield {100*y:.2f}% pts vs bond {100*(y-BOND):+.2f} | g needed for 10% {100*greq:.2f}%"]
    out.append(f"  no growth: floor ${ps(oe/FLOOR):.2f} bond ${ps(oe/BOND):.2f}")
    for g in (g7/100,g6/100,0.05):
        out.append(f"  floor g={100*g:.2f}%: ${ps(oe*(1+g)/(FLOOR-g)):.2f}")
    out.append(f"  expectancy yield+g: {100*y+g7:.2f}% to {100*y+g6:.2f}%")
    print('\n'.join(out))
for band,oe,g in [('rerun: 5y dep end, 5% growth, floor',252.2,0.05),('floor: 5y capex end, record organic, floor',237.8,g6/100)]:
    print(band, f"${oe*(1+g)/(FLOOR-g)/(SH/1e6):.2f}")
