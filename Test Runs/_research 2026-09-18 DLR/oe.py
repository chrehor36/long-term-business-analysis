# Owner earnings, hand-built from the filed cash-flow statements (never a net-income proxy). $M.
Y = list(range(2016, 2026))
ocf = dict(zip(Y, [911.2,1023.3,1385.3,1513.8,1706.5,1702.2,1659.4,1634.8,2261.5,2412.1]))
sbc = dict(zip(Y, [17.4,20.5,27.2,34.9,74.6,84.1,92.5,80.5,75.6,93.8]))
da  = dict(zip(Y, [699.3,842.5,1186.9,1163.8,1366.4,1486.6,1577.9,1694.9,1771.8,1894.6]))
plantdep_cf = {2016:518.7,2017:595.0,2018:770.3,2019:809.5,2020:1010.5}           # CF line: buildings, improvements, TIs, ground leases
intang = {2019:271.4,2020:266.2,2021:262.9,2022:253.3,2023:252.0,2024:240.4,2025:231.3}  # acquired-intangible amortization (notes)
pref = dict(zip(Y, [83.8,68.8,81.3,75.0,76.5,45.8,40.7,40.7,40.7,40.7]))
nci  = {2022:11.9,2023:39.4,2024:47.0,2025:63.6}                                   # Teraco minority share of FFO (10-K footnotes)
rec  = {2020:210.7,2021:217.1,2022:266.5,2023:327.0,2024:305.7,2025:343.9}         # company "recurring capital expenditures"
imprv= dict(zip(Y, [758.1,1150.6,1325.2,1436.9,2064.1,2520.8,2643.1,3525.6,2831.7,3181.2]))
impair = {2023:118.4,2024:191.2,2025:78.6}
gains = dict(zip(Y, [169.9,40.4,80.0,335.1,316.9,1380.8,176.8,900.5,595.8,995.6]))
units = {2020:270.497,2021:289.912,2022:292.528,2023:305.138,2024:329.899,2025:346.086}  # wtd diluted shares and units (supplements)
UPLIFT = 14.4/12.6   # Q2 2026 pipeline cost per MW over FY2021-25 pipeline average (supplements)
IMP = sum(impair.values())/3
plant = {y: (da[y]-intang[y]) if y in intang and y >= 2021 else plantdep_cf.get(y) for y in Y}
base = {y: ocf[y]-sbc[y]-pref[y]-nci.get(y,0) for y in Y}
print("year  base  plantdep  OE_company(c)  OE_central  OE_conservative  OE_allcapex  gains  OEc/unit")
rows = {}
for y in Y:
    oc = base[y]-rec[y] if y in rec else None
    ce = base[y]-plant[y]
    co = base[y]-(plant[y]*UPLIFT+IMP)
    ac = base[y]-imprv[y]
    rows[y] = (oc, ce, co, ac)
    pu = ce/units[y] if y in units else None
    print(y, round(base[y],1), round(plant[y],1), None if oc is None else round(oc,1), round(ce,1), round(co,1), round(ac,1), gains[y], None if pu is None else round(pu,2))
def mean(ys, i): return sum(rows[y][i] for y in ys)/len(ys)
for nm, ys in [("5y FY2021-25", range(2021,2026)), ("3y FY2023-25", range(2023,2026)), ("10y FY2016-25", range(2016,2026))]:
    ys = list(ys)
    print(nm, "company", round(mean([y for y in ys if y in rec], 0),1) if all(y in rec for y in ys) else "n/a", "central", round(mean(ys,1),1), "conservative", round(mean(ys,2),1), "all-capex", round(mean(ys,3),1), "gains mean", round(sum(gains[y] for y in ys)/len(ys),1))
# TTM to 2026-06-30
ttm_ocf = 2412.1 + 1595.2 - 1040.3; ttm_sbc = 93.8 + 54.3 - 45.9; ttm_da = 1894.6 + 1006.6 - 904.2
print("TTM ocf", round(ttm_ocf,1), "sbc", round(ttm_sbc,1), "da", round(ttm_da,1), "base(ex pref 40.7, nci ~63.6)", round(ttm_ocf-ttm_sbc-40.7-63.6,1), "central (intangibles at FY2025 231.3)", round(ttm_ocf-ttm_sbc-40.7-63.6-(ttm_da-231.3),1))
print("UPLIFT", round(UPLIFT,3), "IMP mean", round(IMP,1))
