# Company Run: AdaptHealth Corp. (NASDAQ: AHCO), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The blind rule of this run forbids opening `PORTFOLIO.md`, so
the analyst does not know whether the operator holds AHCO. Written as for a name not held.

**CONTAMINATION DECLARED.** (1) The git status shown at session start lists file names of other 2026-10-05 runs (ABG,
CAG, WSC) and the recent commit subjects (GIII, HOS, CSW, a small-cap triage screen of S&P SmallCap 600 names, a session
state note). None names AHCO. (2) Listing `Test Runs/` to check for an earlier AHCO file showed the names of other
companies' 2026-10-05 run and research-pass files; none was opened; no AHCO file exists there. (3) The AHCO name may
have come to this run through the small-cap triage screen named in the commit subject of 948fb709; its content was not
read. (4) `tools/run.py` prints v4 rows and a v4 floor; only its arithmetic lines are used (Part VII). Nothing else.

Working folder: `Test Runs/_research 2026-10-05 AHCO/` (filings as text, `run_py_output.txt`, the owner-cash workings).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $5.74 (2026-10-05 intraday, Yahoo chart API, an aggregator, flagged per operator rule 5; `tools/run.py`
  printed $5.76 from its aggregator the same day; last close $5.60 on 2026-10-02). Fifty-two-week range on the same
  aggregator: $5.21 to $13.43.
- **Shares by class** from the latest filing's cover: common stock, par $0.0001, **136,344,196** shares as of 2026-07-31
  (10-Q for the quarter to 2026-06-30, filed 2026-08-04, accession `0001628280-26-052646`; `python Screens/cover_shares.py
  AHCO`). One class of common is listed. The balance sheet also carries 124,060 shares of preferred stock (10-K FY2025,
  accession `0001628280-26-011213`, balance sheet). Read before any per-share figure: they are Series B-1 preferred held
  by Deerfield, "convertible into 12,406,002 shares of Common Stock", and are participating securities in the EPS note
  (same 10-K, risk factors and Note 14). Every per-share figure below therefore uses **148.75M shares** (136.344M common
  plus 12.406M as converted). Unvested RSUs and PSUs are not added (a small understatement of the count, confessed).
- **Market cap:** common only, 136.344M x $5.74 = $782.6M; **with the preferred as converted, 148.75M x $5.74 =
  $853.8M**, the figure used.
