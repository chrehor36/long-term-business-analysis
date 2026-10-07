p='frag_beneath.md'; s=open(p,encoding='utf-8').read()
R=[
("Fifteen years old, disclosed by the filer, remediated in its later 10-Ks;",
 "Fifteen years old and disclosed by the filer; the FY2012 10-K reports *\"management has concluded that internal control over financial reporting was effective at the reasonable assurance level as of September 30, 2012\"*;"),
("Repurchases only in FY2015-FY2016 ($21.3M and $3.7M); none in the FY2017-FY2018 trough.",
 "Repurchases, in the tagged years FY2015-FY2018, only in FY2015-FY2016 ($21.3M and $3.7M); none in the FY2017-FY2018 trough."),
("Capex and depreciation are $3-15M a year in most years (FY2012-FY2015's $29-74M was the Canadian and Houston plant build; *\"Property, plant and equipment, net\"* rose from $78.5M at FY2012 to $156.9M at FY2014), and the two ends agree within a few million in every window of three years or more after FY2016. **(c) is a guess [E2-09] that barely matters here; the default [E3-44] holds**, with the capex end above depreciation only in FY2024-FY2025 as the capacity build begins.",
 "Capex and depreciation are $3-15M a year in most years (FY2012-FY2015's $29-74M was a plant build: net property rose from $78.5M at FY2012 to $156.9M at FY2014 in the FY2016 five-year table; its purpose not read here), and the two ends differ by about $10M or less in every window of three years or more that starts in FY2016 or later. **(c) is a guess [E2-09] that barely matters here; the default [E3-44] holds**, with capex above depreciation since FY2016 only in FY2024-FY2025 as the capacity build begins."),
("(1) Operating cash negative in seven of twenty-five years (FY2001, FY2005, FY2006, FY2008, FY2012, FY2018, FY2021, and −$3.6M in FY2022: eight, counting it); not a reliable stream through the cycle.",
 "(1) Operating cash negative in eight of twenty-five years (FY2001, FY2005, FY2006, FY2008, FY2012, FY2018, FY2021, FY2022); not a reliable stream through the cycle."),
("the word EBITDA does not appear in its headline bullets.", "the word EBITDA does not appear anywhere in it (`grep -c` returns 0)."),
]
for a,b in R:
    assert s.count(a)==1, a[:70]
    s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s); print('ok')
