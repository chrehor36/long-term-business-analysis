# Company Run: Velo3D, Inc. (Nasdaq Capital Market: VELO), 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template to this dated name before any
fetch (commit 5480d616).

**Dispatched blind run** under the canonical brief `Screens/_daily/_dispatch_brief.md`, with the one departure the brief
states: the lines of evidence were derived by the analyst from the 10-K's Item 1, Item 1A and Item 7 (listed in Step 0), and
the competitors were to be the rivals the 10-K itself names.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (VELO; also searched for Velo3D); not held.*

**Contamination, declared and not used.** (1) A directory listing of `Test Runs/` made to check that this run's file name was
free showed the names of other run files and research folders dated 2026-10-13 (GRFXY, HDSN, HRIBF, JCSE, KIGRY, LHSW, LZ,
MSM, SIEGY, SITE, SQFT, TPICQ). None was opened; no file about Velo3D under any name appeared in the listing. (2) The
session's opening context carried recent commit subjects about another company's run (TPICQ) and its box, and research
folder names of two other companies (AYI, ARCB) in the git status. Not read further, not used. (3) The session's memory index
carries general queue lines (counts of gate-clearers, a paused wave); none names this company. Not used.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $7.99 (close 2026-10-12; aggregator quote printed by `tools/run.py`, flagged per operator rule 5: a live quote
  only).
