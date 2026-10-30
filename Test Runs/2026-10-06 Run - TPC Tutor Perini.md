# Company Run: Tutor Perini Corporation (NYSE: TPC), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template to this dated name before any fetch** (2026-10-06).

**POSITION NOTE, declared before any verdict:** not checked. The dispatch's blind rule forbids opening `PORTFOLIO.md`, so
the analyst does not know whether the operator holds this name, and wrote the run as if a stranger to it.

**CONTAMINATION DECLARED.** Seen before or during the run, none of it about TPC: the session's git snapshot listed recent
commit subjects (v5 runs of ASO, BTU; tool fixes to `cover_shares.py` and `run.py`) and the names of three untracked
2026-10-06 run files (BCC, PATK, REYN), not opened; the operator's memory index line "57 gate-clearers, nothing buyable"
(a count about other names). No TPC run, research pass, holding review, queue entry, reading list or resume-state file was
opened. `tools/run.py` printed its v4 material (owner-earnings label, "yield", "growth the price assumes"); only its
arithmetic lines were used (Part VII).

Working folder: `Test Runs/_research 2026-10-06 TPC/` (`fetch.py` and `series.py` there are transcription helpers that
download filings and print filed XBRL values; they add no number).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $86.43 (close 2026-10-05; via `tools/run.py`, an aggregator quote, **flagged** per operator rule 5: live quote only).
- **Shares by class** from the latest filing's cover: one class, Common Stock $1.00 par, **52,569,117** shares (10-Q for
  the quarter ended 2026-06-30, filed 2026-08-05, accession `0000077543-26-000186`; `python Screens/cover_shares.py TPC`).
  No second class; preferred authorized 1,000,000, none issued (10-K FY2025 balance sheet).
- **Market cap:** 52.569M × $86.43 = **$4,543.5M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 10/05/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-26, accession `0000077543-26-000028` (Items 1, 1A, 7; balance sheet, income statement,
    cash flows, equity; Notes 1(p), 4, 8, 10, segment note).
  - 10-Q Q2 2026, filed 2026-08-05, accession `0000077543-26-000186`.
  - DEF 14A filed 2026-04-09, accession `0000077543-26-000088`.
  - Earlier 10-Ks for the span: FY2024 `0000077543-25-000025`, FY2022 `0000077543-23-000023`, FY2019
    `0000077543-20-000008`, FY2016 `0000077543-17-000009`, FY2014 `0000077543-15-000013`, FY2011
    `0001140361-12-012479`, FY2009 `0000077543-10-000008`.
  - **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025,
    `tools/run.py` 748.1M against the filed cash-flow statement $748,065 thousand (10-K FY2025, F-7): agrees. Total debt
    $407.4M (run.py sum of tagged lines 407) against the 10-K risk factor "our total debt was $407.4 million": agrees.
- `python tools/run.py TPC` arithmetic lines only (USD millions; saved in the working folder as `run_py_output.txt`):

  | FY | OCF | SBC | D&A | capex | OCF − SBC − capex |
  |---|---|---|---|---|---|
  | 2023 | 308.5 | 12.3 | 45.2 | 53.0 | 243.2 |
  | 2024 | 503.5 | 40.4 | 53.8 | 37.4 | 425.7 |
  | 2025 | 748.1 | 150.0 | 49.8 | 180.9 | 417.2 |

  The tool's five-year window gives 205.1 (capex basis) against 362.1 for three years, a divergence of −48%: the window
  decides the answer, so the whole cycle is read below (Q4) and neither window is used as given. SBC resolved: 2023–2024
  `AllocatedShareBasedCompensationExpense`, 2025 `ShareBasedCompensation`; both equal the filed cash-flow add-back
  (10-K FY2025, F-7: 150,002; 40,356; 12,259). Two corrections the tool does not make, found in the filing and carried to
  Q4: (i) the FY2025 SBC is mostly **cash-settled** liability awards, of which "$90.4 million in 2025, $4.0 million in
  2024 and $2.8 million in 2023" was paid in cash (Note 10), so OCF − SBC counts the paid part twice; (ii) OCF includes the
  cash of consolidated joint ventures, and "Distributions paid to noncontrolling interests" ($51.7M in 2025, financing)
  belong to the partners, not to TPC's owners.

## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own TPC if the market shut for five years, "Because then you’re buying a business" **[M1997-109]**? The stock rose 176.9% in 2025 (10-K FY2025, MD&A) and sits at $86.43 against book of $23.08 a share (1,218.6M equity / 52.79M shares, 10-K FY2025 balance sheet); the rise is no evidence, since the market "just tells us prices" **[M2006-077]**. No macro enters: the filer's growth case leans on the Bipartisan Infrastructure Law, ballot measures and lower interest rates (10-K FY2025, MD&A), and those are set aside, since in the speakers' practice such conclusions "just never enter into the discussion" **[M2000-094]**. Who is paid to tell you: the filer features "adjusted" earnings that exclude stock pay (10-K FY2025, Non-GAAP Financial Measures); recorded under Q4. The analyst's habits: looking for "what’s wrong in things" **[M2025-013]**, and stating the other side's case before disagreeing with it **[M2016-055]**.

**The other side's case, stated as strongly as I can** **[M2016-055]**: the legacy disputes from the 2010s are largely settled and collected (claims assets fell from $451.8M to $324.7M in 2025, Note 4); the old low-margin book has burned off; TPC is one of a handful of US firms that can bond and execute multi-billion tunnelling, transit and detention projects, and it now bids into a market the filer describes as having "diminished competition"; the first full year of the new book shows Civil margin 13.7%, record operating cash four years running ($748.1M in 2025), debt cut from $958M (2022) to $407M (2025) and the 11.875% notes refinanced at 6.625% (July 2026, 10-Q Q2 2026); the stock-pay spike falls away in 2027 (10-K FY2025, MD&A); backlog is a record $20.6B, 86% government.

**Contrary evidence, written down as found** **[M1997-127]** (in the order found):
1. *Against the business:* cumulative net income attributable to TPC, 2010 to 2025, is **−$159.6M** (sum of the filed annual figures: 10-K FY2014 selected data for 2010–2014; FY2019 selected data for 2015–2019; XBRL `NetIncomeLoss` first-filed vintage for 2020–2025). Book value per share was $27.88 at 2010 year-end (10-K FY2014, selected data) and $23.08 at 2025 year-end.
2. *Against the business:* FY2025 SBC of $150.0M is mostly cash-settled liability awards indexed to the stock, issued "as a short-term solution to deal with a depleted share pool [...] and a low stock price" (10-K FY2025, MD&A); $90.4M was paid in cash in 2025 (Note 10).
3. *Against the business:* only $270.7M of the $734.6M year-end cash is "immediately available for general corporate purposes"; the rest sits in joint ventures (10-K FY2025, Liquidity).
4. *For the business:* Civil segment cumulative operating margin 2013–2025 is 9.8% (segment tables, see Q2), a real and lasting figure.
5. *Against the business:* the same span gives Building 1.1% and Specialty Contractors −1.6%, and corporate costs and impairments take the consolidated figure to 1.8%.
6. *Against the business:* claims plus unapproved change orders were $726.8M at 2025 year-end and $763.4M at 2026-06-30 (321.1 + 442.3; 10-Q Q2 2026, contract assets note), unapproved change orders rising.
7. *For the business:* H1 2026 operating cash $334.1M and record quarterly operating income $117.7M (10-Q Q2 2026, MD&A).
8. *Against the business:* the filer's own words for the recent margins are "limited competition" and customers who "have at times had to make concerted efforts to attract bidders" (10-K FY2025, Items 1 and 7): a shortage of bidders, which the owners are working to end.

