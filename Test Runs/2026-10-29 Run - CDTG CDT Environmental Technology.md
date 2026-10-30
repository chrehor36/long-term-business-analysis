# Company Run — CDT Environmental Technology Investment Holdings Limited (Nasdaq: CDTG) — 2026-10-29
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch** (commit
9951c482).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session, 2026-10-29, after the run was committed: not held (no CDTG line in `PORTFOLIO.md`).*

**Dispatched run.** Written by a dispatched analyst under the brief of 2026-10-29 (canonical brief
`Screens/_daily/_dispatch_brief.md`, with the brief's two stated departures: the repository path, and lines of evidence
chosen by the analyst rather than written in the brief). Working folder `Test Runs/_research 2026-10-29 CDTG/`
(notes, scripts, the arithmetic output, the sovereign and exchange-rate files; raw filings in its gitignored `cache/`).

**Lines of evidence chosen** (the brief's departure; derived from the 20-F's Item 4, Item 3.D and Item 5): (1) the
collection of what the business bills to customers funded by local governments, against what it reports as revenue
(Item 3.D, the going-concern and receivables risk factors; Item 5, revenue and the provision for credit losses); (2) the
castle of the deciding part, rural sewage treatment systems sold through state-owned construction contractors (Item 4,
Business Overview, Customers, Sales and Marketing, Manufacturing, Competition); (3) the stated move into green hydrogen
and the wind-down of the septic-tank line (Item 4); (4) the issuance of shares and the financing of operations (Item 5,
Recent Developments; Item 7); (5) the corporate structure as the filing describes it (Introduction against Item 4.A), and
related-party dealings (Item 7.B).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $1.02 (close 2026-10-28; Yahoo Finance chart endpoint, an **aggregator, flagged**, live quote only, operator
  rule 5). `tools/run.py` printed $1.01 for 2026-10-29 (intraday, same class of source, flagged). The price is
  post-consolidation (the 1-for-25 consolidation took effect 2026-06-01).
- **Shares by class:** Class A only; no Class B issued (20-F cover and Item 4.A). Built from the filings:
  - 13,525,000 Class A issued and outstanding at 2025-12-31 (20-F for FY2025, filed 2026-05-15, accession
    `0001731122-26-000740`, cover page; `python Screens/cover_shares.py CDTG` prints the same 13,525,000 from that cover).
  - 62,000,000 Class A sold 2026-04-17 at $0.105 a share, gross $6,510,000, completed (same 20-F, Item 5, Recent
    Developments, and Item 7.A); 75,525,000 outstanding at 2026-04-30 (Item 3.D).
  - 1-for-25 consolidation effective 2026-06-01: "from approximately 75,525,000 to approximately 3,021,000" (6-K of
    2026-05-28, accession `0001731122-26-000796`, Exhibit 99.1). **Count used: 3,021,000.**
  - Cross-check: Jane Street's Schedule 13G (accession `0001595888-26-000111`, event 2026-08-17) reports 154,512 shares as
    5.1%, which implies about 3.03 million outstanding, consistent. No treasury shares are stated. Of the 2,000,000
    pre-consolidation shares subscribed in December 2025 at $0.50 (6-K of 2026-01-05, `0001731122-26-000010`), 1,200,000
    are in the year-end count; the other 800,000 (32,000 after consolidation) are not in the 2026-04-30 count and are left
    out (immaterial). The extraordinary general meeting of 2026-07-28 raised the authorised capital to 470,000,000 Class A
    (6-K `0001731122-26-000978`, Exhibit 99.1); no issuance after the consolidation is reported on any 6-K through the price
    date. A Form 3 and a Form 4 filed 2026-08-25 by HRT Financial LP (accessions `0001475597-26-000213`, `-000214`) mark
    the filer a ten-percent owner while reporting 6,987 and 9,039 shares from short sales; that cannot be reconciled with a
    3.02 million count and is recorded, not used.
- **Market cap:** 3,021,000 × $1.02 = **$3.08M**.
- **Sovereign for the earnings currency (renminbi):** **2.0467%**, the 30-year point of the China treasury bond yield
  curve (中债国债收益率曲线), as served on the Ministry of Finance's treasury yield curve page by China Central Depository &
  Clearing (ChinaBond), `yield.chinabond.com.cn/cbweb-czb-web`, curve dated 2026-10-29; 30 years is the longest tenor on
  the curve. File: `Test Runs/_research 2026-10-29 CDTG/sovereign_chinabond_czb_20261029.json`. (The protocol's table
  covers USD, JPY and EUR only; this is the issuing authority's curve for RMB, named and dated. `tools/run.py` printed the
  USD sovereign, 5.37%, which is not the earnings currency and is not used.)
