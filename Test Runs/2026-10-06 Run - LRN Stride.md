# Company Run: Stride, Inc. (NYSE: LRN), formerly K12 Inc. (2026-10-06)
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template to this dated name before
any fetch (the research folder was created in the same command).

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is closed to this run under the blind rule of
the brief, so whether the operator holds LRN is unknown to the analyst.

**CONTAMINATION, declared.** (1) The session's opening context showed five recent commit subjects of other companies'
v5 runs (NWL OUT at Q2, MD OUT at Q2, COLL OUT at Q1, MHO OUT at Q2, and an S&P 600 session-state commit); their run files
were not opened. The MD subject ("operating margin 25% to 11% over twenty years ... contracts end without cause") is a
government-payer service business closed at Q2; I declare that I read that line before judging this one. (2) The
operator's memory index was in context (v5 adopted; "57 gate-clearers, nothing buyable"; holding reviews owed, no names).
(3) The repository map (`CLAUDE.md`) and the operator protocol were in context. (4) From general knowledge I knew LRN's
price fell sharply in late October 2025; nothing in this file rests on that memory: every fact below is from a filing.
No `Test Runs/` file about this company, no `Screens/` reading list or queue, and no holding review were opened.

**Working folder:** `Test Runs/_research 2026-10-06 LRN/` (filing texts, `fetch.py`, `grepc.py`, `series.py`,
`owner_cash.py`, `q.py`; `run_py_output.txt`; `cover_shares.txt`; `peers/` for Pearson).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $78.88 (close 2026-10-05, the live quote `tools/run.py` fetched; aggregator, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock $0.0001 par, **41,559,845** shares as of
  2026-07-31 (Form 10-K for FY ended 2026-06-30, filed 2026-08-05, accession `0001104659-26-090515`;
  `python Screens/cover_shares.py LRN` returns the same count). No other class on the cover.
- **Market cap:** $78.88 x 41.560M = **$3,278M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, 30-year par yield, US Treasury daily par yield curve,
  10/05/2026 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2026 (filed 2026-08-05, `0001104659-26-090515`): business, regulation, risk factors, MD&A, cash-flow
    statement, notes 10, 11, 12, 13.
  - 10-Q Q3 FY2026 (filed 2026-04-29, `0001104659-26-050510`) and 10-Q Q1 FY2026 (filed 2025-10-29,
    `0001104659-25-103288`, read for what it said of the platform and of risk factors).
  - Proxy DEF 14A (filed 2025-10-24, `0001140361-25-039264`): pay design, summary compensation table, ownership.
  - 8-Ks: CEO change and preliminary FY2026 (2026-07-30, `0001140361-26-030147`); FY2026 results and buyback extension
    (2026-08-04, `0001171843-26-005202`); buyback authorization (2025-11-03, `0001104659-25-105334`); Q1 FY2026 results
    (2025-10-28, `0001171843-25-006722`); Q2 and Q3 FY2026 results (`0001171843-26-000444`, `0001171843-26-002775`);
    FY2025 results (`0001171843-25-005051`); director changes (`0001104659-25-036383`, `0001104659-25-091691`); annual
    meeting (`0001104659-25-120014`).
  - Prior 10-Ks for FY2010 to FY2025 (accessions in `_research 2026-10-06 LRN/sub.json`; those read for facts quoted
    below: FY2011 `0001193125-11-266919`, FY2013 `0001047469-13-008761`, FY2014 `0001047469-14-007036`, FY2015
    `0001047469-15-006545`, FY2016 `0001047469-16-014855`, FY2017 `0001558370-17-006309`, FY2018 `0001558370-18-006642`,
    FY2019 `0001558370-19-007293`, FY2020 `0001558370-20-010355`, FY2021 `0001558370-21-011173`, FY2022
    `0001558370-22-012941`, FY2023 `0001558370-23-015003`, FY2024 `0001558370-24-011134`, FY2025 `0001558370-25-010334`).
  - Competitor: Pearson plc Forms 20-F for 2025 (`0001193125-26-104945`), 2024 (`0001193125-25-054371`) and 2021
    (`0001193125-22-089608`). Pearson does file with the SEC (20-F), so Connections Academy is read from a primary filing,
    as Pearson's "Virtual Learning" segment, not from an aggregator.
- **One figure cross-checked against the filed statement:** net cash from operating activities FY2026 is $433,814
  thousand on the filed cash-flow statement of `0001104659-26-090515`; `tools/run.py` prints 433.8. Agrees. A second:
  `tools/run.py`'s alternate three-year owner cash (232.4) equals my own FY2024 to FY2026 mean built from the filed lines
  (232.3, table below).
- **`tools/run.py LRN`, arithmetic lines only** (its rule text and v4 floor ignored, Part VII): OCF FY2024/25/26 278.8 /
  432.8 / 433.8; SBC 31.5 / 36.8 / 40.3; D&A 109.7 / 114.7 / 126.6. Its "as filed" capex (PP&E plus capitalized software)
  leaves out two capital lines the statement lines section prints: capitalized curriculum (18.7 / 21.8 / 16.7) and
  finance-lease principal on student computers (40.9 / 41.5 / 56.9, in financing). Capitalized curriculum and software are
  capital, and the student computers are capital equipment bought on 36-month leases (10-K, Liquidity), so **the
  alternates are the honest figures**: three-year mean 232.4 (capex basis), five-year window 232.7 per `run.py`.

**Owner cash after every real cost, fifteen years** (USD millions; OCF less stock pay less all capital spending:
PP&E + capitalized software + capitalized curriculum + finance/capital-lease principal. XBRL first-filed vintage,
read against the filed cash-flow statements; `owner_cash.py`):

| FY (June) | Revenue | Op. income | Op. margin | OCF | SBC | All capex | D&A | **Owner cash** | % of revenue |
|---|---|---|---|---|---|---|---|---|---|
| 2012 | 708.4 | 29.0 | 4.1% | 33.0 | 10.1 | 65.2 | 58.0 | **-42.3** | -6.0% |
| 2013 | 848.2 | 45.7 | 5.4% | 95.3 | 14.4 | 70.6 | 65.7 | **10.3** | 1.2% |
| 2014 | 919.6 | 22.9 | 2.5% | 123.5 | 22.8 | 72.1 | 86.3 | **28.6** | 3.1% |
| 2015 | 948.3 | 18.4 | 1.9% | 120.1 | 21.3 | 83.7 | 83.8 | **15.1** | 1.6% |
| 2016 | 872.7 | 13.9 | 1.6% | 121.8 | 18.6 | 80.3 | 68.2 | **22.9** | 2.6% |
| 2017 | 888.5 | 13.1 | 1.5% | 88.7 | 22.6 | 63.9 | 74.3 | **2.2** | 0.2% |
| 2018 | 917.7 | 25.5 | 2.8% | 103.6 | 20.8 | 56.4 | 75.3 | **26.4** | 2.9% |
| 2019 | 1,015.8 | 45.5 | 4.5% | 141.6 | 16.7 | 69.4 | 71.4 | **55.5** | 5.5% |
| 2020 | 1,040.8 | 32.5 | 3.1% | 80.4 | 23.6 | 72.7 | 72.1 | **-15.9** | -1.5% |
| 2021 | 1,536.8 | 110.5 | 7.2% | 134.2 | 39.3 | 76.6 | 90.1 | **18.3** | 1.2% |
| 2022 | 1,686.7 | 156.6 | 9.3% | 206.9 | 18.6 | 100.6 | 97.9 | **87.7** | 5.2% |
| 2023 | 1,837.4 | 165.5 | 9.0% | 203.2 | 20.3 | 109.5 | 110.4 | **73.4** | 4.0% |
| 2024 | 2,040.1 | 249.6 | 12.2% | 278.8 | 31.5 | 102.6 | 109.7 | **144.7** | 7.1% |
| 2025 | 2,405.3 | 360.1 | 15.0% | 432.8 | 36.8 | 101.5 | 114.7 | **294.5** | 12.2% |
| 2026 | 2,518.1 | 450.8 | 17.9% | 433.8 | 40.3 | 135.8 | 126.6 | **257.7** | 10.2% |

Five-year mean (FY2022-26) **$171.6M**; fifteen-year mean $65.3M; fifteen-year mean owner-cash margin **3.31%** of
revenue, and 1.07% over FY2012-2020. All capital spending ran at about the depreciation charge in FY2022-26 (100.6 to
135.8 against 97.9 to 126.6). FY2025 includes a $59.5M non-cash Galvanize impairment inside operating income (10-K FY2026,
MD&A); it does not touch owner cash.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, and the answer turns entirely on whether the payers (states, through independent charter boards) and the
parents keep choosing it, which is a question about the business, not the quotation. The market serves: "It just tells
us prices." **[M2006-077]**; the price moves of the last year are not evidence here. Margin of safety: "if you have to actually do it on — with pencil and paper, it’s too close to think about"
**[M1996-084]**; the arithmetic belongs to Q7. No macro forecast: "macro conclusions are — just never enter into the
discussion" **[M2000-094]**; the school-choice statistics the 10-K
opens with (75% of parents considering a different school; home-education estimates) are the filer's selling case and are
not used as a forecast. Who is paid to tell you: "you do not get impartial advice from Wall Street" **[M2020-037]**; the filer leads every release with "Adjusted EBITDA" and
"Adjusted operating income" that exclude stock pay; those figures are not used.

**Contrary evidence, written down as found**, Darwin's rule, "write it down in the first 30 minutes" **[M1997-127]**:
1. FY2012-FY2020 operating margin never exceeded 5.4%; owner cash was negative in FY2012 and FY2020 and 0.2% of revenue in
   FY2017 (table above). The high returns are four or five years old.
2. The customer can and does leave: Agora Cyber Charter School (Pennsylvania) gave a notice of non-renewal in 2012 and did
   not renew its managed agreement (10-K FY2017 and FY2019, legal proceedings: the class action that "pertain[ed] to
   non-disclosure of Agora's 2012 notice of non-renewal" settled for $3.5M paid by insurers); Georgia Cyber Academy engaged
   "other educational products and service providers for the school year 2019-2020" and the dispute settled with GCA paying
   $19M (10-K FY2020).
3. Managed public-school enrollment fell from 123,259 (FY2014) to 102,935 (FY2016), a 16.5% fall (10-K FY2014, FY2016).
4. The price is not Stride's to set: revenue is "primarily a function of the number of students enrolled ... and
   established per enrollment funding levels, which are generally published on an annual basis by the state or school
   district"; and Stride is "responsible for substantially all of the expenses incurred by the school and [has] generally
   agreed to absorb any operating losses of the schools" (10-K FY2026, critical accounting estimates).
5. California: July 2016 settlement with the Attorney General's investigation of for-profit virtual schools and a qui tam
   on attendance reporting, $2.5M + $0.1M + $6.0M, with conduct provisions, no admission (10-K FY2016).
6. FY2026: General Education enrollment fell 2.5% to 134.2K; fourth-quarter total enrollment fell 0.5% year on year;
   Adult revenue fell 29.6% to $56.6M after falling 19.4% the year before (10-K FY2026, MD&A; 8-K `0001171843-26-005202`).
7. The FY2026 platform rollout: the 10-K FY2026 now says "we have experienced and may continue to face negative student
   or parent reactions from implementation of new IT Systems or technology, resulting in higher student withdrawal rates
   and lower conversion rates"; the Q2 release headline line reads "Core platform issues stabilized"; a securities class
   action covering 2024-10-22 to 2025-10-28 alleged misleading statements about "the rollout of a new platform for Fiscal
   Year 2026" and was dismissed on 2026-06-18 (10-K FY2026, note 11). The Q1 FY2026 10-Q, filed the day after the period
   the suit names ended, said "There have been no material changes to the risk factors".
8. Receivables rose 18.8% in FY2026 (559.6 to 664.8) against revenue up 4.7%; receivables were 19.2% of revenue at
   FY2018 and 26.4% at FY2026 (balance sheets, `tools/run.py` table and XBRL).
9. The CEO of five years "ceased serving" on 2026-07-29, effective immediately, with severance under his agreement; the
   new CEO, 71, is a director who had resigned from the board in April 2025 and rejoined it in September 2025 (8-Ks
   `0001140361-26-030147`, `0001104659-25-036383`, `0001104659-25-091691`).
10. Pearson's own 20-F reports "partner school losses" in Virtual Schools (20-F 2024, `0001193125-25-054371`): the boards
    leave the rival too.

Against the case against: the speakers record having "tended to overestimate the difficulties from regulation" for
licensed television stations **[M2004-058]**; written down here so the regulatory argument at Q2 is not taken as settled
by its own weight.

## THE STANDING RULE
A purchase for cash, unlevered, sized so that a total loss could be borne, keeps the buyer inside "We are never going to
risk what we have and need for what we don’t have and don’t need." **[M2012-081]** and "Never risk permanent loss of
capital." **[L2023-005]**. Nothing about the target changes that; the rule is met by the buyer's conduct.

---
## Q1: CAN I UNDERSTAND IT? STOP.
- **What the business is, from the filing.** A contractor to publicly funded schools. "The majority of our revenue is
  derived from these school-as-a-service service agreements with the governing authorities of our public school
  partners"; revenue per school is set by state per-pupil funding; Stride supplies curriculum, platform, teachers,
  computers, marketing and administration and absorbs the school's operating deficit (10-K FY2026). 92 General Education
  schools in 31 states and DC, 57 Career Learning schools or programs in 25 states and DC; 243.9K average enrollments;
  agreements average more than five years and mostly auto-renew; no contract above 10% of revenue in FY2024-26 (10-K
  FY2026, note 2 and Item 1). Adult Learning (Galvanize, Tech Elevator, MedCerts, bought 2020) is $56.6M of $2,518.1M.
- **The key variables**, "trying to identify the key variables in that particular business, and evaluating how
  predictable they were first" **[M1998-044]**: (a) enrollments; (b) revenue per enrollment, which is the states' per-pupil
  funding less what the board keeps; (c) instructional cost per enrollment (teachers, mostly variable: instructional
  costs ran 60.8% to 66.6% of revenue FY2017-2026); (d) contract retention with independent boards and the charters
  their authorizers renew; (e) the laws of 31 states permitting full-time virtual schools and how they fund them.
- **Can I understand the economic dynamics?** Yes in the sense the rows ask first: "What is important is that I
  understand the economic dynamics of the industry. Is there — are there competitive moats? Is there ease of entry?"
  **[M2011-014]**. The money flows, the cost structure and where the company stands in its industry (the largest
  operator; Pearson, named first among Stride's competitors in its 10-K and the one rival with an SEC filing, runs 41 schools) can be read from the filings:
  "where the company will stand within the industry" **[M2012-065]**.
- **What I cannot fix**: the same row asks "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**. Earning power swung from 1.5% to 17.9% operating margin within the span,
  and variables (b) and (e) are set by legislatures and boards, not by the company. Whether that is a defect of
  understanding or a question about the castle's permanence is the Q1/Q2 line. The rows put the edge after the first filter: "if it passes through that, it’s
  whether a company can have a sustainable edge" **[M1997-148]**; and the risk to the castle is asked as what will
  "destroy, or modify, or reduce the economic strengths" **[M2000-014]**, which the framework places at Q2. I take it to
  Q2 and say so in the last section.
- **Doubt rule**, "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**:
  my doubt is not whether I can follow how the business makes money or what moves it; it is
  whether the payer keeps paying on these terms, which is the castle question. Not a doubt about the circle as defined by
  **[M2011-014]**.
- **VERDICT: IN**, narrowly, on **[M2011-014]** and **[M2012-065]** (second sentence), with the earning-power fix carried
  to Q2.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "What are the key factors? And how permanent are they?" **[M1995-038]**.

1. **The castle questions** **[M1995-038]**. Key factors, from the filing: (i) the states' permission and per-pupil funding
   for full-time virtual public schools; (ii) Stride's scale and bundle (curriculum library, platform, teacher recruiting,
   enrollment marketing, compliance know-how across 31 states); (iii) multi-year, auto-renewing contracts. Permanence:
   (i) is set by legislatures that, in the filer's words, have laws that "vary significantly from one state to the next and
   are constantly evolving", with "uncertainty ... because the concept of virtual and blended public schools is still
   evolving" (10-K FY2026, Regulation); (ii) and (iii) were already in place in FY2013-FY2017, when Stride (then K12) was the
   largest operator and earned 1.5% to 5.4% operating margins. The scale did not protect the return then.
2. **Would it stand without the lord?** The CEO left with immediate effect on 2026-07-29 and FY2026 results were unaffected
   by it; the business does not look like one that needs a superstar. Weighs for.
3. **The money test**: "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?"
   **[M2011-015]**. The attacker that matters has been the customer, not a rival with money: Agora
   (2012 notice) and Georgia Cyber Academy (2019) moved off Stride's full service, and the
   10-K warns boards "may seek to employ their own Principal or ED as a condition for contract renewal" and "unbundle
   previously provided services". Pearson (Connections Academy, named in Stride's 10-K), a group with £3,577m of 2025 sales, holds 41 schools in 31
   states with Virtual Learning sales of £511m (20-F 2025), against Stride's 92 General Education schools and $2,461.5M
   of K-12 revenue (10-K FY2026); it has not displaced Stride, and over 2019-2025 Stride has not displaced it. State-administered programs compete as well (10-K FY2026, Competition); none
   files with the SEC and none was read.
4. **Pricing power**: "you can almost measure the strength of a business over time by the agony they go through in
   determining whether a price increase can be sustained" **[M2005-020]**. There is no price to raise. Revenue per enrollment is
   the state's per-pupil funding less the board's share; it rose 2.4% in FY2026 ($9,677 to $9,914, company figure,
   8-K `0001171843-26-005202`). Stride takes the deficit when funding falls short (10-K FY2026). The test fails in its own
   form: the "price behavior" **[M2005-020]** belongs to the payer.
5. **Unit volume and share of mind**: "It’s share of mind. It’s not share of market." **[M1997-099]**. Managed public-school enrollments 74,755 (FY2011) to 123,259 (FY2014)
   to 102,935 (FY2016) to 118.6K (FY2020); on the present basis 120.9K (FY2020), 186.3K (FY2021), 178.2K (FY2023), 194.3K
   (FY2024), 234.0K (FY2025), 243.9K (FY2026) (10-Ks FY2013, FY2014, FY2016, FY2020, FY2021, FY2023, FY2026; the basis
   changed in FY2021 to General Education plus Career Learning). The volume doubled through the pandemic and held, but the
   General Education line fell in FY2026 and the fourth quarter was below the prior year. The parent pays nothing, so share
   of mind is bought with marketing inside SG&A; the board, which holds the charter, stands where the retailer stands in "the value of having the brand moves over to
   the retailer from the product itself" **[M2001-090]**.
6. **The low-cost position** **[M1995-039]** (advantages of scale). SG&A fell from 34.4% of revenue (FY2017) to 19.8%
   (FY2026) while instructional cost stayed at 61% to 67%: the margin gain is leverage on overhead. But the rival's
   margin rose as far without Stride's scale (table at test 10), so the leverage is not shown to be an edge over the rival;
   and it is leverage on volume: the FY2014-2016 enrollment fall shows the same leverage running the other
   way.
7. **The brand.** Renamed from K12 to Stride (former name to 2020-12-15, EDGAR); the record carries the California
   settlement (2016), two securities suits on academic and contract disclosures (2016, settled $3.5M) and on the platform
   (2025, dismissed). No evidence in the filings that parents ask for the operator by name rather than for "online school".
8. **The low bid**: "it wouldn’t be a question of people buying candy for the low bid" **[M2017-009]**. The board is the buyer; GCA chose other
   providers; the 10-K's renewal risk factor says renewals "could involve a restructuring of our services and management
   arrangements that could lower our revenue". The board does not buy on price alone, but it does switch.
9. **Ask the competitors.** Pearson's own report of "partner school losses" (20-F 2024) says the boards are mobile across
   the industry, not only away from Stride.
10. **Widening or narrowing**, "whether it’s likely to widen further or shrink on you" **[M1999-108]**, over the whole span, with the rival's own figures:

| Year | Stride op. margin (GAAP, FY to June) | Pearson Virtual Learning adjusted op. margin (calendar) | Pearson VL statutory op. profit |
|---|---|---|---|
| 2019 | 4.5% | £13m / £584m = 2.2% | £(36)m |
| 2020 | 3.1% | £29m / £692m = 4.2% | £(1)m |
| 2021 | 7.2% | £32m / £713m = 4.5% | £(41)m |
| 2022 | 9.3% | £70m / £820m = 8.5% | not extracted |
| 2023 | 9.0% | £76m / £616m = 12.3% | not extracted |
| 2024 | 12.2% | £66m / £489m = 13.5% | not extracted |
| 2025 | 15.0% (FY2025); 17.9% (FY2026) | £81m / £511m = 15.9% | not extracted |

   Sources: Pearson 20-F 2021 segment note (2019-2021, Virtual Learning then included online program management) and 20-F
   2025 five-year table (2021-2025). Pearson's "adjusted operating profit" excludes intangible charges and restructuring
   and is not comparable to Stride's GAAP figure; it flatters Pearson. Reading: Stride's GAAP margin was ahead of the rival's flattering measure in 2019 to 2022 (by 2.3, -1.1, 2.7 and 0.8
   points), behind it in 2023 and 2024 (by 3.3 and 1.3 points), and between 0.9 behind (FY2025) and 2.0 ahead (FY2026) in
   2025. There is no steady lead, and **both margins rose by eleven to fourteen points over the same years**. The rise is
   the industry's tide (pandemic demand, state funding) at least as much as Stride's castle. The moat widened on the
   evidence from FY2020 to FY2026 (schools served 75 in FY2019, 76 in FY2020, 92 General Education plus 57 Career
   Learning in FY2026), and narrowed on the evidence from FY2014 to FY2017.
11. **What could "destroy, or modify, or reduce the economic strengths"** **[M2000-014]**. From the 10-K's own list: enrollment caps, eligibility
    rules, rules "fixing the percentage of per pupil funding that must be paid to teachers", charter non-renewal for
    performance (a 2025 Arkansas law revokes a charter after three poor years), attendance and funding disputes and
    repayment of funds, opponents' lawsuits, new laws aimed at for-profit operators, platform failures, and AI-priced
    competitors. Each is a decision of a legislature, an authorizer, a board or a court in one of 31 states.

**The verdict, and why it is not OUT.** The castle is not shown open on present evidence: enrollments, schools served and
margins are near their highs, the rival holds 41 schools to Stride's 92, and no single rival is taking it. It is not shown
durable either. "a great company is one that’s going to remain great for 30 years. If it’s going to be a great company for
three years, you know, it ain’t a great company." **[M1996-054]**; this one earned 1.5% to 5.4% for nine years while it
was already the leader, and "Leadership alone provides no certainties" **[L1996-031]**. Whether FY2024-26 is the new level
or the top of a tide turns on what 31 legislatures and their authorizers pay and permit over ten years. The speakers'
own case of a regulated return is the nearest: "it is difficult to project both earnings and asset values in what was
once regarded as among the most stable industries in America" **[L2023-011]**, and "In some businesses that’s very —
it’s impossible — to figure" **[M2000-014]**. "when we see a moat that’s tenuous in any way [...] We don’t know how to
valuate that, and therefore we leave it alone." **[M2000-019]**.

**Which cause.** NATURE, not WORK. The test is whether the industry's insiders would "put down on paper their predictions"
**[M2000-105]** of the deciding question. The deciding question is not whether Stride has a scale edge (knowable: it is the larger operator, though its margin
lead over the rival is not steady) but whether the payer's terms hold for a decade, because the same scale earned thin
returns when they did not.
The filer itself calls the law "constantly evolving" and the concept "still evolving"; that is "the nature of the industry
would be the roadblock" **[L1993-023]**, and the rows put such a question aside: "If something’s important but
unknowable, forget it." **[M2006-076]**. Knowable sub-questions remain (state-by-state funding history, contract renewal
dates, the FY2027 count-date enrollment due in the Q1 FY2027 10-Q), but none of them decides the ten-year payer question,
so a research pass would end unsure, and section I sends a pass that ends unsure to TOO HARD (NATURE).

