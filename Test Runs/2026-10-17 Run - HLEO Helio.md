# Company Run — Helio Corporation (OTC: HLEO) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind run under
the canonical brief `Screens/_daily/_dispatch_brief.md` with its slots filled; the brief's one stated departure (the lines of
evidence and the competitors derived by the analyst from the filing, not hand-written by the dispatcher) is followed below.
Every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD
closes the run and later questions are marked NOT REACHED.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session on 2026-10-17, after the run was committed (cf661bd5): not held; `PORTFOLIO.md` has no line for HLEO, Helio, Heliospace, Web3 or Stirling.*

**CONTAMINATION, declared as found (not used):**
- Before reading the blind rule's full reach I ran one filename filter of the `Test Runs/` directory listing for "hleo", "helio",
  "web3" and "stirling". It printed no file. That is a listing the brief forbids; it is declared here. What it showed is only
  that no file under those four names was listed; nothing of any other run was read.
- The session's opening context showed the repository's git status and the last five commit subjects (folds of CHYCY and BLGO,
  a CHYCY Q2 OUT, research-folder file names for AYI and ARCB), and a memory index line about the queue state ("57 gate-clearers,
  nothing buyable", holding reviews owed). None concerns this company; none was used.
- No other run file, holding review, `PORTFOLIO.md`, register, reading list or session-state file was opened.

**The lines of evidence chosen from the filing (the brief's departure), and why.** The 10-K for FY2025 (accession
0001213900-26-016950) gives no Item 1A: "As a "Smaller Reporting Company," the Company is not required to provide the information
required by this Item." Its risks are therefore read from the summary list in Item 7 and from the S-1 of 2024 that the 10-K
incorporates by name (accession 0001213900-24-113092). The lines chosen: (1) **the customer and its budget**: about 70% of FY2025
revenue from U.S. government sources, three customers over 67%, one NASA IDIQ prime 31% (Item 1), and the MD&A's "Government Budget
Uncertainty and Proposed NASA Cuts"; chosen because it is the variable the filer itself says decides volume. (2) **the contract
form**: "Time and Materials, Cost-Plus, or Fixed Price contracts", "fee amounts limited by government or agency policies", parts
"sent out for competitive bid to third-party fabricators" (Item 1); chosen because it sets what the business can earn on a dollar
of work. (3) **the growth strategy**: Space Based Solar Power, "an initial in-space SBSP system by 2030" (Item 1); chosen because it
is where the filer says the money will go. (4) **liquidity and debt**: cash of $7,305 at year end, notes in default, going-concern
doubt (Item 7 and the audit report); chosen because it decides whether the business reaches year ten in its present form.
(5) **the people and the issuance**: the January 2026 change of chief executive, the share grants and the stream of convertible
notes (Items 5, 10, 11 and the 8-Ks); chosen because it bears on Q5 and Q6.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $4.55 (close 2026-10-16; Yahoo Finance chart API, an AGGREGATOR, flagged per operator rule 5; OTC "OID" tier,
  thin: 6,733 shares traded that day, closes between $3.09 and $4.87 over the prior fifteen sessions). The 10-K itself warns the
  quote "may not reflect an actual or perceived value".
- **Shares by class** from the latest filing's cover: **5,190,024** common, no par, "As of September 14, 2026" (10-Q for the
  quarter to 2026-07-31, filed 2026-09-14, accession 0001683168-26-007107; `python Screens/cover_shares.py HLEO` returns the same
  figure from the same accession). Checked against issued less treasury: the balance sheet shows 5,190,024 issued and outstanding
  and no treasury line (the 9,231 shares bought back in the quarter are deducted from the count). Checked across the one-for-five
  reverse split (effective 2026-07-20 per the 8-K of 2026-07-24, accession 0001683168-26-005762; the 10-Q dates it July 22): the
  10-K's 11,371,966 shares at 2025-10-31 restate to 2,274,393, and the 10-K cover's 23,182,425 at 2026-02-17 restate to 4,636,485,
  the 10-Q's count at 2026-01-31. No 8-K was filed after the 10-Q (EDGAR list to 2026-10-17: two Forms 3 and 4 on 2026-09-21 and
  an S-8 on 2026-08-05). **Other classes outstanding at 2026-07-31:** Series A, B and C convertible preferred (575,000, 355,000 and
  200,000 shares, carried as mezzanine equity of $333,096 with accruing dividends) and Series D convertible preferred (250,000
  shares, issued for $100,000 of notes). Their conversion terms were not read; the count above is the common alone, said so.
