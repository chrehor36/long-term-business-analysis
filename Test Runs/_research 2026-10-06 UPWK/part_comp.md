
---
## COMPUTATION — NOT A CLEARANCE
*Everything in this section was produced after the file closed at Q1. It is reported at the owner's request (not a rule
change) and carries no entry language. No figure here reopens Q1 **[M2000-038]**.*

### A. The balance sheets, 2017 to mid-2026 (evidence for a Q4 that was not reached)
Read before the income account, as **[M2025-032]** asks ("balance sheets over an 8 or 10 year period before I even look
at the income account"). USD millions; `tools/run.py` table (first-filed XBRL) checked against the filed FY2025 and FY2023
statements and the Q2 2026 10-Q.

| year-end | total assets | equity | cash + securities | escrow (= payable) | goodwill | intangibles | debt | retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2017 | 275 | −31 | n/r | n/r | 118 | 9 | 34 | −124 |
| 2018 | 392 | 244 | n/r | n/r | 118 | 6 | 24 | −143 |
| 2019 | 446 | 259 | n/r | n/r | 118 | 3 | 18 | −172 |
| 2020 | 529 | 299 | n/r | n/r | 118 | 1 | 11 | −195 |
| 2021 | 1,081 | 260 | n/r | n/r | 118 | 0 | 561 | −251 |
| 2022 | 1,080 | 249 | n/r | n/r | 118 | 0 | 564 | −341 |
| 2023 | 1,038 | 381 | n/r | n/r | 118 | 3 | 356 | −294 |
| 2024 | 1,212 | 575 | 622 | 196 | 121 | 13 | 358 | −78 |
| 2025 | 1,300 | 630 | 673 | 181 | 149 | 37 | 360 | 37 |
| 2026-06-30 | 1,274 | 611 | 614 | 193 | 149 | 31 | 361 | 94 |

(n/r = not read for this run; the 2024 to 2026 cash lines are from the filed statements.)

What moved and why:
- **Equity was negative before the 2018 IPO** and then stood near $250M to $300M for five years while the company lost
  money every year; stock pay credited to paid-in capital roughly offset the losses. Equity rose to $575M in 2024 mostly
  because of a **$140.3M non-cash tax benefit** from releasing a valuation allowance (10-K FY2025 MD&A), not from cash
  earned. The deferred tax asset it created ($111.5M at 2025, $109.9M at mid-2026) is a future saving of cash tax, not cash.
- **Goodwill of $118M** is the Elance-oDesk combination and sat unchanged from 2017 to 2023; the rise to $149M is the 2025
  purchases of Ascen and Bubty ($58.4M cash for acquisitions in 2025). No write-down in the span.
- **Debt**: $575M of 0.25% convertible notes issued in 2021 (FY2023 10-K cash flows); $171.3M of cash retired part of them
  in 2023 at a $38.9M gain; $361.0M fell due 2026-08-15, to be paid "using existing cash on hand and borrowings under our
  Revolving Credit Facility" (Q2 2026 10-Q). A $150M secured revolver was signed 2026-06-23 (8-K `0001627475-26-000039`),
  secured on "substantially all assets", with leverage and fixed-charge covenants. Whether it was drawn is not yet filed
  (the Q3 10-Q is not out).
- **Cash is not all the company's.** The escrow line (customer money held in trust) is matched by an equal liability and
  is excluded. Company cash and securities at 2026-06-30: $614.2M; less the notes at principal, **net cash about $253.2M**
  before any revolver draw.
- **Receivables** rose from $31M (2017) to $76M (2025) while revenue rose from $203M to $788M, so receivables fell as a
  share of revenue (about 15% to about 10%): nothing building up against sales. No inventory.
- **Retained earnings** went from −$341M (2022) to +$94M (mid-2026); about $140M of that is the 2024 tax release.
- **Share count**: 132.4M (end 2022) → 137.3M (2023) → 135.3M (2024) → 130.5M (2025) → 124.8M (mid-2026), with
  buybacks of $100.0M (2024), $136.0M (2025) and $109.7M (H1 2026, average $13.24 a share), against RSU settlements of
  3.7M to 4.6M shares a year.

**What the figures do not say**: how much of the 2024 to 2025 rise in owner cash came from cutting sales and marketing
($246.9M in 2022 to $143.4M in 2025) and headcount (two restructurings) rather than from the business, and whether the
lower marketing is why active clients fell. **One presentation change, disclosed**: in Q4 2024 the company moved the
change in client receivables funded through escrow from operating to financing cash flow, which raised reported operating
cash flow by $25.5M (2023) and $4.9M (2022) (10-K FY2024 `0001627475-25-000011`, Note 2). It is disclosed and plausibly
correct (the money is the talent's), so it is recorded as a fact, not as a tell; the owner-cash series above uses the
recast figures for 2022 and 2023.

### B. Owner cash after every real cost (operator rule 5; stock pay deducted)
USD millions; OCF − SBC − (property and equipment + capitalized software). From the filed cash-flow statements.

| | 2021 | 2022 | 2023 | 2024 | 2025 | H1 2025 | H1 2026 | TTM to 2026-06 |
|---|---|---|---|---|---|---|---|---|
| owner cash | −48.9 | −72.8 | −34.8 | 70.7 | 157.7 | 68.2 | 19.3 | 108.9 |

Notes on the real costs: stock pay ($65.4M in 2025) equalled 26% of OCF and is deducted in full **[L2015-003]**; the
company's "adjusted EBITDA" ($225.6M in 2025) excludes it and is not used. 2025 cash taxes ($13.5M paid) were well below
the book provision ($37.8M) because of the deferred tax asset; a full-tax variant deducts the $18.5M non-cash deferred tax.
2025 OCF also includes $23.9M of other income, mostly interest on about $670M of cash and securities, much of which went to
repay the notes in August 2026. **2025 adjusted** (full tax, interest removed after tax at 24.6%, the 2025 effective rate)
= 157.7 − 18.5 − 18.0 = **$121.2M**. H1 2026 owner cash fell because accrued liabilities fell $32.1M (bonus payments and
the restructuring) and capitalized software rose to $17.7M.

Five-year mean (2021 to 2025): **$14.4M**. Three-year mean: $64.5M. The five-year window holds two abnormal loss years
(2021 and 2022, when sales and marketing reached 36% and 40% of revenue against 18% in 2025), so the owner's whole-cycle
variant is shown beside it.

### C. Value range (the Q7 convention, applied only as computation)
Discount rate 5.66% (30-year Treasury, 2026-10-05); ten years at the stated growth, then zero nominal growth; plus net
cash of $253.2M; 124.903M shares. "Growth shown" cannot be measured on aggregate owner cash (it starts negative), so GSV
growth is used as the nearest shown rate: +9.8% a year 2020 to 2025, −0.6% a year 2022 to 2025; −4% is the Q2 2026
year-on-year GSV change. Script: `Test Runs/_research 2026-10-06 UPWK/value.py`.

| base (owner cash, $M) | −4% | 0% | −0.6% | +9.8% |
|---|---|---|---|---|
| five-year mean, 14.4 (the convention's base) | $3.51 | **$4.06** | $3.97 | **$6.45** |
| 2025 adjusted, 121.2 (whole-cycle variant) | $14.55 | **$19.18** | $18.35 | $39.29 |
| TTM to June 2026, 108.9 (raw, not tax-adjusted) | $13.27 | $17.43 | $16.68 | $35.49 |

- **Convention range: $4.06 (no growth) to $6.45 (shown growth) a share, against $8.36.** The price sits above the top.
  By the convention that is an OUT through the floor; but the file closed at Q1, so it is recorded only.
- **Whole-cycle variant (the five-year window holds abnormal years): $14.55 (GSV −4% a year) to $19.18 (flat).** On
  this base the price is below the bottom.
- Across the two bases the range runs from about $3.50 to about $39, more than three to one: the convention would
  itself close it TOO HARD ("the range must be so wide that no useful conclusion can be reached" **[L2000-025]**; a
  wide range is not cured "by having some extra large margin of safety" **[M2007-022]**). The arithmetic reaches the same
  place as Q1 by another road.

### D. Fair price and cheap price (owner's reporting, COMPUTATION)
- **Rule for the fair price:** the price at which the central case's expected pre-tax return equals about 10% (the floor
  CONVENTION), with no growth, so the expected return is the pre-tax owner-cash yield on the enterprise (equity less net
  cash). Owner cash is after cash tax; it is grossed up at the 2025 effective rate of 24.6% to put it on a pre-tax footing.
  The floor is applied to **equity less net cash** (the operating business), and the net cash is added back at face.
- **Central case:** the 2025 adjusted figure, $121.2M after tax = $160.8M pre-tax, held flat. Fair price =
  (160.8 / 0.10 + 253.2) / 124.903 = **$14.90**. On the convention's five-year base ($14.4M after tax, $19.1M pre-tax) the
  same rule gives **$3.56**; on the TTM base, $13.59. The central case is a choice (the latest year, adjusted), and the
  spread to $3.56 is the honest width.
- **Rule for the cheap price (CONVENTION of this run):** the price at which even the worst stated base (the five-year
  mean, which carries two loss years) clears the ~10% pre-tax floor with no growth, so that no choice of window is needed
  and no pencil decides it **[M1996-084]**: **$3.56**.
- **Against the price of $8.36:** above the cheap price; about 56% of the central fair price; above the whole convention
  range. The market price implies an operating business worth about $791M, roughly 6.5 times the 2025 adjusted owner cash,
  i.e. the market is pricing a decline. None of this is a clearance; the box is set at Q1.

### E. The competitor row (evidence for a Q2 that was not reached)

| measure | Upwork | Fiverr (FVRR) | Freelancer Ltd (ASX: FLN) |
|---|---|---|---|
| 2025 volume | GSV $4,028M | marketplace GMV $1,073.0M | not obtained |
| 2025 take rate | 18.7% (13.1% in 2019) | 27.7% (27.6% in 2024) | not obtained |
| buyers / clients | 851k (2023) → 785k (2025) → 763k (mid-2026) | 4.2M (2021), 4.3M (2022), 4.0M (2023), 3.6M (2024), 3.1M (2025) | not obtained |
| revenue | $300.6M (2019) → $787.8M (2025); H1 2026 flat | $107.1M (2019) → $430.9M (2025) | A$57.4M (2021) → A$53.2M (2025); **aggregator, flagged** (stockanalysis.com) |
| GAAP operating income | loss every year 2016 to 2023; $65.2M (2024), $129.3M (2025) | loss every year 2017 to 2025 (−$1.2M in 2025) | not obtained |
| 2025 owner cash (OCF − SBC − capex) | $157.7M | $51.9M (104.6 − 51.4 − 1.3) | not obtained |
| what the filer says about AI | demand down in "certain categories of freelance work"; AI-agent sellers now listed as competitors | "AI technologies reducing demand for simple and low-skilled services"; growth in AI-related complex work | not read |

Sources: Upwork filings as above; Fiverr 20-F FY2025 `0001178913-26-000858` and 20-F FY2022 `0001178913-23-001230`
(buyers 2021, 2022), revenue, OCF and SBC from Fiverr's filed XBRL. Fiverr's treatment of customer funds in its cash-flow
statement was not checked. Over the whole span both listed markets show the same shape: volume rising to 2021 to 2022,
then a falling count of buyers and a rising fee per buyer. Upwork has the larger volume and the better margins; neither
filing shows a castle the other cannot cross, and neither shows the volume of work rising since 2022. In-house hiring
platforms and AI-agent sellers file nothing comparable that this run read.

### F. Facts recorded for questions not reached (no verdict)
- **Management:** Hayden Brown, president and CEO (proxy `0001627475-26-000026`); CEO total pay $9.51M (2023), $9.93M
  (2024), $17.09M (2025), the 2025 rise mostly stock awards ($15.15M) in a year when active clients fell 6%; say-on-pay
  support "approximately 94%" in 2025. Officer turnover in fourteen months: chief accounting officer resigned (2025-07),
  new COO (2025-09), new chief accounting officer (2025-12), GM Marketplace departed (2026-03/04), CFO on medical leave with
  the CEO as interim principal financial officer (2026-07); two directors left the board at the 2026 meeting.
- **Buybacks:** authorizations of $100M (2025) and $300M (2026-02-18), "no expiration date", no stated price (8-K
  `0001627475-26-000015`). Prices paid: about $12.4 (2024), $14.6 (2025), $13.24 (H1 2026), all above the bottom of the
  convention range ($4.06) and above the cheap price ($3.56).
- **Restructuring:** 2024 workforce reductions; May 2026 plan, about 24% of the workforce, $16M to $23M of charges, $13.8M
  booked in Q2 2026, plus $12.4M of cash retention awards (10-Q `0001627475-26-000047`, Note 13).

---
## THE BOX
**TOO HARD (NATURE), decided at Q1.** The volume of work businesses will buy from people through an online market once
AI agents do part of that work is the deciding variable, the filer and its nearest competitor both say they cannot
predict it, and Upwork reported in August 2026 that AI was already cutting GSV and active clients. A lower price does not
reopen it. For reference only (COMPUTATION): price $8.36; convention range $4.06 to $6.45; whole-cycle variant $14.55 to
$19.18; central fair price $14.90; cheap price $3.56.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. *Not committed after each: the dispatch
      forbids commits in this session; the file was written in four appends (Step 0, foundations, Q1, computation).*
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every filing fact has its accession; no
      number without a row or a filing, except the Freelancer revenue (aggregator, flagged) and the CONVENTION figures
      labelled as such.
- [x] The order was kept; the first STOP that failed (Q1) closed the run; everything after it is marked NOT REACHED or
      COMPUTATION — NOT A CLEARANCE.
- [x] Owner cash after every real cost, stock pay deducted, never a net-income proxy (operator rule 5); the sovereign from
      the issuing authority (US Treasury); the price quote flagged as aggregator.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (six items under the foundations, and the
      strongest case for the business stated at Q1).
- [x] No row dated after the anchor is cited (this is a live run, not a point-in-time test; the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its printed yield, implied growth and spread lines
      were not.
- [x] `python tools/check_framework.py` PASS before handing back (see the result recorded at the end of this file).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **The dispatch pointed to "Q1's routing where AI may change demand for the work sold" and "network effects at Q2"; the
   framework text has neither.** A search of `Framework/THE FRAMEWORK v5.md` for "network", "AI", "artificial
   intelligence", "marketplace" and "two-sided" finds no instance. Q1's routing is written for "fast-moving technology"
   and "industries prone to rapid change" from the supplier's side (the business must keep up with technology); the case
   here is different in kind: a technology outside the business changing how much of the *product* customers will want
   (substitution of the work sold). I applied the existing route (**[L1993-023]**, **[M1998-008]**: "where we think the
   future technology could hurt the business as it presently exists") because its words cover it, but the framework
   should say whether substitution of demand is Q1 (foreseeability) or Q2 (test 11, "what could destroy, modify or reduce
   it"), since the same facts could be argued as a castle filling in (Q2 OUT) rather than a future that cannot be seen
   (Q1 TOO HARD), and the two boxes are acted on differently. A two-sided market's moat (both sides staying because the
   other side is there) has no test of its own in Q2; a future run that reaches Q2 on a marketplace will have to argue it
   from "share of mind", "the low bid" and "ask the competitors".
2. **The Q7 convention breaks when owner cash starts negative.** "Carried at the growth shown" has no meaning when the
   five-year series runs from −$72.8M to +$157.7M; I substituted GSV growth and said so. The convention should name the
   fallback (a volume measure, or no growth).
3. **The five-year window and the abnormal year.** The owner asks for a whole-cycle variant "if the five-year window holds
   an abnormal year", but neither the framework nor the dispatch says what makes a year abnormal or what the variant's
   base is. I treated the two heavy-marketing loss years as abnormal and used the latest year adjusted for full tax and
   for interest on cash about to leave; another analyst could choose the three-year mean ($64.5M) and get a value about
   half mine. The variant's base is a CONVENTION of this run.
4. **Interest on cash and tax shelters inside owner cash.** The convention does not say whether interest earned on the
   cash (later added as net cash) is removed from owner cash, or whether cash taxes depressed by a deferred tax asset are
   normalized. Leaving both in would have counted the cash twice and overstated the tax-free years; I removed both and
   say so.
5. **The cheap price** has no rule in the framework (it is the owner's reporting request); the rule above is mine.