- **VERDICT: TOO HARD (NATURE)** **[M2006-013]**, **[M2000-019]**, **[L1993-023]**. The file closes here.

## Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED.
## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (balance sheets read below as computation, per the brief's Step 0).
## Q5: WHO RUNS IT. NOT REACHED.
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7: WHAT IS IT WORTH. NOT REACHED.
## Q8: BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9: COULD IT RUIN US. NOT REACHED.
## Q10: THE FAT PITCH. NOT REACHED.
## Q12 (optional): PROUD OF HOW THE MONEY IS MADE. NOT REACHED (facts bearing on it are in the contrary-evidence list,
items 5 and 7, and below; no verdict).

---
## COMPUTATION — NOT A CLEARANCE
*Everything in this section was produced after the closing STOP at Q2. It carries no entry language (operator rule 3)
and is reported at the owner's request, not as a rule change.*

### The balance sheets, FY2011 to FY2026 ("balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**)
USD millions, year-end June; XBRL first-filed vintage, read against the filed balance sheets of the 10-Ks listed above.

| June | Equity | Cash | Mkt. sec. | Receivables | Recv./revenue | Goodwill | LT debt | Treasury stock | Shares out (M) |
|---|---|---|---|---|---|---|---|---|---|
| 2011 | 448.6 | 193.1 | - | 96.2 | 18.4% | 55.6 | - | - | 35.9 |
| 2013 | 530.2 | 181.5 | - | 186.5 | 22.0% | 61.4 | - | - | 37.4 |
| 2015 | 536.9 | 195.9 | - | 188.2 | 19.8% | 66.2 | - | 75.0 | 38.3 |
| 2018 | 587.2 | 231.1 | - | 176.3 | 19.2% | 90.2 | - | 102.5 | 39.6 |
| 2020 | 675.3 | 212.3 | - | 236.1 | 22.7% | 174.9 | - | 102.5 | 41.0 |
| 2021 | 804.6 | 386.1 | - | 369.3 | 24.0% | 240.4 | 299 | 102.5 | 41.6 |
| 2023 | 947.3 | 410.8 | 111.9 | 463.7 | 25.2% | 246.7 | 413 | 102.5 | 43.0 |
| 2025 | 1,479.6 | 782.5 | 202.8 | 559.6 | 23.3% | 246.7 | 416 | 102.5 | 43.5 |
| 2026 | 1,632.3 | 754.5 | 203.5 | 664.8 | 26.4% | 246.7 | 418 | 292.1 | 41.5 |

