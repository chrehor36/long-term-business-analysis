p='_beneath.md'
t=open(p,encoding='utf-8').read()
reps=[
("The 2012 purchase of 10.4M shares from Leucadia for $427.4M (Q2's capital footnote) is recorded, not analysed.",
 "The September 2012 purchase from Leucadia National (10.4M shares, 20.8M after the 2014 split, *\"at a total cost of $427.3 million\"*, FY2014 10-K) is recorded, not analysed."),
("and the 2013 insurance settlement ($106.3M, the fires at the U.K. and Fulton, Mississippi tube mills, FY2010 and FY2013 10-Ks)",
 "and the insurance settlements for mill fires (U.K. 2008 and Fulton, Mississippi 2009, $22.7M recognised in 2010; Wynne, Arkansas, *\"the September 2011 fire\"*, a $106.3M gain in 2013)"),
("$5.0-32.4M a year in 2008-2013 (the 2008 U.K. and 2009 Fulton mill fires)",
 "$5.0-32.4M a year in 2008-2013 (the 2008 U.K., 2009 Fulton and 2011 Wynne mill fires)"),
("and every window of eight years or more is under 3%.","and every window of nine years or more is under 3%."),
("over twenty years, 1-2% of sales)","over twenty years, about 1-3% of sales)"),
("(0.60 in 2006-2010, 1.17 in 2011-2015, 1.14 in 2016-2020, 1.37 in 2021-2025) and 1-2% of sales;","(0.60 in 2006-2010, 1.17 in 2011-2015, 1.14 in 2016-2020, 1.37 in 2021-2025) and about 1-3% of sales;"),
]
for a,b in reps:
    assert t.count(a)==1,a[:50]
    t=t.replace(a,b)
open(p,'w',encoding='utf-8').write(t)
print('ok')
