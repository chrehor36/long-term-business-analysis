p='q2.md'
s=open(p,encoding='utf-8').read()
R=[
("Item 1A, FY2011 to FY2025: *\"We compete with","Item 1A, every 10-K FY2006-FY2025: *\"We compete with"),
("*\"Our products primarily compete on the basis of capability, product quality, cost, and delivery\"* (FY2011-FY2025)","*\"Our products primarily compete on the basis of capability, product quality, cost, and delivery\"*"),
("in 2021 *\"net changes in selling price and raw material co st of 4.8%\"* [sic, as extracted]","in 2021 (FY2021 10-K) *\"net changes in selling price and raw material co st of 4.8%\"* [sic: a split word in the extracted text, not smoothed]"),
("**Freightliner** was a major customer in FY2006 and is not named in any later major-customer list read.","**Freightliner**, a major customer in FY2006, fell below 10% of sales in 2007 (*\"in 2007 Freightliner's individual sales represented less than ten percent\"*, FY2007 10-K) and is not named as a major customer again; the filings read do not say why, and 2007 was a truck downturn, so it is recorded as turnover, not as re-sourcing."),
("Universal Forest Products was a major customer in FY2018 and is not named after.","Universal Forest Products was a major customer in FY2018 only. **Volvo is the one case where the filing says in terms that the business moved to programmes the company does not supply.**"),
("Freightliner, Universal Forest Products and Volvo's existing programmes gone.","Volvo's existing programmes gone to programmes the company *\"does not support\"*; the major-customer list turning over (Freightliner, Universal Forest Products)."),
]
for a,b in R:
    assert s.count(a)==1,a
    s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s)
run='../2026-09-26 Run - CMT Core Molding Technologies.md'
t=open(run,encoding='utf-8').read()
if '## Q2' not in t:
    open(run,'w',encoding='utf-8').write(t.rstrip('\n')+'\n'+s)
print('ok')