- **Exchange rate:** USD/CNY central parity **6.7147**, 2026-10-29 09:15, published by the China Foreign Exchange Trade
  System for the People's Bank of China (`chinamoney.com.cn` ccpr; file `cfets_ccpr_20261029.json`). The filer reports in
  USD translated at its own average rates (RMB 6.45, 6.73, 7.05, 7.14, 7.19 to $1 for 2021 to 2025); for Q7 each year is
  turned back into RMB at the filer's rate and into USD at 6.7147.
- **Filings read** (operator rule 4): the 20-F for FY2025 (2026-05-15, `0001731122-26-000740`): Items 3.D, 4, 5, 6.E, 7,
  15 and the audited statements with the auditor's report; the 20-F for FY2023 (2024-05-15, `0001731122-24-000803`) and
  FY2024 (2025-05-15, `0001731122-25-000746`) statements; the 20-F/A for FY2024 (2025-09-09, `0001731122-25-001219`)
  and the SEC correspondence around it (company responses of 2025-08-26 `0001731122-25-001170` and 2025-09-09
  `0001731122-25-001221`); the IPO prospectus 424B4 (2024-04-18, `0001731122-24-000653`) for FY2021 and FY2022; the
  first F-1 (2021-01-15, `0001731122-21-000083`) for FY2018 and FY2019 and F-1/A No. 6 (2022-03-25,
  `0001731122-22-000538`) for FY2020; the 424B3 of 2026-04-17 (`0001731122-26-000591`, downloaded, not relied on beyond
  the 20-F); the 6-Ks of 2025-09-29 to 2026-07-28 and their exhibits. No proxy statement: a foreign private issuer; the
  notices of meeting are on 6-K.
- **One figure cross-checked against the filed statement:** net cash used in operating activities for FY2025,
  $(1,490,957) on the filed Consolidated Statement of Cash Flows (20-F `0001731122-26-000740`, F-6), against -1.5 ($M) in
  `tools/run.py`'s tagged series; accounts receivable, net, $44,128,933 on the filed balance sheet (F-3) against 44,129
  ($K) in the tool's table. Both agree.
- **`python tools/run.py CDTG`, arithmetic lines only:** operating cash flow -3.1, -2.0, -1.5 ($M, FY2023 to FY2025);
  stock pay not tagged for 2023 (the filed statement shows none that year, so nothing is missed), 0.5 and 2.1; capital
  spending 0.0 each year; depreciation 0.3, 0.3, 0.2; owner cash on the capital-spending basis -3.2, -2.4, -3.6. Every
  line checked against the filed statements (the longer series is built in `scripts/arith.py` from the statements
  themselves, FY2018 to FY2025). The tool's "earnings currency: USD" is the reporting currency, not the earnings currency.

**Owner cash after every real cost, from the filed statements** (operating cash flow, less stock pay added back in it,
less all capital spending including intangibles; USD as filed; `arith_output.txt`):

| FY | net income | operating cash flow | stock pay | capital spending | **owner cash** |
|---|---|---|---|---|---|
| 2018 | 2,743,077 | (2,155,783) | 0 | 129,332 | **(2,285,115)** |
| 2019 | 2,496,129 | (2,319,179) | 0 | 94,944 | **(2,414,123)** |
| 2020 | (1,528,273) | (568,854) | 0 | 28,029 | **(596,883)** |
| 2021 | 6,578,260 | (129,639) | 0 | 101,279 | **(230,918)** |
| 2022 | 5,242,789 | (4,472,780) | 0 | 86,941 | **(4,559,721)** |
| 2023 | 7,024,054 | (3,132,666) | 0 | 21,550 | **(3,154,216)** |
| 2024 | 1,406,282 | (1,987,028) | 454,250 | 3,893 | **(2,445,171)** |
| 2025 | (10,366,087) | (1,490,957) | 2,145,000 | 2,233 | **(3,638,190)** |

Eight years: net income $13.6M in total, operating cash flow $(16.3)M in total. Owner cash was negative in every year
filed. Five-year average (FY2021 to FY2025): $(2.81)M after interest; $(2.71)M with the interest paid added back (cash
income tax paid was $7,271, $141 and nil in FY2023 to FY2025, so no tax shield is deducted).

