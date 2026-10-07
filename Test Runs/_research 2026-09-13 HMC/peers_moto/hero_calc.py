# Hero MotoCorp standalone, INR crore. EBITDA FY22-24 = directors' report margin x revenue (rounded %), and FY26-AR chart values; FY25/26 EBITDA exact from directors' report.
rev = {"FY22": 29245.47, "FY23": 33805.65, "FY24": 37455.72, "FY25": 40756.37, "FY26": 46830.14}
ebitda_chart = {"FY22": 3369, "FY23": 3986, "FY24": 5256, "FY25": 5868, "FY26": 6871}
ebitda_exact = {"FY25": 5867.67, "FY26": 6870.76}
da = {"FY22": 649.75, "FY23": 656.96, "FY24": 711.41, "FY25": 775.86, "FY26": 798.00}
opm_reported = {"FY22": 9.30, "FY23": 9.85, "FY24": 12.13, "FY25": 12.49, "FY26": 12.97}
for y in rev:
    e = ebitda_exact.get(y, ebitda_chart[y])
    op = e - da[y]
    print(f"{y}: EBITDA {e:,.2f} / rev {rev[y]:,.2f} = {100*e/rev[y]:.2f}% | (EBITDA - D&A) {op:,.2f} / rev = {100*op/rev[y]:.2f}% vs reported OPM {opm_reported[y]}%")
