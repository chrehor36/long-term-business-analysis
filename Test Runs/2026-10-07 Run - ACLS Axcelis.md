# Company Run — Axcelis Technologies, Inc. (Nasdaq: ACLS) — 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**Dispatched run.** Brief: `Screens/_daily/_dispatch_brief.md`, slots filled by the dispatching session (lines of evidence:
bookings, backlog and revenue through the last two semiconductor cycles; customer concentration and China's share and its
export-control exposure; gross margin and R&D over the cycle; the installed-base CS&I business; competition and share in
implant; buybacks and their prices; stock pay; working capital and inventory through the downturn; competitors AMAT, LRCX,
KLAC, with Sumitomo Heavy Industries Ion Technology and Nissin Ion Equipment flagged as not SEC filers). The lock in
`Screens/_daily/` was found held by the dispatching interactive session ("2026-10-07 08:33 interactive v5 re-runs batch 1")
when this run started; this analyst did not write or touch it. Research folder: `Test Runs/_research 2026-10-07 ACLS/`.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**The business, and the event that changes what a share is.** Axcelis designs, makes and services ion implanters for chip
fabs; implant was 98.2% of 2025 revenue (10-K FY2025, filed 2026-02-26, accession `0001104659-26-020461`, Item 1). On
2025-09-30 it signed an all-stock merger with Veeco Instruments Inc.: each Veeco share becomes 0.3575 Axcelis share, after
which Axcelis holders own about 58.4% and Veeco holders 41.6% on a fully diluted basis (8-K filed 2025-10-01, accession
`0001104659-25-095307`, Item 1.01). Axcelis holders approved the share issuance on 2026-02-06 (8-K accession
`0001104659-26-011577`, Item 5.07; 24,128,309 for, 1,048,205 against). The only approval still pending is China's State
Administration for Market Regulation, with closing expected "in the second half of 2026" (8-K filed 2026-02-02, accession
`0001104659-26-008916`, Item 8.01; repeated in the 10-Q filed 2026-08-06, accession `0001104659-26-091999`). No 8-K
reporting completion (Item 2.01) appears in the EDGAR index through the 2026-09-16 Form 4s (submissions file read
2026-10-07). No rename. **A share bought today is, if the deal closes, about 58% of Axcelis plus Veeco.**

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $141.15 (close 2026-10-06; aggregator quote via `tools/run.py`, flagged per operator rule 5: live quote only).
- **Shares by class** from the latest filing's cover: one class, common stock $0.001 par, **30,881,489** shares "As of
  August 3, 2026" (10-Q for 2026-06-30, filed 2026-08-06, accession `0001104659-26-091999`, cover; `python
  Screens/cover_shares.py ACLS` returns the same count from the same accession). Checked against issued less treasury: the
  balance sheet shows "30,881 shares issued and outstanding at June 30, 2026"; repurchased shares are retired to authorized
  but unissued, so there is no treasury line (10-Q Note 15). Filings after the 10-Q: one 8-K (2026-08-06, Item 2.02, the
  results release) and Form 4s; no prospectus and no share issuance. The merger shares are not yet issued.
- **Market cap:** $141.15 x 30.881489M = **$4,358.9M**.
- **Net cash at 2026-06-30** (10-Q balance sheet): cash $155.0M + short-term investments $247.2M + long-term investments
  $174.8M = $577.0M, less finance-lease obligation $1.7M current + $39.8M long-term = **$535.5M net cash** (restricted cash
  $10.6M left out; operating leases left out, said so). No bank debt, no notes. The pending merger is a subsequent event the
  filing names but has not closed, so nothing of Veeco is added.
- **Sovereign for the earnings currency:** USD 30-year par yield **5.64%**, 10/06/2026, US Treasury daily par yield curve
  (`python tools/sources.py`, run 2026-10-07).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-26, `0001104659-26-020461`); 10-Q Q2 2026 (filed
  2026-08-06, `0001104659-26-091999`); proxy DEF 14A (filed 2026-03-31, `0001104659-26-037356`); joint proxy
  statement/prospectus 424B3 for the Veeco merger (filed 2025-12-31, `0001104659-25-125599`), Background of the Merger,
  reasons, forecasts and fairness analyses; 8-Ks of 2025-10-01, 2026-01-28, 2026-02-02, 2026-02-06, 2026-03-12, 2026-05-06,
  2026-08-06 and the results releases (Ex. 99.1) for Q4 2024 to Q2 2026; for the cycles, the 10-Ks for FY2003
  (`0001113232-04-000002`), FY2008 (`0001047469-09-003537`), FY2009 (`0001047469-10-002204`), FY2013
  (`0001047469-14-001681`), FY2016 (`0001558370-17-001778`), FY2019 (`0001558370-20-001858`), FY2021
  (`0001558370-22-002096`), FY2023 (`0001558370-24-001628`), FY2024 (`0001558370-25-001855`). Texts saved in the research
  folder.
- **One figure cross-checked against the filed statement:** 2025 revenue $839,048 thousand in the filed income statement and
  revenue note (10-K FY2025, Note 2(b)) against the XBRL figure $839.0M that `tools/run.py` and the companyfacts series use;
  they agree. Interest income 2025 $21,484 thousand and interest expense $5,364 thousand read from the filed income statement.
- `python tools/run.py ACLS` arithmetic lines only (output saved as `run_py_output.txt`): OCF less SBC less all capital
  spending, as filed: 2023 $117.9M, 2024 $107.6M, 2025 $86.2M; with finance-lease principal added to capital spending
  (the alternate): $116.7M, $106.1M, $84.9M. Five-year window (2021 to 2025) on the capex basis: $126.5M. SBC complete in
  the tag shown (AllocatedShareBasedCompensationExpense; 2025 $20.8M). Depreciation and amortization 2025 $17.6M against
  capital spending $11.3M. Nothing else the tool printed is used (Part VII).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this if the market closed for years **[M1997-109]**,
and for this name that test runs straight into the cycle, since what the owner holds through five closed years is a
semiconductor-equipment maker whose revenue fell 18% in 2025 after falling 10% in 2024. No macro forecast enters
**[M2000-094]**; but for Axcelis the largest single variable, China's share of its sales under United States export
controls, is a question of government conduct, and the foundations do not make it one I can answer by refusing to forecast
it. Who is paid to tell you **[M2011-083]**: the only ten-year forecast of this business on the public record was written by
its management for a merger and relied on by the banker paid on the deal; the rows say "we don’t give a hoot about anybody’s
projections" **[M2003-065]**, and to ask for "their past projections" **[M1995-050]**. **Contrary evidence, written down as
found** **[M1997-127]**: (1) the business has been profitable every year since 2015 and kept a gross margin near 45% through
the 2024 to 2025 downturn, which is the strongest evidence that something durable changed after 2016 (written at Step 0,
before Q1); (2) ion implantation has been a step in chip making for decades and the company says it and Applied Materials
"are the only ion implant system manufacturers with a full range of implant products" (10-K FY2025, Item 1), which is
evidence for a standing castle; (3) Axcelis's management did write a ten-year forecast (424B3, "Axcelis Financial
Forecasts", fiscal 2025 to 2034), which cuts against the claim that insiders would not write the forecast down. Each is
answered at Q1, not dropped.

## THE STANDING RULE
Owning a marketable part-interest in Axcelis, unlevered and sized within the buyer's means, puts no demand for sudden large
sums on the buyer; the rule binds the buyer's own financing and sizing **[M2012-081]**, **[M2014-039]**, and nothing in this
file changes that. One line only, as the template asks: no ruin to the buyer from the purchase itself.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test as the text states it.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years" and "how the industry will develop and where the company will stand within the
industry" **[M2012-065]**; "where the business will be in 10 years" **[M2000-037]**. It is not knowing the product: "We just
don’t know the economics of it 10 years from now" **[M2000-104]**. The first step is "trying to identify the key variables in
that particular business, and evaluating how predictable they were" **[M1998-044]**.

**The product is understood.** An implanter fires ionized dopants into a wafer at a set energy and dose; Axcelis sells high
current, medium current and high energy machines on one platform (Purion), plus parts, upgrades and service to an installed
base of "Approximately 3,400" tools (10-K FY2025, Item 1). Understanding the product is not the question **[M2000-104]**.

**The key variables, each with the filing fact.**
1. *The equipment cycle.* Revenue $133.0M (2009), $319.4M (2011), $195.6M (2013), $442.6M (2018), $343.0M (2019),
   $1,130.6M (2023), $839.0M (2025) (selected financial data, 10-Ks FY2013 `0001047469-14-001681`; XBRL first-filed series
   for 2014 on, 10-K FY2025 for 2023 to 2025). The company: "The semiconductor capital equipment industry has historically
   been cyclical" (10-K FY2025, Item 1). The cycle's timing is unknowable but is the least of the four: a cycle average can be
   taken (Q7, specific (a)).
2. *The device mix that sets implant demand.* Power devices "accounted for 55% of the value of our 2025 system shipments"
   (10-K FY2025, Item 1); the company calls 2025 a "continued industry digestion of capacity in our Power and General Mature
   markets" (DEF 14A filed 2026-03-31, `0001104659-26-037356`, CD&A); the Q2 2026 release says "Demand in the Memory market
   remains robust" (Ex. 99.1 to the 8-K of 2026-08-06, `0001104659-26-091697`). Which device families will be built, in which
   wafer material, in which country, ten years out, is a forecast about the customers' technology, not the customers'
   habits **[M2017-019]**.
3. *China's share and the export-control regime.* No filing read gives China's share as a number: the 10-K says China "has
   represented a significant portion of our sales in recent years" and that "Our customers located in China represent a
   significant portion of our revenue" (10-K FY2025, Items 1 and 1A). The regime has changed in 2020 (SMIC on the Entity
   List), October 2022 and 2023 (the equipment framework), December 2024 ("a new Export Controls Classification Number for
   certain 300mm ion implanters") and on 2025-09-29 ("new regulations addressing exports to certain entities in China, which
   potentially impacted Veeco’s and Axcelis’ sales to customers in China", 424B3 `0001104659-25-125599`, Background). The
   company: "We cannot predict whether these policies will continue, or if new policies will be enacted" (10-K FY2025,
   Item 1). The counterparty to the merger treated this as the central unknown: Veeco's board discussed "Axcelis’ reliance on
   a single product and risks surrounding Axcelis’ exposure to the China market" and hired a third-party consultant "to review
   Axcelis’ China business" (424B3, Background, entries of 2024-07-08 and 2024-11-18). The course of that regime is a question
   of what two governments will do; it is important, and it is not knowable **[M2006-076]**.
4. *Share against Applied Materials and the new Chinese makers.* "In the market for ion implantation systems, we mainly
   compete against Applied Materials" and also "Kingstone Semiconductor and CETC Electronics Equipment Group Co., Ltd. in the
   People’s Republic of China. Non-U.S. suppliers may have an advantage over U.S. suppliers under recently established U.S.
   export controls regulation for shipments to China" (10-K FY2025, Item 1). Applied reports no implant figures (its segment
   is Semiconductor Systems), so share cannot be read from either filer. Whether the Chinese makers take the Chinese market
   from Axcelis inside ten years is the winner question the rows say cannot be answered by seeing the industry
   **[M2012-067]**, **[L2009-005]**.

**The tests.**
- *Test 3, do the past statements tell me the future ones* **[M2008-033]**: the same company, in the same step of chip
  making, lost money in total from 2000 to 2016 (net income summed from the selected financial data of the 10-Ks for FY2003
  `0001113232-04-000002`, FY2008 `0001047469-09-003537`, FY2013, and the XBRL series for 2014 to 2016: **minus $284.9M**),
  defaulted on its 4.25% convertible notes due 2009-01-15 and wrote of its "ability to continue in the future as a going
  concern" (10-K FY2008, Items 3 and 7), and then earned **plus $1,089.2M** from 2017 to 2025 (XBRL first-filed series; 2017
  includes an $83.1M tax benefit). Statements read in 2016 would have told an owner nothing about 2017 to 2025, and the rows
  name that case: "sometimes the past doesn’t give you any insights into the future" **[M2007-025]**.
- *Test 5, would the insiders write it down* **[M2000-105]**: the company's own words in the merger document are that
  "Axcelis does not, as a matter of course, normally make public long-term projections [...] given, among other things, the
  unpredictability of the underlying assumptions and estimates inherent in preparing financial projections and forecasts"
  (424B3, Axcelis Financial Forecasts). It wrote one only for the merger (revenue $821M in 2025E rising to $2,302M in 2034E),
  the counterparty's management "made certain adjustments" to it before relying on it (2028E revenue $1,168M against
  Axcelis's own $1,372M), and the counterparty's banker carried
  it only to 2028 and then used a multiple (424B3, Veeco Financial Forecasts for Axcelis; Opinion of Financial Advisor to
  Veeco). The two bankers' discounted-cash-flow ranges for the same Axcelis share barely overlapped: $109.25 to $129.25
  (J.P. Morgan) against $91.91 to $109.93 (UBS) (424B3). A forecast written for a deal by the side issuing the stock is the
  barber's answer **[M2011-083]**, and the rows do not consult it **[M2003-065]**, **[M1995-050]**. In the ordinary course,
  by their own statement, the insiders do not write it down.
- *Test 8, how far off could I be* **[M2011-084]**: on the record above, between a business that loses money for a decade
  and one that earns a quarter of revenue at the operating line (2023 operating margin 23.5%: $265.8M on $1,130.6M).
- *Test 1, where will it be in ten years* **[M2000-037]**: I cannot say whether in 2036 Axcelis sells most of its machines
  into China or none, into silicon carbide or not, against two rivals or five. The filer itself says of its field: "Our
  industry continues to experience rapid technological change, requiring us to frequently introduce new products and
  enhancements" (10-K FY2025, Item 1, Research and Development; the phrase "rapid technological change" is in every 10-K read,
  FY2003 to FY2025), with R&D at 13.0% of 2025 revenue.
- *Test 9, do I doubt it is inside* **[M2002-092]**: yes.

**The contrary evidence written at the foundations, answered.** (1) Nine profitable years and a gross margin held near 45%
through the 2024 to 2025 downturn are real, and they are Q2 and Q3 evidence; they show where the business has been, and the
question here is the ten years ahead **[M2007-025]**. (2) The two-maker full line is evidence about the castle; it is reached
only by a business Q1 passes, and the filer itself says the non-U.S. makers may hold an advantage in its most uncertain
market. (3) The ten-year forecast exists, but it was written for a stock-for-stock deal under a stated disclaimer of
unpredictability, and the side receiving the stock cut it; that is not the insiders writing the forecast down in the course of
business **[M2000-105]**.

**Routing.** This is a business that "must deal with fast-moving technology" and so "is not going to lend itself to reliable
evaluations of its long-term economics" **[L1993-023]**; "where there’s a technological component that’s of significance [...]
it won’t make it through the filter" **[M1998-008]**. The framework's routing sends exactly this case to Q1 TOO HARD, not to
Q2. **The merger, by parts (Q1, A holding company; Q2, A business of parts).** If the deal closes the share becomes a claim on
two parts. Axcelis decides on any measure: its 2021 to 2025 operating profit was $935.0M (sum of the XBRL series) against
Veeco's $290M (Veeco XBRL, OperatingIncomeLoss, 2021 to 2025; Veeco lost money at the operating line every year 2016 to
2019). The deciding part is the part this question cannot see ten years into; the smaller part (MOCVD, laser annealing, ion
beam and wet processing equipment, per the 424B3) is no easier and does not rescue it.

**Which cause.** TOO HARD (NATURE). The deciding question is the ten-year earning power and position of an implant maker
whose demand turns on its customers' device technology and whose Chinese sales, "a significant portion" by its own word, turn on two governments' export policy;
the insiders say in a filed document that they do not make such forecasts "given [...] the unpredictability" (424B3). The
rows say of such fields: "We couldn't solve this problem, moreover, even if we were to spend years intensely studying those industries"
**[L1993-023]** and "Our problem -- which we can't solve by studying up" **[L1999-018]**. The reading for WORK was weighed and
rejected: China's share as a number and the Chinese makers' progress are partly knowable (earnings calls, trade press), and
learning them would close the first fact, not the ten-year forecast; "if we can’t make a decision in five minutes, we can’t
make it in five months" **[M2008-086]**. A pass that ends unsure ends NATURE (section I).

- **VERDICT: TOO HARD (NATURE)** at Q1 **[L1993-023]**, **[M1998-008]**, **[M2000-105]**, **[M2006-076]**, **[M2002-092]**:
  on the filer's own words on rapid technological change and the unpredictability of its long-term forecasts, the 2000 to
  2016 record against 2017 to 2025, and an export-control regime changed in 2020, 2022, 2023, 2024 and 2025 over the Chinese
  sales the filer calls a significant portion of its revenue. It
  is no judgment of quality or price: "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction of
  its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**. The file closes; Q2 onward are NOT REACHED,
  and what was found for them is written below under AFTER THE STOP.

## Q2 to Q10, Q12 — NOT REACHED (Q1 closed the file TOO HARD (NATURE)). Facts found are under AFTER THE STOP.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1** **[L1993-023]**, **[M2000-105]**: the ten-year earning power and position of an
implant maker whose demand turns on its customers' device technology and whose Chinese sales turn on two governments' export
policy cannot be foreseen, by the filer's own account of its field and of its forecasts. Q7 was not reached, so no range is a
finding; the reporting figures below are COMPUTATION, NOT A CLEARANCE: value range (Q7 as built, whole-cycle base) $67.61 to
$188.73 a share, literal five-year window beside it $39.78 to $85.03, against $141.15. **Integrity facts recorded, not
judged** (the Q5 items below: the CEO's and a director's ties to the merger counterparty, a director who was chief executive
of a large Chinese customer, the CFO's resignation after being named CFO of the combined company, a cash bonus paid on
Adjusted EBITDA).

## REPORTING FIGURES, at the owner's request (a reporting convention, not a rule; COMPUTATION, NOT A CLEARANCE)
Built by `Test Runs/_research 2026-10-07 ACLS/q7_computation.py` (output `q7_computation_output.txt`), on Q7's construction
and the Part VI conventions, at the 5.64% Treasury rate. Owner cash each year = operating cash flow less stock pay less all
capital spending less finance-lease principal, from the filed cash-flow statements (XBRL first-filed series; 2023 to 2025
checked against `tools/run.py` and the 10-K FY2025). **All-equity basis (central):** owner cash before interest, that is
less the after-tax net interest income on the cash and securities (interest income $21.5M and interest expense $5.4M in
2025, 10-K FY2025 income statement), at the company's own effective tax rate each year; the value of the business plus net
cash of $535.5M at 2026-06-30, over 30,881,489 shares. **Equity-only beside it:** owner cash after interest, no cash added.
Tax: the company's own; its 2021 to 2025 rates (10.6% to 18.1%) sit below the 21% statutory rate by ongoing deductions and
credits, not by carryforwards that run out inside ten years, so section E's adjustment does not apply (2016 and 2017 were
sheltered by losses carried forward and enter only the prior-cycle average that sets the cycle growth rate).

| Construction | Base owner cash | Ends (growth) | Value range a share | Width (business) | Midpoint | **Fair price** |
|---|---|---|---|---|---|---|
| **Value range as Q7 builds it: whole-cycle base** (specific (a): the window's last year is what the filer calls a "cyclical digestion period", Q4 2024 and Q2 2025 releases, `0001104659-25-010940` and `0001104659-25-073971`), all-equity | $87.6M, average 2019 to 2025 (trough to trough) | 0% and +15.6% | **$67.61 to $188.73** | 3.41 to 1 | $128.17 | **$73.52** |
| same, equity-only | $92.0M | 0% and +15.6% | $52.85 to $180.18 | 3.41 to 1 | $116.52 | $59.06 |
| Literal five-year window 2021 to 2025, all-equity (specific (b): the decline is carried as the bottom) | $117.9M | -14.5% and 0% | $39.78 to $85.03 | 3.02 to 1 | $62.40 | $44.09 |
| same, equity-only | $125.3M | -9.9% and 0% | $33.43 to $71.96 | 2.15 to 1 | $52.70 | $31.00 |

**Fair price, as computed here:** the central case is the year-by-year average of the two ends' cash streams (its value at
the Treasury rate is the midpoint); the fair price is that stream discounted at 10% for ten years and then at no growth,
plus net cash for the all-equity rows. **CONVENTION of this run:** the brief and Part VII define the fair price as "the price
at which the midpoint of the range earns the floor"; a midpoint is a value, not a stream, and this is the reading used;
rationale: it gives the price at which the expected return on the central case equals the floor. **CONVENTION of this run,
the growth cut-back:** the cycle-to-cycle growth of owner cash is 29.2% a year (prior cycle 2016 to 2018 average $24.3M),
which carried ten years gives year-10 owner cash of $1,135M against 2025 revenue of $839M; that traces to an absurdity and
is cut back **[M1999-067]** to the revenue growth between the same cycle averages, 15.6%; rationale: the excess over revenue
growth is margin recovery from near zero, which cannot recur, and the framework gives no figure for the cut. Even cut back it
gives year-10 owner cash of $372M. The top of the whole-cycle range rests on this convention; the bottom does not.

Against the price of $141.15: above the top of the literal-window range, inside the whole-cycle range, and about 1.9 times
the whole-cycle fair price. The whole-cycle range is wider than three to one on the business, which Q7's own convention
would close TOO HARD. No other price figure is reported (brief).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Q1 closed the file. Written down, not weighed **[M1997-127]**; no verdict; the box is unchanged, operator rule 2.)*

**For Q2 (the castle) and the competitor comparison.**
- The implant field, per the filer: Axcelis and Applied Materials are "the only ion implant system manufacturers with a full
  range of implant products"; the others are Sumitomo Heavy Industries Ion Technology and Nissin Ion Equipment (Japan),
  Advanced Ion Beam Technology (Taiwan), Kingstone Semiconductor and CETC Electronics Equipment Group (China) (10-K FY2025,
  Item 1). **Not SEC filers:** Sumitomo Heavy Industries Ion Technology, Nissin Ion Equipment, Advanced Ion Beam Technology,
  Kingstone, CETC; their figures were not read. Applied Materials reports no implant figures (implant sits inside its
  Semiconductor Systems segment), so no implant share can be read from either filer. Implanter prices "range from
  approximately $2.6 million to $12.0 million" (10-K FY2025, Item 1A).
- The competitor row, same metrics from each filer's own XBRL filings (fiscal years labelled by the year of fiscal
  year-end: AMAT October, LRCX and KLAC June; files in `peers/`):

  | Filer (CIK) | Net margin 2009 to 2016 | Net margin 2017 to 2025 | Operating margin 2009 to 2025 | Loss years 2009 to 2025 |
  |---|---|---|---|---|
  | Axcelis (1113232) | **-6.7%** | 17.5% | 12.7% | 2009, 2010, 2012, 2013, 2014 |
  | Applied Materials (6951) | 10.0% | 23.9% | 24.3% | 2009 |
  | Lam Research (707549) | 11.4% | 25.3% | 26.2% | 2009 |
  | KLA (319201) | 16.2% | 29.7% | n/a (tag absent after 2014); net margin 26.4% | 2009 |
  | Veeco (103145), the merger partner | operating loss every year 2013 to 2019 | operating income $23M to $70M a year, 2020 to 2025 | n/a | several |

  Axcelis gross margin: 21.1% (2009), 28.6% (2012), 37.3% (2016), 42.0% (2019), 43.5% (2023), 44.9% (2025); AMAT 48.7% and
  LRCX 48.7% in fiscal 2025. Axcelis R&D: 24.6% of revenue (2009), 12.9% (2016), 8.5% (2022), 13.0% (2025).
- The installed base (CS&I): $170.9M (2007), $143.0M (2008), $120.6M (2013), $127.7M (2016), $162.2M (2018), $140.4M (2019),
  $207.8M (2021), $247.0M (2023), $235.3M (2024), $268.0M (2025), 31.9% of 2025 revenue; "Aftermarket revenue reflects
  current fab utilization" (10-Ks of those years; 10-K FY2025, MD&A). It fell in each downturn, far less than systems.
  Services gross margin was negative in 2025 (-5.1%); product, including parts and upgrades, 47.9% (10-K FY2025, MD&A).
- Backlog including deferred systems revenue: $20.7M (2008), $9.3M (2013), $17.5M (2016), $99.3M (2019), $460.6M (2021),
  $1,211.6M (2023), $645.8M (2024), $457.0M (2025); Q4 bookings $127.6M (2025) against $84.5M (2024); orders "are subject to
  cancellations or rescheduling by customers with limited or no penalties" (10-Ks of those years).
- Customer concentration, top ten share of revenue: 51.5% (2008), 69.1% (2013), 70.2% (2016), 74.1% (2019), 69.5% (2021),
  51.7% (2023), 45.9% (2024), 55.2% (2025); one customer 11.0% in 2025 (10-Ks). China's share: **not stated as a number in any
  filing read** ("a significant portion"); earnings calls were not read (not filings).
- Power devices: 55% of 2025 system shipment value (10-K FY2025).

**For Q3 (capital).** Capital spending is small ($11.3M in 2025 against depreciation and amortization of $17.6M); the capital
is in working capital. Inventory $114M (2016, 43% of revenue), $242M (2022, 26%), $306M (2023, 27%), $329M (2025, 39%),
$338M at 2026-06-30 (`tools/run.py` first-filed XBRL table; 10-Q). Return on the capital needed was not computed.

**For Q4 (the accounts); the balance sheets, read at Step 0 as the brief asks when the file closes before Q4** (ten
year-ends from `tools/run.py`'s first-filed XBRL table, read against the filed 10-K FY2025 and 10-Q balance sheets). Total
assets $302M (2016) to $1,361M (2025); equity $201M to $1,035M; the retained deficit of $332M (2016) turned positive in 2022
and reached $504M (2025), the 2000 to 2016 losses being earned back. No goodwill or purchased intangibles (no acquisitions).
No borrowings; the only debt-like item is a finance-lease obligation of about $41.6M. Cash and securities $577.0M at
2026-06-30. Receivables rose with sales ($51M in 2016, $218M in 2023, $168M in 2025). Inventory rose by $47M in 2025 while
revenue fell 18%, and again in the first half of 2026: a fact for the inventory tell, recorded here, not weighed. The results
releases feature non-GAAP gross, operating and EPS figures and "Adjusted EBITDA" beside GAAP, and give a next-quarter revenue
and EPS outlook (Ex. 99.1, 8-K of 2026-08-06): recorded for Q4's weighing and Q5, not weighed. 2025 general and
administrative expense rose to $83.2M from $70.3M (merger costs not separated in the lines read).

**For Q5 (who runs it): integrity facts recorded, not judged.**
- Russell Low, CEO since May 2023, was a Veeco vice president of engineering 2012 to 2016; Thomas St. Dennis sits on both
  boards and recused himself from every merger discussion; Gerald Blumenstock (EVP R&D) was at Veeco 2011 to 2020 (10-K
  FY2025, Item 1; 424B3, Background).
- Director Tzu-Yin Chiu was CEO of SMIC 2011 to 2017; the 10-K names SMIC as "One of our major Chinese customers" (DEF 14A
  2026, director biographies; 10-K FY2025, Item 1). Elected in 2026 with 97.71% of votes cast (8-K 2026-05-06).
- CFO James Coogan, whom the agreed governance terms named CFO of the combined company and whom the board listed as a
  "Trusted CFO" reason for the merger (424B3), gave notice on 2026-03-10 of his resignation effective 2026-04-24, "to pursue a
  chief financial officer opportunity at a public company in a different industry"; the 8-K says it "did not result from any
  disagreement" (8-K 2026-03-12, `0001104659-26-027104`; DEF 14A 2026).
- The 2025 annual cash bonus was set on "a single metric of Adjusted Earnings Before Interest, Taxes, Depreciation, and
  Amortization"; target pay is aligned to "median compensation in those categories at other companies of a similar size";
  PRSUs on ten operational goals were earned at 112.5% in 2025 (DEF 14A 2026, CD&A).

**For Q6 (the money and the owners).**
- Buybacks and their prices (10-K Item 5 tables): 2021, 1.141M shares at $37.23 to $63.38; 2023, 0.380M shares at $102.49
  to $179.93 ($52.5M); 2024, 0.544M shares at $85.37 to $137.48 ($60.5M); 2025, 1.827M shares at $46.42 to $83.55
  ($121.1M); none in the first half of 2026 (10-Q Note 15). The programme names no price. Against the reporting ranges above
  (computed with today's data, not at the dates of purchase): the 2023 and 2024 prices sit above the top of the
  literal-window range and inside the whole-cycle range; the 2025 prices straddle the bottom of the whole-cycle range.
- Share count: 29.518M (end 2016), 32.048M (end 2017), 33.633M (end 2020), 32.365M (end 2024), 30.717M (end 2025), 30.881M
  (2026-06-30): the $366.8M of buybacks 2019 to 2025 left the count near where stock pay and the 2017 increase had taken it.
- Stock pay: $20.8M in 2025, 2.5% of revenue and about a quarter of 2025 owner cash after it.
- **The merger, an all-stock deal.** Axcelis issues about 41.6% of the combined company for Veeco at an exchange ratio that
  Veeco's board recorded as "an implied premium of 16.7% to the current exchange ratio as of September 26, 2025 and an implied
  premium of 18.8% to the average exchange ratio over the past 30 trading days"; Axcelis's first proposal (October 2024) was
  28% cash; the board listed "the structure of the transaction as all-stock consideration" among its reasons; its own
  banker's discounted-cash-flow range for an Axcelis share was $109.25 to $129.25, when the 52-week range of the price to
  2025-09-29 was $42.42 to $105.10; expected cost synergies "at least $35 million" a year (424B3). Q6's one STOP, the all-stock
  acquisition by a company whose stock sits below its intrinsic value **[L2009-019]**, would need Q7's range at the signing
  date, which was not built; recorded, not judged.

**For Q9 (could it ruin us).** No borrowings; net cash $535.5M. History: default on the 4.25% convertible notes due
2009-01-15 and going-concern language in the 10-K FY2008, cured by selling the SEN joint-venture stake to Sumitomo Heavy
Industries on 2009-03-30. Veeco's convertible debt comes with the merger (424B3, UBS combined-company analysis). The merger
agreement's termination fee: Axcelis's draft proposed 4%, Veeco's draft 3% (424B3, Background); the final figure was not read.

**For Q12.** Nothing found that bears on it.

## WHAT I COULD NOT GET
China's share of revenue as a number (not in any filing read); implant market share (Applied reports no implant figures;
the Japanese, Taiwanese and Chinese makers are not SEC filers); the 2022 buyback prices (the FY2022 10-K was not read); the
final merger termination fee; anything said on earnings calls (not filings).

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the copy preceded the first EDGAR request); written question by question;
      committed after Step 0, after Q1, and after this closing section (write-early).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock was found held by the dispatching session and
      not touched by this analyst. The fold is the dispatcher's (operator rule ten); until it is in the register this run
      binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Contamination, declared and not
      used:** the session's opening context showed the repository's git status and recent commit subjects (they name other
      tickers, a defence-company case, research folders of other names dated 2026-09-26 and 2026-09-27, and a "v5 passers
      list"), the project map, the operator protocol, and a memory index line on queue state and "gate-clearers"; none names
      Axcelis or bears on it. The lock file's one line was read to confirm the lock was held. `tools/run.py` printed only
      arithmetic and its "still owed" checklist; nothing it printed as a rule was used.
      **Seen after the box, by accident:** the `git log` printed after the closing commit showed two commit subjects of a
      parallel run on another company (Applied Materials, a competitor named in the brief), one giving that run's box; it was
      seen after this run's Q1 verdict was committed (`dd80477a`) and was not used.
- [x] Every v5 id resolves (checked by `check_cites.py` in the research folder against `principle_ledger_v5.csv`); every
      filing fact names its document, with the accession at first mention; numbers carry a filing or a CONVENTION label.
- [x] The order was kept; Q1, the first STOP, closed the run; nothing after it is a clearance, and the reporting figures are
      headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay and all capital spending deducted, finance-lease principal included),
      never a net-income proxy; the sovereign from the Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as it was found, at the foundations, and answered at Q1; facts for later questions are
      under AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` run before the final commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **A pending merger has no rule.** Q7's specific (c) values "a deal closed after the window and before the price date" and
   a merger "inside the window", but a signed, shareholder-approved, all-stock merger awaiting one regulator is neither. A
   share bought today is a claim on about 58% of Axcelis plus Veeco if the deal closes, and on Axcelis alone if it does not.
   This run read the business as Axcelis (Q1, and the reporting figures, which add nothing of Veeco) and named the merger at
   Q1 through the parts paragraph; a rule is needed for which business a pending deal makes the subject.