## THE FOUNDATIONS (not a gate)
Two foundations bear on this name. A share is a business **[M1997-109]**: at $3.08M of market value against $30.6M of book
equity at 2025-12-31 the quotation invites the cigar-butt reading, and what decides the outcome is "the prospects of the
businesses" **[M1998-099]**, not the discount to book. And the market serves and does not instruct **[M2006-077]**: the
quotation says only that the market does not believe the receivables, which the questions must test for themselves. No
macro forecast enters **[M2000-094]**; the run does not forecast China's local-government finances, it reads what this
company's customers have paid. Who is paid to tell you **[M2020-037]**: the company's own releases call it "a leading
national player" that "has completed more than 150 plants across China" (6-K of 2026-07-07, Exhibit 99.1,
`0001731122-26-000918`), while its 20-F says "more than 60 rural sewage treatment plants"; the run reads the 20-F. **Contrary
evidence, written down as found** **[M1997-127]**: in favour of the name, the reported gross margin rose to 41.5% in 2025
(from 33.3% in 2023), the backlog at 2026-03-31 was RMB 187 million of provisional contract value (Item 5), the CEO's
entities lend to the company interest-free (Item 7.B), and the price is far below book; against it, everything in the
cash table above. Both sides are carried into the questions.

## THE STANDING RULE
The run concerns a part-interest bought for cash with no borrowing; nothing in owning it puts the buyer at risk of ruin, provided the
purchase is not made on borrowed money **[L2014-005]**. The target's own going-concern doubt is the target's risk (Q9), not
the buyer's; "Never risk permanent loss of capital." **[L2023-005]** is answered by the size of any commitment, which no
question here reaches.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The parts.** The filer reports two lines (Item 5): sewage treatment systems (revenue $17.28M of $18.23M in 2025; gross
  profit $7.20M of $7.56M) and sewage treatment services (septic tanks, "placed into active wind-down", Item 4). The
  third, green hydrogen from organic waste by gasification, has no revenue: "Neither project has commenced construction,
  and the Company has not entered into binding agreements for feedstock supply or offtake of energy products" (Item 4).
  By Q1's paragraph on parts (a part matters when it decides, more than half of five-year operating profit, or the
  largest), **sewage treatment systems decide**; the hydrogen line does not decide on any filed figure. It is a start-up,
  and "Start-ups are not our game." **[L2007-015]**; it is recorded here and weighed below, not used to close the file.
- **The test as the draft states it** **[M2012-065]**, **[M2000-037]**: a reasonable fix on the earning power and
  competitive position of the deciding part in ten years. The economics of that part are plain on the filings: the
  company designs small decentralised treatment plants (5 to 500 tons a day), has the equipment made by four outside
  suppliers, installs and operates them, and is engaged by city or provincial state-owned construction companies that
  win the bids from local governments (Item 4, Sales and Marketing). Revenue is recognised over time on a cost-to-cost
  basis and billed at milestones (SEC response of 2025-08-26). There is little technology in it of the kind the filter
  excludes **[M1998-008]**: the method is a biochemical process the filing compares with A/O, A2/O and MBR.
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) the number and size of projects won through
  the state-owned contractors; (2) the margin on them; (3) whether, and when, the customers pay. All three are read off
  the figures, as the five-minute rule asks: "So if you can’t make a decision on something like PetroChina off the
  figures, forget about going further" **[M2008-069]**. The third is the one that decides, and the filing states its
  history year by year: collection rates on progress billings "were 99.3%, 99.8%, 98.4%, 72.8%, 75.6%, 52.4%, 9.9% and
  3.1% for the years 2018, 2019, 2020, 2021, 2022, 2023, 2024, and 2025" (Item 3.D). Whether that record makes the
  castle good or bad is Q2's question; that it can be read is Q1's.
