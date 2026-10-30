# Company Run — HMH Holding Inc. (NYSE: HMH, Class A) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template to this dated name before any fetch** (commit daf6111f).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-16, after the run was committed: not held (`PORTFOLIO.md` carries no line for
HMH, MHWirth or Akastor).*

**Dispatch:** a dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the brief's stated departure (the lines of
evidence taken from the 424B4 prospectus and the two 10-Qs, since no 10-K exists). Working folder
`Test Runs/_research 2026-10-16 HMH/` (raw filings in its gitignored `cache/`; `_notes.md`, `q7.py`, `check_run.py` tracked).
The lock in `Screens/_daily/` was present, written by the dispatching session (2026-10-16T00:46).

**Contamination, declared and not used.** (1) The session context that launched this run carried the repository's recent
commit subjects, which include the fold of another company's v5 run (NOV, a rival named in this filer's prospectus) with that
run's box and its Q2 margin figures for NOV, SLB, Halliburton and Baker Hughes. None of those figures is used here; the rival
figures below were taken by me from the rivals' own 10-Ks, over a different span and on a different metric (segment margins).
(2) The memory index loaded with the session names queue counts and holdings-review debts in general terms; nothing about
this company. (3) The git status list shows other companies' research-folder file names (AYI, ARCB) and daily digest file
names; not opened. (4) Before the first fetch I ran a name filter for "HMH" over the `Test Runs/` directory listing to see
whether the run-file name was free; it returned no match. I declare it because a listing of that folder is on the blind list.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $17.34 (close 2026-10-15; Yahoo Finance chart endpoint through `tools/sources.py` `price()`; an aggregator,
  used for the live quote only, flagged per operator rule 5).
- **Shares by class:** Class A 12,201,501 and Class B 31,891,652 outstanding as of 2026-09-28 (resale S-1 filed 2026-09-28,
  accession `0001193125-26-405527`, "Description of capital stock" and "Shares eligible for future sale"). Total used for
  per-share figures: **44,093,153**. Cross-checks: `python Screens/cover_shares.py HMH` gives the 10-Q cover of 2026-07-31
  (accession `0001628280-26-053385`): Class A 12,042,625, Class B 31,891,652; the 10-Q balance sheet gives Class A issued
  12,296,857 less 254,232 treasury = 12,042,625, which agrees. The rise to 12,201,501 by 2026-09-28 is later issuance under
  the 2026 plan (RSU vesting); the S-1 is the latest filed count and is used. **How both classes are counted:** HMH Inc.
  holds one B.V. Voting Class A and one B.V. Voting Class B share of HMH B.V. for each Class A share outstanding; each Class B
  share is held together with one B.V. Non-Voting Class A and one B.V. Non-Voting Class B share and the bundle is redeemable for
  one Class A share (424B4, "Corporate reorganization"; resale S-1, Exchange Agreement). Each share of either class therefore
  carries one equal economic unit of HMH B.V., the operating company, and the per-share figures divide by the sum. Class B has
  no economic rights at HMH Inc. itself (10-Q, EPS note); its economics sit in the B.V. units it travels with. Not added:
  unvested RSUs (635 thousand) and PSUs (578 thousand) at 2026-06-30 and the plan reserve (10-Q note 13).
- **Market cap:** 44,093,153 × $17.34 = **$764.6M** (both classes). No split seen (`split_factor_after` returns 1.0).
- **Sovereign for the earnings currency:** the filer reports and prices in USD (much of its cost base is in NOK and EUR,
  translated). **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-15 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): there is **no 10-K**; the company listed on 2026-04-02. Read: the final prospectus
  (424B4, 2026-04-01, accession `0001193125-26-138102`: Summary, Risk factors, MD&A, Business including Competition and
  backlog, Management, Executive compensation, the audited statements of HMH B.V. for FY2024 and FY2025 with the segment note);
  the first S-1 (2024-08-12, accession `0001193125-24-198984`: the audited statements for FY2022 and FY2023 with the segment
  note); the 10-Q for Q2 2026 (2026-08-05, accession `0001628280-26-053385`, which carries the six-month figures; the Q1 10-Q,
  accession `0001628280-26-031295`, was fetched and its quarter is inside the six months); the 8-K of 2026-08-05 with its
  Exhibit 99.1 results release (accession `0001628280-26-053339`); the item list of the 8-K of 2026-04-02 (accession
  `0001193125-26-140110`); the resale S-1 of 2026-09-28. **No proxy statement** is on EDGAR (no annual meeting held yet);
  pay and board facts are from the 424B4. **One figure cross-checked:** net cash from operating activities, six months to
  2026-06-30, $25,156 thousand in the filed 10-Q statement and $25,156,000 in the XBRL company facts (same accession); total
  debt at 2026-06-30, $197,836 thousand in both.
- **How many years the filings give (stated as the brief asks):** income statements and cash-flow statements for **four
  audited fiscal years, FY2022 to FY2025**, plus the unaudited six months to 2026-06-30 and 2025-06-30; balance sheets at
  **four year-ends, 2022 to 2025**, plus 2026-06-30, and the opening equity at 2022-01-01 from the equity statement. HMH B.V.
  was formed on 2021-10-01 by combining Akastor's MHWirth and Baker Hughes's Subsea Drilling Systems; no filing on EDGAR gives
  either contributed business's own statements before that date. The framework asks for five years of owner cash (Q7) and
  eight to ten years of balance sheets (Q4, **[M2025-032]**); four exist. What is missing is treated below under the
  framework's own text and is not replaced by any substitute number.