## THE STANDING RULE
The buyer's conduct only: a marketable stake bought with cash, unborrowed, gives no one a call on the buyer, and nothing here requires sudden sums of the buyer; so the rule is met by how the purchase would be financed and sized, not by anything in TPC, which is weighed at Q9 **[M2012-081]**, **[M2004-065]**.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "the first question is, can I understand it?" **[M1995-051]**, where understanding means "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**; the product need not be understood if "I understand the economic dynamics of the industry" **[M2011-014]**.
- **What the business is, from the filing.** A general contractor with three segments (Civil, Building, Specialty Contractors) that performed "approximately 1,600 construction projects" in 2025; backlog $20.56B at 2025 year-end, 79% fixed price, 13% guaranteed maximum price, 86% from government customers; Civil customers award "through one of two methods: the traditional public “competitive bid” method, in which price is the major determining factor, or through a best value proposal" (10-K FY2025, Item 1, accession `0000077543-26-000028`).
- **The key variables and how predictable they are** **[M1998-044]**: (1) the margin bid into new work, set by how many able bidders turn up; (2) execution against fixed-price estimates; (3) recovery of claims and unapproved change orders ($726.8M on the balance sheet at 2025 year-end, Note 4); (4) public funding. Variables 1, 2 and 4 belong to a slow-changing industry: tunnels, bridges, transit and jails are built and bought much as they were fifteen years ago, so the rapid-change routing does not apply **[M1999-063]**. Variable 3 is a run of negotiations and lawsuits whose outcomes cannot be forecast one by one from outside; but its aggregate behaviour is on the record (Q2 and the balance sheets below), and the rows place the accounting risk of "construction in progress or progress payment-type things" **[M2013-086]** under the numbers question (Q4), not under understanding.
- **Do the past statements tell me the future ones?** **[M2008-033]**: in kind, yes. Sixteen years of filings show the same pattern repeating: a large backlog, fixed-price work, recurring charges on completed projects, claims built up and later settled below the amounts carried. That is a foreseeable economics, and Q2 asks what it shows.
- **The doubt rule** **[M2002-092]**: "if you have doubts about something being into your circle of competence, it isn’t." The doubt I hold is about the size of particular disputes, not about where the industry's economics and TPC's position in it will stand. A reader who treats the claims as the whole of the economics would close here TOO HARD (WORK); the action would be the same (no purchase), and the alternative is recorded rather than hidden.
- **VERDICT: IN.** The ten-year economics of a fixed-price public-works contractor can be foreseen in kind, "where the business will be in 10 years" **[M2000-037]**; the uncertainty in the claims is carried to Q2 and Q4.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years from now." **[M1995-038]**.

