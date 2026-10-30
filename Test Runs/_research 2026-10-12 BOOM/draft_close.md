
## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The template asks for the eight to ten years of balance sheets even when the file closes
before Q4; that reading is under AFTER THE STOP, Q4, and is not weighed.

## Q5 — WHO RUNS IT. STOP on integrity.
NOT REACHED. Facts carried from the accounts that bear on the people are recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Q6's buyback test needs the bottom of Q7's range; Q7 is not reached either, so nothing is written back
here. Facts under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The owner's reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. No business of the company is of a kind the question names; not asked.

---
## COMPUTATION, NOT A CLEARANCE: the value range and the fair price (the owner's reporting figures)
*Arithmetic beneath a closing STOP (operator rule 3). It carries no entry language, decides nothing, and does not
reopen Q2. Every figure is in `calc.py` / `calc_out.txt`; USD millions unless "a share".*

**Owner cash after every real cost** (operator rule 5; never a net-income proxy): net cash from operations less the
stock pay added back in it, less all capital spending, plus proceeds of equipment sold, from the filed cash-flow
statements (10-K fiscal 2025 `0000034067-26-000009` for 2023 to 2025, fiscal 2023 `0000034067-24-000025` for 2021 and
2022). All-equity basis (Q7, On what the floor is earned): cash interest paid added back after tax at the 21% US rate
(a CONVENTION of this run: the rows give no rate; the US group carries a valuation allowance, so the true shield may be
smaller, which would lower these figures by under $1M a year). The company's own cash tax is in the figure (Q7, Whose
tax); no carryforward shelter is priced, because cash tax paid ($10.5M in 2025 on a pre-tax loss, mostly German) runs
above the statutory rate, not below it.

| Year | Operating cash | Stock pay | Capital spending | Owner cash, equity | Owner cash, all-equity | Paid to Arcadia's 40% holder | All-equity, after the minority's cash | Acquisitions | Sales |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | -12.8 | 6.6 | 8.7 | -27.0 | -27.0 | 0 | -27.0 | 285.9 (Arcadia: $261.0M cash plus the $24.9M note to the seller) | 260.1 |
| 2022 | 44.9 | 10.1 | 18.6 | 16.4 | 21.3 | 12.3 | 9.0 | 2.4 (price adjustment) | 654.1 |
| 2023 | 65.9 | 10.3 | 16.0 | 40.0 | 47.3 | 13.5 | 33.8 | 0 | 719.2 |
| 2024 | 46.6 | 6.9 | 17.3 | 22.5 | 28.4 | 10.9 (incl. a $2.5M deemed dividend) | 17.5 | 0 | 642.9 |
| 2025 | 53.5 | 5.5 | 16.5 | 31.5 | 35.4 | 6.4 | 29.0 | 0 | 609.8 |

Depreciation variant (spending replaced by depreciation alone): 2024 $25.8M, 2025 $33.1M against $22.5M and $31.5M on
the spending basis; capital spending ran 1.1 to 1.2 times depreciation. The filing gives no split of maintenance from
growth spending, so the all-spending case is central (specific (e)). Working capital is inside operating cash
(specific (d)).

**The window.** The literal window is 2021 to 2025. 2021 is the merger year: Arcadia was bought on 2021-12-23 and ‘no
sales were recorded’ for it in 2021 (10-K fiscal 2021 `0000034067-22-000023`, segment note). The specific says a merger
inside the window is valued on the combined companies' own averages; Arcadia's own full-year 2021 cash record was not
read (only the combined company files), so the combined base is the four fully combined years 2022 to 2025 (CONVENTION
of this run: the only combined years on file). The deal's financing (a $150M term loan drawn in 2021 and since repaid or refinanced into the present
credit facility, and about $149M of shares issued in 2021) is in today's net debt and share count.

