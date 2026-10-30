p='frag_q2.md'; s=open(p,encoding='utf-8').read()
R=[
("*\"Our principal competitors include ABB, Eaton, GE, Schneider Electric and Siemens\"* (FY2009-FY2011; GE dropped from FY2019)",
 "*\"Our principal competitors include ABB, Eaton Corporation, GE, Schneider Electric and Siemens\"* (FY2009-FY2011; GE named through FY2017 and dropped from FY2018; *\"ABB, Eaton, Schneider, and Siemens Industries, Inc.\"* FY2024-FY2025)"),
("and *\"Certain of our competitors may have lower cost structures and may, therefore, be able to provide their products or services at lower prices than we are able to provide\"* (FY2013-FY2018; FY2021-FY2025 with *\"at lower prices\"*).",
 "and *\"Certain of our competitors may have lower cost structures and may, therefore, be able to provide their products or services at lower prices than we are able to provide\"* (FY2013-FY2018; the clause *\"may, therefore, be able to provide their products or services at lower prices\"* is in every 10-K FY2007-FY2025, checked by `q2check.py`; FY2025 adds *\"or a more favorable geographic footprint\"*)."),
("**Twenty-two of the twenty-five filed years sit between −5% and 9% operating (or the pre-tax and net equivalents); the three that do not are the last three.**",
 "**Twenty-three of the twenty-five filed years sit between −4.9% and 9.3% operating (or the pre-tax and net equivalents; FY2006 is an eleven-month transition period, 10-KT); the two above that range are the last two, FY2024 and FY2025, and nine months of FY2026 (19.1%) continue them.**"),
("Twenty-five filed years give that ratio for this company: three tight years to twenty-two ample ones, so far.",
 "Twenty-five filed years give that ratio for this company, so far: two full years and a third in progress above the range, twenty-three inside it."),
("- **[E4-04]:** not the ground. The products are mature (480 volts to 38 kilovolts, the same list in FY2002 and FY2025);",
 "- **[E4-04]:** not the ground. The products are mature (switchgear and breakers from 480 volts, described in every 10-K since FY2002);"),
("the filings show the upturn is the aberrational part of the record, twenty-two years to three.",
 "the filings show the upturn is the aberrational part of the record, twenty-three years to two and a part."),
("*\"Revenues | 1,104,315\"* … *\"Operating income | 217,864\"* (19.73%)", "*\"Revenues | 1,104,318\"* and *\"Operating income | 217,860\"* (19.73%)"),
("| ABB (CY, 20-F to 2023) |", "| ABB (CY, 20-F to 2023; Form 15F-12B filed since, deregistered) |"),
("named competitor; consolidated, IFRS, deregistered after 2023; Electrification segment not separated here |", "named competitor, SIC *\"Switchgear & Switchboard Apparatus\"* like Powell; consolidated, IFRS; Electrification segment not separated here |"),
("| data-centre power and cooling; consolidated |", "| SIC *\"Electronic Components, NEC\"*; consolidated; business not read in its filing |"),
("| balance tags not resolved | electrical enclosures and connections; consolidated |", "| balance tags not resolved | SIC *\"Special Industry Machinery\"*; consolidated; business not read in its filing |"),
("| electrical contractor with a switchgear-making segment; consolidated |", "| SIC *\"Electrical Work\"* (a contractor); consolidated; business not read in its filing |"),
("**named competitors, not SEC filers** (`cik_for` returned none; Siemens deregistered in 2014); not entered", "**named competitors, not SEC filers** (`cik_for` returned none for SIEGY; Schneider has no US listing); not entered"),
("**OUT, on the business.** [E3-03] criterion (2) fails in the registrant's own words: each project is competitively bid, non-recurring, against ABB, Eaton, Schneider and Siemens, who *\"may ... be able to provide their products or services at lower prices\"*;",
 "**OUT, on the business.** [E3-03] criterion (2) fails in the registrant's own words: each project is competitively bid, non-recurring, against ABB, Eaton, Schneider and Siemens, who *\"may, therefore, be able to provide their products or services at lower prices\"*;"),
("Twenty-two of twenty-five filed years earned −5% to 9% operating; the last three earned 9-20% on a record backlog and tight supply,",
 "Twenty-three of twenty-five filed years earned −4.9% to 9.3% operating; FY2024-FY2025 earned 17.7% and 19.7% (and nine months of FY2026 19.1%) on a record backlog and tight supply,"),
("Typically, our contracts may have an early termination for convenience clause at the discretion of our customers; however, most of these contracts typically provide for the reimbursement of our costs incurred and a reasonable margin\"*.",
 "Typically, our contracts may have an early termination for convenience clause at the discretion of our customers; however, most of these contracts typically provide for the reimbursement of our costs incurred\"* and, across a page break in the filing, a reasonable margin."),
]
for a,b in R:
    assert s.count(a)==1, a[:80]
    s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s); print('ok')