- `python tools/run.py HMH`: "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." The tool has nothing for a filer with
  no 10-K. Every figure below is taken by hand from the filed statements named above.

**Owner cash by year, $ thousands** (operating cash flow, less purchases of property and equipment, capitalized development
costs and purchased intangibles, plus asset-sale proceeds, less the pre-IPO stock awards spread over the award years; the
all-equity line adds back cash interest paid after a 25% tax shield; acquisitions shown separately):

| | 2022 | 2023 | 2024 | 2025 | H1 2026 |
|---|---|---|---|---|---|
| Revenue | 677,213 | 785,446 | 843,363 | 821,754 | 342,143 |
| Operating income | 20,317 | 78,001 | 118,614 | 107,889 | 14,332 |
| Net income | (26,564) | 17,402 | 51,956 | 46,123 | (1,144) |
| Operating cash flow | 974 | 25,574 | 34,861 | 88,310 | 25,156 |
| PP&E, development costs, intangibles, less sales | (13,935) | (24,056) | (18,319) | (16,643) | (7,982) |
| Pre-IPO stock awards, spread (CONVENTION below) | (5,694) | (5,694) | (5,694) | (5,694) | in the period |
| Owner cash after interest, before acquisitions | (18,655) | (4,176) | 10,848 | 65,973 | |
| Cash interest paid | 18,604 | 26,159 | 23,284 | 28,024 | 9,195 |
| Owner cash all-equity, before acquisitions | (4,702) | 15,444 | 28,311 | 86,991 | |
| Acquisitions, net of cash | (3,254) | 0 | (19,624) | (4,457) | (770) |
| **Owner cash all-equity, after acquisitions** | **(7,956)** | **15,444** | **8,687** | **82,534** | |
| Working-capital lines inside operating cash flow | (30,500) | (36,586) | (82,281) | (33,984) | |
| PP&E depreciation (D&A less intangible amortization) | 19,292 | 18,013 | 20,139 | 18,113 | |

Sources: FY2022 and FY2023 cash-flow and income statements, S-1 `0001193125-24-198984` pages F-16 and F-20; FY2024 and FY2025,
424B4 `0001193125-26-138102` pages F-15 and F-19; H1 2026, 10-Q `0001628280-26-053385`. Paid-in-kind interest on the
shareholder loans (FY2024 $9,964k, FY2025 $11,055k) is non-cash and is added back inside operating cash flow; it is not in cash
interest paid. CONVENTION of this run: the pre-IPO awards (founders' and 2022 to 2025 long-term incentive awards, settled in
shares at the IPO and expensed only then, $22,775k in Q2 2026, 10-Q note 13) are a real cost of the years in which they were
earned **[L2015-003]** and are spread evenly over the four years; rationale: they were granted for those years and the filer's
historical statements carry none of their cost. CONVENTION of this run: the interest tax shield is taken at 25%, the blended
statutory rate the 424B4 states for HMH Inc. (MD&A, "Income Taxes"); rationale: the filer gives no other single rate, and its
effective rates (32% to 47% in 2023 to 2025) are distorted by valuation allowances and withholding taxes.

**The balance sheets, read before the income account** **[M2025-032]** (read here in Step 0, as the template asks when the file
may close before Q4). $ thousands, from the same filings:

| | 2022-12-31 | 2023-12-31 | 2024-12-31 | 2025-12-31 | 2026-06-30 |
|---|---|---|---|---|---|
| Cash | 47,336 | 62,524 | 48,912 | 96,585 | 119,705 |
| Receivables (incl. related party) | 136,176 | 120,092 | 119,214 | 109,559 | 126,704 |
| Contract assets | 137,958 | 160,933 | 153,150 | 114,918 | 104,622 |
| Inventories | 184,154 | 242,228 | 279,957 | 253,759 | 252,192 |
| PP&E | 217,675 | 214,834 | 198,684 | 200,818 | 197,673 |
| Goodwill | 287,525 | 287,848 | 300,939 | 307,014 | 307,954 |
| Customer relationships and other intangibles | 155,579 | 147,244 | 135,154 | 122,070 | 115,402 |
| Total assets | 1,294,322 | 1,368,418 | 1,381,217 | 1,357,704 | 1,362,565 |
| Accounts payable (incl. related party) | 96,073 | 109,734 | 108,358 | 56,313 | 64,452 |
| Contract liabilities | 57,639 | 75,525 | 55,627 | 35,249 | 42,780 |
| Accrued expenses | 127,444 | 117,923 | 128,420 | 95,780 | 84,964 |
| Debt (bonds, revolver, shareholder loans) | 304,555 | 340,628 | 343,144 | 340,083 | 197,836 |
| Total equity | 567,243 | 593,131 | 631,337 | 700,452 | 846,399 |
| Tangible equity (equity less goodwill and intangibles) | 124,139 | 158,039 | 195,244 | 271,368 | 423,043 |
| Net debt | 257,219 | 278,104 | 294,232 | 243,498 | 78,131 |

