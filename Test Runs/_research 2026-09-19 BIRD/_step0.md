## STEP 0: THE SKIP REASON, THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

Run unattended from scratch on 2026-09-19 (from 06:02 local); the template was copied and committed before any fetch (`4ae1654`).
**This is a NEW NAME, not a holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.** WAVE 5, the fourth and **last** name in the
"cap rejected as a broken input: read the cover" row (HBB, LCID, SOUN, BIRD). Research, scripts and downloaded filings are in
`Test Runs/_research 2026-09-19 BIRD/` (scripts copied from the SOUN folder with the CIK and ticker changed). **No BIRD row exists in
`Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`**, and no `Allbirds` or `BIRD` row in any CSV under the repository (grepped:
zero matches outside the ledger, where the string is a word). Every figure below is from the registrant's own filings, fetched by this
run, with the accession, unless marked otherwise.

### THE ENTITY: the share no longer buys Allbirds
CIK 0001653909, `submissions.json` (fetched by this run, `subs.py`): **"Smartbird, Inc."**, SIC 7374 *"Services-Computer Processing &
Data Preparation"*, fiscal year end 1231, ticker BIRD on Nasdaq; **former name "Allbirds, Inc." from 2016-03-11 to 2026-06-15.**
SEC's `company_tickers.json` maps BIRD at this CIK to *"Smartbird, Inc."* (`cik.py`). What happened, from the filings:
- **2026-03-29, Asset Purchase Agreement** (8-K `0001628280-26-022181`): Allbirds agreed to sell to *"Allbirds IP LLC, a Delaware
  limited liability company affiliated with American Exchange Group"* *"substantially all of the Seller's assets, including those
  related to intellectual property assets (including global trademarks, trade names, copyrights, patents, domain names, social media
  accounts, customer lists, and related IP), inventory"* for *"$39 million in cash"*. The release of the next day (EX-99.1) described
  the plan as the sale and *"subsequent dissolution and winding down of the Company (the "Dissolution")"*, with *"a distribution to
  stockholders of net proceeds, taking into account wind-down expenses"*.
- **2026-04-14/15, the pivot** (8-K `0001193125-26-164338` and its EX-99.1): a *"$50 million convertible financing facility"* to
  *"pivot its business to AI compute infrastructure, with a long-term vision to become a fully integrated GPU-as-a-Service (GPUaaS)
  and AI-native cloud solutions provider"*, under an anticipated name *"NewBird AI"*. Dissolution dropped.
- **2026-06-03**, stockholders approved the sale, the charter amendment and the note issuance (8-K `0001628280-26-040772`).
- **2026-06-09, closing**: *"the aggregate consideration received by the Company in connection with the Asset Sale was $40.7 million
  in cash"*, $3.0M of it in escrow for 60 days (8-K Item 2.01, `0001628280-26-043145`).
- **2026-06-15, renamed Smartbird, Inc.**, public-benefit-corporation references removed (8-K `0001193125-26-273417`, Item 5.03);
  a new chief executive, Dr. Nadia Carlsten (formerly CEO of DCAI), from 2026-06-18; the prior CEO resigned 2026-06-19.
- **The Q2 2026 10-Q** (`0001437749-26-028446`, filed 2026-08-19) presents the footwear business as discontinued operations for every
  period and describes the registrant thus: *"Smartbird operates within the Artificial Intelligence ("AI") infrastructure market,
  including the acquisition and monetization of graphics processing units ("GPUs")"*.

**So the brief's name is out of date and so is its business**: "BIRD (Allbirds, Inc.)" is Smartbird, Inc.; the Allbirds brand, its
trademarks, customer lists and inventory belong to American Exchange Group since 2026-06-09. **Every annual year in every window below
(FY2021-25) is the footwear business, now wholly discontinued**; the business the share buys today is H1 2026's continuing operations:
a corporate office, cash, one GPU lease and a convertible facility.

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"cap rejected as a broken input: read the cover."* The triage narrative (`Screens/2026-08-31 PREPPED READING LIST
(operator lists).md`, line ~1429): *"a yield outside -100% to +50%, or a cap under $5M, is **a broken input and never a finding**. It
immediately caught four more - **BRK-B** ... plus LCID, SOUN and BIRD."* **A prompt to read, never a verdict.** Four readings from
the three earlier runs were tested (`_probe_screen.py`, `split_probe.py`, `triage_repro.py`, `vintage_probe.py`, outputs beside them).

