
## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED** (Q2 closed the file OUT). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** The balance sheets were read in Step 0; facts found are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.** Facts found are under AFTER THE STOP, with the integrity flag in the box line.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** Q6's buyback line needs the bottom of the Q7 range; the computation below puts the bottom below zero, and
the facts on buybacks are under AFTER THE STOP. No weighing is given.

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED.** The two reporting figures the owner asked for are computed below, headed as the protocol requires.

### COMPUTATION, NOT A CLEARANCE
*Computed after a closing STOP at Q2 (operator rule 3). It carries no entry language and decides nothing; the box is OUT at
Q2 whatever it shows. Script and output: `Test Runs/_research 2026-10-16 GBX/scripts/q7.py`, `q7_output.txt`.*

**Inputs.** Price $39.11 (aggregator, flagged); 30.940M shares (cover); market value $1,210.1M. Net debt at the latest filed
balance sheet, 2026-05-31 (10-Q `0001193125-26-292719`): debt, net $1,805.6M (recourse $733.3M, of which the 2.875%
convertible notes due April 2028 are $373.8M; non-recourse, lease fleet, $1,072.3M) less cash and cash equivalents $273.7M
= **$1,531.9M**; restricted cash ($49.1M) is collateral for the non-recourse debt and is not subtracted; operating leases
left out (lessee leases, said so); finance leases "not a material component" (10-Q lease note). No subsequent event in the
10-Q or the later 8-Ks changes the debt (the Series 2026-1 notes of February 2026 are already in the May balance). The
contingently redeemable noncontrolling interest ($31.9M) and the noncontrolling interest ($123.1M) are not subtracted,
because owner cash already deducts the cash paid to the joint-venture partner; subtracting them as well would charge the
partner twice. Enterprise value at the price: $2,742.0M. Sovereign 5.43% (US Treasury 30-year, 2026-10-15). The company's
own tax is inside operating cash; the interest added back for the all-equity basis is taken at a 25% shield (CONVENTION of
this run, Step 0).