What they say. (1) **Most of the asset base is purchase accounting from the 2021 formation**: goodwill and intangibles were
$443M of $1,294M of assets at 2022 and $423M at mid-2026; the intangibles amortize at about $20M to $24M a year, goodwill not
at all. Tangible equity was only $124M at 2022. (2) **Working capital absorbed cash every year**: the cash-flow statements'
working-capital lines sum to **$183M of outflow over 2022 to 2025** against revenue that grew $145M. The balance sheet shows
where: inventories rose from $184M to $254M (27% to 31% of revenue), while payables fell from $96M to $56M, accrued expenses from
$127M to $96M and customer prepayments (contract liabilities) from $58M to $35M. Net income summed $89M over the four years
and depreciation and amortization $160M, yet owner cash before acquisitions summed $54M after interest. This is the
business in which "there’s your profit sitting in the yard" **[M2008-036]**, at least for these four years; the filings
do not say whether the unwinding of formation-date payables and prepayments was a one-time cause. (3) **Debt was flat at
about $340M to the IPO**, refinanced twice (2023 and December 2025, at 103.292% of par for the 2026 bonds), and cut to $198M
with IPO proceeds in April 2026 when the shareholder loans ($137.1M including paid-in-kind interest) were repaid. (4)
**Retained earnings** went from a deficit of $30.1M (2022) to $83.9M (2025); no dividends were paid. (5) Contract assets fell
$46M from 2023 to 2025, and a $12.3M contract asset was written off in 2025 on a customer's cancellation (424B4, MD&A). What
they cannot say: how the business behaves in a deep offshore downturn, since every balance sheet is from 2022 or later.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would own this if the market closed for years **[M1997-109]**; the IPO price of
$20.00 and today's $17.34 say nothing about value, the market "just tells us prices" **[M2006-077]**. Who is paid to tell
you: the prospectus is a selling document written for an offering whose proceeds went mostly to the two Principal
Stockholders (AFTER THE STOP, Q6), with its market forecasts
taken from Rystad Energy, and its own definitions of Adjusted EBITDA, Adjusted ROCE and Free Cash Flow; "you do not get
impartial advice from Wall Street" where fees ride on one answer **[M2020-037]**. No macro enters **[M2000-094]**: the oil
price and the offshore rig forecasts in the prospectus are not used as inputs. Margin of safety: if the case needs pencil and
paper, "it’s too close to think about" **[M1996-084]**. **Contrary evidence, written down as found** **[M1997-127]**: (a) the
filer's own words that in its main market, support of existing rigs, "we must be aggressive on pricing to secure work"
(424B4, Competition); (b) 210 floaters retired from the global fleet since 2010, leaving 173 at end-2025 (424B4, Industry
overview, citing Rystad), which is the installed base on which the aftermarket depends shrinking by more than half; (c)
working capital absorbed $183M over four years; (d) revenue fell 2.6% in FY2025 and 14.9% in the first half of 2026, product
revenue down 53%; (e) material weaknesses in internal control in 2023 and again in 2025 (revenue cutoff in certain
subsidiaries), each reported as remediated (424B4, Risk factors); (f) the rival segments' records over 2014 to 2025 (Q2).

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin: a part-interest bought for cash, unlevered and sized so that a total loss is
survivable, keeps the rule "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**
and "Never risk permanent loss of capital" **[L2023-005]** as conduct of the buyer; no borrowing is involved **[M2004-065]**.
The target's own debt is weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand the economic dynamics of the industry"
  **[M2011-014]**.
- **What the business is, from the filings.** Revenue FY2025 $821.8M: aftermarket services 46.7%, spare parts 27.3%,
  projects and products 26.0%; in the first half of 2026 services and spares were 84.4% (424B4, Summary; 10-Q MD&A). About 75%
  of the installed base of over 1,100 installations serves offshore drilling. The customers are drilling contractors,
  operators and shipyards; the top five took 45.2% of FY2025 revenue (424B4, Risk factors). Two reported segments: PCS
  (pressure control: blowout preventers, controls, risers, wellhead connectors, the Hydril and VetcoGray lines from Baker
  Hughes) and ESS (topside: top drives, drawworks, mud pumps, pipe handling, the MHWirth and Maritime Hydraulics lines).
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) the number of rigs carrying HMH equipment that
  are working, and how hard; (2) whether new rigs are ordered (none for floaters "since 2014", 424B4 Industry overview); (3)
  HMH's share of the aftermarket on its own base, which the filer says is nearly all of it ("once we install equipment we tend
  to generate nearly all of the service revenue", 424B4 Summary), backed for subsea BOPs and risers by regulators in the
  United States and Europe that "mandate regular inspections and certification of the equipment, which are performed by the
  OEM"; (4) the price it gets. Variable (3) is foreseeable over ten years: 72% of the marketed mobile offshore units with its
  systems are younger than 16 years against a working life of 20 to 30 years. Variables (1) and (4) are cyclical: they follow
  offshore drilling spending. The framework places that dependence: "A dependence on a commodity price is never by itself a
  STOP at Q1 or Q2" (Q2, A commodity business), since the speakers "don’t think we can predict commodity prices"
  **[M2016-025]** and decide off the figures all the same **[M2008-069]**.
- **Do the past statements tell me the future ones?** **[M2008-033]** Only in part: four years, all on the rising leg of the
  offshore cycle, and none from the 2015 to 2021 downturn. That weakness bears on whether the castle holds through a cycle
  (Q2) and on the cash estimate (Q7); it does not make the economics opaque. The economic dynamics (an installed base that buys
  certified service and parts from its maker for decades; equipment orders that come only with newbuilds, reactivations and
  upgrades; drilling-contractor customers whose day rates set what they will pay) can be read from the prospectus and the
  rivals' filings, and the competitive position is stated: one of three full-package suppliers with NOV and SLB's Cameron,
  "the second-largest installed base of topside drilling equipment and risers and the third largest installed base within the
  main pressure control equipment categories" (424B4, Competition). The winner is named, not just the industry **[M2012-067]**.