- **Sovereign for the earnings currency (USD):** **5.63%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-02 (`tools/run.py`, which reads the Treasury curve, the issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 filed 2026-02-24, accession `0001628280-26-011213`; 10-Q Q2 2026 filed
  2026-08-04, `0001628280-26-052646`; DEF 14A filed 2026-04-28, `0001628280-26-027965` (pay sections); 10-Ks FY2023
  `0001628280-24-007254`, FY2022 `0001628280-23-005590`, FY2021 `0001558370-22-002603` (cash-flow statements,
  impairment, CARES and recall passages); 8-Ks of 2026-09-08 (`0001104659-26-105912`, CFO change), 2026-07-20
  (`0001104659-26-085086`, sale of the diabetes business), 2026-07-07 (`0001104659-26-081305`, note redemption),
  2026-07-02 (`0001104659-26-080297`, Item 1.05 cybersecurity incident), 2023-08-29 (`0001104659-23-096404`),
  2023-09-20 (`0001104659-23-102146`), 2024-07-03 (`0001104659-24-077607`). Fetched into the working folder and not
  read beyond a search: 10-Q Q1 2026 (`0001628280-26-030602`), 10-K FY2024 (`0001628280-25-007740`; its years are
  read through the FY2025 comparatives), 8-K 2026-04-13 (`0001628280-26-024835`; the facility it reports is read in the
  10-Q Q2 2026 debt note).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $601,771
  thousand on the filed cash-flow statement (10-K FY2025, `0001628280-26-011213`); `tools/run.py` prints 601.8 from the
  XBRL. They agree. Also cash capex FY2025, "Purchases of equipment and other fixed assets" (382,388) on the filed
  statement against 382.4 printed.
- `python tools/run.py AHCO`, arithmetic lines only (saved in the working folder): OCF 480.7 / 541.8 / 601.8 (FY2023-25);
  SBC 22.5 / 14.9 / 21.9; cash capex 337.5 / 306.1 / 382.4; D&A 382.8 / 365.4 / 381.9; finance-lease principal 6.8 / 9.9 /
  18.5 (USD millions). The tool's own owner-earnings means are NOT used: they omit the capital that does not pass through
  the capex line (unpaid equipment at year end, equipment taken on finance leases) and the distributions to the
  noncontrolling interest. The recast is at Q4 and in `owner_cash.md` in the working folder.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether "Would I be happy buying this stock if the market closed for five
years?" **[M1997-109]**, and for AHCO the answer turns entirely on the business, since the quotation has fallen from
$13.43 to $5.74 inside a year and "it doesn’t tell us anything. It just tells us prices." **[M2006-077]**. Who is paid
to tell me: the company's key measure is Adjusted EBITDA, which the proxy makes 30% of the 2025 annual bonus and the
10-K says is used "to evaluate acquisition opportunities, where it is most often used for purposes of contingent
consideration arrangements" (10-K FY2025, MD&A, EBITDA definitions; DEF 14A `0001628280-26-027965`); a figure that
both the sellers of businesses and the payees of bonuses are paid on is read as the rows read a paid adviser, "you do
not get impartial advice [...] when there’s (an) enormous amount of fees possible from one action" **[M2020-037]**.
Margin of safety: whatever the arithmetic says at the end, a case that needs pencil and paper is "too close to think
about" **[M1996-084]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) for the business: the company
won a large at-risk capitated contract in Q3 2025 and grew second-quarter 2026 revenue 12.7% (15.9% "organic"), census
rose in PAP resupply and oxygen, and its pre-tax return on tangible assets has run in the low-to-mid teens (Q2 below),
which is not a commodity loser's figure; (2) against it: the same contract cut the Wellness at Home segment's Adjusted
EBITDA margin from 11.5% to 5.4% in the quarter; goodwill was written down in 2023 ($830.8M), 2024 ($13.1M), 2025
($128.0M) and Q2 2026 ($144.2M); two U.S. Attorney civil investigative demands under the False Claims Act are open (2024,
PAP humidifiers; 2025, respiratory devices); a securities class action on diabetes billing and acquired-company
compliance is being settled for $35.0M ($34.0M from insurers); a North Carolina billing class action is to be settled
for $14.5M; a June 2026 data theft is under investigation; the CFO left on 2026-10-01; the diabetes line, 18% of 2025
revenue, is being sold for $235.0M (all from the filings cited in Step 0). Each is placed under the question it bears on.

## THE STANDING RULE
Bought for cash, in a size the buyer can lose entirely without being forced to sell anything else, AHCO cannot ruin
the buyer: the rule binds the buyer's conduct, "We are never going to risk what we have and need for what we don’t have
and don’t need." **[M2012-081]**. With equity of $853.8M standing behind about $2.1B of debt, finance leases and a
tax-receivable obligation, a total loss of the stake is a live outcome of the business, so the rule's other form,
"Never risk permanent loss of capital." **[L2023-005]**, forbids any purchase on borrowed money or of a size whose loss
would matter. No borrowing is contemplated. The rule does not close the file; the target's own debt is Q9's (not
reached).

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**; the product need not be understood if "I
  understand the economic dynamics of the industry. Is there — are there competitive moats? Is there ease of entry?"
  **[M2011-014]**.
- **What the business is, from the filings.** AdaptHealth rents and sells home medical equipment and supplies (PAP
  machines and resupply, oxygen concentrators, home ventilators, hospital beds; CGMs and insulin pumps until the sale
  closes) to about 4.8 million patients a year from about 670 locations (10-Q Q2 2026, MD&A Overview). It is paid by
  insurers, government programs and patients: $1,963.2M, $853.0M and $428.7M of 2025 revenue of $3,244.9M (10-K FY2025,
  revenue by payor type). About a third of revenue is paid as "a fixed monthly amount for certain HME products as
  designated by the Centers for Medicare & Medicaid Services (“CMS”) or commercial insurance payors" (10-K FY2025, Item
  1). Its capital is the equipment placed with patients: patient-equipment depreciation of $341.3M in 2025 sits inside
  cost of revenue (10-K FY2025, cost of revenue). I need not understand the devices, only who sets the price and who
  can enter, which is the petroleum-additives point of **[M2011-014]**.