- **Market cap:** 5,190,024 × $4.55 = **$23.6M** (common only).
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-16
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025 (filed 2026-02-17, accession 0001213900-26-016950), Items 1, 1A, 2, 5, 7,
  8 (statements and Note 1), 10 and 11; 10-Q for the quarter to 2026-07-31 (accession 0001683168-26-007107), statements, subsequent
  events, MD&A revenue paragraph and buyback note; S-1 of 2024-12-27 (accession 0001213900-24-113092), the audited statements for
  FY2022 to FY2024 and the business and risk text; 8-K of 2026-02-26 under Item 4.01 (accession 0001213900-26-020758); the EDGAR
  filing list. The information statement DEF 14C of 2026-05-29 (accession 0001683168-26-004388) was fetched and not read (the file
  closed before Q6). **No 10-K or audited statement exists for any year before FY2022**: the S-1 carries FY2022 to FY2024, and the
  only earlier figure is Heliospace's equity at 2021-10-31 in the S-1's statement of changes.
- **One figure cross-checked against the filed statement:** FY2024 revenue $6,891,223 appears identically in the S-1's audited
  statement of operations and in the FY2025 10-K's audited comparative column; FY2025 revenue $3,875,793 appears identically in
  the 10-K's statement of operations and its MD&A table.
- `python tools/run.py HLEO` printed only "HLEO: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." (saved to the research
  folder). Nothing from it is used; every figure below is transcribed from the filed statements, and the arithmetic is in
  `Test Runs/_research 2026-10-17 HLEO/computation.py`.

**Owner cash after every real cost by year** (operating cash flow, less capital spending, less stock pay and stock issued for
services, which operating cash flow adds back; working capital and lease cash are inside operating cash flow):

| Fiscal year to Oct 31 | Revenue | Operating income | Op. cash flow | Capex | Stock pay + stock for services | **Owner cash** | Accession |
|---|---|---|---|---|---|---|---|
| FY2022 | 8,363,600 | (36,283) | (107,162) | (29,354) | 13,074 | **(149,590)** | 0001213900-24-113092 |
| FY2023 | 9,209,329 | 60,881 | (117,892) | (73,571) | 5,553 | **(197,016)** | 0001213900-24-113092 |
| FY2024 | 6,891,223 | (1,745,155) | (1,560,375) | 0 | 196,437 | **(1,756,812)** | 0001213900-26-016950 |
| FY2025 | 3,875,793 | (3,698,754) | (2,065,017) | 0 | 556,005 | **(2,621,022)** | 0001213900-26-016950 |
| 9 months to 2026-07-31 | 1,543,492 | (4,077,561) | (1,937,196) | 0 | 2,563,077 | (4,500,273) | 0001683168-26-007107 |

Four-year average (FY2022 to FY2025, the years filed): **$(1,181,110)** a year. Trailing twelve months to 2026-07-31:
$(5,444,939). Depreciation $18,262 to $22,663 a year; the business owns $47,729 of equipment and leases its one facility at $38,192
a month. FY2025's operating cash flow was flattered by a $900,776 fall in receivables and a $343,218 fall in work in progress.

**The balance sheets, every one the filings carry** (the template asks for eight to ten years, read here in Step 0 since the file
closes before Q4; the filings carry five year-ends and one quarter):

