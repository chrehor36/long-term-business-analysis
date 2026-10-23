# Company Run: Eversource Energy (NYSE: ES), 2026-10-23
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template to this dated name before any
fetch (write-early).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session, 2026-10-23, after the run was committed (5411dc6c): `PORTFOLIO.md` read for this one ticker; **not held**.*

**Contamination, declared and not used.** (1) The session's opening context carried the repository's recent commit subjects,
which name another company's v5 re-run, its box and its figures; another company's file, not opened, not used. (2) The
project map and the memory index loaded with the session carry general queue lines (counts of passers, owed reviews); none
names this company; not used. (3) A directory listing of `Screens/` and `tools/` made at the start showed file names only
(among them the passers list, the resume-state files and the run queue); none was opened or searched. No file about this
company under any name or ticker was opened, listed or searched.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $67.84 (close 2026-10-22; aggregator quote through `tools/run.py`, flagged per operator rule 5: live quote only).
- **Shares by class** from the latest filing's cover: **376,674,754** Eversource common shares, as of 2026-07-31 (10-Q for
  the quarter ended 2026-06-30, filed 2026-08-03, accession `0001628280-26-051906`; `python Screens/cover_shares.py ES`).
  The cover's three other lines (6,035,205; 200; 301) are the common shares of the co-registrants CL&P, NSTAR Electric and
  PSNH, all held by Eversource (the 10-Q's CL&P equity statement shows 6,035,205 shares at 2026-06-30); they are not added.
  Check: issued 383.144M less treasury gives the balance-sheet count 376.598M at 2026-06-30; the 10-Q reports 289,044 ATM
  shares issued in the second quarter of 2026 under the $1.2B at-the-market programme, which may add a small number after
  the cover date. No 8-K or prospectus after the 10-Q that changes the count was found among the 8-Ks listed below.
- **Market cap:** $25,554M (376.675M x $67.84).
- **Sovereign for the earnings currency (USD):** 5.29%, the 30-year par yield of the US Treasury daily par yield curve,
  2026-10-22 (issuing authority, read by `tools/run.py`).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-17, accession `0001628280-26-008461` (Items 1, 1A, 7,
  the consolidated statements, the segment note); 10-Q for Q2 2026, filed 2026-08-03, `0001628280-26-051906` (balance
  sheet, FERC ROE note, offshore wind note, equity issuance); proxy (DEF 14A) filed 2026-03-27, `0001104659-26-036077`
  (CD&A, summary compensation table, the independent-chair proposal); 8-Ks of 2026-07-30 (`0001104659-26-088698`, Q2
  results, wrapper only), 2026-07-01 (`0001104659-26-079426`, Aquarion sale closed), 2026-03-31 (`0001104659-26-037912`,
  FERC ROE decision), 2026-02-26 (`0001104659-26-020565`, $1.5B junior subordinated notes), 2025-11-24
  (`0001104659-25-115105`, PURA denial of the Aquarion sale, wrapper only), 2025-10-14 (`0001104659-25-098981`, offshore
  wind liability). For the span: 10-K FY2023 (`0000072741-24-000005`), FY2022 (`0000072741-23-000004`), FY2020
  (`0000072741-21-000005`) for the cash-flow statements 2018 to 2023 and the segment earnings 2020 to 2022.
  **Cross-checks against the filed statements:** operating cash flow 2025, $4,113,572 thousand on the filed statement of
  cash flows, against 4,114 in `tools/run.py`; common shareholders' equity at 2025-12-31, $16,197,271 thousand on the filed
  balance sheet, against 16,197 in the run.py table.
- `python tools/run.py ES` arithmetic lines only (saved in `Test Runs/_research 2026-10-23 ES/run_py.txt`): owner cash on the
  capex basis 2023 -2,718, 2024 -2,351, 2025 -79 (three-year mean -1,716; five-year -1,493); on its D&A basis 313, 353,
  1,675 (five-year 733), USD millions. Two corrections to the tool's lines, from the filings: its "D&A" is the filed
  depreciation plus regulatory amortization (2025: 2,404.5 against filed depreciation of 1,568.6), so its D&A basis is not
  a maintenance guess; and its debt table's column d5 (LiabilitiesOtherThanLongtermDebtNoncurrent) is not debt, so its
  "sum" overstates debt; the debt used below is read from the filed balance sheets. SBC from the filings: 28.2, 33.4, 27.8,
  30.0, 33.6 (2021 to 2025); finance-lease principal 4.1 to 5.7 a year, added to capital spending.

**The lines of evidence this name needs, derived from Items 1, 1A and 7 of the FY2025 10-K** (chosen by the analyst under
the brief): (1) the parts: four reportable segments (electric distribution, electric transmission, natural gas
distribution, water), whose earnings decide which castle is read (Item 1, Item 7 segment table); (2) the returns the
regulators allow and the climate they set: FERC's transmission ROE (four complaints since 2011, decided 2026-03-19), the
state commissions' ROEs and equity ratios, Connecticut's PURA, which Item 1A names ("We continue to monitor the evolving
regulatory environment in Connecticut, including changes in the composition of PURA"); (3) the capital: $26.51B of
projected capital spending 2026 to 2030, funded by debt and equity issuance (Item 7, Liquidity); (4) the ventures outside
the castle: the offshore wind losses and the contingent liability to GIP, and the Aquarion sale (Item 1A, "Offshore Wind
Contingent Liability and Tax Risk"; Item 7); (5) the accounts: regulatory deferrals that swing operating cash, and the
non-GAAP earnings the MD&A leads with; (6) credit: ratings, outlooks and maturities (Item 7, Liquidity).

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the market as servant: a regulated wires company is priced daily on its
"earnings guidance" and its dividend, and the analyst's job is to ask only whether "the price is out of line where the
facts and reasoning lead you" **[M2006-077]**, and whether one would be "happy buying this stock if the market closed for
five years" **[M1997-109]**; for a business whose return is set by commissions, that question is answered by the
commissions' record and the cash the business throws off after it reinvests, not by the quotation. No macro view enters;
interest rates enter only through the sovereign at Q7. **Contrary evidence, written down as found** **[M1997-127]**:
(1) owner cash after all capital spending was negative in every year 2021 to 2025 (five-year average -1,560M after the
company's own tax adjustment below), so the dividend and growth have been paid from new debt and new shares; (2) the
offshore wind losses, presented as excluded items, recurred in 2023, 2024, 2025 and again in Q2 2026 (a further $194M
pre-tax charge, 10-Q `0001628280-26-051906`); (3) FERC cut the transmission base ROE from 10.57% to 9.57% on 2026-03-19
and the 10-Q estimates reasonably possible refunds of $62.0M to $968.4M pre-tax; (4) PURA denied the Aquarion sale in
November 2025 before a court remanded it; (5) retained earnings rose only from $3.18B to $4.50B from 2016 to 2025 while
long-term debt rose from $8.8B to $26.9B.

## THE STANDING RULE
Owning a part-interest bought for cash puts the buyer at no risk of ruin; the rule binds the buyer's financing and sizing,
"never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**, and "borrowed money has
no place in the investor's tool kit" **[L2014-005]**. Nothing in this name changes that; the target's own debt is weighed
at Q9.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test, applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**, "a reasonable probability of being able to asses where the business will
  be in 10 years" **[M2000-037]**. The filing describes a holding company "engaged primarily in the energy delivery
  business" through wholly owned regulated utilities: CL&P (about 1.32 million customers, Connecticut), NSTAR Electric
  (about 1.62 million, Massachusetts), PSNH (about 549,000, New Hampshire), three gas utilities, and New England
  transmission with an estimated rate base of about $11.3B at the end of 2025 (10-K `0001628280-26-008461`, Item 1). None
  of the electric utilities owns generation for its customers; supply is a pass-through that "does not earn a return on
  the cost of electricity", and customer migration to other suppliers "has no impact on" the distribution business's
  operating income (Item 1). The water business, Aquarion, was sold on 2026-06-30 (8-K `0001104659-26-079426`); the offshore
  wind interests were sold in 2024 and survive only as a contingent liability (10-Q `0001628280-26-051906`).
- **The key variables** **[M1998-044]**: (1) the rate base, which grows with the capital the commissions let in; (2) the
  allowed return on equity and the equity ratio (PSNH 9.5% on 50% equity, Yankee Gas 9.32% on 53%, FERC transmission base
  9.57% since 2026-03-19); (3) the timing of cost recovery (decoupling, trackers, deferrals, prudency reviews); (4) the
  political climate in the three states, Connecticut above all. Each is stated in the filings, and each is knowable and
  important **[M2006-076]**; none is a technology forecast. The pull against: the 10-K's own risk factor says regulators
  may respond to affordability by "delaying or denying rate increases or cost recovery", and the speakers' own utility
  lesson is that "the regulatory climate in a few states" made it "difficult to project both earnings and asset values"
  **[L2023-011]**. That is a risk to the level of the return, which Q2, Q3 and Q7 weigh; it does not put the ten-year shape
  of the business (wires, pipes, rate base, an allowed return) out of sight.
- **Routing.** Not a fast-changing industry; not a bank; a holding company read by its parts (Q2's parts table): each part
  that decides (transmission, electric distribution) is a regulated wires business whose economics are written in its
  tariffs and orders.
- **VERDICT: IN.** The economics ten years out can be foreseen in shape: a regulated delivery monopoly whose earnings are
  rate base times an allowed return **[M2012-065]**, **[M1998-044]**; the regulatory level is carried to Q2.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (segment net income attributable to common shareholders as filed, GAAP, USD millions; 10-K FY2025 for
2023 to 2025, 10-K FY2022 `0000072741-23-000004` for 2021 and 2022). *CONVENTION of this run: segment net income stands in
for "operating profit", because it is the segment measure the filer reports for all five years; rationale: the segment
note gives operating income only for the latest three years, and the ranking is the same on either measure in 2025
(transmission 1,176.7 operating income, electric distribution 986.5, gas 534.8, water 67.1).*

| part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year | share | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| Electric transmission (FERC) | 544.6 | 596.6 | 643.4 | 724.6 | 776.7 | 3,285.9 | 44% | regulated wires monopoly in ISO-NE; return set by FERC | **yes, the largest part** |
| Electric distribution (CT, MA, NH) | 470.1 | 592.8 | 608.0 | 631.7 | 667.1 | 2,969.7 | 40% | retail franchise; return set by PURA, DPU, NHPUC | no (second; read as well) |
| Natural gas distribution | 204.8 | 234.2 | 224.8 | 291.0 | 360.5 | 1,315.3 | 18% | retail franchise | no |
| Water (Aquarion, sold 2026-06-30) | 36.8 | 36.8 | 33.1 | -253.7 | 44.2 | -102.8 | n/m | sold | no |

2021 distribution includes the CL&P settlement charge of $86.1M after tax; 2024 water includes the $298.3M loss on the
pending sale. No part carries more than half; transmission, the largest, decides, and distribution, nearly as large, is
read beside it because the two are owned by the same three companies and share their capital.

**The castle tests, on the deciding part, each with its filing fact.**
- *The key factors, and how permanent* **[M1995-038]**: transmission rates are set under "a FERC-approved formula
  ratemaking framework" with an annual true-up of actual costs and an allowed ROE, collected from New England wholesale
  customers; rate base "primarily consists of our investment in transmission net utility plant less accumulated deferred
  income taxes" (10-K Item 1). The lines exist, are interconnected under ISO-NE, and nobody else may duplicate them for the
  same service.
- *The attacker with money* **[M2011-015]**: no one can build a second set of lines to the same substations and be paid
  for them. The opening is on new projects: the 10-K warns that competitive solicitations under ISO-NE's Longer-Term
  Transmission Planning "may require us to compete against non-incumbent developers" (Item 1A). The existing castle stands;
  part of its growth may be contested.
- *Pricing power and the agony before a rise*: none in the speakers' sense; the price is the regulator's. FERC set the base
  ROE at 9.57% (from 10.57%) in Opinion No. 594 of 2026-03-19, applied prospectively from 2014-10-16, with refunds; the
  company calls the decision arbitrary and has sought rehearing, a stay, and a Section 205 increase to 11.39%, which FERC
  suspended to 2026-11-30 subject to refund (8-K `0001104659-26-037912`; 10-Q). The 8-K puts the prospective cut at about
  $70M of after-tax earnings for 2026.
- *Unit volume and share of mind; the brand; the low bid*: not applicable to a wires monopoly; the customer has no choice of
  wires, and migration to other energy suppliers "has no impact on" distribution operating income (Item 1).
- *Widening or narrowing* **[M1999-108]**: the franchise is unchanged; what has narrowed is the return the regulators allow
  and the climate in which it is set. In Connecticut a 2023 law prohibits the reauthorization of CL&P's ESI capital tracker
  in its next rate case (Item 1); PURA denied the Aquarion sale on 2025-11-19 on managerial-suitability grounds before the
  Superior Court sustained the appeal (Item 7); PURA set Yankee Gas at 9.32% net with disallowances of capitalized overheads
  (Item 7). In New Hampshire the Department of Energy has appealed PSNH's 2025 rate order (Item 7).
- *What could destroy, modify or reduce it* **[M2000-014]**: the regulatory climate, which the speakers name as the moat that
  broke at their own utilities, "I did not anticipate or even consider the adverse developments in regulatory returns"
  **[L2023-011]**; competitive solicitation of new transmission; storms whose costs a commission disallows; and the 10-K's
  risk factor on new technology and alternative energy sources (distributed generation, storage). None removes the wires.

**The competitor row.** The 10-K names no rival company; its only competitors are unnamed "non-incumbent developers" for new
transmission. *CONVENTION of this run: the comparators are the New England transmission owners that file with the SEC,
Unitil (NH and MA distribution, a small transmission owner) and Avangrid (Connecticut's United Illuminating among its
Networks utilities, and Eversource's co-movant against the FERC order, 10-Q); rationale: they share the regulators and the
FERC ROE proceedings. Flagged: National Grid's New England utilities, the region's other large transmission owner, were not
found filing a 10-K and were not read; Avangrid's last 10-K found is for FY2023, and its consolidated figures include a
renewables business Eversource no longer has.* Metric: GAAP net income to common over average common equity (XBRL
companyfacts transcription of each filer's 10-Ks, `Test Runs/_research 2026-10-23 ES/comp_roe.txt`; one figure each
cross-checked to the filed statement: Unitil 2025 net income applicable to common shares $50.2M, 10-K
`0001193125-26-042983`; Avangrid 2023 net income attributable $786M, of which Networks $726M, 10-K
`0001634997-24-000031`).

| year | ES | Unitil | Avangrid |
|---|---|---|---|
| 2016 | 8.9% | 9.4% | 4.2% |
| 2017 | 9.1% | 9.2% | 2.5% |
| 2018 | 9.2% | 9.6% | 3.9% |
| 2019 | 7.5% | 12.1% | 4.4% |
| 2020 | 9.0% | 8.4% | 3.8% |
| 2021 | 8.5% | 8.6% | 4.1% |
| 2022 | 9.3% | 9.0% | 4.6% |
| 2023 | -3.0% | 9.4% | n/a |
| 2024 | 5.6% | 9.4% | n/a |
| 2025 | 10.8% | 8.9% | n/a |
| span | 7.4% | 9.4% (2016-25) | 4.0% (2016-22) |

**The field's returns over the last full cycle, judged in words.** The regulated field earns about what its commissions
allow, high single digits on book equity, in every year of the span for the pure regulated filer; Eversource fell below it
only through losses outside the castle (offshore wind in 2023 and 2024, Aquarion in 2024). That is a return set by a
regulator, the exception the framework names and carries to Q3 as a second best: "there’s no way we get rich on our utility
investments. But there’s no way we get poor, either" **[M2009-104]**, accepted where the business can expect "decent returns
on the incremental sums they invest" **[L2009-012]**. The castle does not protect "excellent returns on invested capital"
**[L2007-004]**; it protects allowed ones, and at FERC the allowed one has just been cut.

- **VERDICT: IN**, on the deciding parts: the transmission and distribution franchises stand on the evidence, and no attacker
  can take the existing wires **[M2011-015]**, **[M1995-038]**; the return they protect is the regulator's, carried to Q3 as
  a second best **[M2009-104]**, **[L2009-012]**; the regulatory climate, the castle's one real enemy here **[L2023-011]**,
  is carried to Q3, Q7 and Q9. The castle is not open, and its future is judged: a regulated return whose level is the
  uncertainty, not its existence.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed.** The allowed returns are on equity of about half the regulated capital (PSNH
  9.5% on a 50% equity ratio; Yankee Gas 9.32% on 53%; FERC base 9.57% since March 2026), and the regulated segments earned
  about that: GAAP return on average common equity 8.5% to 9.3% in 2016 to 2022 and 10.8% in 2025, with the holding
  company's own leverage helping (Q2 table). Over the whole decade the company earned 7.4% on its equity, because $2.8B of
  after-tax losses (offshore wind 2023 to 2025, Aquarion 2024) were taken on capital put outside the castle (10-K FY2025,
  Item 7 reconciliation).
- **Reinvestment to stand still and to grow.** Capital spending ran 3,175 to 4,481 a year in 2021 to 2025 against
  depreciation of 1,103 to 1,569 (filed cash-flow statements), and the projection for 2026 to 2030 is $26.51B, about $5.3B a
  year (Item 7). The filer's own categories for distribution spending in 2023 to 2025 put "Basic Business" and "Aging
  Infrastructure" (meters, vehicles, replacement of overhead lines, cable, cast iron and bare steel main) at 85.7% of the
  total and "Load Growth and Other" at 14.3% (Item 7 table): most of the spending replaces and hardens what exists, and the
  regulator lets it into rate base, so earnings grow because capital is added, not because more is sold. The speakers name
  the shape: of utilities, "To earn more, their owners must invest more" **[L2011-019]**, and "we have tried to avoid places
  where there was a lot of compulsory reinvestment just in order to stand still" **[M1997-016]**. Owner cash after all
  capital spending, before any credit for debt, was negative in every year 2021 to 2025 (Q7 table); the dividend was paid
  from borrowing and new shares.
- **What the added capital earned.** From 2020 to 2025 debt and common equity together rose from about $31.5B to $46.3B
  (+$14.8B; filed balance sheets, debt lines read as filed), while non-GAAP earnings rose by about $530M (1,237.3 to 1,767.4, 10-K FY2022 and FY2025) and after-tax
  interest by about $557M (interest expense 538.5 to 1,243.3 at a 21% federal rate, a CONVENTION of this run: the statutory
  federal rate, the filer's effective rate swinging from -58.1% to 34.1% in the window): about 7.3% after tax, before
  financing, on the added capital. Decent, not rich, and only on the capital that stayed inside the castle. The speakers'
  test of a capital-heavy business is the "decent returns on the incremental sums they invest" **[L2009-012]**; their own
  utility admits the arithmetic plainly, "we’re not earning a higher rate of return on capital than we were when we
  started. We just put way more capital into the business" **[M2023-081]**.
- **The growth arithmetic and its caps.** Revenue grew 8.3% a year 2021 to 2025 and regulated non-GAAP earnings 8.3% a year,
  carried by rate base; no rate is carried past the discount rate after year ten (Q7).
- **WEIGHS AGAINST.** A second-best business by the speakers' own grading, "as the second-best choice, still a good choice"
  **[M2018-055]**, whose added capital earns a regulated, decent return **[L2009-012]**, **[M2009-104]**, but which must keep
  putting capital in to stand still **[L2011-019]**, **[M1997-016]**, throws off no cash after its spending, and whose record
  on capital put outside the regulated castle is a loss of $2.8B after tax. (The "little or no debt" criterion is applied at
  Q9.)

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them, before the income account** **[M2025-032]** (USD millions; `tools/run.py`'s
  first-filed XBRL table, accessions in `run_py.txt`; 2025 equity and retained earnings checked to the filed balance sheet;
  revenue from the filed income statements):

| year-end | total assets | common equity | goodwill | cash | receivables | LT debt (noncurrent) | retained earnings | revenue |
|---|---|---|---|---|---|---|---|---|
| 2016 | 32,053 | 10,712 | 3,519 | 107 | 847 | 8,829 | 3,175 | 7,639 |
| 2017 | 36,220 | 11,086 | 4,427 | 86 | 925 | 11,776 | 3,561 | 7,752 |
| 2018 | 38,241 | 11,487 | 4,427 | 209 | 994 | 12,249 | 3,954 | 8,448 |
| 2019 | 41,124 | 12,630 | 4,427 | 117 | 989 | 13,771 | 4,177 | 8,527 |
| 2020 | 46,100 | 14,064 | 4,446 | 265 | 1,196 | 15,126 | 4,613 | 8,904 |
| 2021 | 48,492 | 14,600 | 4,477 | 67 | 1,226 | 17,024 | 5,005 | 9,863 |
| 2022 | 53,231 | 15,473 | 4,523 | 375 | 1,517 | 19,724 | 5,527 | 12,289 |
| 2023 | 55,612 | 14,174 | 4,532 | 54 | 1,432 | 23,589 | 4,143 | 11,911 |
| 2024 | 59,595 | 15,039 | 3,571 | 27 | 1,651 | 25,702 | 3,929 | 11,901 |
| 2025 | 63,787 | 16,197 | 4,234 | 135 | 1,847 | 26,872 | 4,505 | 13,547 |

  **What moved and why.** Assets doubled. Long-term debt tripled (8.8B to 26.9B), and at 2026-06-30 total borrowings were
  $29.81B (notes payable 393.7, current long-term debt 2,502.6, current rate reduction bonds 43.2, long-term debt 26,609.0,
  rate reduction bonds 259.3; 10-Q). Common equity rose $5.5B, but about $3.4B of that is new shares (issuance proceeds
  852 in 2019, 929 in 2020, 197 in 2022, 989 in 2024, 465 in 2025, filed cash-flow statements; shares outstanding 316.9M
  in January 2017 to 376.7M in July 2026, 10-K covers and the latest 10-Q); retained earnings rose only from 3,175 to 4,505
  in nine years and fell by 1,384 in 2023 with the offshore wind impairment. Goodwill rose with the Aquarion purchase
  (2017), fell with its 2024 impairment and held-for-sale reclassification, returned in 2025 when the sale was blocked, and
  stood at 3,571 after the sale closed (10-Q). Cash is kept near nothing; the business runs on commercial paper and the
  debt markets. Receivables grew faster than revenue (11.1% of revenue in 2016, 13.6% in 2025), and regulatory assets stood
  at $7.69B against regulatory liabilities of $5.54B at the end of 2025 (10-K regulatory note): costs already paid and not
  yet collected from customers. What the figures "don’t say" **[M2025-032]**: how much of the $7.69B the commissions will
  in the end allow.
- **The real costs.** Depreciation is real **[L2015-004]**, and here it is not even the maintenance figure: the filer's own
  replacement categories (basic business plus aging infrastructure) in distribution alone exceeded total depreciation in
  2023 to 2025 (2,494, 2,632, 2,710 against 1,306, 1,434, 1,569; 10-K Item 7 and cash-flow statement). The speakers say
  the shortfall is subtracted, "merely spending their depreciation expense will not keep them in the same place"
  **[M2016-092]**. Stock pay is small (28 to 34 a year) and counted. Operating cash swings with regulatory timing: the filer
  says 2025's $4.11B was "favorably impacted by an improvement in regulatory recoveries driven primarily by the timing of
  collections" (Item 7), after under-recoveries of 919 in 2024 and 152 in 2023 (cash-flow statements).
- **The recurring "one-time".** After-tax charges excluded from the featured earnings: offshore wind 1,953 (2023), 524
  (2024), 75 (2025) and a further 194 pre-tax in Q2 2026; Aquarion 298 (2024) and about 115 (2026, 8-K
  `0001104659-26-079426`); Northern Pass land 6.9 (2023), after a Northern Pass impairment of 240 pre-tax in 2019 (10-K
  FY2020 cash-flow statement); CL&P settlement 86 (2021). Every year of the window carries one.
- **EBITDA in the filer's own mouth:** no instance found in the FY2025 10-K, the Q2 2026 10-Q or the 2026 proxy (text search
  for "EBITDA"). **The featured adjusted figure and guidance:** the MD&A's first earnings line after GAAP is "non-GAAP
  earnings" of $4.76 a share excluding the offshore wind charge, with a 2026 "earning guidance range" and a "long-term EPS
  growth rate through 2030" of 5 to 7 percent (Item 7; revised in the 8-K of 2026-03-31 to $4.57 to $4.72); the annual
  bonus is paid on the same non-GAAP EPS (proxy). These are recorded here as a WEIGHING against and carried to Q5: "a
  management that regularly attempts to wave away very real costs by highlighting "adjusted per-share earnings" makes us
  nervous" **[L2016-006]**; "the scourge of earnings "guidance"" **[L2019-006]**; "a negative", but not "a total
  exclusionary factor" **[M1994-018]**.
- **Confusion or suspicion?** The regulatory accounting is intricate but explained: each deferral, each recovery and each
  excluded charge is reconciled in the filing to GAAP, and the losses are booked, not hidden. No prepaid or deferred account
  building without explanation, no reserve released into earnings, no profit on both sides of a contract was found in the
  statements read. Not confusion **[M1995-063]**, not obfuscation **[M2003-029]**.
- **VERDICT on the accounts: WEIGHS AGAINST**, with ids: the accounts are readable and the real costs are stated
  **[M2025-032]**, **[L2015-004]**, but depreciation understates the spending needed to stand still **[M2016-092]**, a charge
  excluded as non-recurring appears in every year of the window, and the adjusted figure and guidance are featured and paid
  on **[L2016-006]**, **[L2019-006]**, **[M1994-018]**; carried to Q5. The recast earnings for Q7: owner cash from the filed
  cash-flow statements after all spending, with the maintenance case at depreciation (generous by the filer's own
  categories) and the filer's categories beside.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**. *How well they run the business, against the hand dealt:* the regulated
  utilities earned about their allowed returns and grew rate base, as Unitil did on the same regulators' terms (Q2 table);
  the hand was a set of monopolies. What the managers chose to do beyond the hand was the offshore wind venture, an
  unregulated construction business in which Eversource invested from 2018 to 2024 (investments in unconsolidated
  affiliates 205 in 2018 rising to 1,680 in 2023, filed cash-flow statements) and on which it has now booked after-tax
  losses of 2,552 for 2023 to 2025 plus a further 194 pre-tax in Q2 2026, with a contingent liability of 409.2 still owed to
  the buyer at 2026-06-30 (10-Q). Aquarion was bought in 2017 and sold in 2026 at a cumulative loss (298 in 2024, about 115
  in 2026). In Connecticut, CL&P paid a storm performance penalty and customer credits under PURA's 2021 decisions (10-K
  FY2022, 86.1 after tax in 2021), and the company's relations with PURA run through appeals and remands (Q2). Credit: the
  parent is rated BBB / Baa2 / BBB with Moody's and Fitch outlooks negative (10-K Item 7). *How well they treat their
  owners:* Q6.
- **The tells of dishonesty, sought.** The losses were booked and disclosed in full, reconciled line by line to GAAP, and
  the 10-K states the cost overruns, the stop-work orders and the revised GIP projections that drove them (Item 7). No
  instance found, in the 10-K, the 10-Q or the proxy, of a reserve moved to meet a number, figures changed after the fact,
  or a report that dances around the key figure. How they talk about mistakes **[L2024-003]**: the filings call the venture
  "our previous offshore wind investments"; no instance of the words "mistake" or "wrong" applied to it was found (text
  search of the 10-K, the 10-Q and the proxy for "mistake"); the proxy's word for the share price is "disappointing".
- **The habits carried from Q4, read with the integrity record.** The annual bonus is paid on non-GAAP EPS that excludes the
  offshore wind charges, so the managers' own largest capital decision does not touch their bonus metric, and the 2025
  result "exceeding the earnings goal of $4.71 per share by $0.05 per share" is reported with the same exclusion (proxy);
  guidance is issued yearly and revised on events. These are the tells the speakers call a reason for nervousness and a
  culture risk **[L2016-006]**, **[L2019-006]**, and "things that they do in public in relation to their investors and the
  promises they make" **[M2004-067]**. Against them, read with the rest of the record: the long-term performance shares for
  2023 to 2025 vested at 44% of target on bottom-quartile shareholder return, the committee states it "took into
  consideration the loss from our previous offshore wind investments", and from 2026 the performance shares are capped at
  target when three-year shareholder return is negative (proxy). The record shows a management that featured an adjusted
  figure, not one that hid a cost. Doubt on honesty, on the evidence read: none found that the evidence supports; the doubt
  is on judgment, which is ability.
- **Love of the business.** For a hired management of a public utility, read in what they asked for: the venture away from
  the wires, then the retreat to the wires after it failed (the 10-K now describes the business as "engaged primarily in the
  energy delivery business"). No instance found of conduct that reads as love of the money over
  the business beyond the pay itself (CEO total compensation 2025 $14,987,168, summary compensation table, proxy).
- **VERDICT on integrity: IN** (no instance of dishonesty found in the filings read; the featured adjusted figure and the
  guidance are weighed against, not treated as proof of character) **[M2013-088]** applied: the doubt that the record raises
  is about judgment, not honesty. **Ability WEIGHS AGAINST** **[M1994-008]**: the regulated hand was played to its allowed
  return, and the capital put outside it lost about $2.8B after tax; the chairman is also the chief executive and the board
  opposes separating the roles (proxy, Item 4), the structure of the speakers' warning, "how hard it is to replace a mediocre CEO if that person is also Chairman"
  **[L2014-026]**.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test** **[R1995-009]**, **[M1998-110]**. From 2016 to 2025 net income to common totalled 9,765 and
  common dividends 7,894 (filed statements; XBRL transcription checked against the 2023 and 2025 filed cash-flow
  statements), so 1,871 was retained, while 3,433 of new common equity was raised. Book value per share went from $33.80
  (10,712 over 316.9M shares) to $43.13 (16,197 over 375.5M): $9.33 a share of book added against $5.90 a share retained
  and new money put in at the market. In cash terms nothing was retained at all: owner cash after all capital spending was
  negative in every year 2021 to 2025 (Q7 table) while 4,679 of dividends were paid, so each dividend was in effect paid
  from new debt and new shares. The market leg of the test was not read from a filing; the proxy records three-year
  shareholder return 2023 to 2025 "in the bottom quartile". The forward question, whether the business can keep using all
  the capital it generates, is answered by the filer: it plans $26.51B of spending in five years, more than it generates.
- **Buybacks.** None; the company is an issuer (shares 316.9M to 376.7M; the $1.2B at-the-market programme of 2025 still in
  use in Q2 2026, 10-Q). The buyback test against the bottom of the Q7 range has no purchases to read; the line is written
  back from Q7 below.
- **Issuance and deals** **[M1995-001]**. Shares were issued in 2019, 2020, 2022, 2024, 2025 and 2026: a steady issuer to fund
  a spending plan the commissions approve, which the speakers name among the warning signs, "we have never invested in
  companies that are hell-bent on issuing shares" **[L2014-015]** (carried in section VI of the framework as a candidate
  second STOP, unresolved; weighed here). The deals: Aquarion bought for cash in 2017 and sold for $2.4B in cash in 2026 at
  a cumulative loss; the Columbia Gas of Massachusetts assets bought for 1,113 in cash in 2020 (10-K FY2020 cash-flow
  statement); the offshore wind stakes built from 2018 and sold in 2024 at a loss that is still growing. No all-stock deal:
  the one STOP of Part A does not arise.
- **Part B, the pay, the board and the owners.** The annual bonus rides on non-GAAP EPS that leaves out the offshore wind
  charges, the result of the managers' own capital decision, and its EPS component paid out at 155% of target for 2025 (proxy); the long-term
  plan pays on "recurring" EPS growth and relative shareholder return. "you get what you reward for" **[M2016-083]**: a
  metric that omits the losses on the managers' own venture rewards the venture's upside and spares its downside, the
  pattern the speakers call "heads I win, tails you lose" **[L1994-020]**. Partly against that: the 2023 to 2025 performance
  shares vested at 44% of target, and from 2026 they are capped at target when absolute three-year return is negative
  (proxy). Pay tied "to what is actually under the reasonable control of the person" **[M2003-019]**: EPS growth largely is,
  relative shareholder return is not. The chairman is the chief executive, and the board recommended against the 2026
  independent-chair proposal (proxy, Item 4).
- **Buyback line, written back from Q7 and committed with it:** no shares were repurchased in the window, so no price paid
  can be read against the bottom of the Q7 range (equity-only, central, $71.73 a share). Recorded, not weighed further: the
  new shares of 2024, 2025 and Q2 2026 were sold at about $62.86, $65.27 and $69.89 (proceeds over new shares, filed equity
  statements and 10-Q), below the bottom of that range and above the fair price of $37.58.
- **WEIGHS AGAINST.** Part A: retention adds book value but no cash, dividends are funded by issuance and debt, and the capital
  allocated outside the regulated castle lost about $2.8B after tax **[R1995-009]**, **[M1998-110]**, **[L2014-015]**. Part B:
  pay rides on an adjusted figure that excludes the managers' own losses **[L1994-020]**, **[M2016-083]**, with the
  2026 cap and the low 2023 to 2025 vesting in its favour; chairman and chief executive combined.

## Q7: WHAT IS IT WORTH? STOP.
**The basis.** The deciding parts earn a return a regulator allows on invested capital, "when you get an allowed return in
the electric utility you’re almost certain of earning it" **[M2010-037]**, so Q7's central figure is the equity-only basis,
the exception the all-equity sentence carries in itself for "the fixed-asset commitments at our regulated utilities"
**[L2017-012]**: owner cash after interest and the company's own tax, against the market value of the shares, with the
long-term debt raised over the window credited against the capital spending it funded, up to the debt share the regulator
allows. The filing states allowed equity ratios of 50% (PSNH) and 53% (Yankee Gas) and none for the other utilities; the
debt share used is **50%**, the larger debt share stated (the business's own debt share of capital at 2025-12-31, about 65%
on the filed lines, includes the holding company's borrowing and is not used). Net long-term debt raised 2021 to 2025
(issuance less retirements and rate reduction bond repayments, filed cash-flow statements) was 12,025, above the cap of 50%
of all capital spending, 9,808, so the cap binds. All-equity beside.

**Owner cash by year** (USD millions; filed cash-flow statements; arithmetic in `Test Runs/_research 2026-10-23 ES/q7.py`,
output `q7_out.txt`). Base = operating cash flow less stock pay less subsidiary preferred dividends (7.5), with cash taxes in
2024 and 2025 raised to the 2021 to 2023 average paid (79.6). *CONVENTION of this run, under Q7's Whose tax: the filer
received net tax refunds in 2024 and 2025 (cash taxes -69.6 and -48.4) after the offshore wind losses, a shelter that ends
with them; the base is computed as if the ordinary cash tax had been paid, and no shelter value is added, since the shelter
was realised inside the window.* Capital spending includes finance-lease principal. The offshore wind investments and
receipts (net outflow of 1,927 over 2021 to 2025) are left out of the base, a part sold in 2024 that will not recur; the
liability still owed for it is deducted below. *CONVENTION of this run; rationale: the base is meant to show what the
business now owned throws off; the venture's cost is not forgotten, it is weighed at Q3, Q5 and Q6.*

| year | base | all spending | all spending + debt credit | maintenance case M | equity-funded growth spending G |
|---|---|---|---|---|---|
| 2021 | 1,926.9 | -1,252.3 | 337.3 | 1,375.4 | 1,038.1 |
| 2022 | 2,360.4 | -1,085.4 | 637.5 | 1,763.3 | 1,125.8 |
| 2023 | 1,610.9 | -2,729.8 | -559.4 | 958.0 | 1,517.4 |
| 2024 | 1,973.0 | -2,512.7 | -269.8 | 1,256.3 | 1,526.1 |
| 2025 | 3,944.5 | -219.9 | 1,862.3 | 3,160.2 | 1,297.9 |
| five-year average | 2,363.1 | -1,560.0 | 401.6 | 1,702.6 | 1,301.1 |

M = base less the maintenance spending plus the debt credit on that spending; G = spending above maintenance, the
equity-funded half. **The maintenance guess (specific (e)):** depreciation, the speakers' proxy for required spending
**[M1998-127]**; it is generous here, because the filer's own replacement categories exceed it (Q4), "merely spending their
depreciation expense will not keep them in the same place" **[M2016-092]**, so the filer-category guess is shown beside.

**The specifics, applied.** (a) *Cycles:* 2025 is aberrational on the filer's own description ("favorably impacted by an
improvement in regulatory recoveries driven primarily by the timing of collections", Item 7) and 2023 to 2024 carried the
under-recoveries it collected; the five-year average spans the deferral and its collection and stands as the base
**[L2005-003]**, and the growth is measured between the averages of successive five-year spans (M 1,495 in 2016 to 2020,
1,703 in 2021 to 2025, filed figures): **2.63% a year**. The literal window's growth, between its halves, is 12.06% and is
shown beside; it counts the 2025 collection as growth. (b) *Decline:* none. (c) *Acquisitions:* none inside the window
(the Columbia Gas assets were bought in 2020, inside the earlier span, so the 2.63% overstates organic growth slightly);
the Aquarion sale closed after the window and before the price date and is valued on its own filed record: its 2025 net
income 44.2 and depreciation 46.8 are taken out of M (67.6 after the debt credit) and its equity-funded growth spending
out of G (59.3), and the $1.7B of adjusted net equity proceeds the 8-K says "will be used to displace Eversource Energy
debt" is added (8-K `0001104659-26-079426`). (d) *Working capital:* inside operating cash flow, including the regulatory
deferrals. (e) *Growth spending:* the maintenance case is central; G is charged against the growth it buys, for ten years,
and stops when growth stops. (f) *The cap:* the shown growth carried ten years needs owner cash of 17.7% of sales, below
the 23.3% the window reached, so no cut by sales; no rate above the discount rate after year ten. *Subsequent events,
stated by the filer and added (CONVENTION of this run: the framework adds stated subsequent events to net debt for the
all-equity basis and says nothing of them for the equity-only basis; they are applied the same way here):* the FERC base
ROE cut, about $70M a year of after-tax earnings (8-K `0001104659-26-037912`), taken out of M; the offshore wind contingent
liability of 409.2 at 2026-06-30 (10-Q), deducted. The FERC refund exposure above the 62.0 already recorded, up to 968.4
pre-tax, is shown beside. Central: **M 1,565, G 1,242, equity added 1,291** (1,700 less 409).

**The range and the floor** (equity-only, per share on 376.675M shares; each end valued at the sovereign 5.29% for the
range and at 10% for the floor and the fair price; the expected return at $67.84 is the rate that equates the case to the
price):

| case | at 5.29%: no-growth / growth | at 10%: no-growth / growth | fair (average at 10%) | return at $67.84 |
|---|---|---|---|---|
| **central: cycle growth 2.63%** | **$81.97 / $71.73** | $44.98 / $30.18 | **$37.58** | 6.45% / 5.52% |
| literal window (no subsequent events), cycle growth | $85.45 / $75.47 | $45.20 / $30.03 | $37.61 | 6.66% / 5.72% |
| literal window, halves growth 12.06% | $85.45 / $174.58 | $45.20 / $66.23 | $55.72 | 6.66% / 9.86% |
| central, halves growth 12.06% | $81.97 / $162.15 | $44.98 / $62.95 | $53.96 | 6.45% / 9.54% |
| central, sales growth 8.26% | $81.97 / $117.17 | $44.98 / $46.71 | $45.84 | 6.45% / 7.80% |
| maintenance by the filer's categories (85.7% of spending), cycle growth | $30.77 / $32.08 | $17.89 / $16.64 | $17.27 | 2.25% / 2.60% |
| central less the FERC refund high end (after 21%) | $80.07 / $69.83 | $43.07 / $28.28 | $35.68 | 6.27% / 5.41% |
| **all-equity beside** (owner cash before after-tax interest, no debt credit, less net debt 27,988, preferred 155.6 and the 409.2 liability) | $0.38 / -$39.13 | -$35.50 / -$73.51 | **-$54.51** | n/a |

On the central case the growth end is below the no-growth end at the sovereign itself: the equity put into growth buys 2.63%
a year on a base of 1,565, less than its cost; "growth can destroy value if it requires cash inputs in the early years"
**[L2000-023]**, and the inversion is the finding.

- **Value range:** **$71.73 to $81.97 a share** (equity-only, central) against **$67.84**; the literal window beside, $75.47 to
  $85.45. **Closes: OUT.** The floor is tested first, and no case earns it at the price: the central ends return 6.45% and
  5.52%, below "real expectancy" of 10 percent, "a point at which we drop out of the game" **[M2003-149]**. The nearest case
  in the whole table, 9.86%, is the literal window with the halves growth, which counts the 2025 timing collection as
  growth, ignores the filed FERC cut and the wind liability, and takes maintenance at depreciation, each of which the filing
  itself contradicts; it is not a case the filing lets the analyst defend, and even at the floor it would be a calculator
  case, "9.6 percent instead of 9.8 percent — forget about the whole exercise" **[M2009-005]**, with the price only about 5%
  below the bottom of the central range, not a screamer **[M1996-084]**. The width (1.14 to 1) does not arise.
- **Fair price (a reporting figure, never a verdict; Part VII):** **$37.58 a share**, equity-only, central (the regulated
  utility basis), after the company's own tax; the all-equity figure beside, **-$54.51**. No cheap price is reported.
- **VERDICT: OUT** **[M2003-149]**, **[M2009-005]**: a regulated wires business valued on its own cash, with the debt that funds
  its plant credited as the regulator allows, earns about 6% on the price, not 10%; "no way we get rich on our utility
  investments" **[M2009-104]**.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7**: no case earns the floor at $67.84; the equity-only (regulated utility) range is $71.73 to $81.97 a share
against the price, with expected returns of 6.45% and 5.52% on its two ends; Q1 IN, Q2 IN (transmission decides, a regulated
return carried to Q3), Q3 against, Q4 accounts weigh against, Q5 integrity IN and ability against, Q6 against. Fair price
$37.58 equity-only (central), -$54.51 all-equity (beside).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; the box is unchanged; each with its source **[M1997-127]**.)*
- **Q8, the bond and the alternatives.** The 30-year Treasury yields 5.29% (2026-10-22); the central cases return 6.45% and
  5.52% at the price (Q7). The dividend declared for 2026 is $0.7875 a quarter (10-K Item 7), $3.15 a year, 4.6% of the price.
- **Q9, the target's debt.** Borrowings at 2026-06-30 were $29.81B and cash $1.82B, the cash being the Aquarion proceeds before
  they displace debt (10-Q); $2.50B of long-term debt is current. In February 2026 the parent issued $1.5B of junior
  subordinated notes due 2056 (8-K `0001104659-26-020565`). Parent ratings BBB (S&P, stable), Baa2 (Moody's, negative), BBB
  (Fitch, negative); the three electric utilities are rated A-range (10-K Item 7). Pre-tax earnings plus interest over
  interest, 2025: (1,699.9 + 140.3 + 1,243.3) / 1,243.3, about 2.5 times (10-K segment note, consolidated column); in 2023 the
  company had a pre-tax loss after the wind impairment. The speakers' test for utility debt is earning power that "even
  under very adverse business conditions, amply covers their interest requirements" **[L2010-012]**, and they warn that a
  single region's utility can be taken down by one event **[L2005-019]**; all of Eversource's service territory is in three
  New England states. Contingencies: FERC refunds reasonably possible up to $968.4M pre-tax (62.0 recorded); the offshore
  wind liability of $409.2M; unrecovered storm costs whose prudence the commissions have yet to rule on (Item 1A). For a
  whole business, the "little or no debt" criterion **[R1997-001]** would not be met; this is a part-interest, where the
  criterion is not stated.
- **Q12.** No business the rows name (casinos, tobacco, loading schemes) is involved.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). *Declared:*
      the filings for every question were fetched and read before Q1 was written, so the sections were written and committed
      in order but the reading ran ahead of the writing; the Q6 buyback line was written back and committed with Q7, as the
      brief requires; one filing quotation in Q1 was corrected in the working copy after Q1's commit (a wording slip, "is
      engaged" for "engaged"), before the run closed.
- [x] If dispatched to an analyst: the brief allowed the per-question commits; the lock is the dispatching session's and was
      not checked here; the run is folded into the register by the dispatcher (operator rule ten). A run not in the register
      binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule); what was seen by
      accident (commit subjects naming another company's run, memory and map lines, file names in a `Screens/` listing) is
      declared under contamination above and was not used.
- [x] Every v5 id resolves (checked by `Test Runs/_research 2026-10-23 ES/check_run.py`); every filing fact has its accession;
      no number without a row, a filing or a CONVENTION label.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing authority
      (US Treasury); the price an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations); the facts found for later questions
      are under AFTER THE STOP. Q5 was reached and answered, so no integrity flag is owed in the box line.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); two of its lines were corrected from the filings (its
      D&A includes regulatory amortization; its debt table adds a non-debt liability line).
- [x] `python tools/check_framework.py` PASS before the closing commit (result recorded in the closing commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The regulated-utility paragraph and specific (e) do not say how they meet.** The debt credit is "credited against the
capital spending it funded, up to the debt share", but the central case under (e) deducts maintenance only and charges growth
spending separately; the text does not say whether the credit attaches to all spending or only to the spending a case
deducts, nor whether the cap is per year or over the window. This run credited the debt share on the spending each case
deducts (maintenance in M, growth in G) and tested the cap over the window (it bound). (2) **The allowed debt share** where
the filing states two equity ratios for two small subsidiaries (50% and 53%) and none for the largest: no rule for choosing
or weighting; the run took the larger debt share stated. (3) **Subsequent events on the equity-only basis.** The basis
paragraph adds "the subsequent events that filing itself states" to net debt for the all-equity figure; for the equity-only
central figure the text is silent, though a utility's post-window events (here an asset sale, a FERC ROE cut, a liability
still owed) bear on it as much; the run applied them the same way and said so. (4) **Specific (a) with one cycle in the
window** asks for growth "between the averages of successive cycles", which needs a span before the window; the text does
not say the earlier span must be read from the filings or may be taken from tagged data; the run used tagged figures for
2016 to 2020, cross-checked to the FY2020 10-K for 2018 to 2020 only. (5) **"About ten percent" and "every case the analyst
could defend".** One beside case returned 9.86% at the price; the text does not say which beside cases count as cases for
the floor test, nor how near "about" is. The run counted as defensible only cases the filing does not contradict, and noted
that a case at the floor would still fail the screamer test. (6) **The parts threshold is written in operating profit**, but
this filer reports segment net income for every year and segment operating income for three; the run used net income and
confessed it. (7) **The tool:** `tools/run.py` prints a "D&A" that includes regulatory amortization (2,404.5 against
depreciation of 1,568.6 in 2025) and a debt "sum" that includes `LiabilitiesOtherThanLongtermDebtNoncurrent`, which is not
debt; for a utility both lines mislead if read as filed figures.
