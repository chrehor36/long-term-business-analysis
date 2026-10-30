# Owner cash for JUTOY (Jutal Offshore Oil Services, HKEX 03303), RMB thousands, from the filed
# consolidated statements of cash flows in each annual report (HKEX file refs in notes.md).
# Each year's figures are taken from that year's report except CFO 2014, which uses the
# comparative restated in the FY2015 report (56,665 against 56,076 as first filed).
# Arithmetic only. No judgment is made here.

Y = list(range(2014, 2026))
# cfo: net cash from operating activities as filed (after interest paid and tax paid; HKFRS, interest paid in operating)
cfo   = dict(zip(Y, [56665, 74354, 2195, -158179, -650578, 148754, 798332, 78546, -125362, 287139, 477366, -52856]))
capex = dict(zip(Y, [122194, 40375, 25236, 9598, 51809, 141428, 146902, 82271, 46551, 25571, 139169, 197285]))
intang= dict(zip(Y, [739, 1185, 749, 1171, 3596, 1830, 7062, 829, 0, 0, 0, 0]))
rou   = dict(zip(Y, [0, 0, 0, 0, 0, 1765, 87, 0, 0, 0, 0, 0]))         # payments for right-of-use assets (land)
disp  = dict(zip(Y, [1372, 898, 1168, 7093, 2364, 598, 8144, 758, 218, 3157, 2575, 991]))
grant = dict(zip(Y, [8000, 22754, 9458, 29903, 11908, 23179, 12533, 6737, 3936, 4184, 9688, 61954]))  # government grants received (investing)
deriv = dict(zip(Y, [0, 763, -3660, 238, 9489, 1176, 13388, 8326, 8529, -29715, -11383, -3702]))   # FX derivative settlements (contract hedges)
lease = dict(zip(Y, [0, 0, 0, 0, 0, 10944, 14728, 10729, 9677, 8173, 7767, 8400]))  # principal elements of lease payments
intpd = dict(zip(Y, [16265, 9933, 7999, 9314, 44801, 32795, 27031, 22935, 25082, 18601, 7592, 4037]))  # interest paid (in CFO)
intrc = dict(zip(Y, [725, 842, 363, 4878, 13055, 6333, 11296, 10019, 4719, 13409, 14673, 7559]))   # interest received (investing)
sales = dict(zip(Y, [950881, 658566, 721614, 724469, 1485964, 1760624, 3647183, 3981612, 1750927, 2591773, 2079022, 799930]))
dep   = dict(zip(Y, [25256+65+1777, 28389+65+1176, 31490+65+1150, 31105+65+1302, 121848+65+780, 103322+23478+1079,
                     128645+27389+1345, 143913+22724+2009, 133390+21466+1928, 115417+20150+1716, 95775+18787+1311, 93608+19174+1119]))
npat  = dict(zip(Y, [28456, 26714, 11586, 55581, 26637, 4424, 146712, 11024, -208234, 254989, 185066, 45838]))
equity= dict(zip(Y, [1126369, 1157495, 1180542, 2058934, 2133016, 2150993, 2249345, 1805467, 1747247, 2011739, 2175401, 2187750]))
eq2013 = 1018554

def oc_equity(y):   # owner cash after interest (equity-only basis), all spending deducted
    return cfo[y] - capex[y] - intang[y] - rou[y] + disp[y] + grant[y] + deriv[y] - lease[y] + intrc[y]
def oc_allequity(y):  # owner cash before interest (all-equity basis): add back interest paid, drop interest received
    return oc_equity(y) - intrc[y] + intpd[y]

def avg(xs): return sum(xs) / len(xs)

print("year   sales     CFO   capex  OC_eq  OC_ae   dep    NPAT  ROE%")
prev = eq2013
for y in Y:
    roe = 100 * npat[y] / ((prev + equity[y]) / 2); prev = equity[y]
    print(f"{y} {sales[y]/1e3:7.0f} {cfo[y]/1e3:7.0f} {capex[y]/1e3:6.0f} {oc_equity(y)/1e3:6.0f} {oc_allequity(y)/1e3:6.0f} {dep[y]/1e3:5.0f} {npat[y]/1e3:6.0f} {roe:5.1f}")

W = [2021, 2022, 2023, 2024, 2025]
print("\nwindow 2021-2025 avg OC_ae", avg([oc_allequity(y) for y in W]) / 1e3, " OC_eq", avg([oc_equity(y) for y in W]) / 1e3)
print("12y 2014-2025 avg OC_ae", avg([oc_allequity(y) for y in Y]) / 1e3, " OC_eq", avg([oc_equity(y) for y in Y]) / 1e3)
for a, b in [(2018, 2021), (2019, 2022), (2020, 2023), (2021, 2024), (2022, 2025), (2014, 2017), (2014, 2019), (2020, 2025)]:
    yy = list(range(a, b + 1))
    print(f"avg {a}-{b} OC_ae {avg([oc_allequity(y) for y in yy])/1e3:7.1f}  OC_eq {avg([oc_equity(y) for y in yy])/1e3:7.1f}  sales {avg([sales[y] for y in yy])/1e3:7.0f}")
print("sum NPAT 2014-2025", sum(npat.values()) / 1e3, " avg equity", avg([eq2013] + [equity[y] for y in Y]) / 1e3)
print("max OC_ae/sales", max(oc_allequity(y) / sales[y] for y in Y))
# halves of the window (spec (b) where the series changes sign)
h1 = avg([oc_allequity(y) for y in [2021, 2022]]); h2 = avg([oc_allequity(y) for y in [2024, 2025]])
print("window halves OC_ae 2021-22", h1 / 1e3, " 2024-25", h2 / 1e3)