| Date | Cash | Receivables | Total assets | Notes and convertibles payable | Derivative liability | Total liabilities | Equity (retained earnings) |
|---|---|---|---|---|---|---|---|
| 2021-10-31 | 647,879 | n/s | n/s | n/s | – | n/s | 955,578 (RE 940,949) |
| 2022-10-31 | 628,771 | n/s | n/s | n/s | – | n/s | 922,622 (RE 894,919) |
| 2023-10-31 | 504,335 | 1,748,179 | 3,797,347 | 427,103 | – | 2,843,444 | 953,903 (RE 920,647) |
| 2024-10-31 | 551,552 | 1,390,202 | 3,408,393 | 1,952,877 | – | 4,010,568 | (602,175) (RE (942,036)) |
| 2025-10-31 | 7,305 | 489,426 | 1,306,616 | 3,421,445 | 39,543 | 5,366,754 | (4,060,138) (RE (4,972,507)) |
| 2026-07-31 | 520,504 | 507,417 | 1,460,186 | 953,430 | 1,655,559 | 3,884,363 | (2,757,273) common deficit; (2,424,177) with mezzanine |

(n/s: not stated in any filing read. Sources: S-1 0001213900-24-113092 for 2021 to 2024; 10-K 0001213900-26-016950 for 2025;
10-Q 0001683168-26-007107 for 2026.) What the figures say: from 2018 to 2023 Heliospace kept its equity near $0.9M to $1.0M and
earned about breakeven on $8M to $9M of revenue, with no goodwill, no intangibles and almost no plant: the asset is the people.
From FY2024, the first year as a public company, equity went from $0.95M to a deficit of $4.1M in two years; receivables fell with
revenue; borrowings rose from $0.4M to $3.4M, much of it from officers and directors; cash reached $7,305. In the nine months to
July 2026 the debt was cut to $0.95M mainly by converting it into shares (the share count rose from 2,274,393 to 5,190,024 and four
preferred series appeared) while the accumulated deficit grew by a further $6.9M, $2.48M of it stock issued for services. What they
cannot say: what the business earns at a normal NASA volume, since the only near-breakeven years were also the only private ones.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the first: "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**. A business with $520,504 of cash, a going-concern doubt in its auditor's report, and losses funded by notes
convertible at a discount to the lowest recent close cannot be owned through a closed market; its owner's outcome depends on the
next financing, not on the business. The second is who is paid to tell you: the 10-K features a projection for the planned
solar-power business, "Expansion of this system to 100 GW capability yields $811B lifetime profit and an IRR at 11% annually", for
a company of about twelve employees with $3.9M of revenue; the rows do not consult projections, "we've never looked at a
projection in connection with either a security we've bought or a business we've bought" **[M1995-050]**, and ask for the
projector's record, which here is a revenue fall of 58% from FY2023 to FY2025. **Contrary evidence, written down as found**
**[M1997-127]**: (a) Heliospace's hardware works in space: the Europa Clipper antennas are "now fully deployed and operating", the
lunar sensors deployed on Blue Ghost in March 2025 (Item 1), and the filer reports a JPL subcontractor-of-the-year award; (b) it
was cumulatively profitable as a private company from 2018 to 2023 (retained earnings $920,647 at 2023-10-31); (c) Congress
restored NASA science funding "to near 2024 levels" after the proposed cut (MD&A); (d) the 9-month FY2026 gross margin rose to 41%
from 21%. Each is weighed below.

## THE STANDING RULE
Does owning this put the buyer at risk of ruin? Not through the business: a part-interest bought for cash with no borrowing loses
at most what is paid, and the rule binds the buyer's conduct, "never going to risk what we have and need for what we don't have
and don't need" **[M2012-081]**. The rule would be broken only by buying on borrowed money or at a size whose loss the buyer could
not bear; neither is proposed. Not engaged.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable probability of being able to asses where the business will be in 10 years"
**[M2000-037]**, "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years"
**[M2012-065]**. Not the product: what Heliospace makes is plain (deployable antennas, booms, sensors, release mechanisms, and
engineering hours for NASA missions); the question is whether its earning power in ten years can be seen.