- **The key variables and whether they are foreseeable** ("trying to identify the key variables in that particular
  business, and evaluating how predictable they were first" **[M1998-044]**): (1) the price, which the payer sets: the
  Medicare fee schedule; the competitive bidding program, resuming with a bid window in late summer or early fall 2026
  and contracts in effect no later than 1 January 2028, this round covering CGMs, insulin pumps, urological and ostomy
  supplies and braces and adding "a Remote Item Delivery competitive model" (10-K FY2025, Item 1, Impact of Competitive
  Bidding); and the commercial and capitated contracts; (2) patient census in sleep apnea and respiratory disease; (3)
  the equipment's cost and supply, bought "primarily from two to three suppliers for each of its product categories"
  (10-K FY2025, Item 1). The direction of (1) is readable in the payer's own documents: the November 2025 OIG-HHS report
  "found that Medicare payments for CGMs and supplies exceeded suppliers’ acquisition costs" and recommended reductions,
  and CMS put CGMs into the bidding (10-K FY2025, risk factors). The level of (1), and the size of the GLP-1 threat to
  (2) that the company names among its risks, cannot be fixed closely; the rows ask for "a reasonable fix", not
  precision.
- **Routing.** This is not an industry of fast technological change; the forecast is about payers and patients, not
  about which device wins (test 7, **[M2017-019]**). The economics are those of a distributor and renter paid at rates
  a third party sets, and that much can be foreseen ten years out: the price will be what the payers decide a supplier
  needs. Whether that leaves an excess return is the castle question.
- **Doubt, recorded.** The size of the GLP-1 effect on sleep-apnea census (Sleep Health was 52.5% of continuing revenue
  in H1 2026; 10-Q Q2 2026) is an important variable I cannot fix; under "if you have doubts about something being into
  your circle of competence, it isn’t" **[M2002-092]** the file could close here. I read that doubt as one threat to the
  castle, which Q2's test 11 asks, not as a failure to understand the business, and pass it on. The other reading is
  recorded in the last section.
- **VERDICT: IN.** The business and its price mechanism are understood; "where the business will be in 10 years"
  **[M2000-037]** is, in shape, a payer-priced service business. The castle is tested next.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now. What are the key factors? And how permanent are they?" **[M1995-038]**

**The castle tests, each with its filing fact.**
- **Who sets the price (test 4).** The customer who pays is not the patient. Medicare and Medicaid fix the rate by fee
  schedule and, product by product, by sealed bid; insurers fix theirs by contract; under capitation the payer fixes a
  per-member fee. The company: "Because payors typically select a limited number of exclusive suppliers, and physicians
  typically refer based on timely delivery and consistency, relationships with both are critical to success in the
  market", and "The rates required to win future competitive bids could continue to depress reimbursement rates" (10-K
  FY2025, Item 1, Competition; Impact of Competitive Bidding). There is no price rise to agonise over, because the
  supplier does not set the price: "whatever he charged for gas was my price" **[M2012-109]**; "he determined our
  profit, because we looked at his price every day" **[M2023-079]**. The measure of strength by "the agony they go
  through in determining whether a price increase can be sustained" **[M2005-020]** cannot even be taken. Costs are not
  passed on: "it is not certain whether AdaptHealth would be able to pass increased costs onto customers to offset
  inflationary pressures" (10-Q Q2 2026, Impact of Inflation).
- **Would the customer still choose it over the low bid (test 8).** The competitive bidding program is a low-bid auction
  run by the largest payer. The See's test asks the opposite, "it wouldn’t be a question of people buying candy for the
  low bid" **[M2017-009]**, and the failing answer is the insurer's, "most insureds don't care from whom they buy"
  **[L2004-003]**. The patient on oxygen or a CPAP does not ask for AdaptHealth by name; the referral source chooses on
  service and the payer chooses the network (10-K FY2025, Competition: "Quality of patient care", "Service quality and
  an efficient, responsive referral process").
- **The payer moves the business at will (test 9, ask the competitors).** Accendra Health (formerly Owens & Minor, owner
  of Apria and Byram) reports in its 10-K for FY2025 (`0001104659-26-018169`) that a commercial payer "has terminated,
  or is in the process of terminating" contracts that "reflected $322 million or 12% of our net revenue, including $231
  million of capitation revenue, which represents nearly all of our capitation revenue", with patients moving to "the
  Payor’s successor provider", and that its 2024 Apria goodwill impairment of $307.1M was due in part to "anticipated
  changes in pricing of a capitated contract". AdaptHealth, in the same months, entered into a capitated contract in Q3
  2025 and paid $127.3M in H1 2026 to "two previous providers in four separate transactions solely to facilitate the
  transition and servicing of the patients related to newly awarded at-risk capitated contracts" (10-Q Q2 2026,
  acquisitions note). Neither filing names the payer and I do not claim the two are the same contract; both show the
  payer, not the provider, deciding where hundreds of millions of revenue go, and the winning provider paying to take it
  on at a lower margin.
- **The money test (test 3).** "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could
  I do it? [...] If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. The company calls its market
  "fragmented and highly competitive", names national, regional and product-specific rivals "as well as numerous other
  smaller local providers", and "non-HME providers, including CVS and Amazon" (10-K FY2025, Competition). Entry needs
  accreditation, licences, payer contracts and delivery routes, all of them purchasable. "Normally, if you’ve got a
  profitable business, you know, a dozen people want to go into it." **[M2000-077]**; here they have, by the hundred.
- **The low-cost position (test 6), the one argument for a castle.** The company's case is scale: "Larger HME providers
  with integrated technology and automated processes are generally better positioned to gain market share and more
  attractive vendor pricing" (10-K FY2025, Competition). The rows admit that route through a commodity field
  **[L2004-007]**, but the evidence does not show AdaptHealth holding it: the largest provider's margin sits below a
  small specialist's (competitor row), its capitated win lowered its margins, and what scale saves goes the way the rows
  describe, "the improvement you get one day, your competitor gets the next day. And it very much tends to work to the
  benefit of consumers but not to increase overall profitability." **[M2004-053]**, here to the payer, who bids it away.
