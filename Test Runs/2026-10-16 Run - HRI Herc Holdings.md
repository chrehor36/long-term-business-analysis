# Company Run: Herc Holdings Inc. (NYSE: HRI), 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*A dispatched blind run, resumed. The template copy was committed before any fetch (commit e2b320b4); the first session
fetched the filings and wrote the scripts in `Test Runs/_research 2026-10-16 HRI/` and was stopped by a session limit
before any section of this file was written. This session committed what was on disk (c130ea9d), refetched nothing that
was already in the folder, and wrote this file from Step 0 on.*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.  *Filled at the fold by the dispatching session, 2026-10-16, after the run was committed: `PORTFOLIO.md` read for this ticker only; not held.*

**Contamination, declared.** Seen by accident and not used: the session context listed recent commit subjects of the
repository, one of which carries another company's v5 re-run result (a rail lessor closed at Q2), and a memory index line
naming counts of gate-clearers and a paused queue; the project map names the alert-list and queue files (not opened). Nothing
seen names this company or its ticker apart from my own run file's commit. No other run file, holding review,
`PORTFOLIO.md`, queue, register, reading list or resume-state file was opened, listed or searched.

**The lines of evidence this name needs, derived from the FY2025 10-K (the brief's stated departure).** From Item 1 (one
operating and reportable segment, equipment rental; 602 locations; an estimated 4% share of North American rental revenue;
"price is one of the primary competitive factors"): (1) the cost position against the national rivals, over the whole span;
(2) pricing and volume, and whether pricing held in the soft years. From Item 1A (pricing pressure, suppliers renting direct,
national accounts 49% of rental revenue, $8.1 billion of debt): (3) the field's returns over the last full cycle (2017 to
2025 holds the 2020 downturn); (4) debt and maturities. From Item 7 (the H&E acquisition, pro forma rental revenue down 6% in
2025, rental capital spending and used-equipment proceeds): (5) owner cash after the fleet, with the acquisitions treated as
capital spending; (6) the H&E deal as a use of the money.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $121.28 (2026-10-16, live quote printed by `tools/run.py`; an aggregator, flagged per operator rule 5, live quote only).
- **Shares by class** from the latest filing's cover: 33,431,444 shares of common stock, par $0.01, the only class (10-Q for
  the quarter to 2026-06-30, filed 2026-07-28, accession `0001364479-26-000109`; `python Screens/cover_shares.py HRI`).
  Checked against the same 10-Q's balance sheet: 38.3 million issued less 4.9 million in treasury = 33.4 million. No 8-K or
  prospectus after the 10-Q issues shares: the two later 8-Ks are a receivables-facility amendment (2026-09-03,
  `0001628280-26-060440`) and a director's election (2026-08-19, `0001364479-26-000112`).