- **Abroad** **[M2000-141]**, **[M2006-021]**: the governance and the tax have two features a buyer must understand and
  the filing makes hard. The 20-F says in its Introduction that CDT Cayman "uses a structure that involves a variable
  interest entity, or VIE, based in China" and that "The VIE is consolidated for accounting purposes but it is not an
  entity in which CDT Cayman or its subsidiaries own equity", and says in Item 4.A that "Our equity structure is a direct
  holding structure" in which CDT Cayman "holds 100% of the outstanding equity of Shenzhen CDT". No VIE agreements,
  VIE entity or VIE note appear anywhere else in the 20-F (text search for "VIE", "variable interest" and "contractual
  arrangement"); the FY2023 20-F carries no such statement. The run reads the structure as the direct holding the rest of
  the filing describes, and records the contradiction for Q4 and Q5. Funds move in only with SAFE, SAMR and MOFCOM
  filings that "may take several months", and the chief executive's own SAFE change registration was incomplete at the
  filing date (Item 4.A).
- **Contrary evidence, written down** **[M1997-127]**: "if you have doubts about something being into your circle of
  competence, it isn’t." **[M2002-092]**. The doubt here is not about how the deciding part makes money; it is whether its
  customers will pay, and whether management will keep the part at all (the filing calls the hydrogen move "a strategic
  transformation"). The first is read from the figures at Q2; the second is a use of the money, Q6. Neither is a doubt
  about understanding the economics of sewage plants built for village governments.
- **Routing:** not a fast-changing industry; not a financial institution; not a holding company in the sense of Q1.
- **VERDICT: IN**, narrowly, on the deciding part, sewage treatment systems: its economics can be read off its figures
  **[M2008-069]**, **[M2008-033]**, and its key variables are knowable from the filings **[M1998-044]**. Recorded against
  it and carried: the structure statement that contradicts itself (to Q4 and Q5) and the hydrogen start-up (to Q6)
  **[L2007-015]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question **[M1995-038]**: "why is that castle still standing? And what’s going to keep it standing or cause it not to
be standing five, 10, 20 years from now." Asked of the deciding part, rural sewage treatment systems.

**The castle tests, each with its filing fact** (20-F `0001731122-26-000740` unless stated):
1. **What keeps it standing, and how permanent** **[M1995-038]**. The filing names its factors: the quick-separation
   process, two invention patents and 36 utility-model patents, a regional network, and its relations with state-owned
   contractors (Item 4, Core Competitive Strengths). On permanence the filing itself says "it may be possible for third
   parties to copy or otherwise obtain and use our proprietary technology without authorization or to develop similar
   technology independently" (Item 4, Intellectual Property), and research spending was $47,602 in 2025, $61,786 in
   2024 and $80,948 in 2023 (Item 4, Research and Development).
2. **Would it stand without the lord** **[M1996-037]**. The projects come through relationships: "We assist the state-owned
   companies in their bidding process with local governments" (Item 4, Sales and Marketing). The rows ask for a business
   that does not need great management; the filing shows a business that needs a contractor to choose it each time.
3. **The money test** **[M2011-015]**: "if I had a hundred million dollars and I wanted to go in and take on See’s Candy,
   could I do it?" The equipment is made outside: "Our suppliers have the ability to manufacture any of our integrated
   rural sewage treatment systems" (Item 4, Manufacturing); the barriers the filing names are "stringent performance
   standards, product qualification protocols and requirements for consistent levels of service and support" (Item 4,
   Competition), which a funded entrant meets by hiring. The whole company was carried at $30.6M of book equity. An
   attacker with money could do it; "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**.
4. **Pricing power, and the agony before a rise** **[M2005-020]**. The power runs the other way. The business cannot get
   paid what it has already billed: collection on progress billings fell from 99.3% (2018) to 3.1% (2025) (Item 3.D);
   "as of April 30, 2026, we had collected approximately 0.0% of the outstanding balances from our five major customers
   as of December 31, 2025" (Item 3.D); days sales outstanding rose "to 455 days at December 31, 2024 and then to 894
   days at December 31, 2025" (Item 3.D). A supplier that waits two and a half years for its money has no price to raise.
5. **Unit volume** **[M1999-108]**. New projects begun: four in 2023 (contract value about $35.4M), three in 2024 (about
   $19.5M), two in 2025 (about $16.8M) (Item 5). Revenue $34.21M (2023), $29.77M (2024), $18.23M (2025); the septic-tank
   line fell from $3.28M (2021) to $0.95M (2025) and is "placed into active wind-down" (Item 4). The filer attributes the
   fall to "decreased demand for the Company’s services due to the economic downturn" (Item 5).
6. **The low-cost position** **[M2004-091]**. No cost figure against any rival is filed, and no rival files. Not shown
   either way.
7. **The brand in the customer's mind.** The customer is the contractor, and the filing puts the standing on the
   contractor's side: "the state-owned companies have good relationships with local governments, well-known brands, and
   sufficient working capital" (Item 4, Sales and Marketing). The castle the filing describes is the customer's.
8. **Would the customer still choose it over the low bid** **[M2017-009]**. Customer concentration moves with each project
   (largest customer 23.4% in 2023, 22.1% in 2024, 46.6% in 2025, Item 4, Our Customers); the six largest receivable
   balances at 2024 year-end were six different construction groups, each tied to one project (SEC response of 2025-08-26,
   `0001731122-25-001170`). Nothing in the filings shows a customer who returns because it must; nothing shows the low
   bid either.
9. **Ask the competitors** **[M1999-130]**. The filing names none (row below).
10. **Widening or narrowing** **[M1999-108]**: on every filed measure, narrowing: projects, revenue, the second line, and
    above all the terms on which the customers pay.
11. **What could destroy it** **[M2000-014]**: the filing names it, and it is happening: "All five of our major customers are
    projects funded by local governments and are awaiting inspection reports and payment approvals" (Item 3.D). And the
    management's own plan is to leave: the 2025 "strategic transformation" toward green hydrogen, with the April 2026
    proceeds "originally intended to fund our new energy initiatives" and "currently being applied to support our ongoing
    operations" (Item 3.D).

**The competitor row.** The 20-F names no rival: "We face competition from several regional competitors in the rural
sewage treatment industry and the septic tank treatment industry", "typically small in scale" (Item 4, Competition). No
named rival, so none whose filings can be read and none that files with the SEC to flag. What that leaves for Q2: the
field's returns can be judged only from the filer's own filings, and the castle tests rest on the filer's own facts above.
The run does not reach for rivals the filing does not name (the brief's rule).

**The parts table** (five years, FY2021 to FY2025; the filer reports gross profit by line, not operating profit, so gross
profit is the measure used, said so):

| part | gross profit FY2021 to FY2025 | share | castle | decides |
|---|---|---|---|---|
| sewage treatment systems | $45.3M | 93% | open (tests 1 to 11) | **yes** |
| sewage treatment services (septic) | $3.6M | 7% | in wind-down | no |
| green hydrogen | nil (no revenue) | 0% | none yet; a start-up **[L2007-015]** | no |

**The field's returns over the last full cycle, judged in words.** The span read runs eight fiscal years, 2018 to 2025,
through the 2020 fall, the 2021 to 2023 rise and the 2024 to 2025 fall (revenue $14.15M, $18.73M, about $8.9M, $23.56M,
$28.85M, $34.21M, $29.77M, $18.23M). Reported net income added to $13.6M over the eight years; operating cash flow was
negative in every one of them and added to $(16.3)M (Step 0 table). The reported return on equity looked high in the
good years (net income of $7.02M in 2023 on equity of about $32M), but in no year filed did the business return cash to
its owners: even in 2018 and 2019, when the collection rates stood at 99.3% and 99.8%, owner cash was $(2.3)M and
$(2.4)M. Judged in words, as the convention asks: over a full cycle the castle protected no cash return at all. A moat is
what "protects excellent returns on invested capital" **[L2007-004]**; this one has protected none.

**A change for the better?** None is claimed for the deciding part; the change the filer describes is a leaving of it.

**VERDICT: OUT.** The castle of the deciding part is shown open on the filer's own evidence, not merely unjudgeable: the
customers set the terms on which they pay and have stopped paying (tests 4 and 11); the product can be made by the
company's own suppliers and, on the filing's own words, copied (tests 1 and 3) **[M1996-017]**, **[M2012-106]**; volume and
revenue are falling and management is moving the money elsewhere (tests 5, 10, 11); and over eight years the business has
not produced a dollar of owner cash **[L2007-004]**. A funded attacker could take it, "If the answer had been yes, we
wouldn’t have done it." **[M2011-015]**; and "If you really think a business is declining, most of the time you should
avoid it." **[M2012-062]**. The box is OUT, not TOO HARD: the tenuous-moat row sends to TOO HARD a moat whose value cannot
be known, "We don’t know how to valuate that" **[M2000-019]**, and here the filings show the outcome. Price does not
reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (closed at Q2).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (closed at Q2).
## Q5 — WHO RUNS IT. NOT REACHED (closed at Q2).
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED (closed at Q2).

## Q7 — WHAT IS IT WORTH? COMPUTATION, NOT A CLEARANCE
*Computed after the Q2 STOP for the operator's two reporting figures (Part VII, The owner's price). Not a verdict, no
entry language (operator rules 2 and 3). The arithmetic is `scripts/arith.py`, output `arith_output.txt`.*

- **The cash input.** Owner cash after every real cost (Step 0 table): operating cash flow, less the stock pay added back
  inside it, less all capital spending. Every working-capital draw is inside operating cash flow and is counted, specific
  (d) **[M2008-036]**, **[M2003-122]**. Five-year window FY2021 to FY2025, each year turned into RMB at the filer's own
  average rate and into USD at the 2026-10-29 central parity of 6.7147: **all-equity basis** (cash interest paid added
  back; no tax shield deducted because the company paid $7,271, $141 and nil of income tax in cash in FY2023 to FY2025)
  RMB (18.97)M a year = **$(2.82)M**; **equity-only** (after interest) RMB (19.61)M = **$(2.92)M**. Literal window as filed
  in USD: $(2.71)M and $(2.81)M.
- **Specific (a), cycles.** No end year is aberrational in a way that would lift the base: the filer describes 2024 and
  2025 as a downturn, but the eight-year average FY2018 to FY2025, which spans the pre-2020 years of near-full collection,
  is also negative, $(2.42)M a year, and owner cash was negative in every year filed. Shown beside; it does not change the sign.
- **Specific (b), decline and sign.** The series is negative throughout; a compound rate between negative end years is
  meaningless, and so is a rate between the halves (FY2021 and FY2022 average $(2.40)M; FY2024 and FY2025 average
  $(3.04)M). **The range is the no-growth case alone, said so.**
- **Specific (c), acquisitions:** none; two small subsidiary disposals (gains of $132,844 and $34,468) are left in.
- **Specific (e), growth spending:** capital spending was $2,233 to $101,279 a year; the drain is working capital. The
  filing allows no maintenance guess that would separate a growth draw from a standing-still draw: receivables and
  contract assets rose while revenue fell (Q4 facts below). The all-spending case is the only case.
- **Specific (f), the cap:** not engaged.
- **Rate:** 2.0467%, the 30-year China treasury yield of 2026-10-29 (Step 0). Zero nominal growth after year ten, and
  zero before it.
- **Net debt** (all-equity basis): borrowings at 2025-12-31 of $6,129,135 (bank short-term $1,153,654, third parties
  $2,057,311, related parties $2,560,675, bank long-term $357,495), less cash of $66,686, less the stated net proceeds of
  about $6.3M from the April 2026 offering (20-F Item 3.D, a subsequent event the filing states) = **net cash of about
  $0.24M**. No finance leases; operating leases none at year-end, said so. Left out of net debt by the convention, and
  stated here because they are larger than the market value: accounts payable $39.22M and taxes payable $10.33M.
- **Floor tested first:** no case earns the floor at any positive price, since the cash stream is negative
  **[M2003-149]**. The width test does not arise.
- **Value range (COMPUTATION):** the single no-growth case at the sovereign, $(2.82)M ÷ 2.0467% = $(138.0)M for the
  business, plus net cash of $0.24M, over 3,021,000 shares = **$(45.61) a share**. A range of one point; there is no
  shown-growth case to make a second end.
- **Fair price (reporting figure, Part VII):** the no-growth case valued at ten percent, $(28.2)M, plus net cash $0.24M,
  over 3,021,000 shares = **$(9.27) a share, all-equity basis, central**, after the company's own tax (which it does not
  pay in cash). **Equity-only beside it: $(9.67)** a share with the offering's cash left out, $(7.56) with the cash of the
  offering and the year-end cash added. Not positive on any basis. Growth spending charged: none, in year one and year ten
  (specific (e)). No cheap price is reported.