- **Unit volume (test 5).** Census rises: PAP resupply patients and oxygen patients (10-K FY2025, segment discussion;
  10-Q Q2 2026). Rising volume at a price the buyer sets keeps revenue; it does not show a place in the customer's mind.
- **Widening or narrowing (test 10).** Narrowing, on four filed facts. (a) Margins: operating margin before goodwill
  impairment and disposal gains 9.2% (2021), 6.4%, 7.3%, 8.5%, 5.7% (2025); in H1 2026 the three continuing segments'
  Adjusted EBITDA less their own patient-equipment depreciation was $36.0M on $1,420.2M of revenue (2.5%), against
  $87.5M on $1,301.6M (6.7%) a year earlier, with Wellness at Home at minus $23.8M (10-Q Q2 2026, segment tables). (b)
  The company's own fair-value tests: goodwill impaired in 2023, 2024, 2025 and Q2 2026, $1,116.1M in all, the last for
  the Respiratory Health and Wellness at Home units (10-K FY2023 `0001628280-24-007254`; 10-K FY2025; 10-Q Q2 2026). (c)
  The payer moving against a line: the OIG-HHS finding on CGMs, CGMs placed in the bidding, and the company selling the
  line (2025 revenue $592.4M) for $235.0M (8-K 2026-07-20, `0001104659-26-085086`). (d) Revenue at today's scale flat:
  $3,200.2M (2023), $3,261.0M, $3,244.9M (2025), 1.7% organic growth in 2025 offset by disposals (10-K FY2025). "Every
  day, in countless ways, the competitive position of each of our businesses grows either weaker or stronger."
  **[L2005-010]**; here the filed figures say weaker, a notch at a time, as the newspapers "had lost a notch in their
  economic attractiveness" **[L1995-023]**.
- **What could destroy, modify or reduce it (test 11).** "what can happen — say five, 10, 15 years from now — that will
  destroy, or modify, or reduce the economic strengths" **[M2000-014]**: the next bidding rounds (the remote-item-delivery
  model invites national mail-order bidders); payer re-pricing and re-allocation of capitated contracts; GLP-1 drugs on
  sleep-apnea census; the two False Claims Act investigations into PAP and respiratory billing reaching back to 2017 and
  2018. On a government that sets the price, the speakers' own error with utilities: "I did not anticipate or even
  consider the adverse developments in regulatory returns" **[L2023-011]**; and their report on health care, "the
  political power that the industry will have" and "I was somewhat pessimistic going in and I was a little more
  pessimistic when we came out" **[M2025-056]**.
- **Average is terrible and does not leave.** "if you are average, you’re going to have a very poor business. [...]
  average is not going to go away, either." **[M2000-072]**. The competitor row shows the average.

**The competitor row.** Operating income after all depreciation, before goodwill impairment and disposal gains, as a
share of revenue; and the same divided by tangible assets excluding cash, a pre-tax return on tangible assets in the
sense of "you should look at return on tangible assets" **[M2011-060]**. From each filer's XBRL as filed with its 10-K
or 40-F; working in `peers/metrics.py`, output reproduced by running it.

| Company | Years | Operating margin by year (%) | Mean margin | Mean pre-tax return on tangible assets | Filings |
|---|---|---|---|---|---|
| AdaptHealth (AHCO) | 2019-2025 | 5.6, 6.8, 9.2, 6.4, 7.3, 8.5, 5.7 | 7.1% | 12.8% | 10-Ks `0001558370-22-002603`, `0001628280-24-007254`, `0001628280-26-011213` |
| Viemed (VMD), home ventilation | 2018-2025 | 15.6, 10.9, 20.4, 9.9, 5.9, 7.8, 8.0, 8.5 | 10.9% | 16.9% | 10-Ks `0001729149-21-000049`, `0001729149-23-000040`, `0001729149-26-000009` |
| Apria (APR), before its sale to Owens & Minor | 2019-2021 | 2.5, 6.4, 8.5 | 5.8% | 18.7% (2020-21; 2019 assets not tagged) | 10-Ks `0001558370-21-003745`, `0001558370-22-002454` |
| Quipt Home Medical (QIPT), years to 30 Sept | 2023-2025 | 1.3, 0.5, -1.6 | 0.1% | 0.3% | 40-F `0001558370-23-019968`; 10-Ks `0001558370-24-016299`, `0001104659-25-120879` |
| Accendra Health (Apria and Byram), continuing operations | 2023-2025 | 5.2, 3.3, 1.0 | 3.2% | not computed (balance sheet recast by the 2025 divestiture) | 10-K `0001104659-26-018169` |
| Lincare (Linde) | n/a | not reported as a segment by Linde | n/a | n/a | no figure obtained |