- **Market cap:** 33.431444M x $121.28 = $4,054.6M.
- **Sovereign for the earnings currency (USD):** 5.43%, the 30-year par yield on the US Treasury daily par yield curve,
  2026-10-15 (`tools/run.py`, which reads the Treasury curve; the issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-17, accession `0001364479-26-000050` (Items 1, 1A, 7,
  the statements and Notes on acquisitions, debt, segments); 10-Ks for FY2024 (`0001364479-25-000007`), FY2022
  (`0001364479-23-000006`), FY2019 (`0001364479-20-000005`) and FY2016 (`0001364479-17-000008`) for the earlier years and the
  named rivals; 10-Q to 2026-06-30 (`0001364479-26-000109`); proxy, DEF 14A filed 2026-03-27 (`0001364479-26-000076`);
  8-K of 2026-07-28 (`0001364479-26-000108`, the quarter's release, cover only read). **One figure cross-checked against the
  filed statement:** net cash provided by operating activities for 2025, $1,085M in the FY2025 10-K's cash-flow statement,
  equals the tagged figure `tools/run.py` prints (1,085); total assets at 2025-12-31, $13,776M, are the same in the 10-K and
  in the 10-Q's comparative column.
- `python tools/run.py HRI` arithmetic lines only (`Test Runs/_research 2026-10-16 HRI/run_py_output.txt`). Its own owner
  figure takes only non-rental capital spending as capex (156, 161, 157) and so leaves the rental fleet out; it lists rental
  equipment spending (1,320, 1,048, 1,097) as an "other capital payment" and prints a warning that its depreciation column
  holds only intangible amortization. Both are confirmed against the statements and neither column is used. Owner cash is
  rebuilt from the filed cash-flow statements in `value.py` (below, and in the COMPUTATION under Q7). SBC is the filed
  "stock-based compensation charges" line, complete (23.3, 27.1, 18, 17, 34 for 2021 to 2025).

**The rental fleet, and how it is treated.** Rental equipment spending is a real capital cost and used-equipment proceeds
offset it; both are read from the cash-flow statement (FY2022 10-K for 2021 and 2022; FY2025 10-K for 2023 to 2025):
spending 593.8, 1,168.5, 1,320, 1,048, 1,097; proceeds 106.9, 121.1, 325, 288, 448 ($M). Owner cash on the all-spending basis
deducts the spending and credits the proceeds; the maintenance case uses rental and property depreciation as the proxy for the
spending needed to stand still, "the depreciation charge is not inappropriate in most companies to use as a proxy for required
capital expenditures" **[M1998-127]**, and adds back the gain on sale of rental equipment that the operating section removes,
since the proceeds above book are cash the fleet returns. Acquisitions are kept separate and treated by Q7's specific (c).

**The balance sheets, ten year-ends, read before the income account** (the file closes before Q4, so they are read here as
the template asks; figures from `tools/run.py`'s ten-year table, first-filed vintage, accessions listed in
`run_py_output.txt`; 2025 checked against the FY2025 10-K and the 10-Q). "balance sheets over an 8 or 10 year period before I
even look at the income account" **[M2025-032]**.

| year-end | assets | equity | goodwill | intangibles | tangible equity | debt on the face | receivables | retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2016 | 3,463 | 318 | 91 | 304 | -77 | 2,179 | 293 | -625 |
| 2018 | 3,610 | 573 | 91 | 294 | 188 | 2,130 | 332 | -391 |
| 2020 | 3,588 | 742 | 100 | 296 | 346 | 1,652 | 301 | -278 |
| 2021 | 4,490 | 977 | 232 | 389 | 356 | 1,916 | 388 | -53 |
| 2022 | 5,957 | 1,109 | 419 | 431 | 259 | 2,938 | 522 | 224 |
| 2023 | 7,061 | 1,273 | 483 | 467 | 323 | 3,692 | 563 | 498 |
| 2024 | 7,877 | 1,396 | 670 | 572 | 154 | 4,090 | 589 | 633 |
| 2025 | 13,776 | 1,948 | 2,873 | 1,665 | -2,590 | 8,053 | 769 | 547 |

($M; 2017 and 2019 are in `run_py_output.txt` and lie between their neighbours; tangible equity is equity less goodwill and
intangibles, my subtraction.) What the figures say: assets quadrupled while equity rose by $1.6B, so the growth was paid
for with debt and, in 2025, with $584M of shares; debt went from 2,179 to 8,053 and was 4.1 times equity at the end of 2025.
Goodwill and intangibles went from 395 to 4,538, nearly all of it bought (the acquisitions of 2021 to 2025 cost $6.2B net of
cash acquired), and tangible equity, positive from 2017 to 2024, is negative $2.6B after H&E. Receivables held at about 18% of
revenue (293 on 1,555 in 2016; 769 on 4,376 in 2025), so the book shows no build-up of receivables against sales. Cash is kept
at a minimum (12 to 83), the business living on its credit lines. The retained deficit of 2016 was earned back by 2022, and
retained earnings fell in 2025 (633 to 547) as dividends of $87M were paid against net income of $1M. What they cannot say: what
the fleet would fetch in a downturn, and whether the depreciation charged keeps the fleet whole at today's equipment prices.
Deferred tax liabilities ($1,446M at 2025-12-31, 10-Q) show the fleet depreciated faster for tax than for the books, which is
why cash taxes paid are small (22.8, 22.1, 30, 12, 24 for 2021 to 2025).

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the first: "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**; with $8.0B of net debt behind $4.05B of equity, the owner of the shares owns the residue of a business whose
lenders come first. Macro conclusions "just never enter into the discussion" **[M2000-094]**: the construction cycle is not
forecast here; what is read is how the business earns across a cycle that already happened. The margin of safety is an
attitude here and arithmetic only at Q7 **[M1996-084]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) the
filer's operating margin rose from 4.3% (2017) to 20.4% (2023), a real improvement before the H&E year; (2) Herc grew from a
3% (FY2016 10-K) to a 4% (FY2025 10-K) share of a fragmented field and claims scale advantages over most of its rivals; (3)
pricing rose 5.8% in 2022 and 3.2% in 2024 (FY2022 and FY2024 10-Ks, MD&A); (4) national accounts are 49% of rental revenue,
a sticky base. Against: price is "one of the primary competitive factors", customers can "shift suppliers quickly", and
suppliers can rent direct (FY2025 10-K, Item 1A); pro forma rental revenue fell 6% in 2025 (Item 7).

## THE STANDING RULE
The run concerns a part-interest bought for cash in the market; nothing in it borrows, gives an option or invites a call on
the buyer, so owning it puts the buyer at no risk of ruin, provided it is bought without borrowed money and sized so that
"we are never going to risk what we have and need for what we don't have and don't need" **[M2012-081]** holds, with "Never
risk permanent loss of capital." **[L2023-005]** as the rule. The target's own debt is Q9's subject, not this rule's.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it:** understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**, and "the first question is, can I understand it?"
  **[M1995-051]**.
- **What the business is** (FY2025 10-K, Item 1 and Note 21, `0001364479-26-000050`): one operating and reportable segment,
  equipment rental; a fleet of aerial, earthmoving, material handling, trucks and trailers, compressors, lighting, trench
  shoring and the ProSolutions specialty lines, "fungible" and deployable across the network; revenue from rental, from
  selling used fleet, and from new equipment and supplies; 602 locations in 46 states and five provinces.
- **The key variables and whether they can be foreseen** **[M1998-044]**: the volume of fleet on rent (original equipment
  cost on rent), the rental rate, the cost of the fleet and what it fetches used, and the cost of money. The filer names the
  drivers: non-residential construction and industrial activity, and price competition (Item 1A). Equipment rental is not a
  fast-moving technology; the product a contractor rents in ten years is a lift, a loader or a generator, as now. The
  filer's mention of digital tools (Item 1A) is about how rentals are booked, not what is rented. Where the business stands in
  the industry, a mid-sized national renter with a single-digit share among a few larger national rivals, can be read from the
  filings, which is what the definition asks: "how the industry will develop and where the company will stand within the
  industry" **[M2012-065]**. The economics can be judged off the figures **[M2008-069]**, and the chemistry of the product need
  not be understood when "the economic dynamics of the industry" are **[M2011-014]**.
- **Would the insiders write it down?** **[M2000-105]**: the rental companies set fleet plans years ahead and report fleet
  age, utilization and pricing; the timing of the next construction downturn is not knowable, but it is a cycle the filings
  already show (2020), not a change in the business's nature, and macro timing does not enter **[M2000-094]**. The ten-year
  economics are knowable in the sense of **[M2006-076]**: an asset-heavy renter whose returns depend on its cost position and
  the cycle.
- **Doubt test** **[M2002-092]**: I have no doubt that the business is inside the perimeter; the doubts this name raises are
  about its castle and its debt, which are Q2's and Q9's.
- **Routing:** one segment, so no part decides against another (Q1's holding-company paragraph does not apply).
- **VERDICT: IN.** A cyclical, asset-heavy, single-segment rental business whose economics can be read from its own and its
  rivals' filings **[M2012-065]**, **[M2011-014]**, **[M2008-069]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what's going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**. A moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The rivals.** The FY2025 10-K's Competition section names none. The FY2024 10-K (`0001364479-25-000007`, Item 1) names the
large national rivals: United Rentals, Inc., Ashtead Group plc's Sunbelt Rentals brand and H&E Equipment Services, Inc. Used:
United Rentals (10-K for FY2025, `0001067701-26-000007`, and its earlier 10-Ks) and H&E (10-K for FY2024,
`0000950170-25-024867`, and its earlier 10-Ks; bought by Herc on 2025-06-02, so it filed no FY2025 year). **Flagged, not
used:** Sunbelt Rentals (Ashtead) did not file with the SEC over the span; its US holding company (Sunbelt Rentals Holdings,
Inc., CIK 2083785) has one 10-Q on EDGAR (filed 2026-09-09), so no full span of its own filings is on the SEC record. The
rivals' figures are their filed annual statements as tagged in their own 10-Ks (SEC companyfacts, read by `returns.py`);
Herc's are transcribed from its filed statements as pre-tax income plus interest expense, so that Herc's figure is before
financing like the rivals' operating income.

**The competitor row, the whole span** (`Test Runs/_research 2026-10-16 HRI/returns_output.txt`):

| year | HRI EBIT / revenue | URI operating income / revenue | HEES operating income / revenue | HRI / avg total assets | URI / avg total assets | HEES / avg total assets |
|---|---|---|---|---|---|---|
| 2017 | 4.3% | 22.7% | 13.4% | 2.2% | 11.2% | 10.2% |
| 2018 | 10.4% | 24.2% | 13.5% | 5.7% | 11.8% | 10.4% |
| 2019 | 11.9% | 23.0% | 13.9% | 6.4% | 11.6% | 8.4% |
| 2020 | 10.5% | 21.1% | 4.3% | 5.0% | 9.8% | 2.2% |
| 2021 | 18.2% | 23.4% | 12.5% | 9.3% | 11.9% | 6.5% |
| 2022 | 20.3% | 27.8% | 18.3% | 10.6% | 14.5% | 10.4% |
| 2023 | 20.4% | 26.7% | 18.8% | 10.3% | 15.4% | 11.2% |
| 2024 | 15.4% (20.9% before the $194M loss on Cinelease held for sale) | 26.5% | 15.1% | 7.4% | 15.1% | 8.4% |
| 2025 | 9.5% (10.6% before the $48M loss) | 24.7% | not filed | 3.9% | 13.7% | not filed |
| mean of the years shown | 13.4% | 24.5% | 13.7% (2017 to 2024) | 6.8% | 12.8% | 8.5% (2017 to 2024) |

On average debt plus equity, Herc's pre-tax return ran 2.9% to 16.0% and United Rentals' 12.2% to 20.1% (same file). The loss
lines are the FY2025 10-K's cash-flow statement ("Loss on assets held for sale", 194 and 48).

**The parts table.** One operating and reportable segment (FY2025 10-K, Note 21): the whole is the deciding part.

**The castle tests, each with its filing fact.**
1. *What keeps it standing* **[M1995-038]**: the filer names scale, a broad footprint, purchasing power, service and its
   specialty lines (Item 1, "Our Competitive Strengths"). These are real, and a larger rival has more of them in every year of
   the table.
2. *The attacker with money* **[M2011-015]**: the filer writes that its competitors, "some of whom may have greater resources
   and better access to capital or lower fixed operating costs, may seek to compete aggressively on the basis of pricing", and
   that its own suppliers "may appoint additional distributors, elect to sell or rent directly to our customers" (Item 1A).
   The field is entered by buying fleet, yards and people; Herc itself grew by buying H&E for $4.8B and paying off $1.4B of
   H&E's debt (FY2025 10-K, Note on acquisitions). Money can cross this moat.
3. *Pricing power and the agony before a rise* **[M2005-020]**: "If we try to increase our pricing, our competitors [...] may
   seek to compete aggressively on the basis of pricing" (Item 1A of the FY2025, FY2024 and FY2022 10-Ks, the same words).
   Pricing rose 5.8% in 2022 and 3.2% in 2024, both strong years; in 2025 pro forma rental revenue fell 6% (Item 7). The
   filer's own description is the prayer session.
4. *Would the customer still choose it over the low bid?* **[M2017-009]**: "price is one of the primary competitive factors.
   The Internet has enabled cost-conscious customers to more easily compare rates", and "Because we do not have multi-year
   contractual arrangements with many of our customers, these competitive factors could cause our customers to cease renting
   our equipment and shift suppliers quickly" (Item 1A). The fleet is "fungible" (Note 21). This is the commodity mark the rows
   give, that "most insureds don't care from whom they buy" **[L2004-003]**.
5. *The low-cost position* **[L2000-017]**, **[M1997-010]**: where the customer buys on price, "being the low-cost producer is
   all-important" **[L2000-017]**. United Rentals' operating margin exceeded Herc's in each of the nine years, by 18.4 points
   (2017) at most and 5.2 points (2021) at least, and by 5.6 points (2024) and 14.1 points (2025) with the Cinelease losses
   taken out of Herc's figure; United Rentals also earned more on its assets in every year. H&E, the smaller rival, had the
   higher margin in 2017, 2018 and 2019; Herc had the higher margin from 2020 to 2024. The rows measure the cost position
   against the competitor, not in the absolute: "if your costs are on parity or less [...] than your other major competitors,
   that is much more important to you than the absolute level" **[M2001-013]**, and the figures that show it "are available"
   **[M2009-059]**. Herc is not the low-cost producer; the largest national rival is, on every year shown.
6. *Unit volume, share of mind, the brand* **[M2000-031]**: Herc's share rose from about 3% (FY2016 10-K) to about 4% (FY2025
   10-K), and the rise was bought (H&E in 2025; Otay in 2024 for about $273M; $6.2B of acquisitions over 2021 to 2025). The
   filer calls the "Herc Rentals" mark material (Item 1); no filing fact shows customers asking for it by name or paying more
   for it.
7. *Widening or narrowing* **[M1999-108]**: the margin rose from 4.3% (2017) to 20.4% (2023) and fell to 9.5% (10.6% adjusted)
   in 2025; the gap to United Rentals narrowed to 5.2 points in 2021 and widened again to 14.1 points (adjusted) in 2025.
8. *What could destroy, modify or reduce it* **[M2000-014]**: a construction or industrial downturn met with $8.0B of net
   debt, suppliers renting direct, and a larger rival with lower costs that can price below it.
9. *Ask the competitors* **[M1999-130]**: no conversation was held; the rivals' own conduct on the record is that United Rentals
   agreed to buy H&E (FY2024 10-K, Item 1) and Herc then bought it (FY2025 10-K, Item 7): the field consolidates by purchase.

**A change for the better, and why it is not credited.** The rise in margin from 2017 to 2023 is a change for the better, and
the framework credits one "only on the evidence of a full cycle in which the price behaviour held" (Q2, Change, on
**[M2005-020]**, **[L1995-022]**); it did not hold into 2024 and 2025, and at its best (2023, 20.4%) Herc still earned 6.3 points
less on its revenue than United Rentals. The improvement does not change which producer is the low-cost one, which is the
question the box turns on, so the file does not go to TOO HARD (NATURE) on it.

**The field's returns over the last full cycle** (2017 to 2025, with the 2020 downturn inside it), judged in words: the largest
rival earned decent pre-tax returns on its assets through the cycle; Herc earned ordinary-to-poor ones, 2.2% to 10.6% on
average total assets; the smaller rival earned between the two. The field is not uniformly one of ordinary returns, so the
"standing castle that protects only ordinary returns" item is not the ground used; the ground is the cost position.

**Contrary evidence, written down** **[M1997-127]**: Herc closed much of the margin gap in 2021 to 2023; its specialty lines and
national accounts (49% of rental revenue) are less price-driven than the general fleet; and part of the 2024 and 2025 gap is the
Cinelease write-down and the H&E year's purchase accounting (intangible amortization of $115M in 2025, against $45M in 2024).
None of these reverses the order of the row in any year.

- **VERDICT: OUT.** A commodity-type field in the filer's own words (customers compare rates on the Internet and shift
  suppliers quickly; the fleet is fungible), in which Herc is not the low-cost producer against the rival its own 10-K names,
  in any of nine years: "commodity businesses have risk unless you're the low-cost producer, because the low-cost producer can
  put you out of business" **[M1997-010]**; "In an unregulated commodity business, a company must lower its costs to
  competitive levels or face extinction." **[L1994-035]**; "the guy with the lower cost comes in and kills you" **[M2001-013]**.
  The framework sends the high-cost producer in a commodity field to OUT (Q2, What it rules OUT), and a castle shown open on the
  evidence is not reopened by price: "If the answer had been yes, we wouldn't have done it." **[M2011-015]**; the box is the
  rows' "out" **[M2006-013]**.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed at Q2). Facts found are under AFTER THE STOP.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The balance sheets were read in Step 0, as the template asks when the file closes before Q4. Facts