- **Against the price** of $1.02 (2026-10-28, aggregator, flagged): the price is above every figure computed; market value
  $3.08M.
- **VERDICT:** none (computation after a closing STOP). Had Q7 been reached, the floor convention would have closed it OUT
  on these figures.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES. NOT REACHED (closed at Q2).
## Q9 — COULD IT RUIN US. NOT REACHED (closed at Q2).
## Q10 — IS IT THE FAT PITCH. NOT REACHED (closed at Q2).
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE. NOT REACHED (closed at Q2).

---
## THE BOX
**OUT at Q2**: the castle of the deciding part (rural sewage treatment systems) is shown open on the filer's own evidence:
customers who have stopped paying, a product its suppliers can make, falling volume, management moving the money to a
hydrogen start-up, and negative owner cash in every year filed **[M2011-015]**, **[L2007-004]**, **[M2012-062]**.
COMPUTATION beneath the stop: value $(45.61) a share (no-growth case alone), fair price $(9.27) all-equity, $(9.67)
equity-only, against $1.02. **Integrity facts recorded, not judged** (Part VII; see Q5 below).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts already found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; no
verdict; the box unchanged, operator rule 2.)*

**Bears on Q3 (capital).** Receivables plus contract assets against the year's revenue, from the filed balance sheets:
0.79 (2018), 1.24 (2019), 1.80 (2020), 1.29 (2021), 1.60 (2022), 1.99 (2023), 2.86 (2024), 4.58 (2025). Capital spending
on fixed assets is small ($2,233 in 2025); the capital the business consumes is the money its customers owe it.