- **Shares by class** from the latest filing's cover: common stock, $0.00001 par, **32,149,118** shares as of 2026-08-07
  (10-Q for the period ended 2026-06-30, filed 2026-08-11, accession `0001193125-26-344560`; `python Screens/cover_shares.py
  VELO`). One class. Checked against the balance sheet of the same 10-Q: 32,149,118 shares issued and outstanding at
  2026-06-30, no treasury shares. Filings after the 10-Q: 8-K of 2026-10-02 (`0001193125-26-412304`, CFO separation, interim
  CFO services agreement) and 8-K of 2026-10-09 (`0001493152-26-046400`, a chief executive's social-media post on guidance);
  neither reports an issuance. **Open item:** the at-the-market program (sales agreement of May 2026, capacity $100.0M, $59.4M
  sold by 2026-06-30 per the 10-Q, Note 1 and Note 16) may have sold shares after 2026-08-07; no filing read states a later
  count. Reverse splits: 1-for-35 effective 2024-06-13 and 1-for-15 effective 2025-07-28 (a cumulative 1-for-525); every
  share figure below is on today's basis.
- **Market cap:** 32.149M x $7.99 = **$256.9M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, US Treasury daily par yield curve, 30-year, 2026-10-09
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-03-31, `0001193125-26-134997` (Items 1, 1A, 7, the financial
  statements, Note 1 going concern, the revision note); 10-Q June 2026, filed 2026-08-11, `0001193125-26-344560` (balance
  sheet, Note 1 going concern, Note 17 subsequent events, the Livermore lease note, Item 4 controls); DEF 14A filed
  2026-04-27, `0001825079-26-000007` (related-party transactions, ownership, CEO pay); 8-K of 2026-08-11,
  `0001193125-26-344537`, and its Exhibit 99.1 press release; the two 8-Ks above; for the cycle and the balance sheets, the
  10-Ks for FY2021 (`0001628280-22-007442`), FY2022 (`0001825079-23-000012`), FY2023 (`0001825079-24-000008`) and FY2024
  (`0000950170-25-047760`).
- **One figure cross-checked against the filed statement:** net cash used in operating activities FY2025, $(27,327)
  thousand on the filed consolidated statement of cash flows of the FY2025 10-K, equal to the `tools/run.py` line (-27.3M).
  Also checked: stock-based compensation FY2025 $9,509 thousand and purchase of property and equipment $(2,715) thousand on
  the same statement.
- **`python tools/run.py VELO` arithmetic lines only** (its v4-era labels and rules not used, Part VII). Owner cash after every
  real cost, operating cash less stock pay less all capital spending, from the filed statements (USD millions; stock pay for
  2024 as revised in the FY2025 10-K, 11.8, against 15.4 as first filed):

  | Year | Operating cash | Stock pay | Capital spending | Owner cash (after interest) | Cash interest paid | Owner cash before interest | Revenue |
  |---|---|---|---|---|---|---|---|
  | 2020 | -26.4 | 1.5 | 0.4 | -28.3 | 0.5 | -27.8 | 19.0 |
  | 2021 | -56.4 | 4.4 | 9.6 | -70.4 | 1.4 | -69.0 | 27.4 |
  | 2022 | -124.0 | 20.1 | 13.8 | -157.9 | 0.4 | -157.6 | 78.7 (80.8 as first filed) |
  | 2023 | -105.6 | 24.9 | 1.0 | -131.6 | 9.7 | -121.9 | 77.4 |
  | 2024 | -32.7 | 11.8 | 0.0 | -44.5 | 1.2 | -43.3 | 41.0 |
  | 2025 | -27.3 | 9.5 | 2.7 | -39.6 | 1.1 | -38.4 | 46.0 |

  Five-year mean (2021 to 2025): **-88.8M** after interest, **-86.0M** before interest. Depreciation and amortization:
  2.2, 5.3, 9.3, 4.8, 3.4 (2021 to 2025); the depreciation variant (operating cash less stock pay less depreciation) is -88.5M
  over the five years, no different in sign. No year of positive owner cash in the six filed. First half of 2026: operating
  cash -$39.5M (press release of 2026-08-11, Exhibit 99.1 to `0001193125-26-344537`; the 10-Q's own statement not
  transcribed here), more than the whole of 2025. Computation file: `Test Runs/_research 2026-10-13 VELO/q7_computation.py`.
- **The balance sheets, read in Step 0 because the file may close before Q4** (USD millions, each year as filed in that
  year's 10-K; 2022 and 2024 were later revised, noted):

  | Year-end | Cash + short-term inv. | Receivables | Inventory | Total assets | Debt (current + long) | Earnout + warrant liab. | Total liabilities | Paid-in capital | Accumulated deficit | Equity |
  |---|---|---|---|---|---|---|---|---|---|---|
  | 2020 | 15.5 | 1.2 | 7.3 | 32.7 | 8.0 | 0.2 | 16.8 | 15.0 | -122.8 | -107.8 (preferred outside equity) |
  | 2021 | 223.1 | 12.8 | 22.5 | 302.7 | 8.1 | 133.2 | 192.3 | 340.3 | -229.9 | 110.4 |
  | 2022 | 80.2 | 9.2 | 71.2 | 225.1 | 8.2 | 20.2 | 84.3 | 361.5 | -219.8 (-221.9 revised) | 140.8 |
  | 2023 | 31.1 | 9.6 | 60.8 | 153.8 | 33.1 | 13.3 | 85.5 | 425.5 | -357.0 | 68.3 |
  | 2024 | 1.2 | 3.7 | 50.0 | 89.2 | 5.7 | 2.2 | 49.5 | 470.0 (466.4 revised) | -430.3 (-426.8 revised) | 39.7 |
  | 2025 | 39.0 | 6.3 | 27.1 | 105.3 | 31.0 | 0.1 | 67.2 | 536.3 | -498.1 | 38.2 |
  | 2026-06-30 | 91.1 | 8.4 | 27.6 | 200.1 | 8.2 | 0.2 | 53.6 | 663.2 | -516.7 | 146.5 |

  What moved and why, in words: the business has no goodwill to speak of, so equity is paid-in capital less losses, and the
  ledger of the two is the story. Paid-in capital rose from $15.0M (2020) to $663.2M (June 2026) while the accumulated deficit
  rose from $122.8M to $516.7M: about $394M of losses in five and a half years, paid for by the merger cash of 2021 and by
  share issues since. Cash went from $223M (2021) to $1.2M (2024), the year of the going-concern disclosure and the
  debt-for-equity exchange, and back to $91.1M (June 2026) only by issuing shares ($50M direct offering, $59.4M at the market
  in the first half of 2026, per the 10-Q). Inventory ran from $22.5M (2021) to $71.2M (2022) against flat sales and was
  worked down to $27.1M with reserves for excess and obsolete stock of $7.2M (2024) and $7.0M (2025) charged on the cash-flow
  statement. Debt was never large except in 2023 ($33.1M of secured notes); the earnout and warrant liabilities of 2021
  ($133.2M) were valuation entries that swung the income account (the 2022 "net income" of $10.0M came from them, the 10-K's
  own cash-flow discussion). The share count rose from 0.35M (end 2021, on today's basis: 183,232,494 / 525) to 32.15M:
  roughly ninety-fold. What the figures cannot say: whether any year shown is the business's normal state.
- **Lines of evidence chosen, and why** (the brief's departure): from Item 1, (1) the technology and how fast it changes (the
  R&D list and "The high-value metal parts and AM segments are undergoing technological advancements across hardware,
  software and materials") and (2) the business model and customers (printers against the RPS service business; 56% of 2025
  revenue from defense-related programs); from Item 1A, (3) competition and obsolescence, (4) the going concern and the
  dependence on new financing, (5) the material weaknesses in internal control; from Item 7, (6) revenue, gross margin and
  operating cash over the whole span, and the financing history. These are the lines that bear on Q1's test, whether the
  ten-year economics can be foreseen, and on the facts recorded after the stop.
- **Competitors named in the 10-K:** none. A sweep of the FY2025 10-K's Items 1, 1A and 7 for "competitor" and for the
  names of metal-printing firms found the rivals described only as a class ("a wide variety of producers of additive
  manufacturing and/or 3D printing equipment"; "a number of companies that have substantial resources"), with no company
  named; the FY2021 to FY2024 10-Ks gave the same result on the same name sweep. No named rival, filing or not, to flag. Q2 is
  not reached (below), so no competitor row was built; had it been, the brief's rule would have left it empty, which is
  recorded under "What in the framework was wrong or unclear".

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be happy owning it "if the market closed for five years"
**[M1997-109]**. Here the business itself needs the market open: the 10-K says it does "not have sufficient liquidity to meet
our operating needs" for twelve months and "will need to engage in additional financings", and the 10-Q of June 2026,
with $91.1M in cash, still concludes that "substantial doubt continues to exist" because it expects to "require additional
financing to fund operations" (Note 1, `0001193125-26-344560`). A business that must sell shares to the market to live is
the reverse of the foundation's picture; that is a fact about the business, carried to the questions, not a verdict here.
The market serves and does not instruct: the price has moved from a $3.00 offering (August 2025) to $7.99, and "It just
tells us prices." **[M2006-077]**. Who is paid to tell you: the chief executive posts guidance on a personal social account
(8-K of 2026-10-09) and the company's growth story is carried by underwritten offerings and an at-the-market program; the
foundation is applied to that material as a seller's account **[M2006-077]**. No macro forecast enters **[M2000-094]**: the
defense-spending tailwind the filings describe is not used. **Contrary evidence, written down as found** **[M1997-127]**:
against the hypothesis forming as I read (a fast-changing technology that has never earned money), the 2026 record runs the
other way: second-quarter revenue of $20.7M, up 52.3% on the year, gross margin of 21.5% against (11.7)%, backlog of $31M,
$29M of new bookings in the quarter, and guidance raised to $65M to $75M of 2026 revenue (Exhibit 99.1 to
`0001193125-26-344537`); defense customers are named (RTX, Honeywell, Lockheed Martin, among others, 10-K Item 1). I looked
for what is wrong **[M2025-013]** and for what would show me wrong; these are written down here and weighed at Q1.

## THE STANDING RULE
A purchase of the common for cash, with no borrowing and no position that can call on the buyer, puts nothing the buyer
has and needs at risk, provided the stake is sized so that its total loss is bearable; "We are never going to risk what we
have and need for what we don’t have and don’t need." **[M2012-081]**. The going-concern disclosure makes a total loss of
the stake a real case, which governs sizing, not the questions. Not engaged on this name if bought that way.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
The test is "where the business will be in 10 years" **[M2000-037]**, meaning "a reasonable fix on about what the earning
power and competitive position will look like in five or 10 years" **[M2012-065]**. The product is understood well enough
from Item 1 (laser powder-bed fusion printers, the Flow and Assure software, a parts-production service); the question is
the economics, "We just don’t know the economics of it 10 years from now." **[M2000-104]**.

The tests, each against the filings:
1. **Where will it be in ten years?** The company itself states the ten-year premise as a belief about a transition not yet
   made: "We believe the industry is transitioning toward production-scale deployment" (10-K Item 1,
   `0001193125-26-134997`), and "many legacy AM solutions have remained limited to prototyping". The economics in ten years
   depend on whether that transition happens and who captures it.
2. **The key variables, and how predictable** **[M1998-044]**. (a) Whether metal printing displaces casting, forging and
   machining for production parts in defense and aerospace; (b) whether Velo3D's process lead holds, when its own risk factor
   says "any of our products may be rendered obsolete or uneconomical by our or our competitors’ technological advances" and
   that "a number of companies that have substantial resources have announced that they are beginning production of 3D
   printing systems"; (c) price and cost, when "Demand for our product lines is sensitive to price" and the gross margin has
   run 33.6% (2020), 18.1% (2021), 1.1% (2022 as revised), (33.9)% (2023), (5.1)% (2024), (16.1)% (2025) and 21.5% in one
   quarter of 2026 (partly from "a refinement in the allocation of certain labor and overhead costs", the press release's
   own words); (d) the business model itself, which the filer is changing: RPS "will contribute an increasing share of
   revenue" under a "new go-to-market strategy", with segment reporting to be expanded in 2026 and $40M to $50M of 2026
   capital spending planned for RPS and a 289,000-square-foot Livermore campus on a 124-month lease (10-Q,
   `0001193125-26-344560`). None of the four is predictable from the record: "If something is not very predictable, forget
   it." **[M1998-044]**.
3. **Do the past statements tell me the future ones?** **[M2008-033]**. Six filed years show revenue of 19.0, 27.4, 78.7,
   77.4, 41.0 and 46.0 ($M), owner cash negative every year from -28M to -158M, a sales halving in 2024 that the filer ties to
   "delayed shipments, the going concern with the Company, and customer order delays", and two revisions of prior statements
   (FY2022 revenue cut by $2.1M in the FY2023 10-K; FY2024 stock pay revised in the FY2025 10-K). The statements describe a
   business in search of its economics; they do not tell me what the 2030s statements will look like.
4. **Important and knowable?** **[M2006-076]**: the deciding variable, the long-run margin and return of a production
   metal-printing business against better-funded rivals, is important and not knowable from where I stand. "If something’s
   important but unknowable, forget it." **[M2006-076]**.
5. **Would the insiders write it down?** The filer's own forward account is written as belief and risk ("We believe", "may be
   rendered obsolete", "We expect to face increasing competition"), and its owner-cash record has no profitable year to
   anchor a forecast. Of the tech field's insiders: "They would say, “That’s too hard.”" **[M2000-105]**.
6. **Can I name the winner, not just the industry?** The 10-K names no rival and calls the field "fragmented and
   competitive", with competitors of "substantially greater financial, technical, marketing and sales" resources. "we don’t
   have the faintest idea who the winners will be" **[M2012-067]**; seeing growth "does not mean we can judge what its profit
   margins and returns on capital will be as a host of competitors battle for supremacy" **[L2009-005]**.
7. **Customers or technology?** **[M2017-019]**: the forecast here is about technology (the R&D list in Item 1: machine
   sub-system refactoring, rapid build-module exchange, AI-assisted tool-path software, closed-loop control), not about
   settled customer habit. "if something comes in where there’s a technological component that’s of significance [...] it
   won’t make it through the filter." **[M1998-008]**.
8. **How far off could I be?** **[M2011-084]**: revenue fell 47% in one year (2023 to 2024) and owner cash has ranged over a
   factor of five; I could be off by the whole value of the company in either direction.
9. **Do I doubt it is inside?** Yes; "if you have doubts about something being into your circle of competence, it isn’t."
   **[M2002-092]**.

The 2026 improvement written down above (revenue up, margin up, backlog) does not answer the test: one quarter of margin,
partly from a cost reallocation, is not a fix on the ten-year economics, and "usually if something can gain competitive
advantage very quickly, you have to worry about them losing it quickly, too." **[M2002-050]**. "whenever we look at a
business and we see lots of change coming, 9 times out of 10, we’re going to pass on that." **[M1999-063]**.

The start-up rows ("Start-ups are not our game." **[L2007-015]**) were considered and not used as the ground: Velo3D was
founded in 2014 and has filed revenue for years, so it is not a start-up in the rows' sense, although it has never had a year
of positive owner cash. The ground is the fast-changing technology, which the routing sends to TOO HARD, not OUT
**[M2000-038]**.

**Which cause.** NATURE. The deciding question is a forecast of a fast-moving technology's economics and of its winner,
which the rows say study does not cure: "a business that must deal with fast-moving technology is not going to lend itself
to reliable evaluations of its long-term economics" and "We couldn't solve this problem, moreover, even if we were to spend
years intensely studying those industries." **[L1993-023]**; "Our problem -- which we can't solve by studying up -- is that
we have no insights into which participants in the tech field possess a truly durable competitive advantage." **[L1999-018]**.
No filing not yet read would state the ten-year margin of production metal printing (test 5, **[M2000-105]**), so the cause
is not WORK.

- **VERDICT: TOO HARD (NATURE)**, by the routing fixed at Q1 (fast-changing industry, ten-year economics not foreseeable)
  **[M1998-008]**, **[L1993-023]**, **[M2006-013]**. "It just means that we don’t know how to evaluate it." **[M2000-038]**.
  The file closes here. Q2 to Q12 NOT REACHED.

## Q2 to Q10, Q12: NOT REACHED (operator rule 2; the Q1 STOP closed the file).

---
## THE BOX
**TOO HARD (NATURE), decided at Q1** (a fast-changing technology whose ten-year economics and winner cannot be foreseen; no
filing would state them) **[L1993-023]**, **[M2000-105]**, **[M2006-013]**. Q7 not reached; the computation beneath the stop
gives a value range of **-$45.21 a share (all-equity, no-growth case alone) against $7.99**, every case negative.
**Integrity facts recorded, not judged.** The closed box is not reopened by a lower price **[M2000-038]**; no research pass
is owed (the cause is NATURE, and no case of the computed range earns the floor at any positive price).

## COMPUTATION, NOT A CLEARANCE (the brief's two reporting figures; Q7 was not reached)
Built by Q7's range convention as written, applied to a business whose owner cash has been negative in every filed year.
- **The base.** Owner cash after every real cost, five-year mean 2021 to 2025: **-$86.0M** a year before interest (the
  all-equity basis) and **-$88.8M** after interest (equity-only). All capital spending deducted, the depreciation variant
  beside it (-$88.5M after interest): the sign does not change. (e) The maintenance guess: capital spending was $9.6M,
  $13.8M, $1.0M, $0.0M and $2.7M; the filing gives no maintenance figure, and with every year negative before any capital
  spending at all (operating cash less stock pay alone was -60.8M, -144.1M, -130.6M, -44.5M, -36.8M) no maintenance split
  could make any case positive. (d) Working capital is inside operating cash as filed. (c) No cash paid for businesses in the
  window (investing lines read in the FY2025 and earlier cash-flow statements); no signed deal. (a) Cycle base: no end year
  of the window is described by the filer as aberrational (the filer's explanation of a bad year attaches to 2024, a middle
  year), so the literal window is the base; beside it, the latest year alone (2025, -$38.4M before interest) and the
  three-year mean (2023 to 2025, -$67.9M before interest).
- **The growth.** The series is negative in every year, so a compound rate between end years is meaningless; by specific (b)
  the halves were tried (first half 2021-2022 mean -$114.2M, second half 2024-2025 mean -$42.0M, after interest): a shrinking
  loss, still a loss, and a growth rate of a negative stream is equally meaningless. **The range is the no-growth case alone,
  said so.** (f) The cap is not engaged: no growth is carried.
- **Rate and term.** 5.60% (Treasury 30-year, 2026-10-09); ten years at no growth then zero nominal growth, which for a
  constant stream is the perpetuity.
- **Net debt** at 2026-06-30 (10-Q, `0001193125-26-344560`): debt $3.2M current + $5.0M long-term = $8.2M, less cash $91.1M =
  **net cash $83.0M**. Operating leases left out and said so (noncurrent lease liabilities $22.5M at 2026-06-30; the Livermore
  lease of 124 months commenced 2026-07-01 and is not yet on the balance sheet). Subsequent events stated in the 10-Q: none
  requiring adjustment beyond the lease. Shares 32.149M.
- **Whose tax.** The company paid almost no income tax (provision $0.1M in 2025) and carries a full valuation allowance;
  owner cash is negative before any tax, so the shelter convention has nothing to price.

| Case | Annual owner cash | Business value at 5.60% | Per share |
|---|---|---|---|
| **Central, all-equity, five-year mean, no growth** | -$86.0M | -$1,536.3M; plus net cash $83.0M | **-$45.21** |
| Equity-only, five-year mean, no growth | -$88.8M | -$1,585.7M | -$49.32 |
| Beside: three-year mean, all-equity | -$67.9M | -$1,212.1M; plus net cash | -$35.12 |
| Beside: latest year alone (2025), all-equity | -$38.4M | -$686.2M; plus net cash | -$18.76 |

- **The floor, tested first.** No case in the range earns the floor at any positive price: the expected return at $7.99 on the
  central base is about -49.5% a year (-$86.0M against market value plus net debt of $173.9M), and on the latest year alone
  about -22.1%. Had Q7 been reached it would have closed OUT on the floor whatever the width **[M2003-149]**; the width test
  does not arise.
- **(a) VALUE RANGE:** **-$45.21 a share** (all-equity, the no-growth case alone; equity-only -$49.32), against **$7.99**.
- **(b) FAIR PRICE** (Part VII: each end case valued at ten percent, averaged; here one case): all-equity -$86.0M / 0.10 =
  -$860.3M plus net cash $83.0M = **-$24.18 a share** (central); equity-only -$88.8M / 0.10 = -$888.0M = **-$27.62 a share**.
  No positive fair price exists on the filed record. Neither figure is a verdict or entry language (operator rule 3).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.
- **Bearing on Q2 (the castle).** The 10-K names no rival; it calls the field "fragmented and competitive" and says "Demand for
  our product lines is sensitive to price" (Item 1A, `0001193125-26-134997`). Gross margin was negative in 2023, 2024 and 2025
  ((33.9)%, (5.1)%, (16.1)%). Inventory reserves for excess and obsolete stock of $7.2M (2024) and $7.0M (2025). The 10-K calls
  its IP a "Deep moat"; issued patents expire from 2035.
- **Bearing on Q3 (capital).** The 10-K describes "an asset-light business model"; the 2026 guidance plans $40M to $50M of
  capital spending "primarily for RPS expansion, subject to the availability of sufficient financing", and a 289,000-square-foot
  Livermore campus on a 124-month lease is to become the primary production centre (Exhibit 99.1 to `0001193125-26-344537`;
  10-Q lease note). In December 2025 the company sold printers and post-processing equipment to Varilease for $10M in a
  sale-leaseback reported as debt.
- **Bearing on Q4 (the accounts).** Material weaknesses in internal control reported in the FY2023 10-K (debt and equity
  instruments, inventory, contract assets and liabilities, statement preparation, IT general controls), carried in the FY2025
  10-K, and "not been remediated as of June 30, 2026" (10-Q Item 4). Prior statements revised twice: FY2022 revenue reduced
  from $80.8M to $78.7M in the FY2023 10-K (a "formula error and an incorrect hourly rate" in variable consideration); FY2024
  stock pay reduced from $15.4M to $11.8M in the FY2025 10-K (forfeitures on earnout awards not accounted for). The second
  quarter 2026 gross-margin improvement is attributed in part to "a refinement in the allocation of certain labor and overhead
  costs between cost of revenue and operating expenses". The press release features a non-GAAP net loss and adjusted EBITDA,
  and guides to "Positive EBITDA in the second half of 2026" and a gross margin above 30% in the second half.
- **Bearing on Q5 (the people): integrity facts recorded, not judged.** (i) The chief executive, Arun Jeldi, beneficially
  owned about 48.6% of the common as of 2026-03-04 (10-K Item 1A) through Arrayed Notes Acquisition Corp., a subsidiary of
  Arrayed Additive, Inc., of which he holds 100%; Arrayed Acquisition bought the senior secured notes from the note holders
  on 2024-12-09 (a forbearance on specified events of default was signed the same day) and exchanged $22.4M of them on
  2024-12-24 for 12,343,423 shares, owning about 95% of the company that day (10-K Item 7; DEF 14A, `0001825079-26-000007`).
  (ii) He is also chief executive and president of Arrayed Additive, Inc., described in the DEF 14A as "engaged in magnesium
  and aluminum lightweight alloy additive manufacturing (3D printing) for the aerospace and defense industries", the same
  field and customers. (iii) 3,000,000 shares in his beneficial holding are pledged as collateral for a loan (DEF 14A
  ownership footnote). (iv) A director, Kenneth Thieneman, held through his entities the January and February 2025 secured
  convertible notes (12% after amendment, conversion prices reset in August 2025 from $23.40 and $15.00 to $16.38 and
  $10.50), converted in March 2026; his Thieneman Construction is jointly and severally liable as co-lessee on the Varilease
  sale-leaseback and "did not receive any compensation for serving as co-lessee". (v) The chief financial officer separated
  on 2026-09-28; the interim CFO is furnished under a services agreement by KongBasileConsulting LLC, which also provides the
  company's "accounting, financial reporting and related consulting services" under a separate engagement dated 2021-01-25
  (8-K, `0001193125-26-412304`). (vi) Revenue guidance is issued, and was restated by the chief executive on a personal X
  account after the CFO's departure (8-K, `0001493152-26-046400`). (vii) The DEF 14A lists late Section 16 filings by eight
  insiders for 2025 and one Form 3 not filed.
- **Bearing on Q6 (money and owners).** Shares outstanding rose from about 0.35M (end 2021, on today's basis) to 0.49M (end
  2023), 12.99M (end 2024, after the exchange), 24.61M (end 2025) and 32.15M (June 2026). Issue prices on today's basis:
  $3.00 (August 2025 offering), $8.25 (December 2025 private placement), about $14.00 (April 2026 direct offering, $50M for
  3,571,428 shares), about $27 on average at the market in the second quarter of 2026 ($59.4M for 2.2M shares). No buyback.
  Chief executive pay: base salary raised from $425,000 to $650,000 from 2026-01-01, target bonus to 100% of salary, and a
  planned one-time option on 3% of the common vesting at market-capitalisation milestones of $1 billion to $10 billion (DEF
  14A).
- **Bearing on Q9 (ruin).** Substantial doubt about continuing as a going concern stated in the FY2025 10-K and again in the
  10-Q of June 2026 with $91.1M of cash; at 2026-06-30 debt was $8.2M against that cash.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 5480d616); written question by question; committed after Q1
      (e3ccb0ab) and at the close.
- [x] Dispatched to an analyst: the brief allowed the per-question commits and states that the dispatching session holds
      the lock; the fold into the register is the dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched for this company. One listing of
      `Test Runs/` (file names only) was made to check the dated file name, and is declared under contamination above with
      the commit subjects and memory lines seen; none was used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (check script `Test Runs/_research 2026-10-13 VELO/check_ids.py`);
      every filing fact has its accession; no number without a row, a filing or the CONVENTION it comes from.
- [x] The order was kept; the first STOP that failed (Q1) closed the run; nothing after it is a clearance; every figure after
      the stop is headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (operating cash less stock pay less all capital spending), never a net-income proxy
      (operator rule 5); the sovereign from the Treasury; the price quote flagged as an aggregator's.
- [x] Contrary evidence was written down as it was found (the 2026 revenue, margin and backlog, in the foundations) and
      weighed at Q1; the facts found for later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor is cited (the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its three-year mean is not a v5 rule and was not used
      for the base.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **The range convention has no instruction for a stream that is negative in every year.** Specific (b)
covers a sign change and a meaningless compound rate, and sends the run to "the no-growth case alone"; read literally that
yields a single negative figure, so the "range" has one end, the three-to-one width test cannot be applied (a ratio of two
negatives, or of one, means nothing), and the fair price (the average of two end cases) collapses to one case. I applied (b)
literally, said so, and showed the latest year and the three-year mean beside it only as context; the floor test first
(2026-10-10) is what closes such a computation, and it closes it at once. A sentence saying that a stream with no positive
year has no range and no fair price would make the reporting figures less misleading than a negative dollar price.
(2) **The brief's competitor rule (the rivals the 10-K names) returns nothing for a filer that names none**, as here across
five 10-Ks. Q2 was not reached, so nothing turned on it; had it been, Q2's "ask the competitors" and section C's field
returns "from the filer's and the rivals' filings" would have had no rival to read, and the run would have needed either a
CONVENTION of its own choosing the rivals or a TOO HARD (WORK) on the field's returns. The canonical brief or Q2 should say
what to do when no rival is named. (3) **The start-up rows sit in Q1's OUT list with no definition of a start-up.** A
business eleven years old with filed revenue but no year of positive owner cash is near the line; I did not apply the OUT
and recorded why, but another analyst could close the same file OUT at Q1 on **[L2007-015]** and **[M2008-088]**, a
different box from mine on the same facts.