**(a) A per-class dimensioned cover plus a stale undimensioned fallback fact (the HBB and SOUN two layers): CONFIRMED, both layers,
and the stale fact is the pre-IPO count.** `python Screens/cover_shares.py BIRD` reads the Q2 2026 10-Q's inline cover as two facts,
*"Common Class A [Member] 9,315,794"* and *"Common Class B [Member] 2,493,399"*, and prints *"MULTIPLE CLASSES ... READ THE FILING"*.
companyfacts publishes only undimensioned facts, so its only dei element for this CIK is `EntityPublicFloat`. The only undimensioned
share counts it carries are **`us-gaap:CommonStockSharesOutstanding` 53,683,269 (2020-12-31) and 56,508,441 (2021-09-30), both from
the first 10-Q of 2021-12-07** (`0001653909-21-000014`): the count of common stock before the November 2021 IPO and the preferred
conversion, and before the 2024 reverse split. `Backtests/scripts/bt17_microcap.py` `shares_asof(..., 2026-09-01)` returns **(2021-09-30,
56,508,441)**, because it has no staleness test; the `a8bc84f` `shares_outstanding()` returns **None** with its 550-day test and the same
fact without it.

**(b) A split: CONFIRMED real, and it bites.** The brief's belief is right: *"ALLBIRDS ANNOUNCES 1-FOR-20 REVERSE STOCK SPLIT"*, effective
*"at 5 p.m. Eastern Daylight Time on September 4, 2024"* (8-K `0001653909-24-000064`, EX-99.1; charter amendment EX-3.1), *"intended to
bring the Company into compliance with the minimum bid price requirement"*. companyfacts **does mix pre- and post-split counts**, in the
weighted-average series: FY2023 is **151,672,437 as first filed** (10-K of 2024-03-13) and **7,583,622 as recast** (10-K of
2025-03-12), and every quarter from Q3 2023 to Q2 2024 carries both (`split_probe_out.txt`). The dei series has nothing to mix (no
undimensioned cover), so `a8bc84f` `share_count_shift()` returns None. **Where the split bites is the house rule**: `cap = close x
shares(measurement) x splits AFTER measurement` multiplies the stale 2021 count by the 0.05 of the 2024 split (`sources.split_factor_after
("BIRD", "2021-09-30")` = 0.05), giving **2,825,422 shares, about a quarter of the true 11.8M**, because the pre-IPO count omits the
IPO's new shares and the converted preferred. The rule is right for a count measured before a split; the count it was handed was
measured before a different event (the IPO) that the rule cannot see.

**(c) The guard's lower yield bound on correct inputs (the LCID reading): CONFIRMED.** On facts filed by 2026-09-01 the `a8bc84f`
`owner_earnings()` returns **{5y_da: -$85.5M, 5y_capex: -$86.8M, 3y_da: -$76.4M, 3y_capex: -$68.6M}** (`triage_repro_out.txt`). At
the 2026-08-31 close of $2.455:

| denominator a reader could have used | cap | yields (5y D&A, 5y capex, 3y D&A, 3y capex) | guard |
|---|---:|---|---|
| **cover A+B, 11,809,193 (correct)** | $29.0M | -294.9%, -299.4%, -263.6%, -236.7% | **fires, lower yield bound** |
| stale pre-IPO count x split factor (bt17 house rule), 2,825,422 | $6.9M | -1,232%, -1,251%, -1,102%, -989% | fires, lower yield bound |
| Q2 2026 weighted average, 9,164,890 | $22.5M | -380% to -305% | fires |
| stale pre-IPO count raw, 56,508,441 | $138.7M | -61.6%, -62.6%, -55.1%, -49.5% | **does not fire** |
| FY2023 weighted average as first filed, pre-split, 151,672,437 | $372.4M | -23.0% to -18.4% | does not fire |

At the 2026-09-01 close ($2.35) the pattern is the same. **The $5M cap floor never tripped** (smallest cap $6.6M). **So the guard fired
on its lower yield bound under every denominator except the two unadjusted pre-split counts**, and since the name was rejected, the
triage used either the correct count or the split-adjusted stale one; **the code that wrote the row is not on disk** (the HBB finding),
so which of the two cannot be read, only bounded.