**Bears on Q4 (the accounts).** The balance sheets, eight years, read before the income account **[M2025-032]** (USD
thousands, 31 December; F-1 `0001731122-21-000083`, F-1/A6 `0001731122-22-000538`, 424B4 `0001731122-24-000653`, 20-F
FY2023 `0001731122-24-000803`, 20-F FY2025 `0001731122-26-000740`; receivables and contract assets include the non-current
portions):

| year | revenue | receivables, net | contract assets | accounts payable | taxes payable | borrowings | total equity | cash |
|---|---|---|---|---|---|---|---|---|
| 2018 | 14,146 | 8,915 | 2,295 | 1,938 | 1,081 | 2,991 | 9,861 | 1,455 |
| 2019 | 18,732 | 18,359 | 4,782 | 7,729 | 2,526 | 1,778 | 15,877 | 982 |
| 2020 | about 8,900 | 11,678 | 4,352 | 4,277 | 2,923 | 2,405 | 15,386 | 322 |
| 2021 | 23,557 | 14,671 | 15,677 | 10,298 | 3,894 | 2,037 | 22,392 | 1,093 |
| 2022 | 28,849 | 20,091 | 26,090 | 14,863 | 4,864 | 5,577 | 25,560 | 200 |
| 2023 | 34,210 | 29,077 | 39,166 | 23,785 | 5,424 | 8,506 | 32,087 | 268 |
| 2024 | 29,765 | 45,188 | 39,989 | 36,348 | 7,409 | 5,660 | 37,438 | 124 |
| 2025 | 18,226 | 44,129 | 39,310 | 39,221 | 10,330 | 6,129 | 30,640 | 67 |