- **How far off could I be** **[M2011-084]**: far on the level of activity in any given year; much less on who services the
  installed base. The forecast that matters is about customers' spending, not about technology: the product changes slowly
  (an electric BOP and a 20,000 psi BOP in development), and the routing to Q1 TOO HARD for fast-moving technology **[M1998-008]**
  does not apply.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. My doubt is
  not about what the business is or how it makes money; it is about how its returns behave through a downturn, which the
  framework asks at Q2 (the field's returns over a full cycle) and Q7, not here.
- **VERDICT: IN.** The economics and the competitive position can be foreseen in the sense of **[M2012-065]** and
  **[M2000-037]**; the cyclical level is carried to Q2 and Q7.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now. What are the key factors? And how permanent are they?" **[M1995-038]**. A moat is what "protects excellent returns
on invested capital" **[L2007-004]**.

**The parts table** (section B of the gaps case; the segment note of each filing). Segment operating income after
depreciation and amortization, $ thousands: for 2022 and 2023 the filer's segment profit (before D&A) less the segment D&A it
states (S-1 `0001193125-24-198984`, note 18); for 2024 and 2025 the filer's own after-D&A measure (424B4 `0001193125-26-138102`,
note 19). The definitions differ slightly between the two filings; both exclude headquarters cost.

| Part | 2022 | 2023 | 2024 | 2025 | 4-yr total | Share | Margin 2022 to 2025 | Decides |
|---|---|---|---|---|---|---|---|---|
| PCS (BOPs, controls, risers; ex-Baker Hughes) | 24,239 | 71,799 | 81,423 | 71,286 | 248,747 | 67.6% | 7.6%, 17.7%, 20.3%, 18.6% | **yes** (more than half) |
| ESS (topside; ex-MHWirth) | 12,072 | 13,641 | 46,133 | 47,496 | 119,342 | 32.4% | 3.4%, 3.6%, 10.4%, 10.8% | no |

Four years, not five, are filed; PCS carries more than half on any span the filings allow, so PCS decides. Its FY2025 revenue
was services $187.6M, spare parts $107.3M and products $88.3M: 77% aftermarket. The file closes on PCS's castle.

**The castle tests, each with its filing fact.**
1. *Key factors and how permanent* **[M1995-038]**. The installed base: "over 1,100 equipment installations", rig packages on
   "more than 140 offshore drilling rigs", BOP aftermarket "for over 25 years, which includes recertification every five
   years"; for subsea BOPs and risers, regulators "mandate regular inspections and certification of the equipment, which are
   performed by the OEM"; "it is uncommon for a customer to engage a third party" (424B4, Summary and Business). That holds as
   long as the rigs work. Against permanence: the base is not being replenished, "there have been effectively no newbuild
   orders for floaters since 2014", and "210 floaters have been retired from the global fleet since 2010, leaving the available
   number of floaters at 173 by year-end 2025" (424B4, Industry overview, citing Rystad). The castle's walls held through the
   last downturn; the land inside them was halved.
2. *Without the lord*: the base does not depend on a manager's genius. Passes.
3. *The money test* **[M2011-015]**: money cannot buy 140 installed rig packages or the regulator's OEM certification; for the
   certified aftermarket on its own base this passes. It is weaker elsewhere: two larger incumbents already hold the bigger BOP
   bases (HMH is third), and the filer's own spare parts "can serve as replacements for, equipment from most other major OEMs"
   (424B4, Summary), which says rivals can do the same to its uncertified parts.
4. *Pricing power and the agony* **[M2005-020]**: against. In its main market, support of existing rigs, "we see a
   particularly competitive environment because our primary customers, drilling rig owners, face highly competitive day rates
   ... therefore, we must be aggressive on pricing to secure work"; and "Most sales of products and projects are awarded on a
   bid basis ... Pricing is one of the primary factors" (424B4, Competition; Risk factors). For: raw-material increases have
   "generally" been passed on "by applying surcharges" (424B4, Raw materials), the sign of a strong position **[M2005-017]**.
5. *Unit volume*: spare-parts revenue fell 9.5% in FY2025 "due to lower spares volume resulting from current market
   conditions"; product revenue fell 53.1% in the first half of 2026 on "a lower backlog to start the quarter"; book-to-bill
   0.9x in FY2025, 1.2x in Q2 2026 (424B4 MD&A and Business; 10-Q MD&A; Ex. 99.1).
6. *The low-cost position*: no filing states unit costs for HMH or its rivals; not testable from what was read.
7. and 8. *The low bid* **[M2017-009]**: for certified BOP service the customer stays with the maker (test 1); for equipment the
   customer takes bids, the commodity mark **[L2004-003]**. Split along the line between aftermarket and products.
9. *Ask the competitors*: the rivals' 10-Ks read (NOV, Nabors) describe their own markets as "highly competitive" and do not
   name HMH; nothing more on the public record that I read.
10. *Widening or narrowing* **[M1999-108]**: HMH's margins widened every year from 2022 to 2024, held in 2025 and rose in the first
   half of 2026 (cost of sales 66.1% of revenue against 73.0%) while revenue fell; all of it on the rising leg of the offshore
   cycle, after cost cutting that the filer names.
11. *What could destroy, modify or reduce it* **[M2000-014]**: a long offshore downturn like 2015 to 2021, which both retires the
   rigs the aftermarket lives on and turns the drilling contractors' "highly competitive day rates" into price pressure on
   their suppliers. Ten to twenty years out, the level of offshore drilling itself.