**The key variables** **[M1998-044]** ("trying to identify the key variables in that particular business, and evaluating how
predictable they were first"), from the filing:
1. **NASA science spending, through a few primes.** About 70% of FY2025 revenue came, directly or indirectly, from U.S. government
   sources; three customers were over 67% in each year; one NASA IDIQ prime alone was 31% (10-K Item 1). The MD&A states that the
   administration's FY2026 proposal "recommends a significant reduction in overall discretionary spending, including an
   approximately 50% cut to NASA's Science Mission Directorate", and that even after Congress restored funding, "the
   administration's stated intent to reprioritize government resources away from space science programs present a material
   uncertainty for our future growth" (10-K MD&A). Revenue fell from $9.21M (FY2023) to $3.88M (FY2025) and by a further 54% in the
   nine months to July 2026, which the 10-Q attributes to "continuing budget cuts to NASA programs enacted by the current
   administration, combined with the extended government shutdown"; customers served fell from thirteen (FY2024) to six (nine
   months FY2026). The variable that sets the volume is a federal budget decided by politics. Predictable? No: the filer's own
   word is "material uncertainty", and the swing in two years was more than half the business.
2. **What a dollar of work earns.** Contracts are T&M, cost-plus or fixed price, with "fee amounts limited by government or agency
   policies", and "the limited fee structure allowed may limit profit under these contracts" (Item 1). This variable is
   predictable, and low: the best year filed earned an operating margin of 0.7% (FY2023).
3. **What the company will be.** The filer's growth strategy is not the present business but "Space Based Solar Power (SBSP)", with
   a plan to "demonstrate an initial in-space SBSP system by 2030, followed by larger capacity in the following decade" (Item 1).
   That is a new venture with no revenue and no demonstrated economics; the rows put it outside at once: "Start-ups are not our
   game." **[L2007-015]**; "We don't do startups." **[M2008-088]**. And the present business is described by the filer as
   operating "in a very competitive and rapidly changing environment" (Item 1, Our Challenges), in a market whose "rapidly growing
   space economy will present a host of new applications and revenue opportunities that many current hardware and services
   providers are ill equipped to address" (Item 1, Market Overview).
4. **Whether it exists in its present form.** Going-concern doubt in the audit report (Astra, 2026-02-17) and in the 10-Q; secured
   notes of $900,000 and $250,000 unpaid at their November 2025 maturity with default notices received (10-K Subsequent Events).
   This variable belongs to Q9 and the balance sheet, and it is recorded, not used, to decide Q1.

**The tests applied.**
- *Do the past statements tell me the future ones?* "do I understand enough about this business so that the financial statements
  will tell me the information that's useful to me in making a judgment about what the future financial statements are going to
  look like" **[M2008-033]**. No: the four filed years run from breakeven at $9.2M of revenue to a loss of $3.7M at $3.9M, the only
  near-breakeven years predate the public company, and the filer points the future to a business (SBSP) that has no statements.
- *Is it important and knowable?* The NASA science budget for a decade is important and not knowable from any filing: "If
  something's important but unknowable, forget it." **[M2006-076]**.
- *Would the insiders write it down?* The industry's insiders, as the filer reports them, could not say whether the science budget
  would be cut by half or restored; it was first proposed for the cut and then restored within one year. The rows' test is whether
  they "would not want to put down on paper their predictions about where 10 companies you would choose in the tech field would be
  in 10 years, in terms of their economics" **[M2000-105]**: for a twelve-person subcontractor whose largest customer is one prime on
  one NASA IDIQ, and whose stated future is space-based power, no one could write that line.
- *Can I name the winner, not just the industry?* The filer cites forecasts of the space market growing to "over $1 trillion by
  2040"; the rows answer that growth in an industry does not tell "what its profit margins and returns on capital will be as a
  host of competitors battle for supremacy" **[L2009-005]**.
- *Technology that could hurt the business:* "if something comes in where there's a technological component that's of
  significance, or where we think the future technology could hurt the business as it presently exists [...] it won't make it
  through the filter" **[M1998-008]**. The filer's own risk list includes that competitors "may develop technologies and products
  that are more effective than those we develop or that render our technology and products obsolete or noncompetitive" (10-K MD&A
  summary of risks).