What moved: receivables and contract assets grew from $11.2M to $83.4M while revenue went from $14.1M up to $34.2M and
back to $18.2M; accounts payable grew from $1.9M to $39.2M and taxes payable from $1.1M to $10.3M, so the unpaid receivables
were carried by unpaid suppliers and the unpaid tax authority; cash never exceeded $1.5M. What the figures do not say: when
the $68.4M of gross receivables (allowance $24.3M at 2025-12-31, Note 4) will be paid. Further facts: income tax expense of
$1,403,880 (2023) and $462,043 (2024) against cash income tax paid of $7,271 and $141 (supplemental cash-flow information);
a deferred tax asset of $3.50M recognised at 2025-12-31 on the credit-loss allowances; provisions for credit losses of
$6.46M (2024) and $14.69M (2025) after a net recovery of $0.09M in 2023; two material weaknesses and disclosure controls
not effective (Item 15); going-concern doubt in the auditor's report; the auditor, Wei, Wei & Co., dismissed effective
2024-04-25, three days after the IPO closed, and Enrome LLP engaged the next day (Item 16F); in the IPO prospectus, the
completion of the Wuyishan and Guankou projects, and the expected completion of the Zhongshan project, stated "according to
verbal discussions with such customer" (424B4, risk factors); and the structure stated two ways in one 20-F (Q1). The SEC staff's comment of July 2025 on the FY2024 20-F
asked how collectability was assessed under ASC 606 given days sales outstanding of 455 and an allowance of 31% of revenue
(company response `0001731122-25-001170`).

**Bears on Q5 (the people): integrity facts, recorded, not judged.**
- In its response to the SEC dated 2025-08-26 the company wrote that collections "accelerated significantly to
  approximately $3.0 million during July and August 25, 2025, demonstrating the effectiveness of the government’s debt
  resolution initiatives and validating our customers’ payment commitments", that "the Company believes the customer
  payment plans are credible", and that it "expects to collect the remaining balance of the December 31, 2024 accounts
  receivable on or before December 31, 2026" (`0001731122-25-001170`). Eight months later its 20-F reported a 2025
  collection rate of 3.1%, a 2025 provision for credit losses of $14.69M, and "approximately 0.0%" collected by
  2026-04-30 from the five major customers (`0001731122-26-000740`, Item 3.D).
- The same response told the SEC that the company "has not identified any such significant change" in its customers'
  ability to pay; the FY2025 provision was attributed in the 20-F to "increased credit risk and collectability concerns"
  (Item 5).
- Press releases describe "a leading national player" that "has completed more than 150 plants across China" (6-K
  exhibits of 2026-05-15 `0001731122-26-000748` and 2026-07-07 `0001731122-26-000918`); the 20-F says "more than 60 rural
  sewage treatment plants" (Item 4).
- The 20-F states a VIE structure in its Introduction and a direct holding structure in Item 4.A (Q1).
- In favour: the chief executive's companies lend to the group interest-free (Item 7.B: Shenzhen Li Yaxin $90,804;
  Beijing Minhongyun, among $2.56M of related-party loans); the risk factors disclose the collection collapse in plain
  figures.