**The competitor row** (the rivals the 424B4 names, Competition section: "We are, along with NOV Inc. ... and Schlumberger
Limited's Cameron ... the main providers of full equipment packages"; also named: Canrig, owned by Nabors, which files;
Huisman Equipment, KCA Deutag, Worldwide Oilfield Machine, Drillmec, Honghua and Rongsheng, which do not file with the SEC,
flagged). Metric: segment operating margin as each filer reports it. Segment capital was not collected, so this is a margin
comparison, not a return-on-capital one.

| Year | NOV rig segments | Nabors Rig Technologies (Canrig) | SLB Cameron / Production Systems | HMH PCS / total |
|---|---|---|---|---|
| 2014 | 23.4% (Aftermarket alone 29.0%) | not separately reported | (Cameron not yet in SLB) | not formed |
| 2015 | 20.8% (Aftermarket 25.9%) | not separately reported | | not formed |
| 2016 | (19.5)% (Aftermarket 16.2%) | not separately reported | | not formed |
| 2017 | (0.6)% | (13.2)% | 14.3% | not formed |
| 2018 | 8.3% | (9.5)% | 11.8% | not formed |
| 2019 | (19.5)%, 9.7% before other items | (4.3)% | 11.5% | not formed |
| 2020 | (18.9)% | (10.2)% | 9.4% | not formed |
| 2021 | 2.5% | 0.1% | 9.4% | formed 2021-10-01 |
| 2022 | 7.1% | 4.6% | 9.5% | 7.6% / 3.0% |
| 2023 | 12.0%, 10.9% before other items | 8.0% | 12.7% | 17.7% / 9.9% |
| 2024 | (resegmented: Energy Equipment 12.4%) | 10.0% | 15.9% | 20.3% / 14.1% |
| 2025 | (Energy Equipment 10.0%) | 5.4% | 16.4% | 18.6% / 13.1% |

Sources: NOV 10-K FY2016 `0001193125-17-047937` (Rig Systems and Rig Aftermarket, 2014 to 2016), FY2019 `0001564590-20-004552`
(Rig Technologies 2017 to 2019 and its other items), FY2022 `0000950170-23-002767`, FY2023 `0000950170-24-015145`, FY2025
`0001193125-26-048350`; Nabors 10-K FY2019 `0001558370-20-001335`, FY2022 `0001558370-23-001064`, FY2025 `0001104659-26-014997`
(adjusted operating income, Nabors's segment measure, which excludes impairments); SLB 10-K FY2019 `0001564590-20-001578`,
FY2022 `0001564590-23-000762`, FY2025 `0001193125-26-021017` (segment income before charges). NOV's figures are GAAP operating
profit, impairments included except where "before other items" is written. SLB's segments mix drilling equipment with
production, subsea and valve products, so its row is the weakest comparison; NOV's 2024 and 2025 segment mixes rig equipment
with completion and production equipment. HMH total is consolidated operating income over revenue (S-1 and 424B4 income statements).

**The field's returns over the last full cycle, judged in words** (section C). The full-package suppliers' rig businesses earned
excellent margins at the 2014 peak, then for six years, 2016 to 2021, lost money or earned next to nothing at NOV and at Canrig,
and have recovered to high single or low double digits since 2022. That is the record of an equipment field that does not
protect its returns through a downturn. But the evidence splits exactly where HMH's deciding part sits: the one rival record
that separates aftermarket from equipment, NOV's Rig Aftermarket, still earned 16.2% in 2016 on revenue down 56% from 2014,
while NOV's equipment arm lost 40.6%; after 2016 NOV stopped reporting the split. HMH's own record is four years, all on the
rising leg: pre-tax operating income on tangible capital employed (tangible equity plus net debt, year-end) of 5.3%, 17.9%,
24.2% and 21.0% for 2022 to 2025 (on all capital, goodwill included, 2.5% to 12.8%). No filing gives the PCS business's own
record through 2015 to 2021: the 424B4 and the S-1 carry no predecessor statements of Baker Hughes's Subsea Drilling Systems.

**Weighing it.** Not OUT: the evidence that this castle protects only ordinary returns comes from rival segments dominated by
equipment sales, while the closest analogue to the deciding part held its margins into the trough's first year, and the
filer's own returns in its four years are not ordinary. Not IN: no filing shows this business through a downturn; the field's
combined records collapsed in the last one; the filer itself says it must be "aggressive on pricing to secure work" in its main
market; and the installed base on which the aftermarket lives was cut by more than half in the floater fleet by retirements.
Leadership in a rising market "provides no certainties" **[L1996-031]**; a castle whose future cannot be judged is "just too
risky. We don’t know how to valuate that" **[M2000-019]**, and goes to the "too hard" pile **[M2006-013]**. The recent returns,
coming after the field's six bad years, are a change for the better of the kind the rows record ("the railroads were a
terrible business for decades and decades and decades and then they got good" **[M2017-026]**), which the framework credits
"only on the evidence of a full cycle in which the price behaviour held" (Q2, Change, section C). The cause is NATURE: what
decides it is how PCS's prices and margins behave when offshore drilling falls, and only a downturn read from the filings can
answer that, "We couldn't solve this problem, moreover, even if we were to spend years intensely studying those industries"
**[L1993-023]**. A research pass would not reach it: there are no predecessor statements to read.

**The re-look condition, dated.** The framework's condition is "the first fiscal year in which the business's volume or its
field's volume falls, read from the filings". FY2025 already qualifies literally (revenue down 2.6%, spare-parts volume down);
I have read it: PCS margin went from 20.3% to 18.6% and the consolidated cost of sales ratio rose from 67.7% to 70.1% (with a
$12.3M write-off), a dip, not a cycle. The first half of 2026 is deeper (revenue down 14.9%, products down 53.1%) and margins
rose. **Re-look: the FY2026 10-K** (expected by early 2027), read for PCS's and the aftermarket's margins in the year of the
fall; the question is then put again, and again at each later falling year until a full cycle is on file.

- **VERDICT: TOO HARD (NATURE)**, with **[M2000-019]**, **[M2006-013]**, **[L1993-023]**, **[M2017-026]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0, as the template asks; facts found are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Facts found are under AFTER THE STOP (integrity facts recorded, not judged).

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP. The buyback line Q6 would need: no repurchase programme or stated price
was found in the filings read; 254,232 Class A shares were bought into treasury in Q2 2026 for $4,888 thousand (about $19.23 a
share, 10-Q equity statement), a price above the top of the COMPUTATION range below ($14.13); the 10-Q does not say why.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a clearance. The arithmetic is under COMPUTATION, NOT A CLEARANCE below, for the operator's reporting figures.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (No business named in Q12's list is involved: drilling and mining equipment and service.)