Read over the whole span, not one year: no participant earns a high margin; the best is a small ventilation specialist
at about 11% with a COVID year in its mean; the two largest (AdaptHealth; Apria inside Accendra) run between 1% and 9%;
and 2020-21 contain the CARES Act relief years (AdaptHealth recognised grant income in 2020 and 2021; 10-K FY2022
`0001628280-23-005590`). The returns on tangible assets look respectable because the equipment is depreciated fast and
the bought goodwill is set aside, as the row says to do when judging the business; the margin they rest on is the
payer's decision. Two filers in the row wrote down acquired HME goodwill in 2023-26, AdaptHealth four times and
Accendra once, the latter in part for capitated pricing.

- **Shown open, or merely unknown?** The tests are answered by filed facts, not by forecasts: the price is set by the
  buyer by fee schedule, sealed bid and contract; the buyer moves the business between providers; entry is open and
  populated; margins across five providers over the span are thin; AdaptHealth's own margins and fair values are
  falling. That is a castle shown to be open, on the section's OUT list as the business whose price another sets and
  the customer who buys on the low bid, with the payer in the competitor's place. "If the answer had been yes, we
  wouldn’t have done it." **[M2011-015]**; "one competitor is frequently enough to ruin a business" **[M2012-108]**,
  and the one that matters here is the payer. It is not a tenuous moat whose value cannot be judged **[M2000-019]**,
  which would be TOO HARD; there is no moat to judge. Price does not reopen it: "What you can’t do is turn any investment
  into a good deal by paying little" **[M2019-015]**.
- **The strongest case against this verdict, stated as its holder would** **[M1997-127]**: payers want one national
  network, AdaptHealth is the largest, it has just won a large capitated contract, PAP resupply census grows, and a
  pre-tax return on tangible assets near 13% over seven years beats what a commodity business earns. My answer: the
  capitated win came at a lower margin and with $127.3M paid to take it on, which is the low bid winning; the tangible
  return rests on a 7% margin the payer can lower by rule; and the company's own impairment tests have said four times
  in four years that its units are worth less than it paid for them.
- **VERDICT: OUT.** The castle is shown open on the evidence: price set by the payer, patients allocated by the payer,
  open entry, thin margins across the competitor row over the whole span, narrowing on every filed measure
  **[M1995-038]**, **[M2012-109]**, **[L2004-003]**, **[M2011-015]**, **[M2000-072]**. The file closes here. Q3 to Q12
  are NOT REACHED and nothing written below them is a clearance.

---
## Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED (the file closed OUT at Q2).
Facts gathered before the close, recorded and not weighed: capital put into equipment 2021-25 (cash capex, plus the
increase in unpaid equipment at year end, plus equipment taken on finance leases) $1,784.3M against depreciation of
$1,610.0M (D&A less intangible amortization, plus finance-lease right-of-use amortization); in 2023-25, with revenue
flat, $1,149.1M against $1,087.1M, 106% of depreciation; in H1 2026, $306.6M against total D&A of $226.8M as equipment
was bought for the capitated contract. On these figures nearly all capital spending is spending to stand still.
Cash acquisitions 2021-25 $1,710.9M (of which $1,620.3M in 2021) plus $1,261.2M of stock issued for acquisitions in
2021, against five-year owner cash of $364.4M (`owner_cash.md`).

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED as a verdict. The balance sheets are read here because the template asks for them in Step 0 when the file closes before Q4.
**Balance sheets, 2019 to June 2026, before the income account** **[M2025-032]** (USD millions; `tools/run.py` table,
checked against the filed balance sheets of the 10-Ks in Step 0 and the 10-Q Q2 2026):

| Year-end | Assets | Equity | Goodwill + intangibles | Tangible equity | Cash | Receivables (% of revenue) | Debt on the face | Retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2019 | 546 | -15 | 267 | -282 | 77 | 79 (14.9%) | 397 | -27 |
| 2020 | 1,813 | 418 | 1,115 | -697 | 100 | 171 (16.2%) | 785 | -91 |
| 2021 | 5,250 | 2,062 | 3,715 | -1,653 | 150 | 360 (14.7%) | 2,204 | -43 |
| 2022 | 5,220 | 2,151 | 3,708 | -1,557 | 46 | 359 (12.1%) | 2,188 | 26 |
| 2023 | 4,509 | 1,458 | 2,855 | -1,397 | 77 | 389 (12.2%) | 2,148 | -653 |
| 2024 | 4,487 | 1,571 | 2,781 | -1,210 | 110 | 408 (12.5%) | 1,981 | -562 |
| 2025 | 4,317 | 1,519 | 2,626 | -1,107 | 106 | 371 (11.4%) | 1,736 | -633 |
| 2026-06-30 | 4,341 | 1,378 | 2,402 | -1,024 | 43 | 390 | 1,888 | -783 |

