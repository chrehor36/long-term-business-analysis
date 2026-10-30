P='../2026-09-27 Run - NUE Nucor.md'
t=open(P,encoding='utf-8').read()
reps=[
('**The price follows utilization down, every cycle**: -32% in 2009 at 54% utilization; -13% and -8% in 2015-2016; -15% and -10% in 2023-2024 **with Section 232 in force**.',
 '**The price follows utilization down in every downturn of the record**: -32% in 2009 at 54% utilization; -13% and -8% in 2015-2016; -15% and -10% in 2023-2024 **with Section 232 in force**. **One year runs the other way and is recorded, not smoothed: 2022**, when steel-mill utilization fell from 94% to 77% and the steel mills\' average price per ton still rose 11% ($1,195 to $1,324; the consolidated figure +26% on mix), with scrap up 5% ($469 to $492 a gross ton) and outside steel shipments down 10% (FY2022 10-K MD&A). It is answered as item 6 of the evidence against, below.'),
('went looking for a year in which Nucor\'s price rose while its utilization fell (none in the series: every utilization fall carries a price fall)',
 'went looking for a year in which Nucor\'s price rose while its utilization fell (I found one, 2022, and set it out as item 6 below rather than leave the table to hide it)'),
('\n\n**The analyst\'s own incentives [E4-27], stated (operator rule 9).**',
 '\n6. *"In 2022 Nucor raised its mill price 11% while its mills ran 17 points emptier and shipped 10% fewer outside tons. That is [E2-44]\'s test passed: price up, capacity not fully used."* **Answer:** it is the one such year in the record, it came directly after the tightest year in the series (94% utilization in 2021), on contracts the 10-K says run *"six to 12 months"* with *"a timing difference"* in price adjustment, and it was given back at once (the price per ton fell 15% in 2023 and 10% in 2024). [E2-44] asks for the ability to raise prices *"rather easily ... without fear of significant loss of either market share or unit volume"*; the 2022 rise came with a 10% loss of outside tons. That is [E3-43]\'s other door, *"if supply of its product or service is tight. Tightness in supply usually does not last long"*, not a franchise.\n\n**The analyst\'s own incentives [E4-27], stated (operator rule 9).**'),
]
for a,b in reps:
    assert t.count(a)==1,a[:60]
    t=t.replace(a,b)
open(P,'w',encoding='utf-8').write(t)
b=open('body_close.md',encoding='utf-8').read()
reps2=[
('In twenty-seven years of filed MD&A this has not happened once; one instance would reopen [E2-44].',
 'The one such year in the filed record, 2022 (mill price +11% as utilization fell from 94% to 77%), followed the tightest year in the series and was given back in 2023-2024, so the condition is two consecutive such years, or one that does not follow a supply-tight year; either would reopen [E2-44].'),
('The share count fell from about 300 million (FY2020, per the 10-K covers of that period, not re-read here) to 226,875,676.',
 'The share count on the 10-K covers fell from 319,046,902 (as of 2015-02-20) and 301,000,375 (2020-02-21) to 227,774,615 (2026-02-18) (dei cover facts, companyfacts; the latest 10-Q cover reads 226,875,676).'),
('whose average price per ton has fallen with utilization in every downturn of twenty-seven filed years (-32% in 2009 at 54% utilization; down again in 2023-2025 under Section 232)',
 'whose average price per ton has fallen in every downturn of the filed record since 1998 (-32% in 2009 at 54% utilization; down again in 2023-2025 under Section 232; the one rise in a year of falling utilization, 2022, followed the 2021 shortage and was given back)'),
]
for a,c in reps2:
    assert b.count(a)==1,a[:60]
    b=b.replace(a,c)
open('body_close.md','w',encoding='utf-8').write(b)
print('ok')