- The chief executive's holding fell from 33.82% to 6.06% with the April 2026 offering; the buyers are "certain
  investors", not named (Item 6.E and 7.A).

**Bears on Q6 (the money and the owners).** Shares issued: 1,500,000 under the 2025 Equity Incentive Plan, all issued by
2025-03-28 (S-8 of 2025-02-14), expensed at $2.145M in 2025 to "one employee and two consultants" (Item 5); 1,200,000 at
$0.50 in December 2025 (6-K `0001731122-26-000010`); 62,000,000 at $0.105 in April 2026, $6.51M gross, for 82% of the
enlarged company, when book equity at 2025-12-31 was $30.6M, about $2.26 per pre-consolidation share (Item 5). The IPO in
April 2024 sold 1,500,000 shares at $4.00 (Item 4.A). Authorised capital raised to 470,000,000 Class A after the
consolidation (6-K `0001731122-26-000978`). The offering's proceeds, "originally intended to fund our new energy
initiatives", are "currently being applied to support our ongoing operations" (Item 3.D). No dividends ever; no buyback.

**Bears on Q9 (the target's debt and exposures).** Cash $66,686 at 2025-12-31; $5.77M of short-term borrowings due within
the year; going-concern doubt (auditor's report and Item 3.D); liquidated damages in the Zhongshan contract of 0.1% of the
contract a day for late tasks and 10% on termination (424B4, risk factors); dependence on local-government payment
approvals (Item 3.D).

**Bears on Q12.** Nothing in the named businesses; treating village sewage is a public good.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 9951c482); written question by question; committed after each
      (Q1 2b4ac693, Q2 a32e6703, this section last).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock and the fold are the dispatching
      session's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Contamination declared:** the
      session's opening git status and log showed commit subjects for another company's run (CWST, OUT at Q2, folded);
      a memory index line in the session context named the queue's general state; a filtered listing of `Test Runs/` for
      "cdt" returned nothing. None of it bears on this name and none was used.
- [x] Every v5 id resolves (checked by `scripts/check_ids.py`); every filing fact has its accession; every number has a
      row, a filing or the arithmetic file.
- [x] The order was kept; Q2 closed the run; Q7 below it is headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy (operator rule 5);
      the sovereign from the treasury curve the Ministry of Finance publishes, dated; the price from an aggregator, flagged.
- [x] Contrary evidence written down as found (foundations, Q1); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used; its USD sovereign and its "earnings currency: USD" were not.
- [x] `python tools/check_framework.py` PASS before the final commit (2026-10-29); `scripts/check_ids.py`: 37 distinct ids,
      all in `principle_ledger_v5.csv`, no E-ids, every quoted fragment beside an id found in its row.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1's parts rule cannot see a business that has announced its own transformation.** A part "matters" when it carries
more than half of five-year operating profit; the hydrogen line has none, so the rule makes it irrelevant to understanding,
while the filing says the company's strategy is to become it. The run read the sewage part and carried the start-up to
Q6; the operator may want a line on a declared pivot. (2) **Q2's "ordinary returns" test does not say which return.** The
reported return on equity was above 20% in 2021 to 2023; the cash return was negative in every year. The run judged on
owner cash, reading **[L2007-004]** with **[M2003-122]**, but the text should say. (3) **The competitor row when the filing
names no rival.** The brief says what to record; the framework's section C still speaks of "the filer's and the rivals'
filings". With no rival, the field is one company, and the run said so. (4) **The sovereign for a currency outside the
table.** The protocol's table covers USD, JPY and EUR; for RMB the run used the China treasury curve that the Ministry of
Finance publishes, compiled by ChinaBond. Whether ChinaBond's service of that curve counts as the issuing authority should be
ruled, and a CNY row added. (5) **The fair price when owner cash is negative.** Part VII defines the fair price as the
midpoint earning the floor; on a negative stream it is a negative number, which the run reports as such ("not positive").
The text could say that a non-positive fair price is reported as computed and no alert is set from it. (6) **A filing that
states its own structure two ways** (VIE in the Introduction, direct holding in Item 4) has no home in the framework
beyond Q4's confusion test; the run recorded it under Q1 and AFTER THE STOP rather than letting it decide, since Q2 closed
first. (7) **The brief described the company as using a VIE "which it consolidates but does not own"**, taken from that one
sentence of the 20-F; the rest of the filing describes a direct holding. A brief that quotes a filing's self-description
can carry the filing's own inconsistency.