- *Do I doubt it is inside?* I do: "if you have doubts about something being into your circle of competence, it isn't."
  **[M2002-092]**.

**The strongest case for IN, stated before it is answered** (the habit of hunting the other side): the present business is
simple to describe (engineering hours and custom builds, paid monthly), its hardware has flown, and it was near breakeven for
years. That makes the *product* understood, which the rows say is not the test: "We understand the product. [...] We just don't
know the economics of it 10 years from now" is the very case Q1 sends to the box (**[M2000-104]**, quoted in the framework's Q1).
The ten-year earning power turns on the budget variable and on a pivot to a start-up venture, neither of which the filings
can show.

**Which cause.** NATURE, not WORK: the deciding variable (a decade of NASA science appropriations and what a pivot to space-based
solar power will earn) is not knowable from any filing not yet read; "We couldn't solve this problem, moreover, even if we were to
spend years intensely studying those industries." **[L1993-023]**; "we're not going to learn enough in the followings five months to
make up for the fact that we went in deficient in the first place" **[M2008-086]**. A lower price does not reopen it: "It doesn't
mean it isn't a good buy. It doesn't mean it isn't selling for a fraction of its worth. It just means that we don't know how to
evaluate it." **[M2000-038]**.

**VERDICT: TOO HARD (NATURE)**, "in, out, and too hard" **[M2006-013]**. The file closes here. Deciding facts: revenue $9.21M
(FY2023) to $3.88M (FY2025) to $1.54M (nine months to 2026-07-31) on NASA science budget cuts the filer cannot forecast
(10-K 0001213900-26-016950, MD&A; 10-Q 0001683168-26-007107, MD&A); the stated growth strategy is an undemonstrated space-based
solar power venture with a first demonstration planned for 2030 (10-K, Item 1).

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED (file closed at Q1).
## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED (the balance sheets were read in Step 0).
## Q5 — WHO RUNS IT? NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7 — WHAT IS IT WORTH? NOT REACHED (see the COMPUTATION, NOT A CLEARANCE, below).
## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED.
## Q10 — IS IT THE FAT PITCH? NOT REACHED.
## Q12 — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## COMPUTATION, NOT A CLEARANCE: Q7's range and the fair price (reporting figures at the owner's request; operator rule 3)
*Computed after the Q1 STOP. No entry language; nothing here changes the box. Arithmetic in
`Test Runs/_research 2026-10-17 HLEO/computation.py` and its output file.*

- **The cash input.** Owner cash after every real cost, averaged over the years filed: FY2022 to FY2025, **four** years, not five,
  because no statement for FY2021 or earlier was ever filed (CONVENTION of this run: the window is the years the filings carry,
  said so; rationale: the alternative would invent a year). Average **$(1,181,110)** a year after interest (equity-only basis);
  **$(1,118,601)** before cash interest (all-equity basis; cash interest paid is stated for FY2024 and FY2025 only, so the FY2022
  and FY2023 add-back is taken as nil, which understates it by at most the $35,153 of FY2023 interest expense).
- **(a) Cycles.** The filer ties FY2025 to NASA cuts, the government shutdown and a loss on one fixed-price contract, which makes
  it a candidate aberrational end year. A cycle base needs a full cycle of owner cash, trough to trough or peak to peak; the four
  filed years hold none (one plateau near breakeven, then a fall). The literal window is the one used; even the best filed year,
  FY2022, is negative at $(149,590).
- **(b) Decline.** Owner cash is negative in every year and the losses grow (first-half average $(173,303), second-half
  $(2,188,917)). A compound rate between negative end years is meaningless, and so is the halves' ratio; by the text, **the range
  is the no-growth case alone**, said so.
- **(c) Acquisitions.** None: the January 2024 share exchange was a recapitalization with no cash paid for a business (10-K Note 1).
  No signed, unclosed deal is disclosed.
- **(d) Working capital.** Inside operating cash flow. FY2025 was flattered by a $1,243,994 release from receivables and work in
  progress; without it FY2025 owner cash would be $(3,865,016). Not substituted; shown beside.