found are under AFTER THE STOP.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity-bearing facts found in the proxy are under AFTER THE STOP and flagged in the box line.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. The buyback test needs the bottom of a Q7 range that was computed only as a COMPUTATION; facts are under AFTER
THE STOP.

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED as a verdict (operator rule 2). The reporting figures the brief asks for follow, under the protocol's heading.

### COMPUTATION, NOT A CLEARANCE
*Arithmetic in `Test Runs/_research 2026-10-16 HRI/value.py`, output in `value_output.txt`. Inputs are the filed cash-flow
statements (FY2022 10-K `0001364479-23-000006` for 2021 and 2022; FY2025 10-K `0001364479-26-000050` for 2023 to 2025) and the
10-Q to 2026-06-30 (`0001364479-26-000109`) for the debt. $M unless a share figure.*

**Owner cash by year, the window FY2021 to FY2025.**

| year | all spending, after interest (A) | maintenance only, after interest (M) | A before interest | M before interest | acquisitions, net of cash |
|---|---|---|---|---|---|
| 2021 | 177.5 | 251.3 | 242.8 | 316.6 | 431.0 |
| 2022 | -268.9 | 312.2 | -178.8 | 402.3 | 515.2 |
| 2023 | -84.0 | 432.0 | 90.6 | 606.6 | 430.0 |
| 2024 | 278.0 | 515.0 | 481.8 | 718.8 | 600.0 |
| 2025 | 243.0 | 155.0 | 574.0 | 486.0 | 4,257.0 |
| average | 69.1 | 333.1 | 242.1 | 506.1 | 1,246.6 |