---
## THE BOX
**TOO HARD (NATURE), at Q2**: the deciding part (PCS, pressure control, 67.6% of four-year segment profit, 77% aftermarket)
has a real castle in its certified installed base, but no filing shows its returns through an offshore downturn, the field's
rig businesses lost money or earned little from 2016 to 2021, and the filer says it must be "aggressive on pricing to secure
work"; the recent good returns are a change for the better credited only on a full cycle. Re-look: the FY2026 10-K (the first
full fiscal year of the 2026 fall), then each falling year until a full cycle is on file. Integrity facts recorded, not judged.
COMPUTATION beside the box: value $8.53 to $14.13 a share against $17.34; fair price $5.09 (all-equity), equity-only not
positive on the interest filed ($3.58 on today's bonds); no case earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Q2 closed the file. Written down as found **[M1997-127]**; no verdict; the box unchanged, operator rule 2.)*

**Q3 (capital in, capital out).** Pre-tax operating income on tangible capital employed (tangible equity plus net debt at
year-end) 5.3%, 17.9%, 24.2%, 21.0% for 2022 to 2025; with intangible amortization added back 11.0%, 22.5%, 28.2%, 25.7%; on
all capital including formation goodwill 2.5%, 9.0%, 12.8%, 11.4% (Step 0 tables). Capital spending including development
costs was 2.0% to 3.1% of revenue (net $13.9M to $24.1M) against PP&E depreciation of $18.0M to $20.1M a year; the filer
expects $15M to $20M for 2026 (424B4 MD&A). Working capital absorbed $183M over the four years (Step 0). Acquisitions: $3.3M
(2022), Drillform $19.6M (2024), $4.5M (2025), $0.8M (H1 2026, Deep Blue remeasurement); 21.7% of owner cash before purchases
over the window. The strategy names further acquisitions ("a substantial opportunity set of potential acquisition candidates",
424B4 Summary).

**Q4 (the accounts).** (a) Material weaknesses in internal control were identified in Q4 2023 (four: qualified personnel, risk
assessment, IT general and process controls, segregation of duties), reported remediated in 2024; a new material weakness in
2025 over "controls over revenue cutoff, in subsidiaries in certain regions", reported remediated by 2025-12-31 (424B4, Risk
factors). (b) The historical statements carry no stock-based compensation; $22.8M was recognized at the IPO for awards earned in
2022 to 2025, and $18.6M of unrecognized cost remained at 2026-06-30 over 2.52 years (10-Q note 13); an "administrative error"
in the April 2026 grants was trued up with 186,085 RSUs on 2026-05-05 (10-Q Item 5). (c) The filer features Adjusted EBITDA,
Adjusted EBITDA Margin, Adjusted ROCE and Free Cash Flow; in Q2 2026 its reported Free Cash Flow of $22.2M exceeded operating
cash flow of $17.9M because it adds back a $9.5M "Non-cash IPO related settlement" (Ex. 99.1 and the 10-Q reconciliation; the
10-Q lists a $9,541 thousand non-cash settlement of related-party debt against related-party notes receivable). (d) FY2025
carried a $12.3M write-off of a contract asset on a customer's cancellation and a bad-debt provision of $11.1M against $2.0M
in 2024 (424B4 MD&A and cash-flow statement). (e) The revenue lines were re-presented between filings (FY2022 and FY2023 put
spare parts inside service revenue; FY2024 onward show spare parts separately); totals agree. (f) The auditor for FY2021 to
FY2024 was KPMG AS, Oslo; for FY2025 KPMG LLP, Houston. (g) A $16.0M remeasurement of the Step Oiltools receivable was charged
in 2022. (h) The filer says it will stop reporting ESS and PCS as segments in 2026 and report by projects and products,
aftermarket services and spare parts (424B4 MD&A); the parts table above may not be reproducible from later filings.

**Q5 (the people; integrity facts recorded, not judged).** Chief executive Eirik Bergsvik; 2025 total compensation $1.19M
(salary $531K, stock awards $570K), the CFO and the chief administrative officer about $0.87M to $0.88M each (424B4, Summary
compensation table); the pre-IPO awards were dollar-denominated and settled in shares at the IPO, their value set by the
company's value at the liquidity event against its value at grant. The featured adjusted figures in Q4 (c) and the Free Cash
Flow definition are habits the framework weighs at Q4 and judges at Q5. The material weaknesses in Q4 (a) bear on the
framework's "weak accounting where it is visible". No earnings guidance figure was found in the Q2 release read; the release
speaks of "confidence in the opportunities ahead".

**Q6 (the money and the owners).** Of the IPO's net proceeds ($197.8M plus $12.9M from the over-allotment), $39.5M bought B.V.
shares from Baker Hughes and Akastor, $137.1M repaid their shareholder loans (8% interest, paid in kind), $12.9M redeemed
their units in the over-allotment, and $21.2M went to working capital (Ex. 99.1; 10-Q cash-flow statement). A Tax Receivable
Agreement pays the Principal Stockholders 85% of the net cash tax savings HMH Inc. realizes from exchanges and certain tax
attributes (424B4); a TRA liability of $3.8M was recorded in Q2 2026 (10-Q). The Principal Stockholders hold all 31,891,652
Class B shares (about 72% of the vote on the 2026-09-28 count); each may designate two directors while holding at least
8,800,000 shares, and they are permitted to compete with the company (424B4, Summary and Risk factors). The board includes
Baker Hughes's Vice President of Corporate Development and Akastor's chief executive. A resale registration for up to
31,891,652 Class A shares by selling stockholders was filed 2026-09-28. No dividend is intended (424B4, Dividend policy).

**Q9 (debt and exposures).** Debt at 2026-06-30: $200M senior secured bonds, 7.875%, due 2028-12-17, and $1.5M on a China credit
line; a $75M revolver to 2028-06-17, undrawn; covenants on both of minimum liquidity $30M, net borrowings to equity at most 1.0
and Adjusted EBITDA to net interest at least 2.5, with cross-default and a 101% change-of-control put (424B4 MD&A; 10-Q).
Coverage as the rows define it, pre-tax earnings over interest: FY2025 (72.6 + 43.4) / 43.4 = 2.7 times on the old structure;
FY2025 operating income over the bonds' $15.75M a year, about 6.9 times. Operating lease obligations $79.5M (2025). The top
five customers took 45.2% of FY2025 revenue. The products include subsea blowout preventers, whose failure in service is the
kind of single event Q9 asks about; no product-liability claim of size was found in the sections read.

---
## COMPUTATION, NOT A CLEARANCE
*(Q7's arithmetic, done because the operator asks for the two reporting figures; the file closed at Q2, and nothing here is a
verdict or entry language, operator rule 3. Script: `_research 2026-10-16 HMH/q7.py`.)*

**Construction, by Q7's range convention and its specifics.**
- **Cash input:** owner cash all-equity, after every real cost and the company's own tax, before interest, acquisitions
  deducted (Step 0 table): $(7,956)K, $15,444K, $8,687K, $82,534K for 2022 to 2025. **Window: the four filed years**
  (CONVENTION of this run: the framework's five-year average needs five years and four exist; rationale: the window is the
  whole filed record and no year is dropped). **Base, four-year average: $24,677K.**
- **(a) Cycle:** no end year is described by the filer as aberrational; the whole window sits on the rising leg of the
  offshore cycle, so no cycle base can be built from the filings; the literal window is the base.
- **(b) Sign change:** the series changes sign (2022 negative), so growth is measured between the halves: $3,744K (2022 and
  2023) to $45,611K (2024 and 2025), 249% a year, a rate that traces to an absurdity.
- **(f) The cap:** 249% a year carried ten years would require owner cash far above the highest share of sales earned in the
  filings (10.6%, 2025), so growth is cut to the business's own sales growth over the window, 6.66% a year (2022 $677.2M to
  2025 $821.8M), and then to the discount rate, **5.43%**, since the cut rate is never carried above it. Both the shown rate
  and the cut are written here. (Read the other way, the halves rate as "meaningless", specific (b) leaves the no-growth case
  alone, $8.53; the close is the same.)