What the figures say. (1) The company is the sum of its purchases: goodwill and intangibles went from $267M to $3,715M
in two years (AeroCare and others, 2020-21), paid for with $2.4B of cash acquisitions financed by notes and with $1.4B
of stock (cash-flow statements, 10-K FY2022). (2) Tangible equity has been negative every year; the owners' stake is
the goodwill, and $1,116.1M of it has been written off since 2023. (3) Retained earnings: everything earned since 2019,
and $783M more, is gone by June 2026; the 2022 high of $26M was the only positive year-end. (4) Debt on the face has
run between $1.7B and $2.2B since 2021, about 24 years of the five-year mean owner cash of $72.9M; it rose again to
$1,888M in H1 2026 while cash fell to $43M. (5) Receivables fell
from 15-16% of revenue to 11-12%, which is collection improving, not a tell; inventory is small. (6) The balance sheet
also carries a tax-receivable obligation of $265.7M at 2025 year end ($238.9M after the H1 2026 payment) owed to the
pre-SPAC owners, 85% of the tax savings on the deferred tax asset of $267.8M (10-K FY2025, TRA note; 10-Q Q2 2026).
What they do not say: what the acquired branches are worth, which the impairment tests answer only after the fact.

**The real costs, recorded.** Patient-equipment depreciation ($341.3M in 2025) is the business's main capital cost and
the company leaves it out of its segment measure: "Patient equipment depreciation is not reflected in the segment
measure of profit or loss" (10-K FY2025, segment note). The rows' words for that measure: "The one figure we regard as
utter nonsense is the so-called EBITDA" **[M1998-086]**, and, of exactly this kind of business, "if you compare a
business that, you know, leases pencils or something like that where they all get depreciated in a two-year period and
then compare that to some business that uses virtually no capital, you know, like See’s Candies, it’s just nonsense. But
it works for the people that sell businesses." **[M2012-034]**. Adjusted EBITDA of $616.7M in 2025 against owner cash
of $149.4M. Stock pay $21.9M in 2025, 2.6% of today's market value a year. Recurring "non-recurring" items added back
every year (consulting on systems implementation, asset dispositions, litigation, severance: 10-K FY2025, footnote (g)
to the Adjusted EBITDA table). Two presentation facts a Q4 reader would weigh: "organic" revenue counts the revenue of
patients bought from "previous providers" for $127.3M in H1 2026, because the company excludes those purchases from
"Acquisition" (10-Q Q2 2026, revenue drivers, note (b)); and the method for revenue drivers was changed "Beginning with
the quarter ended September 30, 2025" (10-K FY2025, MD&A). Each is disclosed; neither confused me; on the Q4 two-tell
line they would weigh against, not stop. Not a verdict.

**Owner cash after every real cost** (operator rule 5; `owner_cash.md`; COMPUTATION — NOT A CLEARANCE):

| FY | OCF | Stock pay | Cash capex | Rise in unpaid equipment | Finance-lease equipment | NCI distributions | Owner cash | Depreciation basis | Working capital inside OCF |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | 275.7 | 25.3 | 203.3 | 6.1 | 23.0 | 1.1 | **17.0** | 37.7 | -125.3 |
| 2022 | 373.9 | 22.4 | 391.4 | 10.3 | 1.3 | 2.0 | **-53.6** | 38.3 | -76.8 |
| 2023 | 480.7 | 22.5 | 337.5 | 11.6 | 32.1 | 2.5 | **74.5** | 99.6 | +7.3 |
| 2024 | 541.8 | 14.9 | 306.1 | 20.3 | 17.9 | 5.6 | **177.2** | 167.2 | +6.9 |
| 2025 | 601.8 | 21.9 | 382.4 | 9.8 | 31.4 | 7.0 | **149.4** | 196.0 | +97.7 |
| H1 2026 | 239.0 | 12.1 | 287.5 | 15.8 | 3.3 | 2.3 | **-81.9** | n/a | +15.9 |

Five-year mean **$72.9M** (capex basis), $107.8M (depreciation basis); 2023-25 mean $133.7M. OCF is after cash interest
and cash tax, so owner cash is cash to the equity. The tax-receivable payments ($25.0M in 2025, $26.8M in H1 2026) are
financing outflows and are carried as debt-like below, not deducted twice. 2025 owner cash includes $97.7M of working
capital released; 2021 and 2022 carry the CARES Act recoupments ($36.7M and $12.8M; 10-K FY2022) and a business half
its later size for part of 2021.