A = operating cash less stock pay, less rental and non-rental capital spending, plus the proceeds of both kinds of disposal,
less principal paid on finance leases and financing obligations. M = operating cash less stock pay, less rental and property
depreciation, plus the gain on sale of rental equipment, less the same principal. "Before interest" adds back cash interest paid
(82.7, 114.1, 221, 258, 419) at 79%: **CONVENTION of this run:** interest is added back net of the 21% federal statutory rate;
rationale: the company paid little cash tax in these years (deferred taxes from fleet depreciation), so its true shield is
smaller and the larger add-back is the one kinder to the business, which the floor test below can afford. Intangible
amortization is not charged (purchased customer relationships and trade names; **[M1997-015]**, **[L2012-003]**). Working
capital is inside operating cash (specific (d)). Stock pay is charged.

**Net debt** at 2026-06-30 (10-Q): total debt as filed $7,912M (senior notes, ABL, term loan, AR facility and $89M of finance
leases, net of $51M of issuance costs) plus financing obligations $98M ($93M long-term, $5M current), less cash $43M =
**$7,967M**; operating lease liabilities ($1,548M) are left out, as the convention says. No later filing states a subsequent
event that changes it. Market value of the shares $4,054.6M; **what is paid for the business, $12,021.6M**.

**Q7's range convention, applied in full.**
- *The four PG specifics.* Growth is measured on aggregate owner cash, not per share. All spending is deducted in case A, the
  depreciation variant (M) beside it with the maintenance judgment stated. After year ten, zero nominal growth. A price above
  the top of the range closes OUT through the floor.
