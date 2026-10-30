# All figures in $ thousands, read off the FILED consolidated statements of cash flows.
# FY2018-19: FY2020 10-K. FY2020-22: FY2022 10-K. FY2023-25: FY2025 10-K. H1: 2026-06 10-Q.
d = {
2018:dict(ocf=-91948, sbc=168482, capex=45205, da=53887, dep=-21774),
2019:dict(ocf=163770, sbc=196291, capex=51053, da=78584, dep=37146),
2020:dict(ocf=-98796, sbc=73893, capex=37913, da=52279, dep=-12972),
2021:dict(ocf=-60681, sbc=73274, capex=49810, da=53454, dep=-22677),
2022:dict(ocf=-191723, sbc=112259, capex=116823, da=61608, dep=35156),
2023:dict(ocf=-372531, sbc=84480, capex=83739, da=62609, dep=-42635),
2024:dict(ocf=91998, sbc=82424, capex=58852, da=53048, dep=139868),
2025:dict(ocf=113949, sbc=139406, capex=56759, da=50566, dep=-142605),
}
h1_26=dict(ocf=300042, sbc=100432, capex=77823, da=27025, dep=301232)
h1_25=dict(ocf=-323793, sbc=59338, capex=21504, da=24582, dep=-178807)
ttm={k: d[2025][k] - h1_25[k] + h1_26[k] for k in d[2025]}
print("OWNER EARNINGS BY YEAR ($ thousands), CONVENTION: OCF - SBC - (c)")
print(f"{'yr':8} {'OCF':>10} {'SBC':>9} {'capex':>8} {'D&A':>8} | {'OE capex end':>13} {'OE D&A end':>12} | {'deposit line':>13} {'OCF ex-dep':>11}")
rows=list(d.items())+[('TTM',ttm)]
for y,v in rows:
    oe1=v['ocf']-v['sbc']-v['capex']; oe2=v['ocf']-v['sbc']-v['da']
    print(f"{str(y):8} {v['ocf']:10,} {v['sbc']:9,} {v['capex']:8,} {v['da']:8,} | {oe1:13,} {oe2:12,} | {v['dep']:13,} {v['ocf']-v['dep']:11,}")
print()
print("EVERY WINDOW [E4-38] - mean owner earnings, $ thousands")
wins={'FY2018-25 (8y)':range(2018,2026),'FY2019-25 (7y)':range(2019,2026),'FY2021-25 (5y, corpus default E2-42)':range(2021,2026),
      'FY2022-25 (4y)':range(2022,2026),'FY2023-25 (3y)':range(2023,2026),'FY2024-25 (2y)':range(2024,2026),'FY2025 (1y)':range(2025,2026)}
allv=[]
for n,r in wins.items():
    ys=[y for y in r]
    a=sum(d[y]['ocf']-d[y]['sbc']-d[y]['capex'] for y in ys)/len(ys)
    b=sum(d[y]['ocf']-d[y]['sbc']-d[y]['da'] for y in ys)/len(ys)
    allv+= [a,b]
    print(f"  {n:40} capex end {a:12,.0f}   D&A end {b:12,.0f}")
t1=ttm['ocf']-ttm['sbc']-ttm['capex']; t2=ttm['ocf']-ttm['sbc']-ttm['da']
allv+=[t1,t2]
print(f"  {'TTM to 2026-06-30 (1y)':40} capex end {t1:12,.0f}   D&A end {t2:12,.0f}")
print()
print(f"WIDTH ACROSS EVERY WINDOW AND BOTH (c) ENDS: {min(allv):,.0f} to {max(allv):,.0f}  = width {max(allv)-min(allv):,.0f}")
print()
print("SCREEN BAND REPRODUCTION TEST (SBC set to ZERO, as the XBRL fetch does):")
z5=sum(d[y]['ocf']-d[y]['capex'] for y in range(2021,2026))/5
z3=sum(d[y]['ocf']-d[y]['da'] for y in range(2023,2026))/3
print(f"  5y FY2021-25 capex end, SBC omitted: {z5:,.0f}   (screen oe_bottom_m -157)")
print(f"  3y FY2023-25 D&A  end, SBC omitted: {z3:,.0f}   (screen oe_top_m    -111)")
print()
cap=294527346*275.75/1000
print(f"CAP $k {cap:,.0f}")
for lbl,v in [('best window/end (TTM D&A)',t2),('TTM capex end',t1),('5y default capex end',sum(d[y]['ocf']-d[y]['sbc']-d[y]['capex'] for y in range(2021,2026))/5)]:
    print(f"  yield on {lbl:28} = {v/cap*100:7.2f}%")
print()
print("NET OF THE DEPOSIT LINE - owner earnings if the deferred-revenue-and-customer-deposit")
print("inflow is removed from operating cash (capex end):")
for y,v in rows:
    print(f"  {str(y):8} {v['ocf']-v['dep']-v['sbc']-v['capex']:12,}")