**The castle tests, each with its filing fact.**
1. **The key factors and how permanent they are** **[M1995-038]**. The filer names its advantages: prequalification on "financial strength", a record on large complex projects, and "vertical integration capabilities" that let it "self-perform a greater amount of work than our competitors" (10-K FY2025, Item 1). None is exclusive: the same filing names six large civil rivals (FlatironDragados USA, Kiewit, Lane, OHL USA, Skanska USA, Walsh) and fourteen national building rivals, and TPC builds its largest projects in joint ventures with such firms (SR 99 with Dragados USA, a 45% TPC interest, Note 8).
2. **The money test** **[M2011-015]**: "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it? [...] If the answer had been yes, we wouldn’t have done it." Here no new money is needed: the attackers already exist, several are larger, and they bid on each job. The rows name "some industries that are just never going to have barriers to entry" **[M2012-106]**.
3. **Pricing power and the agony before a price rise** **[M2005-020]**. TPC's price is fixed at the bid for 79% of backlog; further price is pursued after the fact through claims, which the filing defines as arising "when there is a dispute regarding both a change in the scope of work and the price associated with that change" (Note 4). The firm's way of getting more price is the dispute: the opposite of a customer who accepts a rise.
4. **Would the customer still choose it over the low bid?** **[M2017-009]**: the See's test was that "it wouldn’t be a question of people buying candy for the low bid." The filing says the reverse of TPC's public customers: the competitive bid, "in which price is the major determining factor" (Item 1); Building names "competitive pricing" among the reasons it wins (Item 1). The rows' commodity mark: "most insureds don't care from whom they buy" **[L2004-003]**.
5. **The low-cost position** **[L2000-017]**: "being the low-cost producer is all-important." No evidence that TPC is the low-cost bidder: its whole-span operating margin equals Granite's and trails AECOM's and Sterling's (competitor row below), and Specialty Contractors, whose electrical and mechanical crews are the "vertical integration" claimed as an edge, lost money in 2019 and in every year 2021 to 2025. "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**.
6. **Widening or narrowing** **[M1999-108]**: "whether it’s likely to widen further or shrink on you." The segment margins (pre-impairment, from the segment tables of the 10-Ks listed in Step 0):

   | year | Civil | Building | Specialty | Consolidated |
   |---|---|---|---|---|
   | 2013 | 12.3% | 1.6% | 4.1% | 4.9% |
   | 2014 | 13.1% | 1.6% | 3.9% | 5.4% |
   | 2015 | 7.7% | −0.1% | 1.3% | 2.1% |
   | 2016 | 10.3% | 2.5% | 3.1% | 4.1% |
   | 2017 | 12.0% | 1.8% | 1.6% | 3.8% |
   | 2018 | 10.6% | 2.4% | 4.3% | 4.3% |
   | 2019 | 3.3% | 2.1% | −1.8% | 0.3% |
   | 2020 | 11.2% | 2.7% | 1.5% | 4.9% |
   | 2021 | 12.7% | 2.0% | −0.9% | 4.9% |
   | 2022 | 1.2% | 0.6% | −20.7% | −5.4% |
   | 2023 | 10.5% | −7.0% | −20.9% | −3.0% |
   | 2024 | 6.5% | −1.5% | −17.5% | −2.4% |
   | 2025 | 13.7% | 3.1% | −0.9% | 4.2% |
   | **2013–2025 cumulative** | **9.8%** | **1.1%** | **−1.6%** | **2.4% (1.8% after the 2019 impairment)** |

   Arithmetic in `Test Runs/_research 2026-10-06 TPC/tpc_span.py`. 2019 segment figures are the filer's "adjusted" (before the $379.9M goodwill impairment); consolidated 2013–2025 corporate and unallocated cost was −$989.9M. Over thirteen years the castle has not widened: two of three segments earned about nothing, and the consolidated margin in 2025 (4.2%) is below 2013 and 2014. The 2025 to 2026 rise is credited by the filer to "favorable market dynamics, including limited competition in select markets for some of the larger projects" (10-K FY2025, MD&A), while "customers have at times had to make concerted efforts to attract bidders" (Item 1). An advantage made by rivals' absence is the kind the rows warn about: "usually if something can gain competitive advantage very quickly, you have to worry about them losing it quickly, too." **[M2002-050]**.
7. **The moat that must be rebuilt** **[L2007-005]**: "A moat that must be continuously rebuilt will eventually be no moat at all." Each project is a new contest; Civil backlog converts "over a period of three to five years" and Building and Specialty "over a period of one to three years" (10-K FY2025, MD&A), so the whole book is re-won at a new bid price within about five years.
8. **Would it stand without the lord?** **[M1995-038]**: "How much do they depend on the genius of the lord in the castle?" The proxy credits Ronald Tutor as "the catalyst behind the Company’s evolution" (DEF 14A 2026, accession `0000077543-26-000088`), and he has stated through a Schedule 13D/A that he intends to sell some or all of his shares over the next 18 months (DEF 14A 2026, ownership note 6). The test is not decisive here; the business-level evidence above is.
9. **The rival who sets the price** **[M2012-109]**: "whatever he charged for gas was my price." In competitive public bidding, the next-lowest bidder caps TPC's price on every job; the filing's own phrase is that "price is the major determining factor".
10. **What could destroy or reduce it** **[M2000-014]**: one adverse decision on one completed project moves a year: SR 99, "a pre-tax charge of $166.8 million" in 2019 (Note 8); a $101.6 million adverse arbitration on a completed California bridge in 2024; a $54.7 million settlement on a Canadian tunnel in 2025 (10-K FY2025, MD&A, Civil). These came from projects completed years earlier, after the profit on them had been booked.