2. **The fair price's definition.** "The price at which the midpoint of the range earns the floor" (Part VII and the brief)
   names a value where a cash stream is needed; the reading used is confessed above as a CONVENTION of this run.
3. **The cut-back of an absurd growth rate has no figure.** Specific (f) says a result that traces to an absurdity "is cut
   back" and gives no level; this run's cycle-to-cycle rate (29.2%) needed one and got a confessed CONVENTION.
4. **Specific (a) and the width rule pull against each other here.** The cycle base that (a) requires gives a range wider
   than three to one, which the width convention closes TOO HARD, while the literal window that (a) sets aside gives a range
   about three to one with the price above its top (OUT). Which governs when they disagree is not said.
5. **Part VII still says "The run template for v5 does not yet exist"**, though `Test Runs/_TEMPLATE - Company Run.md` is
   the v5 template: a stale sentence.

## WHERE THE BRIEF WAS WRONG OR UNCLEAR
The reporting paragraph defines the fair price as the price at which the midpoint "earns the floor of about ten percent
pre-tax" and in the next sentence says "The tax treatment is the company's own tax"; read literally the two clash (a
pre-tax floor against an after-tax cash figure). Q7's "Whose tax" settles it (the floor applies to owner cash after the
company's tax, "pre-tax" meaning before the holder's own tax), and this run followed Q7; the brief should say "after the
company's own tax". The dispatching message names Applied Materials as the rival "which makes implanters" and asks for
competitors "from their own filings over the whole span"; Applied's filings carry no implant figures, so no implant share or
implant margin can be read for any named rival, and the comparison above is necessarily at the level of whole companies.