- **(c) Acquisitions:** deducted, total growth credited (the default pair). Net purchases were 21.7% of owner cash before
  purchases, under half, so the serial-acquirer rule does not apply. The filer reports no organic growth rate, so no organic
  pair is shown. No signed, unclosed deal was found.
- **(d) Working capital:** counted, as the specific requires. No single year's draw is tied by the filer to one contract or
  event.
- **(e) Maintenance:** the filings give no split of capital spending between maintenance and growth, so the all-spending case
  is central. Depreciation variant beside: PP&E depreciation averaged $18,889K against net capital spending of $18,238K, a
  $0.7M difference; immaterial.
- **Rate:** the 30-year Treasury, 5.43% (2026-10-15). Ten years at the growth carried, then zero nominal growth.
- **Net debt** at 2026-06-30: borrowings $197,836K less cash $119,705K = **$78,131K** (10-Q balance sheet; operating leases and
  the $3.8M TRA liability left out, said so). Shares 44,093,153.

**The range.**

| Case | Enterprise value | Per share (less net debt) |
|---|---|---|
| No growth | $454.5M | **$8.53** |
| Growth 5.43% for ten years, then none | $701.2M | **$14.13** |

Width 1.54 to 1. **The floor tested first:** at today's enterprise value ($764.6M market value plus $78.1M net debt, $842.7M)
the expected return is 2.93% on the no-growth case and 4.58% on the growth case; no case earns the floor of about ten percent
(the Q7 CONVENTION, from **[M2003-149]**), and the price ($17.34) sits above the top of the range. Had Q2 passed, Q7 would close
OUT on the floor, whatever the width.