- *(a) Cycles.* The first year (2021) follows the 2020 trough and the last (2025) is the acquisition year, with seven months of
  H&E and what the filer calls "acquisition disruption at H&E" and "ongoing moderation in certain local markets" (Item 7). No
  full cycle, peak to peak or trough to trough, is inside the owner-cash series the filings give (one trough, 2020, and no
  later one), so no cycle base can be built; the base is the literal window, which is therefore also the literal window shown
  beside. Check on the combined business: the filer's pro forma pre-tax income for Herc with H&E and Otay was $140M (2024) and
  $106M (2025) (FY2025 10-K, Pro Forma Supplementary Data), so a full year of H&E does not lift the base materially.
- *(b) Decline.* The organic growth the filer reports is one figure: pro forma equipment rental revenue down 6% in 2025 (Item
  7). It is carried as the bottom; the no-growth case is the top. The total series change sign (A) or grow only by purchase.
- *(c) Acquisitions.* H&E was paid $2.9B in cash and $584M in shares, and $1.4B of its debt was paid off (Note on
  acquisitions): the larger part was cash, so it is an acquisition, capital spending, not a merger, and Q6's STOP on an
  all-stock deal does not apply. Net purchases over the window ($6,233M less $99M from the Cinelease sale = $6,134M) exceed half
  of owner cash before purchases ($605M), so this is **a serial acquirer: the central figure is the organic pair** (purchases
  left out, the filer's organic growth credited), with the default pair beside. The default pair, acquisitions deducted and
  total growth credited, gives owner cash after purchases of -$984.7M a year, negative on every growth rate, so no positive
  value. No signed unclosed deal.
- *(d) Working capital.* Counted, inside operating cash; no single-event draw is tied by the filer to one contract.
- *(e) Growth spending.* The filing gives no maintenance figure; the depreciation proxy is the guess the rows allow
  **[M1998-127]**, so the maintenance-only case M is central and the all-spending case A beside. The growth spending bought no
  organic growth the filer reports (2025: minus 6%), so the inversion applies: the maintenance-only no-growth case is the top.
- *(f) The cap.* The organic growth carried is not positive, so no cap binds. The total-growth series, between the first two and
  the last two years, grew 18.8% a year (M before interest) and 154.5% a year (A before interest), against sales growth of 20.5%
  a year with acquisitions; these are not creditable without deducting the purchases (specific (c)) and are shown only here.

**The floor, tested first.** Owner cash against what is paid, no growth: central case M before interest, $506.1M on
$12,021.6M = **4.21%**; A before interest 2.01%; equity-only M, $333.1M on $4,054.6M = 8.22%; equity-only A 1.70%. With the
organic growth negative, the growth cases earn less. For the central base to earn 10% at the price it would need to grow 12.4% a
year for ten years with no purchases, against the filer's only organic figure of minus 6%. **No case in the range earns the floor
at the price**: by the floor convention the file would close OUT here, whatever the width **[M2003-149]**.

**(a) THE VALUE RANGE (reporting figure, COMPUTATION), discounted at the sovereign 5.43%:**

| case | bottom (organic -6% for ten years, then flat) | top (no growth) |
|---|---|---|
| **central: organic pair, maintenance only, all-equity, less net debt** | **-$64.84 a share** | **$40.47 a share** |
| beside: organic pair, all spending, all-equity | -$155.33 | -$104.95 |
| beside: organic pair, maintenance only, equity-only | $114.18 | $183.49 |
| beside: organic pair, all spending, equity-only | $23.69 | $38.08 |
| beside: default pair (acquisitions deducted, total growth) | negative | negative |

Against **$121.28**. The literal window is the same five years (specific (a) above), so it is the same table. The equity-only
maintenance case brackets the price at the sovereign, but at the price it earns 8.22%, below the floor; it never decides alone.

**(b) THE FAIR PRICE (reporting figure, COMPUTATION; Part VII: each end case valued at 10%, the two averaged), after the
company's own tax (cash taxes as paid, inside operating cash):**
- **Central, all-equity basis: -$111.67 a share** (top -$86.93, bottom -$136.41: at 10%, the business's owner cash before interest
  is worth $5,061M at no growth, less than the $7,967M of net debt).
- **Equity-only beside: $83.35 a share** (top $99.64, bottom $67.07).
- All-spending cases beside: -$177.73 all-equity; $17.30 equity-only.

The central fair price is not positive. Under specific (c) the alert would fall to the organic pair; the central figure is
already the organic pair, so there is no further fallback to state. No cheap price is reported.

## Q8: IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Debt facts are under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Nothing in the filings read touches the businesses the question names.

---
## THE BOX
**OUT at Q2** (Q1 IN): equipment rental is a commodity-type field on the filer's own account, and Herc is not the low-cost
producer against United Rentals in any year from 2017 to 2025 **[M1997-010]**, **[L1994-035]**. COMPUTATION, not a clearance:
value range -$64.84 to $40.47 a share (central, all-equity, organic pair) against $121.28; no case earns the floor at the price
(4.21% central, 8.22% at best on equity alone); fair price -$111.67 all-equity ($83.35 equity-only). **Integrity facts
recorded, not judged** (the 2025 pay design and the 2026 restatement of the PSUs, under AFTER THE STOP, Q5).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.*

**Bears on Q3 (capital).** Rental fleet, net, $5,880M at 2025-12-31 against revenue of $4,376M (10-Q comparative column; FY2025
10-K). Rental capital spending of $5.2B over 2021 to 2025 against disposal proceeds of $1.3B; acquisitions of $6.2B on top. Pre-tax
return on average total assets 2.2% to 10.6% (2017 to 2025, the table at Q2). Owner cash after all spending averaged $69.1M a
year after interest over the window (Q7 computation).

**Bears on Q4 (the accounts).** The proxy's pay metrics are non-GAAP: "REBITDA", "Average REBITDA Margin" and "Average ROIC",
each excluding Cinelease (DEF 14A `0001364479-26-000076`, CD&A). The proxy calls 2025 a year of "record results" while net income
was $1M (FY2025 10-K). Losses on Cinelease held for sale of $194M (2024) and $48M (2025) and a $49M pre-tax loss recognised in the
second quarter of 2025 (FY2025 10-K, Note on assets held for sale; the cash-flow line shows $48M for the year). Receivables steady
at about 18% of revenue; no build-up of prepaid or deferred accounts seen in the ten balance sheets read. The earnings release of
2026-07-28 was not read beyond its 8-K cover, so whether an adjusted figure is featured there was not checked.

**Bears on Q5 (the people), integrity facts recorded, not judged** (DEF 14A `0001364479-26-000076`):
- For 2025 the annual incentive moved from 90% financial metrics and 10% management objectives to 30% financial (REBITDA) and
  70% objectives (integration steps and cost synergies), "to reflect our strategic priorities following the acquisition of H&E".
- The 2025 REBITDA target was $1,680.0M, with the maximum set equal to the target ($1,680.0M) and a threshold of $1,512.0M;
  actual REBITDA was $1,679M, "100.0%" of target. Every objective was scored 100%, and every named officer's individual score
  was set at 100%, for an overall payout of 100%.
- In February 2026 the committee "amended and restated the PSUs awarded in 2025 and 2024", from one measurement at the end of
  three years to annual measurement with goals re-established each year.
- For the 2023 PSUs the committee "assumed target performance for 2025" because after H&E it could not measure the metrics
  "on a consistent basis"; the 2023 grant paid 88.4%.
- A new independent director, a former chief executive of two rental companies, was elected on 2026-08-18 (8-K
  `0001364479-26-000112`).

**Bears on Q6 (the money).** H&E bought for $4.8B (cash $2.9B, 4.7M shares valued at $584M) plus $1.4B of H&E debt paid off,
funded with $2.8B of senior notes, a $750M term loan and borrowings on the ABL (FY2025 10-K, Note on acquisitions). Share
repurchases $115.2M (2022) and $120M (2023), none since; dividends $14.8M (2021), $68.1M, $73M, $77M, $87M (2025) and $47M in the
first half of 2026 while the first half's net result was a $5M loss (10-Q). The prices paid on the buybacks were not read.

**Bears on Q9 (debt).** Total debt $7,912M at 2026-06-30: senior notes of $800M (2029), $1,650M (2030), $600M (2031), $1,100M
(2033), $600M (2034); the ABL $1,878M (floating, 2030); term loan $746M (floating, 2032); the AR facility $500M, extended on
2026-08-31 to mature 2027-08-31 (8-K `0001628280-26-060440`). Cash $43M. Cash interest paid $419M in 2025 against pre-tax income of
$1M; pre-tax earnings plus interest of $417M against interest of $416M (FY2025 10-K). The filer's own risk factor: indebtedness
"could [...] place us at a competitive disadvantage to our competitors that have proportionately less debt" (Item 1A).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit e2b320b4, by the first session); written question by question in this
      session and committed after each (172833d4 Step 0 to Q1; b1578cb7 Q2; this commit the rest). The first session wrote no
      section before it was stopped; that gap is stated at the head of the file.