- **(e) Growth spending.** Capital spending was $0 to $73,571 a year; the filing does not separate any growth spending (the SBSP and
  R&D work sits inside general and administrative expense, unquantified). No maintenance-only case can be separated; the
  all-spending case is the only case.
- **(f) The cap.** No growth is carried, so nothing is capped.
- **Tax.** No tax paid in any year (loss carryforwards of about $3,179,000, Section 382 unanalysed, 10-K MD&A). No case has taxable
  income, so the shelter is not priced.
- **Net debt** at 2026-07-31 with the subsequent event the 10-Q states (a $165,000 note of 2026-09-01, net proceeds $126,950):
  borrowings $953,430 + $165,000 less cash $520,504 + $126,950 = **$470,976**. Left out and said so: the derivative liability of
  $1,655,559 (conversion features that settle in shares), the four preferred series (mezzanine $333,096 plus Series D), and
  operating leases ($387,215).

**Value range:** the no-growth case alone, at the 30-year Treasury of 5.43%: business value $(20.6)M, less net debt, **$(4.06) a
share** (all-equity, central); **$(4.19) a share** equity-only. Against **$4.55**. Beside it: the literal best filed year carried
flat (FY2022) would give $(0.62); the trailing twelve months, $(19.41).

**The floor, tested first.** No case in the range earns the floor of about ten percent at the price, or at any positive price,
because owner cash is negative in every case the filings allow; "there's just a point at which we drop out of the game"
**[M2003-149]**. Under Q7 this would close **OUT** before the width test. The box stays as Q1 closed it.

**Fair price (reporting figure, Part VII):** with one case only, that case valued at ten percent: **$(2.25) a share** on the
all-equity basis (central), **$(2.28)** equity-only, after the company's own tax (nil). Against $4.55. A negative fair price is
reported as computed; it means no price earns the floor on the filed record.

## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**: the ten-year earning power turns on a decade of NASA science appropriations, which the
filer itself calls "a material uncertainty for our future growth", and on a stated pivot to an undemonstrated space-based solar
power venture; integrity facts recorded, not judged. COMPUTATION, NOT A CLEARANCE: range $(4.06) a share (no-growth case alone,
all-equity; equity-only $(4.19)) against $4.55; fair price $(2.25) all-equity, $(2.28) equity-only; no case earns the floor at any
positive price. No research pass: the cause is NATURE, and in any case no case of the range earns the floor at the price (Part VII).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found **[M1997-127]**; no verdict; the box unchanged (operator rule 2).*

**Bearing on Q2 (the castle).**
- The 10-K names no rival. It describes competition as ranging "from divisions of large corporations who are challenged by cost
  control and inflexibility, to small, privately held companies with singular capabilities" (Item 1). Any peers are therefore a
  CONVENTION of this run: Redwire (CIK 1819810) and Sidus Space (CIK 1879726), chosen as SEC filers that build space hardware
  including deployable structures. Their figures are XBRL company-facts transcription, not cross-checked against the filed
  statements (flagged; not weighed).
- Operating margin over each filer's whole filed span: **Helio** FY2022 (0.4)%, FY2023 0.7%, FY2024 (25.3)%, FY2025 (95.4)%;
  **Redwire** CY2020 (41.5)%, CY2021 (51.0)%, CY2022 (91.2)%, CY2023 (6.4)%, CY2024 (13.9)%, CY2025 (68.5)% (last accession
  0001819810-26-000029); **Sidus Space** CY2020 (84.8)%, CY2021 (249.4)%, CY2023 (210.1)%, CY2024 (336.4)%, CY2025 (827.7)% (last
  accession 0001493152-26-014547; CY2022 not tagged). No year of operating profit at either peer in the span read.
- "The Company has no filed or registered copyrights, trademarks or patents" (Item 1); components are designed in-house and "sent
  out for competitive bid to third-party fabricators" (Item 1); fees are "limited by government or agency policies" (Item 1).