**The competitor row** (operating income ÷ revenue, cumulative over the span, each from the company's own 10-K XBRL, first-filed vintage; arithmetic in `Test Runs/_research 2026-10-06 TPC/peers.py`):

| company | span | cumulative operating margin | latest 10-K accession | note |
|---|---|---|---|---|
| TPC | 2013–2025 | 1.8% (2.4% before the 2019 impairment) | `0000077543-26-000028` | Civil 9.8%, Building 1.1%, Specialty −1.6% |
| Granite (GVA) | 2013–2025 | 1.9% | `0000861459-26-000004` | losses 2013, 2019, 2020; 2025 6.4% |
| Sterling (STRL) | 2013–2025 | 7.4% | `0000874238-26-000024` | losses 2013–2016; recent years dominated by site work for data centers, not heavy civil; not like for like |
| AECOM (ACM) | 2013–2025 (FY Sep) | 3.1% | `0000868857-25-000013` | mostly design and professional services, a lower-risk model |
| Fluor (FLR) | 2017–2025 (2013–2016 untagged) | 0.6% | `0001124198-26-000007` | losses 2019, 2021, 2025 |
| Skanska | not fetched | n/a | non-SEC (Nasdaq Stockholm) | **flagged:** not on EDGAR; not read |

Across the span the fixed-price builders (TPC, Granite, Fluor) sit between about 0.6% and 2% on revenue; the one peer with a high recent margin (Sterling) earned it in a different end market. TPC is not distinguished from the field on the evidence of its own record.

**The exception the rows allow, the low-cost operator**, is not shown (test 5). **Price does not reopen it:** "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

**Why OUT and not TOO HARD.** The castle's future is not unknowable: thirteen to sixteen years of segment results, the competitive-bid mechanism stated in the filer's own words, and the named rivals bidding the same work show it open. A castle shown on the evidence to be filling in closes OUT under the framework's routing (Q2, What it rules OUT), whose list includes the customer who buys on the low bid **[L2004-003]**, **[M2017-009]**, the business whose price a competitor sets **[M2012-109]**, and the moat continuously rebuilt where the rebuilding is seen failing **[L2007-005]** (Building and Specialty, 2019 to 2024). The recent margin rise is recorded as contrary evidence (items 4, 7 and 8 above) and weighed: it rests on a shortage of bidders, which the rows treat as quickly lost **[M2002-050]**.

- **VERDICT: OUT.** The run closes here. Everything below is NOT REACHED, recorded only where the dispatch or the template asks for it, and none of it is a clearance.

---
## THE BALANCE SHEETS, EIGHT TO TEN YEARS (read in Step 0 because the run closes before Q4; not a verdict)
Read "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**. From `tools/run.py` (first-filed XBRL), checked against the filed FY2025 balance sheet, and from the FY2014 and FY2019 selected data (USD millions):

| year-end | equity | goodwill | retained earnings | total debt | cash (of which corporate) | contract assets | contract liabilities |
|---|---|---|---|---|---|---|---|
| 2010 | 1,313 | 622 | n/a | 396 | n/a | 139 | 200 |
| 2014 | 1,366 | 585 | n/a | 865 | n/a | 726 | 319 |
| 2017 | 1,713 | 585 | 622 | 736 | 193 | 933 | 457 |
| 2019 | 1,440 | 205 | 314 | 834 | 194 | 1,124 | 844 |
| 2021 | 1,655 | 205 | 514 | 994 | 202 | 1,357 | 762 |
| 2022 | 1,450 | 205 | 304 | 958 | 259 | 1,378 | 976 |
| 2023 | 1,292 | 205 | 133 | 900 | 381 | 1,144 | 1,104 |
| 2024 | 1,135 | 205 | −31 | 534 | 455 (266) | 943 | 1,217 |
| 2025 | 1,219 | 205 | 46 | 407 | 735 (271) | 819 | 1,839 |

What moved and why. (1) **Equity**: $1,713M (2017) to $1,219M (2025), retained earnings $622M to $46M; book value per share fell over fifteen years. (2) **Goodwill**: $376.6M of goodwill and intangibles written off in 2012 and $379.9M of goodwill in 2019, together more than the $341.9M paid for businesses in 2011 (XBRL `PaymentsToAcquireBusinessesNetOfCashAcquired`); the capital paid for the 2008 merger and the 2011 acquisitions was largely lost. (3) **The contract asset** (costs and estimated earnings in excess of billings, mostly claims and unapproved change orders) grew from $139M (2010) to $1,378M (2022) while profits were being reported, then fell to $819M by 2025 through collections and through charges: net losses attributable of $210.0M, $171.2M and $163.7M in 2022, 2023 and 2024. The profit had been booked years before the cash, and part of it never came. (4) **The contract liability** (billings in excess of costs: customers' money received ahead of the work) rose from $762M (2021) to $1,839M (2025) and $1,930M (2026-06-30); this is what made operating cash a "record" four years running, and it is the customers' money for work still to be done, not earnings. (5) **Debt** fell from $958M (2022) to $407M (2025), paid out of those working-capital releases. (6) **Cash**: only $270.7M of $734.6M is available for general corporate purposes. What the figures "can’t say" **[M2025-032]**: what the $763.4M of claims and unapproved change orders at 2026-06-30 will finally collect. A business that reports profit and holds it as receivables and claims is the one where "there’s your profit sitting in the yard" **[M2008-036]**.

## Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED.
Recorded, not weighed: capex rose to $180.9M in 2025, "mostly related to owner-funded equipment on newer projects" (10-K FY2025, MD&A), against depreciation of $47.6M.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED.
Recorded, not weighed (a later run would test these against the two-tell line): the filer reconciles to "Adjusted diluted earnings per common share" excluding share-based compensation ($4.29 against GAAP $1.51 in FY2025), the pattern of "a management that regularly attempts to wave away very real costs by highlighting" adjusted earnings **[L2016-006]**; and it describes 2025 charges of $78.7M as "temporary aggregate negative project adjustments" whose "temporary impacts to earnings of which are expected to reverse themselves over the remaining lives of the projects" (10-K FY2025, MD&A). Charges on completed or legacy projects were recorded in 2015, 2018, 2019, 2022, 2023, 2024 and 2025 (FY2019 selected-data notes; FY2022, FY2024 and FY2025 MD&A).

## Q5: WHO RUNS IT. NOT REACHED.
Recorded, not weighed: Ronald N. Tutor, Executive Chairman, 12.6% (DEF 14A 2026); his 2025 pay $14,163,948, including $2,016,322 for personal use of company aircraft and a $1.5 million transition bonus paid when his successor took office; CEO Gary Smalley's 2025 total $10,041,405; Tutor's nominee on the board is his father-in-law; TPC leases facilities from an entity Tutor controls ($1.7M paid in 2025).

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
Recorded, not weighed: the retention record (book value per share $27.88 in 2010 to $23.08 in 2025, with a dividend of $1.00 a share in 2010 and $0.06 in 2025); a $200M buyback with no stated price, under which $30M was bought in H1 2026 at an average $72.28 (10-Q Q2 2026). Q6's convention reads such purchases against the bottom of the Q7 range, and $72.28 is above the bottom of every range in the computation below.

## Q7, Q8, Q9, Q10, Q12: NOT REACHED.
Q9 facts recorded, not weighed: $400M 6.625% senior notes due 2033 issued 2026-07-02; revolver raised to $350M effective 2026-07-02 (10-Q Q2 2026); fixed-price backlog 79%; joint-venture cash not available to the parent.

---
## COMPUTATION, NOT A CLEARANCE (operator rule 3; the file closed OUT at Q2)
Reported at the owner's request; no entry language; the file is closed whatever these figures say.

**Owner cash after every real cost, by year** (USD millions; `tpc_span.py`): operating cash, less capital spending, less the year's stock-pay expense, plus the part of that pay settled in cash (already inside operating cash; Note 10: $2.8M 2023, $4.0M 2024, $90.4M 2025), less distributions to noncontrolling (joint-venture) partners, who own that cash (filed financing line, 2017 onward; earlier years untagged, so the early years are slightly overstated). The depreciation variant replaces capital spending with depreciation.

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| owner cash | 84.2 | 94.6 | −107.5 | −13.3 | 57.7 | −221.4 | 90.7 | 199.5 | 406.4 | 456.0 |

2010 to 2015: −11.7, −106.0, −118.8, 1.7, −150.3, −31.3. Cumulative 2010–2025: **$630.5M** in sixteen years (2011 acquisitions of $341.9M not deducted).

**The five-year window holds abnormal years.** 2021 is −$221.4M; 2023 to 2025 are lifted by customers' advances (contract liabilities +$1,077M, 2021 to 2025) and claim collections (contract assets −$538M), which the rows' warning on base years covers: "a base year in which earnings were poor can produce a breathtaking, but meaningless, growth rate" **[L2005-003]**. So a whole-cycle variant is given beside the convention, and the whole cycle is the central case. Cross-check on the whole cycle: cumulative net income attributable 2010–2025 (−$159.6M) plus the two impairments ($376.6M + $379.9M) gives $596.9M, or $37.3M a year, against owner cash of $39.4M a year.

**Growth shown.** Aggregate owner cash shows no measurable growth rate (negative base years). The only steady series is revenue, $4,175.7M (2013) to $5,543.0M (2025), **2.39% a year**, used as the shown-growth end (CONVENTION of this run, below).

**VALUE RANGE** (Q7 convention: ten years at the growth shown, then no nominal growth, at the 5.66% sovereign; ends = no growth and shown growth; 52.569M shares; `value.py`):

| case | owner cash | no growth | shown growth (2.39%) |
|---|---|---|---|
| Convention, five-year mean 2021–2025, capex basis | $186.2M | $3,290M = **$62.58** | $3,975M = **$75.61** |
| five-year, depreciation variant | $205.2M | $68.97 | $83.32 |
| **Whole cycle 2010–2025, capex basis (central)** | $39.4M | $696M = **$13.24** | $841M = **$16.00** |
| whole cycle, depreciation variant | $48.1M | $16.17 | $19.53 |

Against the price of **$86.43**. Read under the convention as if Q7 had been reached: the convention's own range ($62.58 to $75.61) sits wholly below the price, which would close OUT through the floor; the full span across windows ($13.24 to $83.32) is 6.3 to 1, wider than about three to one, which would close TOO HARD: "the range must be so wide that no useful conclusion can be reached" **[L2000-025]**. Either way, not IN. Not added: corporate cash of $270.7M (a contractor's bonding and working-capital need); not subtracted: the $400M of notes (owner cash is already after interest).

**FAIR PRICE** (the price at or below which the central case clears the floor). The floor is the convention's about ten percent pre-tax, the speakers' "a very high probability of at least 10% pre-tax returns" **[L2002-020]**, below which "there’s just a point at which we drop out of the game" **[M2003-149]**. Tax treatment: owner cash is after tax, so it is grossed up at the filed FY2025 effective rate of 30.0% (CONVENTION of this run). The floor is applied **on equity** (market capitalization), since owner cash is already after interest. Expected return = pre-tax owner-cash yield + growth.
- **Central case (whole cycle, no growth):** $39.4M / 0.70 = $56.3M pre-tax; at 10%: $563M = **$10.71 a share**. With the 2.39% shown growth: $14.07.
- Five-year window, for comparison: $50.60 (no growth), $66.48 (shown growth).
- At $86.43 the after-tax owner-cash yield is 0.87% on the whole cycle and 4.10% on the five-year window.

**CHEAP PRICE** (below which no pencil is needed). Rule, a CONVENTION of this run: half the central fair price, because the margin is taken as "a big discount from that present value" **[M1997-126]** and is "the larger" the more volatile the business **[M1997-080]**; at half, even the whole-cycle owner cash would yield about 20% pre-tax, which needs no pencil. **Cheap: about $5.35** (whole cycle, no growth; $7.03 with growth); on the five-year window it would be $25.30. The price of $86.43 is about eight times the central fair price.

---
## THE BOX
**OUT, at Q2.** The castle is open on the evidence: public customers award on price, named rivals bid the same work, the firm's extra price comes through disputes, and over 2013–2025 the consolidated operating margin was 1.8% (2.4% before impairment), level with Granite, while Building and Specialty earned about nothing; the recent rise rests on a shortage of bidders. COMPUTATION only: whole-cycle value $13.24 to $16.00 a share (five-year convention window $62.58 to $75.61) against $86.43; fair about $10.71, cheap about $5.35. No research pass (the box is OUT, not TOO HARD (WORK)).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. **Not committed after each:** the dispatch forbade commits, so write-early was kept by writing each section to the file as it closed.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every filing fact carries its document and accession (peers by latest 10-K accession; Skanska flagged as not read); no number without a row or a filing, and the run's own inventions are confessed below.
- [x] The order was kept; Q2 failed and closed the run; Q3 to Q12 are marked NOT REACHED and the value arithmetic is headed COMPUTATION, NOT A CLEARANCE, with no entry language.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): operating cash less capex, stock pay and partner distributions; net income appears only as a cross-check. Sovereign from the US Treasury (issuing authority), dated. Price an aggregator quote, flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (Foundations, eight items, both directions).
- [x] No row dated after the anchor: not a point-in-time run (the anchor is today), so the bar does not bite.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 labels, yield and "growth the price assumes" lines were not used.
- [x] `python tools/check_framework.py` run after writing: **PASS** (2026-10-06; ledger 4,279 rows; Test Runs phantom ids in 0 files). The run's own check (`check_ids.py` in the working folder): no E-ids; all 40 distinct M/L/R ids found; every quoted fragment beside an id found in that row; every filing quote found in the filing text.
- **CONVENTIONS of this run, confessed (PRIME RULE 3):** (a) stock pay paid in cash added back so it is not counted twice; (b) distributions to noncontrolling partners deducted from owner cash; (c) revenue growth 2013–2025 used as "growth shown" because aggregate owner cash has negative base years; (d) the whole cycle 2010–2025 taken as the central case; (e) the after-tax owner cash grossed up at the FY2025 effective tax rate to meet a pre-tax floor; (f) cheap price = half the central fair price. Rationale for each is given where it is used; none licenses conduct a rule forbids.
- **Blind rule kept:** `PORTFOLIO.md`, holding reviews, resume-state files, the run queue, the prepped reading list, other TPC run files, other companies' 2026-10-05 and 2026-10-06 run and research files, and the unadopted small-cap gaps case were not opened. Contamination declared at the top.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Operator rule 3 against the dispatch.** The rule requires the heading "COMPUTATION" joined to "NOT A CLEARANCE" by an em dash; the dispatch and the operator's standing rule forbid em dashes. The heading was written "COMPUTATION, NOT A CLEARANCE"; the words are kept, and the rule should say whether the dash is part of it. (2) **Q7's range convention fails for a contractor.** The five-year mean of owner cash is dominated, for a fixed-price builder, by contract-balance swings: in 2021–2025 TPC's customers' advances rose by about $1.08B and its claims assets fell by about $0.54B, so the convention figure ($186M) is nearly five times the sixteen-year figure ($39M). The convention has no rule for working capital that must reverse (customers' money is spent on the work it paid for), and its "growth shown on the aggregate owner cash" is undefined when a base year is negative (2021: −$221M). I used the whole cycle and revenue growth, confessed above; the framework should say which to use. (3) **`tools/run.py` and the convention double-count cash-settled stock pay** (operating cash already contains the $90.4M paid in 2025, and OCF − SBC deducts it again), and neither deducts distributions to joint-venture partners although consolidated operating cash includes the joint ventures' cash; Part VII says nothing on either. (4) **The pre-tax floor is set against an after-tax cash figure** with no stated conversion; I grossed up at the effective rate, which may misstate a company with loss carryforwards (TPC's MD&A cites them). (5) **The template's POSITION NOTE says "check `PORTFOLIO.md`"** while the dispatch's blind rule forbids opening it; I followed the dispatch and declared the position unknown. (6) **Q1 and Q4 overlap on claims accounting**: M2013-086 names construction in progress as prone to games, but no routing says whether a business whose economics turn on unresolvable claims fails understanding (Q1) or the numbers (Q4); I passed Q1 and recorded the alternative close.
