import sys
p='body2.md'; s=open(p,encoding='utf-8').read()
R=[
("sold at rising US net prices for eleven years (*\"Sales growth in the U.S. reflects higher demand and net pricing\"*, 2025), with a gross margin near 75%, a Pharmaceutical segment margin before research of 79%, and a pre-tax return on net tangible operating assets above 50% in four of the last five years;",
 "sold at a rising US net price (*\"Sales growth in the U.S. reflects higher demand and net pricing\"*, 2025), with a gross margin near 75%, a Pharmaceutical segment margin before research of 79%, and a pre-tax return on net tangible operating assets near or above 50% in four of the last five years;"),
("*\"the Company has also agreed that products launched","*\"The Company has also agreed that products launched"),
("Merck's 10-K describes competition *\"from other major pharmaceutical companies\"* and biosimilar and generic makers without a list;",
 "Merck's 10-K names its competitors by class, not by name: *\"The Company’s competitors include other worldwide research-based pharmaceutical companies, smaller research companies with more limited therapeutic focus, generic drug manufacturers, and animal health care companies\"*;"),
("Roche, Bayer, Daiichi Sankyo, Takeda's Japanese filings beyond its 20-F, and the Chinese makers","Roche, Bayer, Daiichi Sankyo and the Chinese makers"),
("(Hengrui, Kelun, the local HPV vaccine maker).","(Hengrui, Kelun, the local HPV vaccine maker); Takeda files a 20-F and was not pulled."),
("**Merck sits in the upper half of the row on every return measure** (tangible 52-58% in 2024-2025; 26-28% including goodwill, behind only Lilly and Novo Nordisk and level with Johnson & Johnson and Novartis)",
 "**Merck sits in the upper half of the row on the return measures** (tangible 52-58% in 2024-2025; 26-28% including goodwill, third of thirteen in 2024 and fifth in 2025, behind Lilly, Novo Nordisk, Johnson & Johnson and Novartis)"),
("The 2011-2015 decline of 18% is the filer's *\"ongoing impacts of the loss of market exclusivity for several products\"* (10-K 2015);",
 "The 2011-2015 decline of 18% is, in part, the filer's *\"ongoing impacts of the loss of market exclusivity for several products\"* (10-K 2015; the same paragraph names a 6% currency effect in 2015 and the 2014 sale of Consumer Care);"),
("and state *\"laws [that] also require manufacturers to provide advance notification of price increases\"*","and the state laws (*\"Some laws also require manufacturers to provide advance notification of price increases.\"*)"),
("**$53.8bn of acquisitions in cash from 2019 to the first half of 2026**","**$65.4bn of acquisitions in cash from 2019 to the first half of 2026**"),
("its output since 2019 has been bought as often as discovered ($53.8bn in cash);","its output since 2019 has been bought as often as discovered ($65.4bn in cash);"),
("(*\"must continue to launch new products\"*; $53.8bn of acquisitions since 2019)","(*\"must continue to launch new products\"*; $65.4bn of acquisitions in cash since 2019)"),
("1. **The returns are very high and have been for most of the filed record**: a gross margin of 75-76%, a Pharmaceutical segment margin before research of 78.7%, a tangible pre-tax return above 50% in four of the last five years,",
 "1. **The returns are very high and have been for most of the filed record**: a gross margin of 74.8-76.3%, a Pharmaceutical segment margin before research of 78.7%, a tangible pre-tax return near or above 50% in four of the last five years,"),
("2. **US net prices have risen on the protected products** every year the MD&A describes, while volume also grew (*\"higher demand and net pricing\"*):",
 "2. **US net prices rose on the protected products** in 2025 while demand also grew (*\"higher demand and net pricing\"*, Keytruda; the same for Gardasil and the pediatric vaccines):"),
("the company survives each expiry;","the company survives each expiry; the lead product is being moved to a new form with a new patent (Keytruda Qlex, US expiry *\"2043\"* in the patent table, $463M of sales in the second quarter of 2026);"),
("the last eight wave 7 runs closed at Q2, which pulls toward OUT by habit;","fifteen of the last sixteen wave 7 runs (LNN to MDT; CHD the exception) closed at Q2, which pulls toward OUT by habit;"),
("(3) The machine argument is the strongest, and the filings answer it in the filer's own words:","(3) The machine argument is the strongest, and the filings answer it in the filer's own words; Keytruda Qlex does not change the filer's own expectation, which is dated in the same risk factor (*\"materially negatively impacted by biosimilar competition between 2028 and 2029\"*):"),
]
for a,b in R:
    n=s.count(a)
    if n!=1: print('COUNT',n,a[:80]); continue
    s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s); print('ok')