- For it: the Firefly antenna contract, where "Our solution displaced another vendor's offering due to its heritage and
  performance" (Item 1); repeat NASA customers since 2019 (Item 1).
- Dependence on a few people: "Our success depends heavily on our executive officers, senior management team and highly trained
  employees" (10-K MD&A risk summary); the S-1 names "the continued service of our President, CTO and Chief Engineer"; about twelve
  employees at 2026-02-13, ten of them hourly (Item 1). The CTO who resigned on 2025-07-24 (Joseph Pitman, Item 11) was the
  founder the S-1 credited with the defence-payload background.

**Bearing on Q3 (capital).** Almost no fixed capital (property and equipment $47,729; capex nil in FY2024, FY2025 and the nine
months); the capital used is receivables and the lease. The return on it was about nil in the private years and deeply negative
since.

**Bearing on Q4 (the accounts).** Stock issued for services $2,481,918 in the nine months to 2026-07-31 against revenue of
$1,543,492; loss on debt extinguishment $1,236,303 and debt-discount amortization $864,738 in the same period; a derivative
liability that rose from $39,543 to $1,655,559; four preferred series created in one year. Short-term loans secured on future
receipts: $63,000 repaid as $91,980 over 30 weeks, $60,000 as $89,940 over 18 weeks (twice), $80,000 as $120,000 over 24 weeks
(10-K MD&A). A receivables sale agreement of May and June 2025 (Note 1). Late-filing notices (NT 10-Q or NT 10-K) on 2025-04-28,
2025-06-16, 2025-09-15, 2026-01-30 and 2026-03-17 (EDGAR list). The auditor (Astra) was dismissed on 2026-02-21, four days after
signing the FY2025 opinion, with no disagreements and no reportable events stated (8-K 0001213900-26-020758). The 10-K's Item 10
says the Code of Conduct "will be available on our website upon the completion of this offering", registration-statement wording
in an annual report.

**Bearing on Q5 (the people): integrity facts recorded, not judged.** A later run that reaches Q5 must answer them **[M2013-088]**.
- The chief executive from 2026-01-05, Edward M. Cabrera, an investment banker by background, received 3,000,000 shares (600,000
  after the split) on signing and a salary of $1; on the same day his son, Edward W. Cabrera, was hired as Manager of Investor
  Relations and received 1,250,000 shares (250,000 after the split) (10-K Items 1, 5, 11). Item 10 states "There are no family
  relationships among any of the directors and executive officers of the Company"; the son is not listed as an executive officer.
- The chief financial officer's cash salary of $10,000 a month is payable only "upon the Company raising an aggregate of $10
  million in financing" (Item 11).
- The founder chief executive and the chief engineer exchanged their loans to the company for 7,398,459 shares (1,479,692 after the
  split) on 2025-12-02 (Item 5; 10-Q statement of changes).
- The 10-K features a projection for the planned solar-power business: "$811B lifetime profit and an IRR at 11% annually" (Item 1).
  The row on such statements, recorded for the later run: "they usually are people that tell you things that are too good to be
  true" **[M2002-028]**.
- Secured notes of $900,000 and $250,000 went unpaid at their 2025-11-05 maturity; default notices were received in November and
  December 2025 and February 2026 (10-K Subsequent Events). Their status at 2026-07-31 was not read.

**Bearing on Q6 (the money and the owners).**
- Common shares rose from 2,274,393 (2025-10-31) to 5,190,024 (2026-07-31), up 128% in nine months, with four preferred series
  issued; a 2025 equity plan with an "evergreen" reserve reset each year to 20% of shares outstanding; each independent director
  eligible for $100,000 a year in restricted stock units (Item 11). The row the framework carries as a candidate second STOP: "we
  have never invested in companies that are hell-bent on issuing shares" **[L2014-015]**.
- In the quarter to 2026-07-31 the company bought back 9,231 shares for $49,828 in the open market, "not made pursuant to a
  publicly announced repurchase plan"; the board authorised up to 250,000 shares on 2026-07-02 "and ratified 9,477 shares
  repurchased prior" (10-Q, equity note). In the same quarter it sold preferred stock, and on 2026-09-01 issued a note convertible
  "at a price equal to 65% of the lowest closing price during the 10 trading days prior to conversion" (10-Q, subsequent events).
  No price limit is stated for the buyback; the bottom of the computed range is negative.