**(d) An earliest-vintage fact inside the cash-flow series (the SOUN shell-year defect): REFUTED.** Allbirds was never a SPAC or a
spin-off; its first 10-K (FY2021, `0001653909-22-000016`) is the operating company's own. **Every annual operating-cash, capex, D&A and
stock-compensation fact carries one value across every vintage that filed it** (`vintage_probe_out.txt`). The one element whose vintages
differ is the P&L charge `AllocatedShareBasedCompensationExpense` for FY2022 (20,231 thousand first filed, 19,031 thousand in the FY2023
10-K), and the current screen's `sbc_annual` takes the first (the cash-flow add-back is 19,873 thousand); immaterial to any verdict.

**(e) A fifth reading the brief did not name, and it is the one that matters: THE NUMERATOR IS A BUSINESS THE REGISTRANT HAD ALREADY
SOLD.** The triage ran on 2026-09-01. By then the footwear business had been sold (2026-06-09) and the 10-Q presenting it as discontinued
had been filed (2026-08-19). The `a8bc84f` five-year and three-year owner earnings are **FY2021-25 and FY2023-25 of the footwear
business**, read from annual 10-K facts that are not yet recast (the first recast annual filing will be the FY2026 10-K); the 10-Q's
split arrives under new tags (`NetCashProvidedByUsedInOperatingActivitiesContinuingOperations`, `CashProvidedByUsedInOperatingActivitiesDiscontinuedOperations`)
for half-years only; the current screen's `ocf_continuing()` removes separately tagged discontinued cash from annual facts only, so it cannot act
until the FY2026 10-K recasts the years. **So the yield the guard rejected was the losses of a sold shoe business divided
by the market value of a GPU-leasing shell.** On the correct count that quotient is a mismatch, not a finding about either business.

**Finding on the label: RIGHT that the quotient was broken, WRONG about where.** "Cap rejected" is loose (the guard fired on the yield,
not the $5M floor; the LCID mechanism). "Broken input" is right, but the broken input was the **numerator**, a perimeter that no longer
belonged to the registrant, and possibly also the denominator (the split-adjusted pre-IPO count, if that is what the triage used). **No
current `floor_screen` guard reads a completed disposition from a 10-Q** (the 8-K Item 2.01 route was tested and rejected as a signal on
2026-09-12, RESUME STATE item 5), so the same mismatch will recur for any name that sells its business and keeps its listing.

