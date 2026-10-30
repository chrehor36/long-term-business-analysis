p='Test Runs/2026-09-28 Run - GWW W.W. Grainger.md'
s=open(p,encoding='utf-8').read()
R=[
("The competition paragraph was read in all thirty-two 10-Ks on EDGAR that carry it (FY1993-FY2025; FY2000's paragraph did not extract as a block and was checked by line):",
 "The competition paragraph was read in all thirty-three 10-Ks on EDGAR (FY1993-FY2025; thirty-two extracted as a block, FY2000's checked by line, where it reads *\"competitive pricing\"* at line 434 of the extraction):"),
("Gross margin stayed 4-5 points below FY2012-FY2014 (35.9-39.4% against 43.3-43.8%)","Gross margin stayed 4 to 8 points below FY2012-FY2014 (35.9-39.4% against 43.3-43.8%)"),
("It continued to FY2013-FY2014 (U.S. segment margin 17.6-18.2%; filed price contribution +3% in FY2011-FY2012, +1% in FY2013-FY2014).",
 "It continued to FY2013-FY2014 (U.S. segment margin 17.6-18.2%; filed price contribution +2-3% in FY2011-FY2012, +1% in FY2013-FY2014)."),
("**Operating-expense ratio against Fastenal: within about one point in every year 2011-2025** (e.g. 2013 30.1% / 30.3%, 2019 27.3% / 27.3%, 2024 24.0% / 25.1%); Fastenal's gross margin is **5.9 to 9.1 points higher** in every year.",
 "**Operating-expense ratio against Fastenal: within 1.5 points in every year 2011-2025 except 2020** (Grainger / Fastenal: 2011 30.4% / 31.1%, 2013 30.1% / 30.3%, 2016 29.5% / 29.5%, 2019 27.3% / 27.3%, 2020 27.3% / 25.3%, 2021 24.4% / 25.9%, 2022 23.9% / 25.2%, 2024 24.0% / 25.1%, 2025 25.2% / 24.8%; Grainger's lower by 1.0-1.5 points in 2021-2024, a narrow lead, and higher by two points in 2020); Fastenal's gross margin is **5.7 to 10.0 points higher** in every year 2009-2025."),
("Return on tangible operating assets: Grainger highest of the three national distributors over seventeen years (40.8% against 38.8% and 37.7%) and clearly highest in 2022-2025 (44-55% against 40-44%); Global Industrial higher in several years on a very small asset base.",
 "Return on tangible operating assets: Grainger highest of the three national distributors over seventeen years (40.8% against 38.8% and 37.7%) and highest in each year 2021-2025 (40.6-54.8% against Fastenal's 37.0-44.2%; 44.3% against 42.8% in 2025); Global Industrial higher in several years on a very small asset base."),
("it has **no cost advantage over Fastenal** (the same operating-expense ratio, year after year)","it has **no wide cost advantage over Fastenal** (operating-expense ratios within 1.5 points in fourteen of fifteen years, Grainger's lower by 1.0-1.5 points only since 2021)"),
("High-Touch Solutions N.A. (78% of sales, 94% of segment earnings)","High-Touch Solutions N.A. (78% of sales, 87% of segment operating earnings)"),
("**not wide** (no cost advantage over Fastenal in any year; a margin behind it in every year)","**not wide** (against Fastenal, operating-expense ratios within 1.5 points in fourteen of fifteen years and a margin behind it in every year)"),
("Against it: the exception's test is a cost advantage over the rivals, and the filed row gives Grainger none over Fastenal, the rival its own peers name beside it;",
 "Against it: the exception's test is a cost advantage over the rivals, and the filed row gives Grainger none of width over Fastenal, the rival its own peers name beside it (a 1.0-1.5 point lower expense ratio since 2021 against a 5.7-10.0 point lower gross margin in every year);"),
("and in FY2019 lost gross margin to *\"the impact of contract renegotiations and customer mix\"*","and in FY2019 lost U.S. gross margin to *\"the impact of contract renegotiations and customer mix\"*"),
("and the last five files closed there (TCMD, DTM, OPXS, TXRH; AIT, the nearest trade, the day before), which is a pull toward pattern;",
 "and the last four files closed there (TCMD, DTM, OPXS, TXRH), as did AIT, the nearest trade, the day before, which is a pull toward pattern;"),
("I read the competition paragraph in all thirty-two annual reports rather than the newest","I read the competition paragraph in all thirty-three annual reports rather than the newest"),
("with no cost advantage over Fastenal at all: **OUT**","with no cost advantage of width over Fastenal: **OUT**"),
("the margin since rebuilt is cost and inflation-year price at a gross margin 4-5 points below FY2012-FY2014.","the margin since rebuilt is cost and inflation-year price at a gross margin 4.1-4.7 points below FY2012-FY2014 in FY2023-FY2025."),
("behind Fastenal on EBIT margin in all seventeen years 2009-2025 with the same operating-expense ratio,","behind Fastenal on EBIT margin in all seventeen years 2009-2025 with an operating-expense ratio within 1.5 points of Fastenal's in fourteen of fifteen years,"),
("*(Consolidated rows from each year's income statement or the percent-of-sales table in the next 10-K (FY1994: 100 − 64.5 − 27.9, including restructuring; FY2000 on the EITF 00-10 basis); gross margin from FY2002 on the basis restated in the FY2004 10-K (earlier years are on other bases and are not set beside these). Segment row: the U.S. segment FY2008-FY2019 (FY2008 and FY2009 from the FY2009 10-K, FY2016-FY2017 as restated in the FY2018 10-K), High-Touch Solutions N.A. (U.S. and Canada) FY2020-FY2025.",
 "*(Consolidated rows from each year's income statement or the percent-of-sales table in the next 10-K (FY1994: 100 − 64.5 − 27.9, including restructuring; FY2000 on the EITF 00-10 basis); gross margin from FY2002 on the basis restated in the FY2004 10-K (earlier years are on other bases and are not set beside these). Segment row: the U.S. segment FY2008-FY2019 from the segment notes and MD&A of the following years' 10-Ks (FY2016-FY2017 as restated in the FY2018 10-K), High-Touch Solutions N.A. (U.S. and Canada) FY2020-FY2025 from the FY2021-FY2025 MD&A."),
]
for a,b in R:
    assert s.count(a)==1,(a[:60],s.count(a))
    s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s)
print('ok')