What moved and why. **Equity** rose 448.6 to 1,632.3, almost all of it after FY2021 (retained earnings -13 at FY2018 to
1,185 at FY2026, `run.py` table): fourteen years of book growth sit in the last five. **Goodwill and intangibles** rose with
the FY2020-21 adult-learning purchases (Galvanize $168.0M, MedCerts $55.0M, Tech Elevator $16.1M in cash, cash-flow
statements FY2020-21); intangibles fell to 11 at FY2026 after the $59.5M Galvanize impairment of FY2025, and the business
they bought earns $56.6M of revenue, falling. **Cash** tripled; it swings seasonally (cash and securities $1,011.4M at
2025-06-30, $749.6M at 2025-09-30, 8-K `0001171843-25-006722`) because the first quarter carries the year's billings.
**Receivables** rose faster than revenue in FY2021-23 and again in FY2026 (contrary item 8); the 10-K notes funding
estimates have differed from actual reimbursements by 0.8% to 2.8% of revenue (FY2023-25). **Debt** is one instrument:
$420M of 1.125% convertible notes due 2027-09-01, conversion price about $52.88, with capped calls to $86.174 (10-K FY2026,
Liquidity); plus finance leases on student computers, $116.9M at FY2026 against $86.9M a year earlier. **Shares**
outstanding rose 35.9M (FY2011) to 43.5M (FY2025) despite $102.5M of buybacks before FY2019, then fell to 41.5M after
$188.7M bought in FY2026 at an average $81.50 (note 10). What the figures cannot say: the state-by-state concentration of
revenue (not disclosed beyond "no contract above 10%") and the renewal dates of the school contracts.