**Bearing on Q9 (debt and exposures).** Cash $520,504 against current liabilities of $3,814,363 at 2026-07-31; going-concern doubt
in the 10-Q; notes "secured by the Company's accounts receivable, and by shares of common stock pledged by one of the Company's
shareholders", some with acceleration rights (10-Q). The acquisition criterion the framework applies at Q9: "Businesses earning
good returns on equity while employing little or no debt" **[R1997-001]**.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after Q1 (the closing STOP) and again
      after this section (write-early). The template was copied and the notes file written before the first EDGAR request.
- [ ] If dispatched: the brief allowed the per-question commits (yes); the lock and the fold are the dispatching session's and
      were not checked by the analyst. A run not in the register binds nothing.
- [ ] **Blind rule: one breach, declared.** A filename filter of the `Test Runs/` listing for the company's four names was run
      before the rule's reach was registered; it printed nothing. No other run file, holding review or `PORTFOLIO.md` was opened,
      and nothing seen by accident was used (CONTAMINATION, above).
- [x] Every v5 id resolves (`check_ids.py` in the research folder: every M/L/R id in `principle_ledger_v5.csv`, no E-ids, every
      quoted fragment beside an id found in that row); every filing fact has its accession; the peer figures are flagged as XBRL
      transcription.
- [x] The order was kept; Q1's STOP closed the run; everything after it is headed COMPUTATION, NOT A CLEARANCE or AFTER THE STOP.
- [x] Owner cash after every real cost, with stock pay and stock issued for services deducted, never a net-income proxy (operator
      rule 5); the sovereign from the US Treasury; the price from an aggregator, flagged.
- [x] Contrary evidence written down as found (THE FOUNDATIONS; the strongest case for IN under Q1; the "for it" line under Q2's
      facts); the facts for later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` produced no arithmetic lines for this name; nothing it prints was used.
- [x] `python tools/check_framework.py` PASS before each commit.
- Not done, said so: the DEF 14C, the 8-Ks of 2026-03-11, 2026-04-28 and 2026-05-01 (financings and preferred designations) and
  the preferred conversion terms were not read, since the file closed at Q1; nor was the status of the defaulted notes at
  2026-07-31.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Where a political customer budget belongs.** Q1's fixed routing sends a business whose ten-year economics cannot be foreseen
"because its industry changes fast" to TOO HARD; Q2 sends a castle shown open to OUT. Here the product is plain and the castle
evidence runs strongly one way (no patents, fee-limited contracts, competitive bidding, losses at the peers), but the deciding
unknown is neither fast change nor the castle: it is a government budget for one directorate, set by politics. I closed at Q1 on
tests 3 to 5 and the doubt row (**[M2002-092]**); another analyst could pass Q1 on the plain product and close OUT at Q2. The text
does not say which question owns a single-payer budget risk. (2) **Q7's specifics assume a positive cash stream.** With owner cash
negative in every year, specific (b) leaves "the no-growth case alone", which values the business below zero, and Part VII's fair
price becomes a negative number that is not a price. I reported it as computed; the text could say that where no year of owner
cash is positive, the fair price is "none". (3) **A short history.** The range convention asks for a five-year average; the
filings carry four fiscal years. I used four and confessed it as a CONVENTION of this run. (4) **Net debt and instruments that
settle in shares.** Q7's definition (borrowings and finance leases less cash) does not say how to treat an embedded-conversion
derivative liability or convertible preferred carried as mezzanine equity; I left both out and said so. (5) **The brief's lines of
evidence assume an Item 1A.** A smaller reporting company may omit it; I drew the risks from the MD&A's summary list and from the
S-1 the 10-K names. (6) **The balance-sheet instruction** asks for eight to ten years; a filer with five year-ends cannot supply
them, and the template has no line for saying so beyond the analyst's own note.