- [x] Dispatched run: the brief allowed the per-question pathspec commits; the lock and the fold are the dispatcher's (operator
      rule ten). This run binds nothing until it is in the register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident (commit
      subjects of another company, a memory index line, the map's file names) is declared under contamination and not used.
- [x] Every v5 id resolves (`check_ids.py`: no E-ids, every M/L/R id in `principle_ledger_v5.csv`, every quoted fragment beside
      an id in that row); every filing fact carries its accession.
- [x] The order was kept; Q2 closed the file; everything after it is NOT REACHED or headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, from the filed cash-flow statements, never a net-income proxy (operator rule 5); the
      rental fleet charged; the sovereign from the US Treasury curve; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations, Q2); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor-date issue.
- [x] Only the arithmetic lines of `tools/run.py` were used; its owner figure (non-rental capex only) and its D&A column (only
      intangible amortization tagged) were checked against the statements and set aside.
- [x] `python tools/check_framework.py` PASS before the final commit.
- Honest limits: the rivals' figures are their own filed statements as tagged (companyfacts), not re-read line by line from
  their 10-Ks; Herc's figure is pre-tax income plus interest while the rivals' is operating income, a small definitional gap
  (other income and expense) that does not change the order in any year. Sunbelt, the second named rival, is not in the row.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) The commodity paragraph of Q2 is written for a dependence on a commodity price, while the earlier section
"The commodity business and its one exception" defines a commodity business by the customer's indifference; a renter of fungible
equipment is the second kind, not the first, and the text does not say outright that the high-cost-producer OUT of the "What it
rules OUT" list applies to the second kind on the same terms. I applied it, on **[L2004-003]** and **[M1997-010]**, because the
list names the high-cost producer in a commodity field without restricting the kind. (2) Q7 says "no real growth" is computed as
zero nominal growth and the floor is about ten percent on owner cash after the company's tax, but it does not say how to add back
interest on the all-equity basis when the company pays almost no cash tax because of deferred taxes; I confessed a CONVENTION of
this run (the statutory rate, the larger add-back). (3) Specific (b) allows the growth "between the first and second halves of
the window" without saying what the halves of a five-year window are; I used the first two and last two years, and in this run
it decided nothing because the serial-acquirer rule put the central figure on the organic pair. Also unclear in practice: the
serial-acquirer rule's "organic growth as the filer reports it" when the filer reports organic growth for one year only (2025,
pro forma); I carried that one figure as the bottom and said so.