## Q5: WHO RUNS IT. NOT REACHED. Facts found, recorded as contrary evidence, not judged.
Chief executive turnover: an interim CEO from 2023-07-01 (8-K `0001104659-23-096404`); a CEO appointed in 2023 whose
employment ended by 2023-09-19 after his former employer sued him (8-K `0001104659-23-102146`); the co-founder President resigned
in July 2024 (8-K `0001104659-24-077607`); the present CEO's agreement is dated 2024-04-10 (DEF 14A); the CFO left
2026-10-01 (8-K `0001104659-26-105912`). Two False Claims Act civil investigative demands (2024, 2025), a securities
class action on diabetes billing and compliance at acquired companies (settlement $35.0M), three derivative suits, one
alleging insider trading, a North Carolina billing class action ($14.5M) (10-K FY2025, legal proceedings). The 2025
bonus plan "added Net Revenue and removed Compliance as performance metrics" (DEF 14A 2026, note to the bonus table)
while the investigations were open. Had Q5 been reached, the integrity STOP is applied on doubt alone.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED. Facts found, recorded.
Acquisitions for stock and cash at the 2020-21 prices, $1,116.1M of the goodwill since written off; shares issued for
cash in 2020 and 2021 (cash-flow statements, 10-K FY2022); buybacks of $14.0M in 2022 at about $18.63 a share and $29.3M
in 2023 at about $9.19 (shares and dollars from the statements of equity and cash flows, 10-K FY2023 and FY2025), the
first well above, the second near, the bottom of the computed range below. Pay: CEO total compensation of $10,256,240
for 2025 (DEF 14A, pay-ratio section); bonus 40% net revenue, 30% Adjusted EBITDA, 30% free cash flow, with an "Approved"
Adjusted EBITDA of $631.2M used for the payout against $616.7M reported (DEF 14A, bonus table).

## Q7: WHAT IS IT WORTH. NOT REACHED. See the reporting section below (COMPUTATION — NOT A CLEARANCE).
## Q8: BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9: COULD IT RUIN US. NOT REACHED. Facts recorded: debt $1,887.9M at 2026-06-30 ($325M term loan at 5.00%, $150M
revolver drawn, the 4.625% notes due 2029 and 5.125% notes due 2030, the 6.125% 2028 notes refinanced on 2026-08-03 by a
$325M delayed-draw term loan), a springing maturity on the 2031 credit facility 91 days before the 2029 and 2030 notes
if more than $150M of either remains, revolver headroom under the covenants $265.7M (10-Q Q2 2026, debt note and market
risk); finance leases $44.8M; the tax-receivable obligation; the open FCA investigations; the data incident.
## Q10: THE FAT PITCH. NOT REACHED.
## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED. Not one of the named businesses. Fact
recorded for a later reader: the money is made under government and insurer payment, and the open matters are billing
matters (PAP humidifiers, respiratory devices, diabetes billing, North Carolina billing after equipment returns).

---
## REPORTING AT THE OWNER'S REQUEST (not a rule change). COMPUTATION — NOT A CLEARANCE. The file closed OUT at Q2; none of these figures is entry language, and a price does not reopen a castle shown open.
**Construction (the Q7 CONVENTION as written):** five-year mean owner cash after every real cost, capex basis,
$72.9M; carried at the growth shown for ten years, then no growth (zero nominal), discounted at 5.63%. The growth shown
on aggregate owner cash, $17.0M (2021) to $149.4M (2025), is from a depressed base year, the case of "a base year in
which earnings were poor can produce a breathtaking, but meaningless, growth rate" **[L2005-003]**; it is capped, as Q3's
arithmetic requires, at the only growth the filings show at today's scale, the 1.7% organic revenue growth of 2025
(CONVENTION of this run: rationale, the owner-cash rate traces to an absurdity and revenue at today's scale grew 0.7% a
year 2023-25, so the stated organic rate is the most generous figure the filings support). Bridge to the equity:
owner cash is already after interest, so the present value is the equity's; less the tax-receivable obligation
($238.9M), plus the diabetes sale price ($235.0M, before tax and escrow, closing expected Q1 2027); 148.75M shares.

- **(a) VALUE RANGE (convention):** **$8.68** (no growth) **to $9.93** (1.7% for ten years) a share, against **$5.74**.
  Width 1.14 to 1. Depreciation-basis variant beside it: $12.84 to $14.70.