**The range, by Q7's range convention.**
- *Cash input and cycle base, specifics (a) and (e).* The literal five-year window FY2021 to FY2025 opens at the filer's
  trough year (FY2021: deliveries 11,300, earnings from operations $41.0M) and so is aberrational at its first year; the base
  is the last full cycle, FY2016 (the prior peak, $408.6M) to FY2025, ten years. The filing allows a maintenance guess: it
  splits capital spending by segment and says that leasing capex is "additions to our lease fleet as part of our leasing
  strategy" (FY2022 10-K MD&A), so the central case charges depreciation as the maintenance spending (the depreciation charge
  "is not inappropriate in most companies to use as a proxy for required capital expenditures" **[M1998-127]**) in place of all
  capital spending, acquisitions and asset sales, with working capital counted, specific (d). All-equity owner cash on that
  basis averages **$26.4M a year** over FY2016 to FY2025 (Step 0's table, the D&A columns).
- *Growth, specific (b).* The series changes sign within the window (it is negative in FY2018, FY2019, FY2021, FY2022 and
  FY2023), so growth is measured between the halves: $48.2M (FY2016 to FY2020) to $4.6M (FY2021 to FY2025), a compound
  decline of 37.4% a year. A decline is carried as the bottom; the no-growth case is the top. The growth spending bought no
  growth (deliveries flat, owner cash falling), so by specific (e) the maintenance-only no-growth case is the top and the
  inversion is the finding, not an error.
- *Acquisitions, specific (c).* Purchases over the cycle were ARI ($361.9M in FY2019) and two small deals ($27.1M and
  $34.9M in FY2017 and FY2018). The serial-acquirer rule compares net purchases with owner cash before purchases; here owner
  cash before purchases is itself near zero or negative, so the comparison means nothing, and with one deal of size in ten
  years I do not treat GBX as a serial acquirer. The maintenance case leaves purchases out; the default pair, acquisitions
  deducted, is the all-spending row beside, and the organic pair is shown too.
- *The cap, specific (f).* Not needed; no case grows.

| case (all-equity basis unless marked) | base, $M a year | growth | value per share at 5.43% | at 10% |
|---|---|---|---|---|
| **TOP:** maintenance-only, cycle base FY2016 to FY2025, no growth | 26.4 | 0 | **-$33.79** | -$40.98 |
| **BOTTOM:** maintenance-only, cycle base, the halves decline carried ten years, then flat | 26.4 | -37.4% a year | **-$48.18** | -$48.36 |
| beside: all spending, acquisitions deducted, cycle base, no growth | -55.2 | 0 | -$82.39 | -$67.37 |
| beside: organic pair (acquisitions left out), cycle base, no growth | -12.8 | 0 | -$57.16 | -$53.66 |
| beside: literal window FY2021 to FY2025, maintenance-only, no growth | 4.6 | 0 | -$46.75 | -$48.01 |
| beside: literal window FY2021 to FY2025, all spending, no growth | -117.7 | 0 | -$119.59 | -$87.57 |
| beside: twelve years FY2014 to FY2025, maintenance-only, no growth | 35.7 | 0 | -$28.27 | -$37.98 |
| equity-only (after interest, against market value): maintenance-only, cycle base, no growth (the halves change sign, so the no-growth case alone) | -4.1 | 0 | -$2.42 | -$1.31 |
| equity-only: all spending, cycle base, no growth | -85.7 | 0 | -$51.02 | -$27.70 |

**Value range (all-equity, central): -$48.18 to -$33.79 a share against $39.11.** Every case is below zero per share.
**The floor, tested first:** no case in the range earns about ten percent at the price **[M2003-149]**. To earn ten percent
on the enterprise value at the price with no growth, owner cash before interest would need to be about $274M a year; the
best single year in twelve was $275.6M (FY2020, a year of large working-capital release), and the ten-year average was
$26.4M on the generous maintenance basis. Had Q7 been reached, it would have closed OUT on the floor, before the width
test.

**A generous case beside, not the convention's range, written down so the result is not an artefact of working capital.**
If every working-capital movement and every dollar of capital spending above depreciation were ignored, owner cash would
be roughly earnings from operations after a 25% tax, less the joint-venture partner's cash, plus net affiliate cash:
FY2016 to FY2025 averages $229.5M × 0.75 − $31.6M − $5.3M ≈ **$135M a year**. At 5.43% and no growth that is about
$2,490M of enterprise value, **$30.96 a share** after net debt, still below the price; at the price it yields about 4.9% on
the enterprise value. Even on figures that leave out the cash the business has actually consumed, no case reaches the floor.

**FAIR PRICE (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent, the two averaged.
**All-equity (central): -$44.67 a share** (top -$40.98, bottom -$48.36). **Equity-only beside: -$1.31 a share** (the
no-growth case alone, since the equity-only halves change sign). Both are below zero: at no positive price does the
midpoint of the range earn the floor. Tax treatment: owner cash after the company's own income tax, as paid inside operating
cash; no carryforward shelter priced separately (the deferred-tax note shows operating-loss carryforward assets of $21M and a total
valuation allowance of $14M at 2025-08-31, XBRL of the FY2025 10-K; immaterial).

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** No business the rows name is involved.

---
## THE BOX
**OUT at Q2** (the deciding part, Manufacturing, is a commodity-type builder whose field, GBX included, earned ordinary
returns over the full cycle FY2016 to FY2025 while GBX's capital tripled; Q1 IN). COMPUTATION, NOT A CLEARANCE: value range
-$48.18 to -$33.79 a share against $39.11 (all-equity; no case earns the floor); fair price -$44.67 all-equity, -$1.31
equity-only. Integrity facts recorded, not judged.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found **[M1997-127]**; no verdict; the box unchanged (operator rule 2).*

**Bearing on Q3 (capital).**
- Capital employed (total equity plus debt less cash) rose from $1,098M (FY2016) to $3,178M (FY2025); after-tax earnings
  from operations went from $306M to $270M (Q2, item 9). Deliveries were 20,300 and 20,400 in the two years.
- Capital spending by segment, FY2016 to FY2025, from the segment notes: Leasing $77.5M, $28.0M, $111.9M, $99.8M, $7.0M,
  $103.8M, $323.2M, $272.9M, $277.0M, and FY2025's total $280.4M (the FY2025 segment split was not read); Manufacturing and
  maintenance together from $35.2M (FY2021) to $121.3M (FY2024) a year. The lease fleet grew from $306M to $1,329M of book value.
- Owner cash after all spending was negative in seven of twelve years and in total (Step 0): "there’s your profit sitting in
  the yard" **[M2008-036]** describes the pattern the table shows; the second kind of business "reports the 12 percent on
  capital but there’s never any cash" **[M2003-122]**. Recorded, not weighed.

**Bearing on Q4 (the accounts).**
- The 10-K and the 10-Q do not feature an adjusted figure or EBITDA in the MD&A; the only EBITDA in the FY2025 10-K is in the
  put option of a noncontrolling partner (priced at the higher of fair value or an EBITDA multiple) and in the pay plan.
- Charges recurring under the "impairment, disposal and exit" heading: $10.0M goodwill impairment in FY2019; $46.7M in
  FY2023 (Portland plant, Gunderson Marine sale, Southwest Steel sale, Rayvag); European plant closures announced in FY2025
  (Romania, Poland, Turkey). The pay metrics exclude "facility-related rationalization/closure costs in Arad (Romania), Olawa
  (Poland), and Adana (Turkey)" (DEF 14A). See **[L2016-007]** on restructuring charges excluded year after year; not weighed.
- The segment basis changed three times in five years: the syndication allocation between Manufacturing and Leasing was
  re-measured from 2021-09-01 (FY2022 10-K) and again from 2025-09-01 (10-Q), and Maintenance Services was folded into
  Manufacturing from 2024-09-01 (FY2025 10-K). Each recast prior periods; the consolidated figures are unaffected.
- Equity-method income ($20.1M in FY2025) is not cash until paid; owner cash counts the affiliates' net cash only.

**Bearing on Q5 (the people): integrity facts.**
- Pay (DEF 14A `0001193125-25-284604`): the CEO and President, Lorie L. Tekorius, was paid $7,706,230 for FY2025
  ($6,500,650 in FY2024; $5,639,481 in FY2023). Fiscal 2025 performance share units vest 60% on "Company EBITDA", 20% on
  Company ROIC and 20% on relative TSR, with a threshold of 6% ROIC, a target of 10% and a maximum of 15%, and EBITDA
  thresholds of $840M, $1,250M and $1,560M for the performance period, as the proxy's table states them. EBITDA is defined as net earnings before interest
  and foreign exchange, tax, depreciation and amortization, excluding the European closure costs above. The rows on EBITDA
  **[M1998-086]** and on the hurdle **[M2004-097]** bear on this; not judged.
- The 2022 to 2024 PSU period: the FY2025 10-K records 55 thousand additional shares earned "based on the EBITDA
  criteria for which actual performance resulted in a payout above target" for the 2022 to 2024 period.
- The proxy asked owners to raise the authorized common shares above 50,000,000, stating that only a fraction remained after
  31,190,881 outstanding, 854,677 reserved for existing awards, 476,748 for future awards and 8,123,421 reserved for the
  convertible notes; and asked to add 1,000,000 shares to the stock plan. Diluted weighted shares were 31.78M against 30.94M
  basic in the nine months to 2026-05-31 (10-Q EPS note).
- Leadership: an 8-K of 2026-08-31 (item 5.02, `0001193125-26-376734`) announced the CEO and President's retirement,
  effective 2027-01-06 (the brief's description; the exhibit press release was not read). Forms 144 were filed on
  2026-01-30 and 2026-07-13 and Forms 4 through 2026-07-20 (titles only seen in the EDGAR index, not read).
- The proxy reads the record "against the hand dealt" **[M1994-009]**; the hand here is a cyclical industry, and the record
  over the cycle is the return in Q2, item 9. Not judged.

**Bearing on Q6 (the money and the owners).**
- Dividends paid $23.3M (FY2016) rising to $39.6M (FY2025); $32.0M in the nine months to 2026-05-31.
- Buybacks: $33.5M FY2016, $20.0M FY2021, $56.9M FY2023, $22.7M FY2025, $13.3M for 313 thousand shares (about $42.50 each) in
  the nine months to 2026-05-31; the programme names a dollar amount ($100M, to 2027-01-31) and no price (10-Q). The prices
  paid sit above the bottom of the computed range, which is below zero; Q6's buyback test is not run because Q6 was not
  reached.
- Shares outstanding rose from 28.2M (2016-08-31) to 32.6M (2022-08-31), then fell to 30.9M; the FY2019 ARI purchase was paid
  in cash ($361.9M) and convertible notes.
- Cash distributed to the Mexican joint-venture partner: $95.1M in FY2016, $73.0M in FY2018, $38.8M in the nine months to
  2026-05-31.

**Bearing on Q9 (debt and exposures).**
- Debt $1,805.6M at 2026-05-31, of which recourse $733.3M (revolving lines $121.4M, senior term debt $240.6M, 2.875%
  convertible notes $373.8M due 2028-04-15) and non-recourse $1,072.3M against the lease fleet (Series 2026-1 notes $300.0M
  at 5.13% and 5.30%, anticipated repayment 2033). The 2028 notes are a maturity that "must actually be met by payment" if
  not refinanced **[L2010-020]**.
- Coverage on the rows' definition, pre-tax earnings over interest **[L2012-002]**: FY2025 earnings before tax and affiliates
  $284.4M against interest and foreign exchange $75.7M; in the FY2021 trough earnings before tax were -$8.6M against $43.3M.
- The acquisition criteria's "little or no debt" **[R1997-001]** is stated for whole businesses; recorded only.
- Contingent: Portland Harbor Superfund site, where the EPA's estimated cleanup cost is $1.7B for all parties, GBX is one of
  about 100 parties in the allocation, and the filer says "sufficient information is currently not available to determine
  our liability, if any, for the cost of any required remediation or restoration of the Portland Harbor Superfund Site or to
  estimate a range of potential loss" (FY2025 10-K Item 1, Environmental Matters).
- Two customers were 26% of FY2025 revenue (customer concentration).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 5542c4a8); written question by question; committed after each
      (5542c4a8 template; 711692db Step 0 to Q1; c1194579 Q2; this commit the close).
- [x] Dispatched: the brief allowed the per-question pathspec commits and the dispatching session holds the lock; the fold is
      the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. One listing of `Test Runs/` was
      made before the copy (to confirm that no file of this name existed); the names it showed are declared under
      contamination and were not used. GATX, whose run file name appeared in it, is used as a rival from its own filings.
- [x] Every v5 id resolves (checked by `Test Runs/_research 2026-10-16 GBX/scripts/check_ids.py`); every filing fact has its
      accession; numbers are from the filings, the tools' arithmetic lines, or labelled CONVENTION.
- [x] The order was kept; Q2 closed the file; everything after it is NOT REACHED, the facts are under AFTER THE STOP, and the
      Q7 figures are headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; the generous beside case
      in the computation is labelled as such and decides nothing. Sovereign from the US Treasury; the price is an aggregator
      quote, flagged.
- [x] Contrary evidence written down as found (Foundations, item 5; Q2 item 5).
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the closing commit.
- Weak points, declared: (1) the return-on-capital series uses a 25% tax on earnings from operations, a CONVENTION of the
  run, and the intermediate years' debt comes from `tools/run.py`'s XBRL table, not from each filed balance sheet; the
  FY2016, FY2019, FY2022 and FY2025 years were read from the filed statements. (2) Trinity's 2017 margin was not read, and
  Trinity's segment perimeter changed with the 2018 Arcosa spin-off. (3) FreightCar America's figures are XBRL
  transcriptions except the 2025 year, checked against its statement. (4) The competitor margins compare an August fiscal
  year with calendar years. None of these would move the box: GBX's own returns and cash over the cycle decide it.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) Q2's rule that "a durable castle that protects only ordinary returns closes OUT" says the field's returns are judged
"from the filer's and the rivals' filings" but not on what measure; I used after-tax earnings from operations on total
capital less cash for the filer, segment margins for the rivals (whose capital by segment is not comparable), and return on
equity as a cross-check, and said so. A named measure, or a rule that the run states its measure and shows a second, would
make two runs comparable. (2) The low-cost exception and the ordinary-returns rule pull against each other when, as here,
the filer is the better-margined of two large builders and still earns an ordinary return; the text says the low-cost
operator is "Another way to prosper" but not what to do when the operator has not prospered. I read the exception as
credited only where it shows in the returns, and closed OUT on the returns; the text does not say so in terms. (3) Q7
specific (e) lets depreciation stand in for maintenance spending, but for a lessor that grows its fleet with non-recourse
debt and sells cars out of it, the asset-sale proceeds and the fleet capex are both "growth" and both left out of the
maintenance case; the text does not say whether recurring sales of fleet cars, which the filer calls a normal part of the
business, belong to the maintenance case. I left them out of the central case and kept them in the all-spending case
beside it. (4) Specific (b)'s "where the series changes sign ... measured between the halves" gave a rate here (-37.4%)
because both half-averages were positive though the yearly series changed sign five times; the text does not say whether a
series that changes sign within each half still yields a meaningful halves rate. Nothing turned on it, since every case is
below zero. (5) The brief's departure (the analyst chooses the 10-K lines) worked; I stated the lines chosen under Step 0.