### The real costs (Q4 material)
Depreciation and amortization ($126.6M FY2026) is mostly student computers, capitalized software and capitalized
curriculum, which "are very real expenses" in the software case **[L2012-003]**; all capital spending ran at about D&A.
Stock pay $40.3M (FY2026) is excluded from every "adjusted" figure the filer leads with: "wave away very real costs"
**[L2016-006]**; stock pay is "the most egregious example" **[L2015-003]**; and the releases feature "EBITDA" and
"Adjusted EBITDA", against "where people are talking about EBITDA, is going to be about zero" **[M2002-026]**. The
FY2025 bonus plan pays on revenue and Adjusted EBITDA; the PSUs on adjusted operating income and stock-price growth (DEF
14A). Recorded for Q4/Q6; not weighed, since the file is closed.

### Value range (the Q7 CONVENTION construction, run as arithmetic only)
- Input: five-year mean owner cash after every real cost, FY2022-26, **$171.6M**.
- Growth shown: on aggregate owner cash FY2022 to FY2026, 30.9% a year, from a low base year ("a base year in which earnings were poor can produce a breathtaking, but
  meaningless, growth rate" **[L2005-003]**); carried ten years from the five-year mean it would put owner cash at about
  $2.5bn, the whole of FY2026 revenue, an absurdity under Q3's cap.
  **CONVENTION of this run:** the growth input is capped at the revenue growth shown over the same window, **10.5% a year**
  (FY2022 $1,686.7M to FY2026 $2,518.1M); rationale: owner cash cannot outgrow revenue for ten years from a margin
  already at the fifteen-year high without the margin rising without limit.
- Ten years at the growth, then zero nominal growth, at 5.66%. Excess cash: **CONVENTION of this run:** cash and
  securities at the seasonal low ($749.6M at 2025-09-30) less the $420M convertible principal = **$329.6M**; rationale:
  only cash free across the whole school year is surplus; at the June year-end figure ($1,034.1M) the per-share values
  below rise by $6.85.
- **VALUE RANGE: $80.88 (no growth) to $175.85 (shown growth, capped) a share, against $78.88.** Width 2.2 to one, under
  the three-to-one line. Under the convention the price sits just below the bottom of a narrower range: that would close
  OUT at Q7, had Q7 been reached, since it does not "scream at you" **[M2009-005]**.
- **Whole-cycle variant** (the five-year window holds the five best years of fifteen): the fifteen-year mean owner-cash
  margin, 3.31%, applied to FY2026 revenue gives $83.2M; **$43.32 (no growth) to $89.39 (capped growth)**. The price sits
  inside it.

### Fair price and cheap price (owner's request)
- **Tax and base.** The floor (CONVENTION, Q7) is about ten percent pre-tax, after "we don’t want to buy equities where
  our real expectancy is below 10 percent" **[M2003-149]**. Owner cash is after tax; at
  the FY2026 effective rate of 23.3% (10-K FY2026, MD&A) ten percent pre-tax is **7.67% after tax**. The floor is applied
  to equity with the excess cash netted out (enterprise value less surplus cash, the convertible principal already
  deducted), since owner cash is struck after interest.
- **Central case (CONVENTION of this run):** the five-year mean owner cash held flat, neither the capped growth nor the
  whole-cycle reversion; rationale: it is the bottom of the convention's own range, and the span gives no ground to pick
  the growth end over the reversion end.
- **FAIR PRICE: $61.76** (= ($171.6M / 0.0767 + $329.6M) / 41.560M). At $78.88 the five-year mean owner cash yields 5.82%
  after tax on equity net of surplus cash, about 7.6% pre-tax: below the floor.
- **CHEAP PRICE: $34.04. Rule (CONVENTION of this run):** the price at which the whole-cycle case (the fifteen-year mean
  owner-cash margin on today's revenue, no growth) still clears ten percent pre-tax; below it the thin-margin decade
  itself pays the floor, so no pencil is needed on which regime returns ("if you have to actually do it on — with pencil and paper, it’s too
  close to think about" **[M1996-084]**).
- None of the three figures reopens the file: "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a
  fraction of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**

### Other computations (Q6 material, not reached)
- Buybacks: 2,314,944 shares at an average $81.50 in FY2026 (note 10), about the bottom of the computed range ($80.88),
  above the fair price ($61.76) and below the whole-cycle top ($89.39); the November 2025 authorization names no
  price (8-K `0001104659-25-105334`).
- Convertible: at $78.88 the conversion spread over principal is about $206M and is covered by the capped calls up to
  $86.174; the $420M principal is due in cash on 2027-09-01, inside the surplus computed above.
- Pay: CEO total compensation $21.5M in FY2025, $15.6M in FY2024, $9.7M in FY2023 (DEF 14A summary compensation table);
  directors and officers own 3.0% (1,305,439 shares). Subsidiary RSUs for named officers vest only on a liquidity event of a
  subsidiary (DEF 14A).

---
## THE BOX
**TOO HARD (NATURE), decided at Q2.** The castle (scale, a 31-state bundle, multi-year contracts) is real, but it was there in
FY2013-2017 when it earned 1.5% to 5.4%; the FY2024-26 returns rose in step with the rival's, so the
ten-year earning power turns on what legislatures, authorizers and boards in 31 states pay and permit, a forecast no
insider writes down. Computation only: value range $80.88 to $175.85 (whole-cycle $43.32 to $89.39), fair $61.76, cheap
$34.04, against $78.88. Q11 belongs to a holding review.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. Not committed: the brief forbids commits
      (the write-early commit step of the template is therefore not met, by instruction).
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, below); every filing fact carries its
      accession or names its document; numbers without a filing are labelled computation or CONVENTION.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; everything after it is headed COMPUTATION and
      carries no entry language.
- [x] Owner cash after every real cost (stock pay, curriculum and software capitalization, student-computer lease
      principal), never a net-income proxy; the sovereign from the US Treasury; the aggregator price flagged.
- [x] Contrary evidence written down as found, "write it down in the first 30 minutes" **[M1997-127]** (ten items, and one against the case against).
- [x] No point-in-time anchor; rows of every year were usable.
- [x] Only the arithmetic lines of `tools/run.py` were used; its as-filed capex was replaced by the alternates, and why.
- [x] `python tools/check_framework.py` PASS after the final edit (2026-10-06); a script check found no E-id, every
      M/L/R id in the v5 ledger, and every quoted fragment beside an id inside that row. Not committed, by instruction.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 against Q2 for a business whose price is set by a government payer.** Q1's definition asks for "a reasonable fix
on about what the earning power and competitive position will look like" **[M2012-065]**, which I could not get; Q2
asks what will "destroy, or modify, or reduce the economic strengths" **[M2000-014]** and sends an unjudgeable castle to
TOO HARD. The routing paragraph sends only fast technological change to Q1. A business
whose economics are simple but whose price is a legislature's decision fits neither sentence; I passed Q1 on "the economic
dynamics of the industry" **[M2011-014]** and closed at Q2, and another analyst could close at Q1 on tests 2 to 4 with the same box. The
framework could say which question owns payer-set economics. (2) **WORK against NATURE when part of the deciding question
is knowable.** Section I tests the cause by whether insiders would "put down on paper their predictions" **[M2000-105]**; here the scale
edge and the contract history are knowable and the legislative future is not. I named the deciding question as the part
that is not knowable, and said why the knowable parts do not decide it; the framework gives no rule for splitting a
question this way, and a pass run on the knowable parts would have had to end NATURE anyway. (3) **The Q7 range convention
breaks on a low base year.** "The growth shown" on aggregate owner cash was 30.9% a year from FY2022's low base; the
convention's only cap is Q3's absurdity test, which names no figure, so I confessed a cap (revenue growth over the same
window). (4) **"Excess cash" is undefined** for a business whose cash swings by a quarter of a billion dollars within the
year; I used the seasonal low and showed the year-end alternative. (5) **The fair and cheap prices** rest on a central case
and a cheap-price rule that the framework does not define; both are confessed above as conventions of this run.
