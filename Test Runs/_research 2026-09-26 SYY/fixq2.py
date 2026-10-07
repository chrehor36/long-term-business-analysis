p=r'C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-09-26 Run - SYY Sysco.md'
s=open(p,encoding='utf-8').read()
R=[
("FAILS, in the registrant's own words, in every 10-K from FY2015 to FY2026, and in its two nearest rivals' words.",
 "FAILS, in the registrant's own words (the switching sentence in every 10-K from FY2014 to FY2026, thirteen running, counted by grep; absent in FY2009-FY2013), and in its rivals' words."),
("and US Foods' in six of the eight overlapping pairs.", "and US Foods' in seven of the eight pairs as aligned (the exception FY2021 against the pandemic calendar year 2020)."),
("and the tangible-return gap from 15-21 points (2016-2019) to nothing", "and the tangible-return gap from 15-18 points (2016-2019) to nothing"),
("the tangible-return lead of 15-21 points in 2016-2019 is gone", "the tangible-return lead of 15-18 points in 2016-2019 is gone"),
("own-brand margin is available to every broadliner (US Foods and PFG both sell private labels as their *\"most profitable products\"*, US Foods 10-K)",
 "own-brand margin is available to every broadliner (US Foods: *\"our private label products, which are our most profitable products\"*; PFG: *\"Performance Brands\"), which are our higher margin products\"*)"),
("and the registrant says in twelve consecutive 10-Ks that its customers can and do, *\"very quickly\"*.",
 "and the registrant says in thirteen consecutive 10-Ks that its customers can switch, *\"very quickly\"*."),
("**[E3-03] criterion (2) fails in the registrant's own 10-K, FY2015 to FY2026**", "**[E3-03] criterion (2) fails in the registrant's own 10-K, every year FY2014 to FY2026**"),
]
for a,b in R:
    assert s.count(a)==1,(a[:60],s.count(a)); s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s); print('ok')