**The minority.** Arcadia is 60% owned. Two readings of the 40% holder's claim, both shown:
- **A (central, by the framework's own net-debt definition, which names borrowings and finance leases only):** the
  owner cash that reaches DMC's holders is consolidated owner cash less the cash actually paid to the 40% holder, and
  claims are net debt at 2026-06-30: debt $59.1M less cash $28.6M = **$30.5M** (10-Q `0000034067-26-000048`; operating
  leases left out, as the convention says).
- **B (beside):** the put is exercised at its floor: DMC owns 100% of Arcadia's cash and owes $187.08M less the $24.9M
  note = **$162.2M** (‘subject to potential working capital adjustments’), added to net debt (claims $192.7M). The 10-Q
  says the put has been exercisable since 2026-09-06, and that its preferred-stock form could give the holder ‘majority
  voting control of the Company’. No 8-K reporting an exercise had been filed by 2026-10-12.

**Growth.** Specific (b): the series changes level sharply, so growth is measured between the halves of the combined
window (2022 to 2023 against 2024 to 2025). Specific (f): where the shown growth carried ten years needs owner cash above
the highest share of sales the series has earned, growth is cut to the business's own sales growth between the same
halves, **-4.5% a year** (sales $686.6M to $626.3M average). Under A the shown growth (+7.4% default pair; +4.3% with
acquisitions left out) rests on the minority's distributions falling, not on the business; carried ten years it would
need 5.6% to 7.3% of sales against a highest share of 4.8% in the combined years, so it is cut. Under B the shown growth
is already negative (-1.7%). Negative growth is the bottom of the range and no growth the top (specific (b)). Ten years,
then zero nominal growth, discounted at the 5.60% sovereign.

| Case | Base owner cash | Growth carried | Range, a share | Width | Fair price, a share (each end at 10%, averaged) |
|---|---|---|---|---|---|
| **A, default pair (acquisitions deducted, total growth), all-equity: CENTRAL** | 21.7 | -4.5% (cut from +7.4%) | **$11.77 to $17.40** | 1.42 | **$7.72** |
| A, default pair, equity-only (after interest, no net debt) | 16.2 | -4.5% (cut from +14.2%) | $9.90 to $14.10 | 1.42 | **$6.88** |
| A, acquisitions left out (the filer reports no organic growth; the only acquisition in the combined window is the $2.4M price adjustment), all-equity | 22.3 | -4.5% (cut from +4.3%) | $12.14 to $17.92 | 1.42 | $7.98 |
| B, put exercised at its floor, all-equity | 32.5 | -1.7% | $15.24 to $18.88 | 1.15 | $5.57 |
| B, equity-only | 27.0 | +0.1% | $15.58 to $15.70 | 1.01 | $5.28 |
| Literal window 2021 to 2025, default pair (Arcadia's $285.9M deducted) | -45.2 | not meaningful | not positive (the no-growth case is -$40.78 a share) | n/a | not positive |
| Beside: the (f) cap read on every filing read (2019, before Arcadia: 8.4% of sales), A default all-equity uncut | 21.7 | +7.4% | $17.40 to $32.46 | 1.80 | $12.60 |

**Against the price of $5.66:** the central range (A) is $11.77 to $17.40 and the central fair price $7.72 (equity-only
$6.88); with the put exercised at its floor (B) the fair price is $5.57 (equity-only $5.28), below the price. The
literal window, which charges the Arcadia purchase, gives no positive value. Which reading of the 40% holder's claim
governs moves the fair price from above the price to below it; the run states both and decides between neither, since
the file is closed. Book equity was $11.78 a share at 2025-12-31.

---
## THE BOX
**OUT** at **Q2** (why is the castle still standing), on the deciding part, DynaEnergetics (56% of five-year segment
operating profit before Arcadia's goodwill charge): the castle is shown filling in on the filer's own evidence, with
prices cut to consolidated customers who also make the product and operating margin down from 22.2% (2019) to 3.8%
(2025 and the first half of 2026). Integrity facts recorded, not judged. COMPUTATION beneath the stop: central range
$11.77 to $17.40 a share (A, all-equity, combined window 2022 to 2025, growth cut to -4.5%), fair price $7.72 (equity-only
$6.88); with the Arcadia put exercised at its floor, fair $5.57 (equity-only $5.28); literal window not positive; price
$5.66.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found **[M1997-127]**; no verdict; the box unchanged (operator rule 2).

**Q3 (capital).** Arcadia was bought for $261.0M cash plus $21.7M non-cash consideration and a $24.9M loan to the seller
(10-K fiscal 2023 `0000034067-24-000025`, cash-flow statement), and its operating agreement sets a ‘Floor Value’ of
$467.7M for 100% (10-Q `0000034067-26-000048`, Note 2). Arcadia's segment operating income was $4.0M, $21.4M, -$1.9M
(before the goodwill charge) and $4.2M in 2022 to 2025; its adjusted EBITDA $25.4M (2024) and $28.6M (2025) (10-K
Item 7). Consolidated capital spending $16.0M to $18.6M a year against depreciation of $13.9M to $14.9M (2024, 2025).
NobelClad's backlog $62.6M at 2025 year-end (Item 1A).

**Q4 (the accounts; the ten balance sheets, read as the template requires).** From `tools/run.py`'s ten-year table
(tagged, first-filed values) checked against the filed 2025 and 2024 balance sheet (`0000034067-26-000009`):
- *Equity against goodwill and intangibles.* Equity $112M (2016), $106M (2017, after a $17.6M goodwill write-off),
  $197M (2020), $361M (2021, after about $149M of shares sold to pay for Arcadia), $410M (2023), $251M (2024), $242M
  (2025). Goodwill $141.3M to $141.7M from 2021 to 2023, then nil after the 2024 impairment; Arcadia's purchased
  intangibles $255.6M (2021) amortized to $155.1M (2025). In 2024 a further $64.3M was charged to equity to carry the
  40% holder's interest at its $187.08M floor (equity statement, ‘Adjustment of redeemable noncontrolling interest’),
  and $4.4M more in 2025; retained earnings went from $146.6M (2023) to nil (2024) to a deficit of $13.5M (2025). The
  redeemable interest sits between liabilities and equity at $187,080 thousand at both year-ends.
- *Cash, receivables and inventory against sales.* Receivables 15.3% of sales in 2019 and 15.4% in 2025; inventory
  13.5% of sales in 2019 and 23.7% in 2025 (Arcadia's model carries more stock). The allowance for doubtful accounts
  rose to $9.8M (2025) from $6.9M, $9.4M of it at DynaEnergetics, where $6.1M was provided in 2025 (Note 2).
- *Debt.* Long-term debt nil (2016), $132.4M (2021), $47.2M (2025); total debt $59.1M at 2026-06-30 with net credit
  facility borrowings of $8.2M in the half year ‘to assist in funding increased working capital’ (10-Q).
- *What the figures do not say.* The balance sheet carries the minority's claim at the floor, not at what Arcadia
  earns; the gap is the contract, not the business.
- *The real costs and the featured figures* (recorded for Q4's weighing and carried toward Q5 by the convention, not
  weighed): amortization of Arcadia's customer relationships, accelerated, $21.2M (2024) and $19.1M (2025); stock pay
  $10.3M (2023) to $5.5M (2025); restructuring and impairment charges in each of 2023 to 2025 ($2.5M in 2024, $3.6M in
  2025) and ‘strategic review and related expenses’ of $7.8M (2024) and $2.7M (2025). The filer features ‘Adjusted
  EBITDA’, ‘Adjusted EBITDA attributable to DMC Global Inc.’ and an ‘Adjusted net (loss) income’ computed ‘prior to the
  adjustment of redeemable noncontrolling interest’ (Item 7): for 2025 that table shows $(0.68) a share before the
  adjustment and $(0.35) ‘As adjusted’, against a GAAP loss of $(0.90) a diluted share after it. Performance shares
  vest on ‘cumulative targeted Adjusted EBITDA’ and ‘Adjusted Free Cash Flow’ (Note on stock compensation); the 2026 cash
  awards for the two segment heads pay on the same two measures (8-K `0000034067-26-000011`). The rows that bear on
  these are listed for the later run, not applied: **[L2016-006]**, **[L2021-003]**.

**Q5 (the people; integrity facts recorded, not judged).** The featured adjusted figures above, which leave out the
transfer of value to the 40% holder and recurring restructuring and review costs, are the habits the convention
carries from Q4 to Q5; any later run that reaches Q5 must answer them **[M2013-088]**. Board: six directors elected
2026-05-13 with between 1.89M and 2.88M shares withheld each against 8.79M to 9.79M for (8-K `0000034067-26-000038`).
CEO James O'Leary (8-K `0000034067-26-000011`); the 2025 10-K records ‘CEO transition expenses’ of $520 thousand
(Item 7). The proxy (`0000034067-26-000022`) was fetched and not read for judgment.

**Q6 (the money and the owners).** (1) The Arcadia contract: the call (DMC's, from 2024-12-23, cash only) and the put
(the holder's, from 2026-09-06 after a December 2024 amendment) both price the 40% at the higher of a value based on the
acquisition price and a multiple of Arcadia's EBITDA, with a floor of $187.08M for the 40% (Item 1; 10-Q Note 2). On a
put DMC may pay 20% in cash and 80% in a new ‘Put Preferred’ paying 3%, issued in a number set at the 60-day average price
of the common and each convertible into one common share, capped at 19.9% of the common until holders vote to lift the cap (the put holder may not vote),
redeemable from 2027-06-23 and in full by the third anniversary, subject to Delaware limits on redemptions that would
impair capital (10-Q, Note 2 and Part II Item 1A). The 10-Q: ‘it is likely that if the Put Preferred is issued, a
stockholder vote to remove the voting and conversion cap would result in the minority interest holder acquiring
majority voting control of the Company through the involuntary dilution of the existing stockholders.’ (2) Shares:
about $149M raised by an offering and an at-the-market program in 2021 (`0000034067-24-000025`); treasury purchases of
$1.2M to $2.5M a year (cash-flow statements); dividends none since 2020 except the $2.5M deemed dividend to the 40% holder
in 2024. (3) A stockholder rights plan of 2024-06-05, extended to 2026-06-04 and, by Amendment No. 2 of 2026-04-24, to
2027-06-04 (8-K `0000034067-26-000028`); Steel Partners and affiliates reported 1,194,441 shares, 5.8%, on Schedule
13D/A of 2026-02-24 (`0000921895-26-000546`). (4) A strategic review of DynaEnergetics and NobelClad from January 2024;
‘no longer actively marketing’ them from October 2024 (Item 1). (5) Long-term incentive awards for 2026 paid partly in
cash ‘given the lack of a sufficient number of available shares’ under the 2025 plan (8-K `0000034067-26-000011`); the
plan was amended and restated and approved on 2026-05-13. Rows for the later run, not applied: **[L2009-019]**,
**[M1995-001]**, **[L2014-012]**.

**Q9 (debt and exposures).** Credit facility with a KeyBank-led group: term loan payable $938 thousand a quarter to
March 2028, $1,250 thousand thereafter, balloon at maturity 2029-02-06; secured by receivables, inventory and fixed
assets including Arcadia; leverage ratio 2.19x at 2026-06-30 against a 3.0x maximum (3.5x for two quarters after a put or
call payment); debt-service coverage 3.28x at 2025 year-end against a 1.25x minimum (10-K Item 7; 10-Q). The put claim
of about $162M (net of the note) against a market value of $116.3M; the 10-K: ‘Debt financing could materially impact
the Company’s leverage while equity financing could materially dilute existing stockholders.’ One customer 22% of
first-half 2026 sales. Explosives at two businesses (Item 1A). Rows for the later run, not applied: **[L2014-024]**,
**[R1997-001]**, **[M2013-076]**.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `061cd131`); written question by question; committed after each
      (Step 0 `e117b49b`, Q1 `5d8d8454`, Q2 `f5c3894a`, the close in the commit that carries this line).
- [x] Dispatched run: the brief allowed per-question pathspec commits; the lock in `Screens/_daily/` was present (held by
      the dispatcher; I did not touch it). The fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched beyond the one listing declared
      under contamination (other companies' file names, not opened).
- [x] Every v5 id resolves (`check_cites.py`: ids against `principle_ledger_v5.csv`, every quoted fragment before an id
      found in that row); every filing fact carries its accession; no E-id.
- [x] The order was kept; Q2 closed the run; Q3 to Q12 NOT REACHED; every figure after the stop is headed COMPUTATION,
      NOT A CLEARANCE or recorded as a fact, not weighed.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; the sovereign from
      the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations; Q2); facts for later questions under AFTER THE STOP, with
      the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` used.
- [x] `python tools/check_framework.py` PASS before the closing commit (result recorded in the commit message).

Honest gaps: Arcadia's own 2021 cash record, Arcadia's EBITDA-multiple put price (only the floor is stated), the
proxy's pay tables, Core Lab's and Halliburton's 2019 to 2020 segment years, and private perforating makers were not
read. The interest add-back at 21% is mine. The parts table counts segment operating income before unallocated
corporate cost.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A put-able minority interest is not in the net-debt definition.** Q7's all-equity basis names ‘borrowings and
finance leases less cash and securities’; a redeemable noncontrolling interest with a contractual floor of $162M (net),
exercisable now and payable partly in convertible preferred that could pass control, is not borrowing, yet it is the
largest claim ahead of the common and larger than the market value. Read literally, the central figure leaves it out and
puts the fair price ($7.72) above the price; counted, the fair price ($5.57) is below it. I showed both and called the
literal one central; the convention should say which governs. (2) **No rule for consolidated subsidiaries with a
minority.** I deducted the cash actually paid to the minority, by analogy with the equity-method rule (dividends
received); the framework says nothing either way. (3) **A merger inside the window whose target's pre-merger year is not
on file.** The specific asks for the combined companies' own averages; when only the acquirer files, the combined
years are fewer than five. I used the four combined years and said so. (4) **Specific (f)'s ‘highest share of sales the
business has earned in the filings read’ is ambiguous across a merger:** the pre-merger company (2019: 8.4%) is a
different business from the combined one (highest 4.8% after the minority's cash). I read it on the combined years and
showed the other reading beside. (5) **Section B's ‘five-year operating profit’ does not say whether an impairment
counts**; here a part's sum is negative with the charge and positive without it. Both readings gave the same deciding
part, so nothing turned on it, but a closer case would. (6) **The brief's competitor rule (rivals the 10-K names)
yields nothing when the 10-K names no rival by name**, as here; I chose the nearest filers and said so.
