# Company Run — Universal Technical Institute, Inc. (NYSE: UTI) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template before any fetch.

**POSITION NOTE, declared before any verdict:** not checked. This run was dispatched blind: `PORTFOLIO.md`, the holding
reviews, the session-state files, the run queue and the prepped reading list were not opened, and no other run file on
this company was opened (a directory listing of `Test Runs/` by name showed none with "UTI" in the title other than
unrelated tickers). Whether the operator holds or wants the name is unknown to this analyst. **Contamination declared:**
none noticed. One preconception is declared: the analyst knows from general reading that for-profit vocational schools
as a class have a history of regulatory trouble (the 2010 to 2016 Title IV actions against other operators); this was
written down before reading so that it could be tested against UTI's own filings rather than imported.

Working folder: `Test Runs/_research 2026-10-05 UTI/` (filings as stripped text, the tool outputs, the arithmetic script).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $19.34 (2026-10-05; `tools/run.py` live quote, **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock $0.0001 par, **55,095,231** shares (10-Q
  for the quarter to 2026-06-30, filed 2026-08-06, accession `0001261654-26-000018`; `python Screens/cover_shares.py UTI`).
  The Series A preferred that existed to FY2024 is gone: 19,297 thousand common shares were issued on its conversion and
  33 thousand preferred shares were repurchased for $11.6M including fees in FY2024 (statement of shareholders' equity, 10-K FY2025,
  accession `0001261654-25-000025`). No other class.
- **Market cap:** 55.10M x $19.34 = **$1,065.5M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, the 30-year par yield, US Treasury daily par yield curve,
  dated 2026-10-02 (`tools/run.py`, which reads the issuing authority through `tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for the year to 2025-09-30, filed 2025-11-26, accession
  `0001261654-25-000025`; 10-Q for the quarter to 2026-06-30, filed 2026-08-06, accession `0001261654-26-000018`; proxy
  DEF 14A filed 2026-01-20, accession `0001140361-26-001690`; 8-Ks of 2026-08-18 (new $200M secured revolver, accession
  `0001193125-26-354799`), 2026-08-05 (Q3 results, accession `0001261654-26-000015`), 2026-03-17 (code of conduct
  restated, no waiver, accession `0001193125-26-110942`); earlier 10-Ks for the history (FY2011, FY2015, FY2019, FY2022; accessions at Q1, test 3, and in the working folder).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, `tools/run.py`
  97 ($M, XBRL) against the filed cash-flow statement **$97,330 thousand** (10-K FY2025, accession `0001261654-25-000025`,
  F-10). Agrees. Capex FY2025 tool 42 against filed "Purchase of property and equipment (41,978)". Agrees.
- `python tools/run.py UTI` arithmetic lines only (the tool's rule text, ids and floor are v4 material and are ignored,
  Part VII): OCF FY2023 / FY2024 / FY2025 = 49 / 86 / 97 $M; SBC 4 / 9 / 9; D&A 25 / 29 / 33; capex 57 / 24 / 42. The
  tool's five-year window reports owner earnings 7 to 38 $M and its three-year window 28 to 43 $M; the owner cash used
  in this run is recomputed by hand in the COMPUTATION section from the filed statements, with the lease cash and the student-loan book
  treated explicitly.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would "be happy buying this stock if the market closed for five years"
**[M1997-109]**, which turns every later question into one about what these schools will earn, and that is the question Q1
below cannot answer. No macro forecast enters: "just never enter into the discussion" **[M2000-094]**. The company says its
enrollment "tends to be counter cyclical" (10-K FY2025, risk factor "Macroeconomic conditions and aversion to debt",
accession `0001261654-25-000025`), so no view on unemployment is taken here; the question that closes the file is political,
not macroeconomic, and the run keeps the two apart. Who is paid to tell you: the 10-K's market sizing ("approximately
111,100 new job openings" a year for automotive, diesel and collision technicians, from the BLS) is the seller describing
what it sells, and is read, not relied on. The rows' warning for it: "don’t ask the barber whether you need a haircut"
**[M2011-083]**. The company's own past forecasts are checked against what followed, as the speakers did when they "asked that the record of the
people who made the projections, their past projections also be presented" **[M1995-050]** (Q1, test 3).

**Contrary evidence, written down as found** **[M1997-127]** (the case against the close this run reaches, set down as it
came up, before the verdict):
1. The speakers record that they once overrated a regulatory threat: "we tended to overestimate the difficulties from
   regulation" **[M2004-058]**.
2. In a politically exposed business "economics usually win out" **[M2012-074]**, and the demand for trained technicians is
   real on the company's account: manufacturer-paid programs with Mercedes-Benz, Porsche, Peterbilt and Tesla, and "over
   9,100 employer location incentive opportunities" (10-K FY2025, Item 1).
3. The company has operated since 1965, returned to profit after FY2020, earned an operating margin of 10.0% in FY2025
   ($83.5M on $835.6M) and grew starts 10.8% in FY2025 and 9.5% in the nine months to June 2026 (10-K FY2025; 10-Q
   `0001261654-26-000018`).
4. Price can pay for some regulatory risk: "If a thing is cheap enough, obviously you can afford a little more country risk,
   or regulatory risk" **[M2004-083]**.
5. The 2025 law (OBBBA) and the Workforce Pell rulemaking may prove friendlier to short career programs than the rules of
   2010 to 2016; the 10-K says the effect "is unknown at this time", which cuts both ways.
6. "We cannot predict" is ordinary risk-factor language; test 5 below must not rest on a lawyer's sentence alone, and is
   therefore read together with the record of what the insiders forecast and what happened.
7. Found against the bull case while reading (written here as found, not saved for the end): UTI's three-year cohort
   default rates before the payment pause were 13.9% to 18.3% across its three institutions against 15.2% to 15.6% for all
   proprietary institutions (10-K FY2019, `0001261654-19-000060`), so its students defaulted at about the sector average;
   diluted earnings per share were about $1.10 in FY2011 and $1.13 in FY2025 while the diluted share count rose from 24.7M
   to 55.6M; the provision for credit losses rose from 0.55% of revenue (FY2023) to 2.65% (FY2025) and 3.39% (nine months
   to June 2026); operating margin fell from 9.5% to 2.9% in the nine months to June 2026 on growth spending; and about
   2,500 borrower-defense claims were lodged against pre-acquisition Concorde, a named school in the Sweet settlement.

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase is made with the buyer's own money, since "borrowed money has no place in
the investor's tool kit" **[L2014-005]**, and sized so that its total loss cannot reach what the buyer has and needs: "We are
never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**. Nothing about UTI changes
that. The question is moot here because the file closes at Q1; no position is contemplated.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in
five or 10 years" **[M2012-065]**; "our definition of understanding is thinking that we have a reasonable probability of
being able to asses where the business will be in 10 years" **[M2000-037]** ("asses" is the transcript's spelling). The
first step is "trying to identify the key variables in that particular business, and evaluating how predictable they were
first" and "If something is not very predictable, forget it." **[M1998-044]**.

**What the business is** (10-K FY2025, Item 1): two divisions of hands-on career schools. UTI: 15 campuses (17 by July
2026) teaching automotive, diesel, collision, motorcycle, marine, aviation, welding, HVACR, electrical and wind; FY2025
revenue $541.8M, average 14,913 full-time students, average revenue per student about $35,100. Concorde (bought
2022-12-01): 17 campuses (18 by June 2026) teaching allied health, dental, nursing and diagnostics; FY2025 revenue $293.8M,
average 9,705 students, about $30,000 a student. The product is understood. The question is the economics in ten years.

**The key variables and how predictable each is** **[M1998-044]**:
1. **Who pays, and on what terms.** "in fiscal 2025, across our institutions, we derived approximately 78% of our revenues,
   on a cash basis, from Title IV Programs and various veterans’ programs": Direct Loans about 43%, Pell about 23%,
   veterans' programs about 11% (10-K FY2025, Item 1, Title IV Programs). The 90/10 percentages of its institutions ranged
   "from approximately 67% to approximately 82%" for FY2025 (same). The terms are set by Congress and the Department of
   Education: the 2025 law added an earnings test for degree programs, limits on federal loans and new borrower-defense
   rules; two negotiated-rulemaking committees (RISE, AHEAD) were named in July 2025 to write the rest; the
   gainful-employment rule has applied since July 2024 to every program of a proprietary school; the HEA "has not been
   comprehensively reauthorized since 2008" (same section). The 90/10 rule itself now counts veterans' money on the federal
   side (Lincoln's 10-K for 2025 dates the change to fiscal years ending on or after 2023-01-01, accession
   `0001140361-26-007380`). This variable decides most of the revenue and is **not predictable**: it moves with elections,
   appropriations and rulemakings.
2. **Student demand.** Counter-cyclical by the company's account; not forecast here (foundations). Its swing is recorded at
   test 8.
3. **The cost of getting a student.** Advertising was 10.6% of revenue in FY2025 and 12.5% in the nine months to June 2026
   (10-K MD&A; 10-Q MD&A). Knowable in the past, not fixed.
4. **Collection on the school's own credit.** About 21% of active UTI students borrowed from UTI's proprietary loan program
   and about 68% of Concorde's active students paid through Concorde retail installment contracts (10-K FY2025, Item 1);
   revenue on the proprietary loans is recognized at an estimated collection rate that "requires significant management
   judgment" (10-K MD&A, Critical Accounting Estimates). Knowable in part; the provision has risen (contrary item 7).
5. **Employer demand for technicians and healthcare workers.** The most foreseeable of the five; it does not decide who pays
   the tuition.

**Test 3, do the past statements tell me the future ones?** **[M2008-033]** The FY2011 statements (revenue $451.9M, net
income $27.2M, average 18,500 students) did not tell the next nine years: revenue fell to $300.8M by FY2020 (-33.4%),
average enrollment to 10,674 in FY2019 (-42.3%; both figures are the UTI schools only, before MIAT and Concorde), operating
losses came in every year FY2015 to FY2020 (-$9.2M, -$18.6M, -$1.8M, -$35.3M, -$7.8M, -$3.9M), and operating cash flow was
negative in FY2017 and FY2018 (-$10.0M, -$13.5M) (XBRL company facts as first filed in the 10-Ks; FY2011 10-K accession
`0001193125-11-324755`; FY2015 `0001261654-15-000042`; FY2019 `0001261654-19-000060`). The insiders' own forecasts at the
time are the record the rows ask for **[M1995-050]**: the FY2011 10-K expected "the average student population for 2012 to
decline by a rate in the low teens", and the decline ran for seven more years; the FY2015 10-K expected FY2016 revenue "to
decline approximately two percent", and it fell 4.3% to $347.1M with a net loss of $47.7M. The FY2025 statements (operating
margin 10.0%) did not tell the nine months to June 2026 (2.9%), although that change was management's choice of growth
spending (about $27.6M of "strategic growth expenses", 10-Q MD&A), not an outside event.

**Test 4, important and knowable?** "If something’s important but unknowable, forget it." **[M2006-076]**. The terms of
federal aid are the most important variable (78% of cash revenue) and are not knowable ten years out.

**Test 5, would the insiders write it down?** **[M2000-105]**. UTI, in its 10-K: "We cannot predict the extent to which the
current administration and Congress, or any future administration or Congress, will act to change or eliminate or to
implement new laws, regulations, standards, policies, and practices, nor can we predict the form that new laws,
regulations, standards, policies, or practices may take" (risk factor "The post-secondary education regulatory environment
has changed and may change in the future as a result of U.S. federal elections"), and of the 2025 law, its impact "is
unknown at this time". Its nearest public competitor, Lincoln Educational, in its 10-K for 2025: "We cannot predict the
scope, timing or likelihood of future actions and changes by Congress, the President or the DOE with respect to the
operations and existence of the DOE or the laws and regulations applicable to and the funding for the Title IV Programs"
(accession `0001140361-26-007380`). Contrary item 6 is honoured: the sentence alone would be boilerplate; read with test 3,
it is the record. The insiders did put forecasts on paper in 2011 and 2015, and the forecasts were wrong in the size and the
length of the change. They now write down a plan ("open at least two new campuses each year between fiscal years 2026 and
2029", 10-K Item 1), which is a bet that the terms hold, not a forecast of them.

**Test 8, how far off could I be?** **[M2011-084]**. On the record above: a third of revenue and two fifths of the students
in one policy-and-labour cycle at UTI, and worse at Lincoln, whose revenue fell from $639.5M (2010) to $261.9M (2017),
-59.0%, with operating losses in every year 2012 to 2018 (LINC XBRL company facts as filed in its 10-Ks; CIK 1286613). The
range of outcomes is set by the same variable for both, which says the variable belongs to the industry, not to either
company's skill.

**The speakers' own cases.** Asked about an industry that had "historically earned good returns" on capital and whose future
turned on government, Buffett answered that "much of it is in the political realm. And my judgment about the" [...] "what
politicians will do is probably not better than yours." **[M2005-098]** (the meeting's heading for the answer, in the
transcript file, is "Future of pharmaceuticals is too hard"). The rows also narrate the cost of assuming a regulatory bargain
will hold: "it is difficult to project both earnings and asset values in what was once regarded as among the most stable
industries in America. [...] I did not anticipate or even consider the adverse developments in regulatory returns"
**[L2023-011]**. Where the speakers did accept a regulatory bet, they named their grounds: "the bet we are making is that
regulatory authorities will treat us fairly in the future", resting on "delivering electricity at lower rates than are
charged by most utilities" **[M2014-087]**; and of railroads, "we’ve got economics on our side" **[M2012-074]**.

**Testing those grounds against UTI (contrary items 1, 2 and 4 weighed).** (a) Lower prices to the customer: the company
itself says it competes with community colleges "mainly due to local accessibility, low tuition rates and in certain cases
free tuition" and that "Public institutions are generally able to charge lower tuition than our schools, due in part to
government subsidies" (10-K FY2025, Item 1, Competition). UTI's ground is the opposite of the utility's. (b) Economics on
its side: the railroad row means cost per ton-mile; UTI's paying customer is mostly the federal government, and its students
defaulted at about the proprietary-sector average (contrary item 7), so no outcome advantage shown in the filings sets it
clearly apart from the schools the rules are written against. (c) The television-station error **[M2004-058]**: there the
feared regulation turned out to be something that "almost never happened"; here it did happen, to this company, in the
record above, and borrower-defense claims and a $19.6M letter of credit to the Department of Education (posted July 2025 so
that Concorde could add programs and campuses, released July 2026) are current, not hypothetical (10-K Item 1; 10-Q
Liquidity). (d) "cheap enough" **[M2004-083]** is a price argument; it does not reach Q1, since a business that cannot be
evaluated is not made evaluable by its price: "It doesn’t mean it isn’t selling for a fraction of its worth. It just means
that we don’t know how to evaluate it." **[M2000-038]**.

**The perimeter.** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. The
doubt here is not about the trades or the schools; it is about the one variable that decides the revenue.

**VERDICT: TOO HARD (NATURE)** **[M2006-013]**. The deciding question, what the terms of federal student aid for proprietary
career schools will be over the next ten years, is important and unknowable **[M2006-076]**, sits "in the political realm"
**[M2005-098]**, and is one the industry's insiders decline to write down and, when they did write it down, got wrong
**[M2000-105]**, **[M1995-050]**. The cause is the industry's, not the reader's: "in other cases the nature of the industry
would be the roadblock" **[L1993-023]**.

**Why NATURE and not WORK (section I, the two causes).** The knowable parts were listed before the verdict: (i) each
program's debt-to-earnings and earnings-premium results under the gainful-employment rule and the 2025 earnings test, from
the Department of Education's published data and College Scorecard; (ii) the 90/10 headroom per institution (known: 67% to
82% at UTI against 82.9% to 88.0% at Lincoln); (iii) post-pause cohort default rates when published (the last three
published years are 0% at every UTI institution because of the payment pause, 10-K FY2025); (iv) the trend of credit
losses on the school's own lending. The operator's case sets the test: do the knowable parts carry the answer, or does the
decision rest on the unknowable one? They do not carry it. Even a clean result on (i) to (iv) leaves the revenue resting on
rules the 10-K itself describes as revised "multiple times" (borrower defense), replaced in 2023 (gainful employment), changed by statute in 2025 and in rulemaking now, and the record shows the company's
outcomes at about the sector average, so it cannot claim to stand outside whatever the next rules target. "we’re not going
to learn enough in the followings five months to make up for the fact that we went in deficient in the first place."
**[M2008-086]** (the spelling is the transcript's). A pass that ended unsure would end in this box anyway (section I,
**[M2002-092]**). No research pass is opened; a lower price does not reopen the box **[M2000-038]**.

## Q2 TO Q12: NOT REACHED
Q1 closed the file in TOO HARD (NATURE). Q2 (the castle), Q3 (capital), Q4 (the numbers), Q5 (the people), Q6 (the money
and the owners), Q7 (value), Q8 (alternatives), Q9 (ruin), Q10 (the fat pitch) and Q12 (pride) are NOT REACHED and carry no
verdict. The dispatch asked for the balance-sheet reading, the owner cash and the competitor comparison regardless; they are
recorded below under the operator-rule-3 heading, as evidence gathered, not as answers to the questions they belong to.

## COMPUTATION — NOT A CLEARANCE
*Everything in this section was gathered or computed after the file closed at Q1. It answers no question, clears nothing,
and carries no entry language. It is kept so that the next reader does not have to fetch it again.*

### The competitor row and the castle evidence as read (Q2 material, no verdict)
| | UTI (FY to 2025-09-30) | Lincoln Educational, LINC (FY to 2025-12-31) |
|---|---|---|
| Revenue | $835.6M | $518.2M |
| Operating income, margin | $83.5M, 10.0% | $30.3M, 5.8% |
| Federal money in cash revenue | about 78% (Title IV about 67%, veterans about 11%) | about 85% Title IV, about 4.8% veterans |
| 90/10 percentages, range across institutions | about 67% to about 82% | about 82.9% to 88.0% |
| Capital spending | $42.0M | $86.6M |
| Peak to trough revenue | $451.9M (FY2011) to $300.8M (FY2020), -33.4% | $639.5M (2010) to $261.9M (2017), -59.0% |
| Years of operating loss in the trough | FY2015 to FY2020 | 2012 to 2018 |
| Source | 10-K `0001261654-25-000025`; XBRL company facts | 10-K `0001140361-26-007380`; XBRL company facts (CIK 1286613) |

Community colleges and manufacturer programs: no primary filing was read for them. What is recorded is the filer's own
description, flagged as such: public institutions charge less "due in part to government subsidies", some offer "free
tuition", and "No single community college is a significant competitor; rather, the sector as a whole provides competition"
(10-K FY2025, Item 1, Competition). The manufacturer programs appear in UTI's filing as partners, not rivals: the
manufacturer-paid MSATs are run by UTI at Mercedes-Benz, Porsche, Peterbilt and Tesla facilities, while some relationships
(Honda, Mercury Marine, Volvo Penta, Yamaha) "are not memorialized in writing and are based on verbal understandings" and
some written agreements "may be terminated without cause by the OEM" (10-K FY2025, Item 1A).

Price evidence: UTI raised average tuition about 1.9% in FY2025, 3.0% in FY2024 and 6.0% in FY2023; Concorde 2.5%, 2.5%
and 3.0%; about 58% of active UTI students received a UTI-funded scholarship or grant (10-K FY2025, MD&A and Item 1). These
are the figures a Q2 reading would set against "the agony they go through in determining whether a price increase can be
sustained" **[M2005-020]**; no reading is made here.

### The balance sheets, ten years (Q4 material, no verdict)
First-filed XBRL vintage from `tools/run.py`, $ thousands, read against the filed statements for FY2024, FY2025 and June
2026 (10-K `0001261654-25-000025`, 10-Q `0001261654-26-000018`):

| year-end | assets | equity | cash | receivables | goodwill | intangibles | long-term debt | retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2016-09-30 | 297,159 | 136,614 | 119,045 | 15,253 | 9,005 | 0 | 0 | -17,454 |
| 2017-09-30 | 274,102 | 125,776 | 50,138 | 15,197 | 9,005 | 0 | 0 | -30,832 |
| 2018-09-30 | 282,278 | 126,645 | 58,104 | 21,106 | 8,222 | 0 | 0 | -31,555 |
| 2019-09-30 | 270,526 | 114,288 | 65,442 | 17,937 | 8,222 | 0 | 0 | -44,673 |
| 2020-09-30 | 441,981 | 176,522 | 76,803 | 35,411 | 8,222 | 0 | 131 | -32,971 |
| 2021-09-30 | 512,570 | 188,530 | 133,721 | 17,151 | 8,222 | 124 | 29,850 | -21,996 |
| 2022-09-30 | 552,911 | 215,397 | 66,452 | 16,450 | 16,859 | 14,215 | 66,423 | -1,307 |
| 2023-09-30 | 740,685 | 225,967 | 151,547 | 25,161 | 28,459 | 18,975 | 159,600 | 5,946 |
| 2024-09-30 | 744,575 | 260,231 | 161,900 | 31,096 | 28,459 | 18,229 | 123,007 | 38,509 |
| 2025-09-30 | 826,139 | 328,110 | 127,361 | 46,078 | 28,459 | 17,352 | 84,234 | 101,527 |
| 2026-06-30 (10-Q) | 897,862 | 344,306 | 130,060 | 49,824 | 28,459 | 25,535 | 157,041 | 117,066 |

What the figures say **[M2025-032]**:
- **Equity was raised, not earned, until 2021.** Retained earnings were negative from FY2016 to FY2022 and first turned
  positive in FY2023. Equity rose from $136.6M to $328.1M over FY2016 to FY2025 (+$191.5M), of which retained earnings
  supplied $119.0M; the rest is paid-in capital: $68.9M of Series A preferred sold in FY2016, $49.15M of common sold in
  FY2020, and stock pay (XBRL company facts; 10-K FY2025 statement of shareholders' equity). Shares outstanding went from
  24.6M (cover, November 2016) to 55.1M (cover, July 2026); diluted earnings per share were about $1.10 in FY2011 and $1.13
  in FY2025; equity per share about $5.76 and $6.03.
- **Cash.** The FY2017 fall from $119.0M to $50.1M is mostly a move into held-to-maturity securities ($47.8M at FY2017),
  with a smaller real decline from operating losses (cash plus securities about $120.7M to $97.9M). Since FY2023 the cash has
  been held beside a revolver drawn and repaid in large amounts: $195.0M drawn and $120.0M repaid in the nine months to June
  2026, $95.0M repaid from cash in July 2026 (10-Q, Liquidity).
- **Receivables and the school's own lending against sales.** Receivables were 4.4% of revenue in FY2016, 4.2% in FY2024 and
  5.5% in FY2025; notes receivable on the proprietary loan program were $42.5M (FY2024), $47.7M (FY2025) and $52.1M (June
  2026); retail installment contracts sit in other assets. The provision for credit losses was 0.55%, 1.03% and 2.65% of
  revenue in FY2023, FY2024 and FY2025, and 3.39% in the nine months to June 2026 against 2.46% a year earlier. This is the
  line a Q4 reading would look at twice **[M1995-064]**: credit extended to the school's own customers growing faster than
  sales, with revenue recognized at an estimated collection rate.
- **Debt and leases.** No funded debt FY2016 to FY2020; campus purchases with term loans (Avondale December 2020, Lisle
  February 2022), the Concorde purchase on the revolver (FY2023), a new $200M secured revolver to August 2031 (8-K
  `0001193125-26-354799`). Operating lease liabilities $191.8M at FY2025 and $199.4M at June 2026.
- **Deferred revenue** of $91.5M (FY2025) is aid and tuition received before it is earned.
- **What the figures cannot say:** the asset the business runs on, each institution's eligibility for federal aid, is on no
  balance sheet; nor is any liability for borrower-defense claims not yet adjudicated (10-K FY2025, Item 1).

### Owner cash after every real cost (Q4 and Q7 material, no verdict)
Operating cash flow less stock pay less capital spending, from the filed cash-flow statements (FY2023 to FY2025, 10-K
`0001261654-25-000025`; FY2021 and FY2022 from XBRL as first filed). Operating-lease rent is already inside operating cash
flow; growth in the student loan book is deducted there too. All capital spending is deducted, including campus purchases
in FY2021 and FY2022 that replaced rent; the depreciation variant is shown beside it (Q7 convention, the PG specifics).
Arithmetic in `Test Runs/_research 2026-10-05 UTI/arithmetic.py`.

| FY | OCF | SBC | capex | D&A | owner cash, all capex | owner cash, D&A variant |
|---|---|---|---|---|---|---|
| 2021 | 55.2 | 1.7 | 61.6 | 14.0 | -8.1 | 39.5 |
| 2022 | 46.0 | 4.3 | 79.5 | 16.9 | -37.8 | 24.8 |
| 2023 | 49.1 | 3.8 | 56.7 | 25.2 | -11.4 | 20.1 |
| 2024 | 85.9 | 8.6 | 24.3 | 29.3 | 53.0 | 48.0 |
| 2025 | 97.3 | 9.2 | 42.0 | 33.0 | 46.2 | 55.2 |
| five-year average | | | | | **8.4** | **37.5** |
| TTM to 2026-06-30 | 74.5 | 12.2 | 101.9 (incl. $4.5M capitalized intangibles) | 36.9 | -39.5 | 25.5 |

($ millions.) Q3 would have to say how much of the capital spending keeps the business in place and how much builds new
campuses; the filing does not split it, and no guess is made here because the file is closed.

### Price arithmetic (Q7 material, no verdict, no entry language)
At $19.34 and 55.10M shares the market value is $1,065.5M. Owner cash as a yield on it: five-year average 0.79% (all capex)
or 3.52% (D&A variant); FY2025 alone 4.34% or 5.18%; the 30-year Treasury is 5.63%. Capitalized at the long rate with no
growth: $149M ($2.71 a share) on the all-capex average, $666M ($12.10) on the D&A variant, $821M ($14.89) and $981M ($17.80)
on FY2025 alone. The shown-growth end of the Q7 range cannot be built: the five-year owner-cash series on the all-capex basis
starts negative, so it has no growth rate (see the framework note below). These figures are recorded only; Q7 was not
reached.

### The people and the money (Q5 and Q6 material, no verdict)
From the proxy (DEF 14A, `0001140361-26-001690`): chief executive Jerome Grant, total FY2025 pay $5,149,264, holding 343,904
shares; the annual cash incentive for the named officers was based on "Post-Bonus Adjusted EBITDA"; the company also
reports EBITDA in its 10-K and 10-Q MD&A. Directors and officers as a group hold 9.8%, most of it the Coliseum entities' 7.2%
(3,971,440 shares); Coliseum Capital Partners and Blackwell Partners sold 33,300 shares of the Series A preferred back to the company
for $11.3M in December 2023 and the remaining preferred converted into 19,297 thousand common shares (10-K FY2025, Note 19
and the statement of shareholders' equity). The chairman adopted a 10b5-1 plan in May
2026 to sell up to 64,210 shares (10-Q Part II, Item 5). No buyback under the $35.0M authorization of December 2020 in FY2023
to FY2025; no common dividend (10-K FY2025, MD&A). The code of conduct was restated in March 2026 with no waiver (8-K
`0001193125-26-110942`). These would bear on Q4's EBITDA tell **[M1998-086]** and Q6's pay test **[M2016-083]**; neither
question was reached.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**. The ten-year economics turn on the terms of federal student aid for proprietary
career schools (about 78% of cash revenue), a political forecast the company and its nearest competitor say in their 10-Ks
they cannot make, and which the company's own written forecasts of 2011 and 2015 got wrong. Not reached at Q7, so no range
is set beside the price; the price arithmetic above is a computation only. No research pass is opened (NATURE), and a lower
price does not reopen the box **[M2000-038]**. Q11 belongs to a holding review, not to this run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written section by section (STEP 0 first, then the foundations and Q1, then
      the record). **Not committed after each:** the dispatch forbade commits; recorded here rather than ticked silently.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script after writing, below); every filing fact carries
      its document and accession; every number is from a filing, a tool line or the arithmetic file.
- [x] The order was kept; Q1 failed and closed the run; nothing after it is a clearance, and it sits under the
      COMPUTATION — NOT A CLEARANCE heading.
- [x] Owner cash computed from operating cash flow after stock pay and capital spending, never from net income (operator rule
      5); the sovereign is the Treasury's 30-year par yield; the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]**, in the foundations list, before the Q1 verdict.
- [x] No row dated after the anchor is cited (the run is dated today; no point-in-time anchor applies).
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 rule text, ids and floor were ignored (Part VII).
- [x] `python tools/check_framework.py` run after writing; result recorded in the reply to the operator.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Q1 has a fixed route only for fast technological change.** The routing sentence sends "a business whose ten-year
   economics cannot be foreseen because its industry changes fast" to Q1 TOO HARD; it says nothing of a business whose
   decisive variable is a government's future conduct (here the payer of 78% of cash revenue). The run reached Q1 through
   tests 4 and 5 and the speakers' own pharmaceuticals answer **[M2005-098]**, but the same facts could be read at Q2 test 11
   (the risk that can "destroy, or modify, or reduce the economic strengths" of a business, **[M2000-014]**) and close TOO HARD there instead. Two analysts could disagree
   on the question, though not on the box. A routing sentence for the political key variable, like the one gap (a) wrote for
   technology, would settle it.
2. **Test 5 has no rule for reading risk-factor language.** Test 5, would the insiders write it down **[M2000-105]**, is answered
   in practice from 10-K risk factors, which disclaim any ability to predict almost everything, for legal reasons. The run
   treated the sentence as evidence only together with the insiders' past written forecasts and what followed
   **[M1995-050]**. The framework should say whether that pairing is required.
3. **The Q7 growth input is undefined when the five-year owner-cash series starts negative.** The convention measures "the
   growth shown" on aggregate owner cash; UTI's all-capex series runs -8.1, -37.8, -11.4, 53.0, 46.2 ($M), which has no growth
   rate. The convention also does not say whether buying a campus that was rented (a swap of rent for capital, part financing)
   counts as capital spending in full. Not decisive here, since Q7 was not reached, but a reached name with this pattern
   would leave the top of the range to the analyst's choice.
4. **The template and the dispatch conflicted twice.** The template's position note says to check `PORTFOLIO.md` and its
   self-audit asks for a commit after each question; this dispatch forbade both. The dispatch was followed and the conflict
   is recorded in the position note and the self-audit.