- **Whole-cycle variants, because the window holds abnormal years** (2021 half-size with CARES recoupment; 2022 CARES
  recoupment and the Philips supply shortage; 2025's $97.7M working-capital release): the five years with working
  capital held neutral (base $90.9M), $10.83 at no growth; the three years at today's scale, 2023-25 (base $133.7M),
  $15.94 to $18.24. **And the variant the latest filing forces:** H1 2026 owner cash was minus $81.9M, so a base that
  admitted the current run rate would give a range with no bottom. At Q7 that would be the TOO HARD case, "the range
  must be so wide that no useful conclusion can be reached" **[L2000-025]**, which is reported, not applied.
- **(b) FAIR PRICE: about $6.55 a share.** The price at or below which the central case clears the floor of about 10%
  pre-tax (the Q7 CONVENTION, from "we don’t want to buy equities where our real expectancy is below 10 percent"
  **[M2003-149]**). Tax treatment: owner cash is after cash tax; cash taxes paid averaged $16.6M in 2021-25 (10-K
  supplemental disclosures), so pre-tax owner cash is $89.5M. Central case: the midpoint of the convention's two growth
  ends, 0.85%. Expected pre-tax return at price P = 89.5 / (148.75 x P + 3.9) + 0.85%; it equals 10% at P = $6.55 (the
  $3.9M is the tax-receivable obligation less the diabetes proceeds). At no growth the fair price is $5.99; at 1.7%,
  $7.35. The price, $5.74, sits just below the central fair price and above the no-growth one: a case for a pencil.
- **(c) CHEAP PRICE: below about $4.34 a share.** Rule (CONVENTION of this run): half the bottom of the convention
  range, so that the price is "a big discount from that present value calculated using the risk-free interest rate"
  **[M1997-126]** and needs no pencil **[M2009-005]**. Rationale: the rows ask for a margin that "ought to just kind of
  scream at you" **[M1996-084]** and give no number; half of the bottom is ours. Even there, the Q2 close stands and the
  H1 2026 run rate would still leave the cash stream unestimated.
- **What the arithmetic leaves out, and which way it leans:** it discounts cash to an equity behind about $2.1B of
  debt-like claims at the government rate (the convention's rate, applied as written); it uses a five-year mean the
  latest half-year does not support; it assumes the payers leave today's margins in place; it puts nothing in for the
  FCA investigations, the derivative suits or the data incident. Each of these leans the true figure lower.

---
## THE BOX
**OUT at Q2.** The castle is shown open on the evidence: the payer sets the price and allocates the patients, entry is
open, margins across five home-medical-equipment providers are thin over the whole span, and AdaptHealth's own margins
and fair values are falling. Not reached Q7; the reported computation, labelled as such, puts a convention range of
$8.68 to $9.93 (whole-cycle variants $10.83 to $18.24, and no bottom on the latest half-year) beside a price of $5.74,
with a fair price of about $6.55 and a cheap price below about $4.34. No research pass is opened: the close is OUT, not
TOO HARD (WORK).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. *Not committed after each: the
      instruction for this run forbids commits; written to disk early instead (Step 0 first, then the foundations to
      Q2, then the rest).*
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, with every quoted fragment beside an
      id found in that row); every filing fact has its accession; no number without a row, a filing or a CONVENTION
      label.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; nothing after it is a clearance, and every
      later figure is headed COMPUTATION — NOT A CLEARANCE or recorded as a fact not weighed.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): stock pay, all capital including
      unpaid and lease-financed equipment, NCI distributions; the sovereign from the US Treasury; aggregator quotes
      flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations, and the strongest case against
      the Q2 verdict).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): this is a run of today; not applicable.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its v4 rows, floor and owner-earnings means
      were not.
- [x] `python tools/check_framework.py` PASS before the commit (no commit made; result recorded in the reply).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Who is the customer when a government pays?** Q2's tests are written for a customer who chooses (the low bid,
the brand, the share of mind); here the payer chooses the price and the supplier, the referral source chooses the
provider within the network, and the patient chooses nothing. I applied the gas-station rows (**[M2012-109]**,
**[M2023-079]**) with the payer in the competitor's place and the insurer row (**[L2004-003]**) for the customer's
indifference; the text has no row that names a government or a payer as the price-setter, and a reader could object
that the gas-station rows are about a rival. Q12's prompt, as given for this run, mentioned "government payment", but
Q12's text names no such case. A sentence in Q2 saying how a third-party payer is read would settle it. (2) **Q1 and a
large unforecastable threat that is not technology.** GLP-1 drugs may shrink the sleep-apnea census; that is neither
"fast-moving technology" **[L1993-023]** in this industry nor an absence of understanding. The routing rule sends fast change to Q1 TOO
HARD and the threat test to Q2; I sent it to Q2, but the doubt row (**[M2002-092]**) could close the file at Q1 instead.
The box would differ (TOO HARD against OUT), the outcome would not. (3) **The Q7 convention's growth input from a
depressed base.** The convention takes "the growth the business has actually shown", but aggregate owner cash grew
from $17.0M to $149.4M in four years, an absurd rate from a poor base year; the cap ("no rate that runs past the discount
rate or traces to an absurdity") says what not to use, not what to use instead. I used the stated organic revenue
growth and confessed it. (4) **The convention's five-year window when the latest half-year breaks it.** H1 2026 owner
cash was negative; the convention has no rule for a run rate that falls outside the window, and the arithmetic gives a
value well above a price the market has nearly halved. I reported the variant and said which way it leans; a rule on
whether the latest interim period may set the bottom of the range is missing. (5) **Levered owner cash at the
government rate.** Owner cash is after interest, so the convention discounts an equity stream behind $2.1B of claims at
the risk-free rate; the rows keep risk out of the rate and in the margin **[M1997-126]**, but for a heavily indebted
equity that puts the whole burden on the cheap-price rule, which the framework leaves to each run. (6) **The template
asks for a commit after each question**, which this run's instruction forbade; the line was ticked with the deviation
stated.