**The two reporting figures** (Part VII, The owner's price and How the fair price is computed; the company's own tax, no
conversion):
- **(a) VALUE RANGE: $8.53 to $14.13 a share**, all-equity, against $17.34.
- **(b) FAIR PRICE: $5.09 a share, all-equity (the central figure)**: each end case valued at ten percent ($246.8M no-growth,
  $358.3M growth), averaged ($302.5M), less net debt, over 44,093,153 shares. **Equity-only, beside:** on owner cash after the
  interest the filer actually bore in 2022 to 2025 (interest expense net of a 25% shield), owner cash averages $(5,248)K and the
  equity-only fair price is **not positive ($(1.46))**; on the interest of today's capital structure ($200M at 7.875%, after the
  25% shield; CONVENTION of this run, since the shareholder loans were repaid in April 2026), **$3.58**.

**Beside, not chosen, so the operator sees what drives it:**
- **Working capital.** The four years absorbed $183M of working capital. Had none been absorbed (owner cash before the
  working-capital lines, average $70.5M), the range would be $27.68 to $43.67 and the fair price $17.83, about today's price.
  The central figure is low because the business consumed cash in inventories and in paying down payables, accruals and
  customer prepayments; whether that continues is what four rising years cannot show.
- **Trailing twelve months to 2026-06-30:** all-equity owner cash $109.0M (operating cash flow $121.0M, helped by the 2025 to
  2026 working-capital swing); on that single base the fair price would be $28.54. A single year does not set the base: "a base
  year in which earnings were poor can produce a breathtaking, but meaningless, growth rate" **[L2005-003]**, and the same
  holds for a year that was rich.
- **Not modelled, each pushing the central figure lower:** US federal tax on HMH Inc.'s share of US income (HMH B.V. is a
  flow-through and its historical statements carry no US federal tax, 424B4 MD&A); public-company costs absent from the
  history; ongoing stock pay (about $7M a year on the $18.6M unrecognized); payments under the TRA.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit daf6111f); written question by question; committed after Step 0 to Q1
      (e2bad7e2), after Q2 (efce3a69), and at the close.
- [x] Dispatched: the brief allowed the per-question commits; the lock was held by the dispatching session; the fold is the
      dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. Declared above: a name filter for "HMH" on the
      `Test Runs/` listing at the start (no match), and the NOV commit subjects seen in the session context, not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in its row (checked by
      `_research 2026-10-16 HMH/check_run.py`); every filing fact has its accession; numbers carry a filing or a CONVENTION label.
- [x] The order was kept; Q2 closed the run; everything after it is facts or COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, from operating cash flow less all capital spending, never a net-income proxy (operator
      rule 5); stock pay deducted though the filer's history omits it; the sovereign from the US Treasury; the price quote flagged.
- [x] Contrary evidence written down as found (Foundations); facts for later questions under AFTER THE STOP, with the integrity
      flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` produced no lines for this filer; no rule, id or verdict from it was used.
- [x] `python tools/check_framework.py` run before the closing commit.
- Honest gaps: four years of statements, not five or ten; the rival comparison is on segment margins, not return on capital;
  SLB's segments and NOV's later segment mix other products; I did not read the Q1 10-Q separately from the six-month 10-Q, nor
  the 8-K of 2026-04-02 beyond its item list; the predecessors' own downturn records (Akastor's Oslo filings for MHWirth, Baker
  Hughes's segment reporting for Subsea Drilling Systems) were not read; for the deciding part (PCS) I found no filing that
  isolates it before 2021.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A newly listed company and the windows.** Q7's range wants five years and Q4 wants eight to ten years of balance sheets;
the text says nothing about a filer with four. I used the four filed years as the window, confessed, and the box did not turn
on it; but a newly listed cyclical will always present a short window on one leg of its cycle, and the range convention then
leans on whatever that leg was. (2) **The re-look condition of the "change for the better" convention is already met by a mild
dip.** "The first fiscal year in which the business's volume or its field's volume falls" was met by FY2025 (revenue down
2.6%); a 2.6% dip is not the test the convention means. I re-read FY2025, said why it is not a cycle, and set the re-look at the
FY2026 10-K; the condition could say what size of fall counts. (3) **The field's returns and a business of parts.** Section C
asks for "the field's returns" from rivals' filings; the rivals report equipment and aftermarket mixed, while the deciding part
here is 77% aftermarket, and the only separated record (NOV, 2014 to 2016) points the other way. The text does not say whether
the field is the rivals' whole segment or the part that matches the deciding part; I read both and let the split send the
castle to TOO HARD rather than OUT. (4) **Working capital dominates the value of a carve-out that spent four years rebuilding
its balance sheet.** Specific (d) counts it, and (a) excuses only a draw tied to one contract or event; a formation-date
unwinding of payables and prepayments is neither, and the fair price moves from $5 to $18 on it. I followed the text and showed
the other figure beside. (5) **An Up-C share count.** The template and Q7 do not say how to count a class with no economic
rights at the issuer but full rights in the operating subsidiary; I counted both classes, as the brief instructs, and stated
the charter facts behind it. (6) **TOO HARD (NATURE) where part of the history is in a non-SEC primary source.** The ESS
predecessor's downturn record is in Akastor's Oslo filings; it does not decide (PCS does), so I did not call the box WORK, but
the text does not say whether a knowable record of a non-deciding part makes a pass worth writing.