**The other guards** (`_probe_screen_output.txt`, current screen): `working_capital_flag` fires at FY2021 (*"AccountsPayableAndAccrued
Liabilities moved 50% of 2021 OCF"*); `scale_shift` 1.339; `restatement_shift` 1.0; `acquisition_flag`, `da_discontinuity_flag`,
`capex_funding_flag` and `lease_capex_flag` None; `stale_filer` 262 days. `sbc_annual` resolves for every year FY2019-25, so the
SBC-of-zero defect does not arise. `shares_outstanding()` None (the staleness test). **Not a verdict**: Q4 rebuilds owner earnings from
the faces.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by this run at
  06:05 local on 2026-09-19 (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned **(5.34, '09/18/2026', 'US Treasury daily par yield curve')** in the same minute
  (`step0_out.txt`). FRED not used. Struck by this run, not inherited (the brief's 5.34% happens to be the same day's figure).
- **Earnings currency: USD.** The one customer *"is located in the United States"* (10-Q Note 7); reporting currency US dollars.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$2.30, the close of 2026-09-18** (Friday). Source: Yahoo Finance chart via `sources._chart("BIRD", rng="1mo", max_age_h=0)`
  (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`): `regularMarketPrice` 2.3, `regularMarketTime` 1789761600 =
  16:00:00 EDT, exchange NMS; the day's bar $2.24-$2.44 on 736,200 shares. `tools/sources.price()` returned the same 2.3 stamped 2026-09-18.
- **The path** (`price2y_out.txt`, `price2y_daily.txt`): $4.10 at 2025-12-31; $2.98 on 2026-03-30 (sale announced); **$2.49 on 04-14 and
  $16.99 on 04-15, the day of the AI announcement, on 288.2M shares with an intraday high of $24.31**; $6.96 on 04-28 (the ATM signed);
  $6.22 on 05-07; $3.93 on 06-09 (the closing); $5.48 on 06-17 (the new CEO, 47.8M shares) and $5.97 on 06-18; $4.28 on 06-25 (the
  dividend record date); $4.00 on 06-30; the two-year low $2.21 on 07-29; $2.455 on 08-31; $2.30 on 09-18.
- **Primary-filing corroboration, three ways:** (1) the Carlsten inducement RSUs granted with effect from 2026-06-18 carry a
  weighted grant-date fair value of *"5.97"* for the 2,423,569 RSUs granted in H1 2026 (10-Q Note 8), equal to Yahoo's 06-18 close;
  (2) the merger proxy (DEFM14A `0001193125-26-213226`): *"the closing price for our Class A common stock on Nasdaq was $6.22 per share"*
  on the latest practicable day, equal to Yahoo's 05-07 close; (3) **after the cover, the CEO's Form 4 (`0001437749-26-029604`) records
  36,315 shares withheld at $2.44 on 2026-09-02**, and the CFO's (`0001437749-26-029607`) a sale of 1,755 at $2.44, against Yahoo's 09-02
  close of $2.435. **The aggregator's series is corroborated at three dates**; the 2026-09-18 close rests on the aggregator alone.
- **Split factor after the count's date: 1.0.** `close` used, never `adjclose`. The 1-for-20 split of 2024-09-04 precedes every count used.

### The share count: from the cover, with the accession, and what happened after it
- **Cover of the Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-19, accession `0001437749-26-028446`**, the latest periodic
  filing (it was late: NT 10-Q `0001437749-26-028074`, *"The Company requires additional time to review and confirm the accounting
  treatment for its Asset Sale"*): *"As of August 10, 2026, the number of shares of the registrant's Class A common stock outstanding
  was 9,315,794 and the number of shares of the registrant's Class B common stock outstanding was 2,493,399 ."*
- **The charter was read before the classes were added** (10-Q Note 6, the description of the amended and restated certificate): Class A
  one vote, Class B ten; *"Holders of Class A common stock and Class B common stock are entitled to ratably receive dividends"*; on
  liquidation the assets *"are distributable ratably among the holders of our Class A common stock and Class B common stock"*; *"Each
  share of our Class B common stock is convertible at any time at the option of the holder into one share of our Class A common stock"*;
  and Note 12: *"The rights, including the liquidation and dividend rights and sharing of losses of the Class A common stock and Class B
  common stock are identical, other than voting, transfer, and conversion rights."* **The classes differ in votes only and convert one for
  one, so they are summed: 11,809,193.** (The votes matter at Q3: 2,493,399 Class B carry 24.9M votes against 9.3M of Class A.)
- **Cross-checks (rule 4):** the 2026-06-30 balance sheet shows 9,283,833 Class A outstanding (9,294,832 issued less 10,999 treasury) and
  2,525,409 Class B, 11,809,242 in all; between 06-30 and 08-10 about 32,000 Class B converted to Class A. **The annual-meeting proxy
  (DEF 14A `0001193125-26-342889`) gives "Total Shares of Common Stock Outstanding 11,809,193" at its record date**, the cover sum exactly.
- **What happened after the cover (not in the count; the Q3 2026 10-Q will carry it):** the 2026-09-01 quarterly vesting (the Form 4s
  above show it occurred; the CEO's award vests 79,811 shares a quarter, the CFO's and chair's awards their first twelfths, 63,849 and
  10,417), net of shares withheld; any ATM sales since 08-10 (none filed); any note conversions or interest paid in shares (none filed;
  the next interest date is 2026-10-01). Of the order of 1-2% before any conversion; immaterial to any verdict.
- **Beside the count, not in it:** **$8.25M face of senior secured convertible notes** convertible at *"the lower of: (i) the Conversion
  Price then in effect; and (ii) ... 93% of the lowest volume weighted average price of our Class A common stock during the ten (10)
  consecutive Trading Days"* (85% in default), 2,828,083 shares reserved; at $2.30 the alternate price is about $2.1, **about 3.9M shares,
  a third of the count**; **$91.75M more notes issuable "solely at the option of the holders"**; an ATM of up to $98.1M (Chardan), $15.4M
  used; 2,316,365 unvested RSUs, 15,000 PSUs, 426,409 options at a weighted $75.12; and a proposal at the 2026-09-30 annual meeting to add
  **3,500,000** plan shares (*"total potential overhang is expected to increase by 29.6% to 55.3%"*).

### THE PAIR
**US$2.30 x 11,809,193 x 1.0 = US$27.2M.** Beside it, at 2026-06-30 (10-Q face): cash and equivalents **$37.4M**, less the special
dividend paid on or about 2026-08-20 (*"we anticipate the total payment will be $3.6 million"*), before the third quarter's costs; the
convertible notes at fair value **$8.2M**; lease liabilities left over from the footwear leases not transferred **$6.3M** against
right-of-use assets of $2.5M; accrued liabilities **$7.9M**, of which *"Employee-related liabilities"* $6.8M; the net investment in the one
GPU lease **$2.7M**; stockholders' equity **$22.5M ($1.91 a share)**. The quote is about 1.2x book and below the half-year's gross cash.

### The deal check
`sources.deal_note("0001653909")` printed *"LIVE DEAL FORM: 2 filing(s) since the annual report of 2026-03-31, first PREM14A on 2026-04-15
... IF A DEAL IS LIVE THE QUOTE IS A SPREAD"*. **Read, per the ROKU lesson: the PREM14A and DEFM14A are the proxy for the registrant's own
ASSET SALE, in which it was the seller, and that deal CLOSED on 2026-06-09.** No offer for BIRD's shares exists (no SC TO, SC 13E-3 or
merger proxy naming it as target since). **The quote is not a spread.** What survives of the deal is a **dividend promise**: the proxy
said *"The Board currently anticipates that the Asset Sale Dividend may be approximately $1.34 per share"*, and Kroll's fairness opinion
was given on *"the $1.34 per share"*; the board declared **$0.31** on 2026-08-06 (8-K `0001437749-26-026796`), payable to holders of
record on 2026-06-25, with a possible further dividend *"to the extent of available Sale net proceeds"*. Carried to Q3.

### The perimeter: every change in the windows used, from the filings
| date | event | consideration (filed) | what it changes |
|---|---|---|---|
| 2024 | sale of international businesses | proceeds $4.0M FY2024, a $0.5M loss (FY2025 10-K cash-flow face) | FY2024 on |
| 2024-09-04 | 1-for-20 reverse split | none | every share count before it |
| 2026-04-19 | purchase of GPU servers and a 36-month sales-type lease to *"a subsidiary of QumulusAI, Inc."* | $2.758M paid; about $3.7M of lease payments including a purchase option | the first and only transaction of the new business |
| 2026-06-09 | **sale of the footwear business** to Allbirds IP LLC (American Exchange Group) | **$40.7M cash**, $3.0M in escrow; the $19.7M revolver repaid from it | **every annual year in every window becomes discontinued** |

### The filing was read (rule 4)
- [x] MD&A [x] cash-flow statement incl. detail lines [x] footnotes
- **Documents:** 10-Q Q2 2026 filed 2026-08-19 (`0001437749-26-028446`), read whole; 10-K FY2025 filed 2026-03-31 (`0001628280-26-022192`),
  audit report, cash-flow face and going-concern note read; DEFM14A 2026-05-08 (`0001193125-26-213226`), reasons, background of the sale
  and Kroll opinion read; DEF 14A 2026-08-11 (`0001193125-26-342889`), proposals 2 and 3 read; 8-Ks and exhibits of 2024-08-30, 2026-03-31,
  04-15, 04-20, 05-28, 06-04, 06-10, 06-15, 06-17, 07-01, 07-29 (with Deloitte's EX-16.1), 08-10 and 08-19 (the CEO's letter); NT 10-Q
  2026-08-17; Form 4s of 2026-08-27 and 09-03. The 10-Q Q1 2026 and the 10-Ks FY2021-24 were downloaded; their figures enter through
  companyfacts, single-vintage (reading (d)). Raw text in the research folder (`*.txt`, `.flat.txt`), not committed.
- **Figures cross-checked against the filed statement:** FY2025 *"Net cash used in operating activities | ( 55,083 ) | ( 63,860 )"*
  (FY2025 10-K cash-flow face) against companyfacts' -55,083,000 and -63,860,000: **identical**; stock-based compensation *"7,763 |
  11,472"*, purchases of property and equipment *"( 3,145 ) | ( 4,095 )"* and D&A *"8,019 | 12,396"*: identical. H1 2026 *"Net cash used in
  operating activities, continuing operations | ( 7,304 )"* (10-Q face) against the new continuing-operations tag's -7,304,000: identical.
