# Company Run - Smartbird, Inc., formerly Allbirds, Inc. (BIRD) - 2026-09-19
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS - every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order - not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation - it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
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

---
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

> "we try to stick to businesses we believe we understand. That means they must be relatively simple and stable in character. If a
> business is complex or subject to constant change, we're not smart enough to predict future cash flows." **[E3-31]**, 1992

**The question is asked of the business the share buys at $2.30 today, not of the business the brief named.** The footwear business is
sold; its record is evidence about the people (Q3) and about what the triage priced (Step 0), not about how Smartbird makes money.

### The unit economics, in my own words, without management's language
**What the registrant owns and does, from the Q2 2026 10-Q:** about $34M of cash (June 30's $37.4M less the August dividend, before the third quarter's costs); $8.25M face of secured notes owed;
the leftover leases of closed stores; and **one contract**. On 2026-04-19 it paid **$2.758M** for server systems built on NVIDIA GPUs
and leased them for 36 months, non-cancellable, to *"a subsidiary of QumulusAI, Inc."*, for *"fixed monthly payments of approximately $0.1
million for the first 30 months and approximately $0.2 million for the final six months"* plus *"an end-of-term purchase option of
approximately $0.1 million"*, about **$3.7M** in all (Note 11). The lessee runs the machines and bears the costs; the lessee can buy them at
the end. **In substance this is a three-year secured loan against a computer.** The accounting says so too: a sales-type lease, so the
quarter booked **$2.758M of "revenue" and $2.758M of "cost"** on day one (*"no material selling profit or loss was recognized at
commencement"*) and thereafter only interest income, **about $0.1M in the quarter**. It is **100% of revenue from one customer** (Note 7).

**What the lending earns and what the money costs** (`oe.py`, `oe_out.txt`; arithmetic, not judgment):
- the lease's implied rate, reconstructed from Note 11's payment schedule: **about 19% a year** (an approximation; the filer does not
  state the implicit rate; its unearned interest of $832 thousand on $3,496 thousand of remaining payments is consistent with it);
- the notes' cost: 12% coupon on face, a 5% original issue discount and about $0.5M of issuance costs, so **$7.3M received for $8.25M
  owed**, about **19.5% a year** to a two-year maturity if paid in cash, and dearer if converted, since conversion runs at *"93% of the
  lowest volume weighted average price"* of ten days (Step 0);
- **so the one contract earns about what its funding costs, before a dollar of overhead**;
- and the overhead: selling, general and administrative expense of the continuing company **$10.7M in Q2 2026 alone** ($16.7M in the half),
  against lease interest of about $0.1M a quarter. The half-year's continuing loss before working-capital movements and after stock pay is
  **-$18.2M** (about -$36M a year at that rate).

**What the filer says the business will be, which is not what it is:** *"Smartbird provides dedicated infrastructure through a managed
model ... They tell us what they need AI to do; we design, procure, deploy, and operate the execution engine for them to build on"* (the
CEO's letter, 8-K `0001437749-26-028541`, EX-99.1); in the filer's words, *"We expect our customers to purchase our services primarily through committed contracts, ranging
from several months to 5 years, where the customer is provided with reserved capacity access over the contract term at a fixed price
regardless of utilization."* (10-Q MD&A). **No such contract is filed.** Four months earlier the same plan read *"a fully integrated
GPU-as-a-Service (GPUaaS) and AI-native cloud solutions provider"*, a *"neocloud platform"*, under the name *"NewBird AI"*, providing
*"access under long-term lease arrangements"* (EX-99.1 of 2026-04-15); by August, *"We do not intend to offer on-demand "pay-as-you-go"
pricing."* Two weeks before that April plan, the plan was dissolution.

### The scarce input this business controls
**None, by the filer's own account.** The CEO: *"capital alone does not create customers, and a public listing does not create a moat."*
The 10-Q's risk factors: competitors have *"superior access to capital, better procurement terms, more sophisticated technical
capabilities"*; *"value in the AI ecosystem may accrue disproportionately to chip designers, hyperscalers, cloud platforms, model developers,
software providers or vertically integrated operators, rather than to independent owners or lessors of computing equipment"*. The asset is
bought from a concentrated supplier by anyone with money; this buyer's money is among the dearest in the market (about 19.5%, above). The
letter names the intended advantage as *"the expertise we build as we deploy and operate that hardware"*, **in the future tense**; it is not
held today.

### Will the fundamentals look broadly the same in ten years?
**Nothing about them is fixed yet, and the filer says the ground moves.** *"The markets for GPUs and related computing infrastructure are
characterized by rapid technological change, vendor concentration and supply-chain dependencies ... and our AI Infrastructure may become
obsolete or less available more quickly than we expect"*; demand *"may also be affected by changes in model architectures, software
optimization, inference efficiency, the adoption of alternative chips or system designs"*. The registrant has changed its entire business
once in 2026 and its stated plan for the new one twice. And the sentence that decides the verdict's kind, in the filer's own words:
**investors *"may have difficulty evaluating our future prospects because ... we have continued and will continue as a public company with
a limited operating history in a new business and no historical information relevant to that business."***

### The case for IN, built first and not taken
A lessor is among the simplest businesses to understand: buy an asset, rent it for more than the money costs, recover the residual. The
one lease's arithmetic is fully stated in Note 11 and took minutes to reconstruct. **Why it is not IN:** understanding one contract is not
understanding how the business makes money. The business has one contract, three months old, with one customer; its rate roughly equals
its funding cost; its overhead runs at more than thirty times its annual lease receipts (about $33M a year at the half-year's rate against about $1.0M); and the product it says it will sell (managed dedicated
clusters on committed contracts) has no filed instance. **Marking Q1 IN would rest the gate on "expect" and "intend", which is the
provisional IN the framework forbids.**

### The case for OUT, built at full strength and not taken
**[E3-31]** excludes a business *"subject to constant change"*, and the filer puts its own market in that class (*"rapid technological
change"*, obsolescence *"more quickly than we expect"*); **[E4-46]**: *"if we can’t make a decision in five minutes, we can’t make it in five
months"*, and a business that would take months of study is outside the circle, which no fetch repairs. On this reading the answer is
already in: an independent GPU lessor in a market its own filer calls one of *"rapid technological change"*, funded at about 19.5%, is not "relatively simple
and stable in character" whatever its record becomes. **Why it is not taken:** OUT is permanent and a finding about the business, and here
there is almost no business to find about: one lease and a plan restated twice in four months. **The queue's precedent for exactly this
case is UNKNOWABLE**: HHH (2026-09-02, twenty-six days of filed history), RGTI (2026-09-13, *"the declared model ... is not the filed
business"*) and above all DJT (2026-09-18, *"THE COMPANY THE SHARE BUYS IS NOT YET DECIDED"*), each recording the [E4-46] case and not
taking it. The run follows the precedent and says here, for any reopening: **the [E3-31] and [E4-04] constant-change argument should be run
first, because the filer's own risk factors already make it.**

### The brief's prior, tested at the gate where it belongs
The brief warned against a streak of Q2 closes on consumer brands and asked for the strongest franchise case (brand, repeat purchase,
pricing, direct-to-consumer data). **That case concerns a business the share no longer buys**, and the gate that catches the mistake is
this one, not Q2: a Q2 verdict on the Allbirds brand would have been a verdict on American Exchange Group's asset. The brand's franchise
case is recorded at Q2 (not governing) because the brief asked for it and because its auction is the best evidence the corpus's own test
could want.

### Can I name the document that would resolve this?
**No.** The record that would show how Smartbird makes money (several years of filed contracts, customers beyond one, per-deployment
returns net of funding and overhead, renewals, the hardware's resale values) does not exist yet. The next dated filing, the Q3 2026 10-Q
(due about mid-November 2026), will add one quarter; it cannot resolve the question and is named only as the next evidence.

- **VERDICT: [ ] IN [ ] OUT [ ] UNRESEARCHED [x] UNKNOWABLE → the company the share buys is a three-month-old GPU lessor with one contract,
  one customer and a plan restated twice, and by the filer's own words has *"no historical information relevant to that business"*
  [E3-31, E4-46]. CLOSED WITHOUT PREJUDICE. No finding about the business is made; the case for OUT is recorded above for any reopening.**

**The file closes here.** Q2 to Q6 below are RECORDED, NOT GOVERNING, as the HHH, RGTI and DJT precedents do; any valuation is headed
`COMPUTATION — NOT A CLEARANCE` and carries no entry language.

---
## Q2 - IS IT A FRANCHISE? **[E3-03]** *(RECORDED, NOT GOVERNING: the file closed at Q1)*

*Recorded because the precedents record every later gate after a close, and because the brief asked for the strongest franchise case.
Nothing here changes the verdict.*

### Part A: the brief's franchise case, for the Allbirds brand, argued first and then tested
**The strongest case the filings permit.** The FY2025 10-K: *"We believe our brand strength will enable us to continue to grow brand
awareness, allowing us to deepen relationships with consumers and expand our access to global markets"*; a mostly direct-to-consumer model
(*"The majority of our revenue is from sales directly to consumers via our digital and retail channels"*), which gives the seller its buyers'
data; gross margins of 41-53% (FY2021-25) that a commodity maker would not earn; distinctive materials (wool, tree fibre, sugarcane foam).

**The test.** (1) **The buyers' vote, in the numbers**: revenue $277.5M, $297.8M, $254.1M, $189.8M, $152.5M (FY2021-25), **halved from its
peak in three years**; gross margin 52.9% (FY2021) to 41.1% (FY2025); an operating loss in every filed year FY2019-25, -$153.0M at worst
(FY2023); 15 US stores closed in 2024 and 10 in 2025. A product *"thought by its customers to have no close substitute"* **[E3-03]** does not
lose half its customers' dollars while its category does not. (2) **The owners' vote, which is the corpus's own attacker's test run live
[E2-45]**: the DEFM14A's chronology records **91 parties contacted** over five months by TD Cowen; offers for the intellectual property alone
of about **$30M** (Party C) and **$30-40M** (Party N); the winning offer **$39M** for the trademarks, inventory ($38.9M at book on
2025-12-31) and receivables, with about $26.5M of payables assumed. **The brand, with its customer lists and domains, fetched roughly what a
buyer would pay for its stock of shoes.** (3) The fairness opinion's liquidation range for the whole company: *"$0.2 million to $16.9
million"*. **Class for the brand: NONE, on the filer's own record and its own auction.** And the registrant no longer owns it.

### Part B: Smartbird, the business the share buys
**The three conditions [E3-03]:**
- **Needed or desired: yes.** Computing capacity for AI is bought; the one lessee pays for it.
- **No close substitute: NO, by the filer's own words.** *"Customers may prefer to procure computing capacity from hyperscale cloud providers,
  vertically integrated platforms, strategic partners or operators with established technical, operational and financing capabilities,
  rather than from us."* The product is servers built on NVIDIA's GPUs, the same parts every rival buys; the filer: *"value in the AI
  ecosystem may accrue disproportionately to chip designers, hyperscalers ... rather than to independent owners or lessors of computing
  equipment."*
- **Not price-regulated: yes.**

**Must the moat be continuously rebuilt? [E4-04]** Its basis would be replaced by design: the filer's own model manages *"the entire
lifecycle, from procurement and deployment to operations and hardware refreshes"*, in markets *"characterized by rapid technological
change"*. **Each refresh buys a replacement, not a defence** (v4's scoping test). This is **[E3-51]**'s *"competitive destruction"* from
both sides at once: the registrant left one business that died in its hands and entered another where, in Munger's words from the same row,
*"there are huge advantages for the early birds"*, and it is not early. **Does success depend on a great manager? [E4-23]** The plan is
the new chief executive's (*"Having spent the last several years close to the buildout of computing infrastructure"*, the letter); the board
hired her to build a business that does not yet exist. **Recorded as a moat defect here, as v4 requires**: the manager is the plan.

**Primary moat metric and trend:** none measurable; one contract, one quarter.

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4)*
Same metrics, each filer's latest filed fiscal year (the lessee's latest half), from companyfacts transcriptions of the filed statements
(`peers/peer_row.py`, `peers/peer_row_out.txt`); **one figure checked to a face**: QumulusAI's H1 2026 *"Operating loss | ... | ( 13,197,322
)"* (10-Q/A `0001628280-26-059295`) equals its companyfacts -13,197,322.

| filer | period | revenue | operating margin | owner cash (OCF - SBC - capex) / revenue | note |
|---|---|---:|---:|---:|---|
| **Smartbird (BIRD), continuing** | H1 2026 | $2.8M | **-606%** | **-452%** (OCF -$7.3M, SBC $2.4M, capex $2.8M) | one lease, booked as a sale at zero margin |
| QumulusAI (QMLS), the lessee | H1 2026 | $10.1M | -130% | OCF +$22.3M on customer deposits | own going-concern doubt, which management says its plans *"will alleviate"* |
| CoreWeave (CRWV) | FY2025 | $5,131M | -0.9% | -153.6% | the largest in the row |
| Nebius (NBIS) | FY2025 | $529.8M | -115.5% | -710.5% | |
| IREN (IREN) | FY to 2026-06-30 | $707.0M | -148.0% | -156.0% | |
| Applied Digital (APLD) | FY to 2026-05-31 | $611.3M | -38.7% | not resolved (capex tag) | |

- **Peers named: five filers.** The industry's real competitors also include what the filer calls *"hyperscale cloud providers"*, whose
  AI-infrastructure results are not reported as a segment, and private GPU clouds that file nothing. **Smartbird's filings name no
  competitor** (the Q2 10-Q, the supplemental risk factors and the CEO's letter grepped for nine rival names: zero hits). The four listed
  public GPU-infrastructure filers were chosen by this run; how many real competitors the industry has is not stated in any filing read.
- **The row's reading:** Smartbird is **the smallest in the row** (its own lessee about four times its revenue, the others two to three orders of
  magnitude larger), with the worst operating margin, and **no filer whose owner cash resolves earns it positive**: the independent class
  is consuming capital in its build. The row states position,
  not conduct **[E3-61]**.
- **The lessee is itself a counterparty risk**: QumulusAI's 10-Q/A: *"These factors raise substantial doubt about the Company’s ability to
  continue as a going concern"*, then *"management concluded these plans will alleviate the substantial doubt"*, the plans including *"an
  additional $15,300,000 draw under the USD.AI protocol"*. Smartbird's entire revenue rests on that one balance sheet.
- **Untapped pricing power [E3-33]:** none; the price is set by lease terms negotiated against larger lessors with *"better procurement
  terms"*. **The two-characteristic test [E2-44]** fails on both limbs: no pricing power, and growth needs capital dollar for dollar (every
  lease is a purchase). **The number [E3-46]:** the one lease earns about 19% on its cost, roughly what its funding costs.
- **The four causes of extreme success [E4-36]:** none is present. The fourth, *"Catching and riding some sort of big wave"*, needs a rider already up; Smartbird entered in April 2026 with
  one lease.
- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: not measurable.**
- **VERDICT (recorded, not governing): would be OUT** on [E3-03] criterion 2 in the filer's own words, with [E4-04], [E4-23] and the row.

---
## Q3 - ARE THEY HONEST, AND ARE THEY RATIONAL? *(RECORDED, NOT GOVERNING: the file closed at Q1)*

### STEP 1 - THE WEIGHT CASE: a GATE, on daily execution
- [x] **Daily execution [E3-38]**: the business is a sequence of capital decisions (which hardware, for which customer, on what term, at
  what funding cost) in a market the filer calls one of *"rapid technological change"*, against rivals with *"better procurement terms"*.
  Every lease is a new purchase; there is no base business to carry a bad decision.
- [ ] **Control [E1-16]**: not ticked (a minority public holder can sell). *For the record:* the Class B holders carry about two-thirds of
  the votes (DEF 14A, record date: Maveron entities 24.6%, co-founder Timothy Brown 20.3%, co-founder Joey Zwillinger 18.3%, director Dick
  Boyce 2.7%), signed support agreements for the June vote, and were left out of the fairness opinion's audience (it *"expressly excludes Maveron,
  LLC, Joseph Zwillinger and Timothy Brown"*).
- [ ] **Leverage [E3-29]**: not ticked today ($8.25M of notes against about $34M of cash). **It can become ticked without a vote**: $91.75M
  more notes are issuable *"solely at the option of the holders"*, secured on *"all of the other assets of the Company"*.

**Case: a GATE.** No price compensates a failure here.

### Honesty - binary, permanent, filings-based **[E5-16]**, each matter dated to when it became public
- **Securities class action** (*Shnayder v. Allbirds*, N.D. Cal., filed 2023-04-13; IPO-era statements): dismissed three times, the last
  *"with prejudice"* on 2026-02-27; plaintiffs appealed to the Ninth Circuit (opening brief 2026-06-10, the company's answer 2026-08-10).
  Two derivative suits in Delaware (2023) stayed. **No finding of misconduct.**
- **No SEC enforcement matter** found in the FY2025 10-K or the Q2 2026 10-Q (searched: "subpoena", "Wells notice", "SEC investigation", "investigation by the SEC":
  zero; the five "enforcement action" hits are generic privacy and regulatory risk factors).
- **No restatement** (no Item 4.02 in the filings list); **no material weakness** disclosed; disclosure controls *"effective at the
  reasonable assurance level"* at 2026-06-30.
- **Verdict on the binary: no disqualifier found.** Under **[E5-17]** that is the absence of found disqualifiers, not a finding that anyone
  is honest.

### STEP 2 - THE FLAGS **[E4-22, E5-15, E4-29]**, each a prompt to read, never a verdict
- [x] **A projection given to stockholders before their vote, against the outturn [E3-48, E4-22].** The merger proxy of 2026-05-08, on which
  the 2026-06-03 vote was taken: *"The Board currently anticipates that the Asset Sale Dividend may be approximately $1.34 per share of
  common stock (based on 6,220,796 shares of Class A common stock and 2,540,381 shares of Class B common stock outstanding on the Record
  Date)"*, about $11.7M; the fairness opinion was given on *"the $1.34 per share of common stock ... that management of the Company
  estimated would be available to distribute"*, and *"based on certain assumptions, including the assumption that ... the Company would
  proceed with a dissolution"*, which the same proxy says the company would not do. **Outturn: $0.31 a share, about $3.6M, 77% less per
  share**, paid on a record date (2026-06-25) on which, by the filer's own arithmetic ($3.6M / $0.31, about 11.6M shares), the new ATM shares sold
  after the proxy took part. The proxy did warn *"The final
  amount ... may vary significantly from this estimate"*. **A prompt, not a finding**: the difference is the cash the new business spent
  (the half-year's continuing operating cash, the GPU purchase, the notes' costs) plus the new shares.
- [x] **Dividends paid while capital is raised [E2-52]** (*"Beware of "dividends" that can be paid out only if someone promises to replace
  the capital distributed."*): the $3.6M dividend was paid in the same season as **$15.4M of new shares sold** and **$7.3M of notes
  borrowed**. The dividend came from the sale proceeds, not from earnings, so the flag fires in form; its substance is that the owners got
  back a quarter of what they were told to expect while the company raised about six times the dividend from new holders and lenders.
- [x] **Serial share issuance [E5-15]**: weighted shares 8.16M (FY2025) to **11.81M on the cover (+45% in a year)**; an ATM of up to
  $98.1M and a note facility of up to $100M against a $27M market value; *"access to over $200 million of capital"* (the CEO's letter);
  a 2026-09-30 proposal for 3.5M more plan shares (*"total potential overhang is expected to increase by 29.6% to 55.3%"*) and for
  conversions above 19.99%.
- [x] **Adjusted EBITDA [E4-29]**: presented and reconciled in the Q2 2026 10-Q's MD&A (*"Adjusted EBITDA $ | (8,683 )"* for the quarter)
  and 21 times in the FY2025 10-K.
- [x] **Pay and incentives [E4-27, E3-70]**: in H1 2026, **2,423,569 RSUs granted at a weighted $5.97, about $14.5M of grant value, 20.5%
  of the shares outstanding**, all service-vested (the CEO's inducement award 1,532,379 RSUs, 255,397 vested on grant; the CFO 766,190;
  the chair 125,000); the three-year average *"Burn Rate"* the proxy reports is 5.3%. Pay unrelated to any per-share result, granted
  against a charge of $2.4M in the half.
- [x] **Stock-price promotion, as a prompt only [E3-50]**: the pivot was announced on 2026-04-15, the stock rose from $2.49 to $16.99 on
  288.2M shares that day, the ATM was signed on 2026-04-28 and sold 2,590,758 shares for $15.4M net by June 30 (about $5.96 each). The
  filings show the sequence; they do not show intent, and the run records no finding about it.
- [x] **The institutional imperative [E2-30]**: (2) *"corporate projects or acquisitions will materialize to soak up available funds"*:
  the sale proceeds were, on 2026-03-30, to be distributed on a dissolution; by 2026-04-15 they were funding a new business. The proxy's
  whole stated reason for the facility: *"The Board believes that the ability to continue as a going concern, and for stockholders to
  continue to have their shares listed and traded on Nasdaq, following the Asset Sale and Asset Sale Dividend, is beneficial and in the best
  interests of our stockholders."* **No filing read sets the expected return of the new business against the cash's return to its owners**;
  the proxy's chronology of the asset sale runs eight pages and there is no chronology of the pivot. (4) imitation: the move is into the
  market the row's larger filers were already in; recorded without a finding on motive.
- [x] **Candor [E2-26], two prompts.** (i) The FY2025 10-K, filed 2026-03-31, says *"the Company does not expect to continue its operations
  following the completion of the Asset Sale"*; the facility that continued them was signed fourteen days later. (ii) The Item 4.01 8-K of
  2026-07-29 says Deloitte's reports *"were not qualified or modified as to uncertainty"*, while Deloitte's FY2025 report carries a paragraph
  headed *"Going Concern"* (*"the Company has experienced recurring net losses and negative cash flows that raise substantial doubt about its
  ability to continue as a going concern"*); Deloitte's letter (EX-16.1): *"We agree with the statements made in the paragraphs one
  through four of Item 4.01(a)."* Whether an explanatory paragraph
  counts as a modification under Item 304 is a reading this run did not settle from a primary source; **recorded as a prompt, not scored.**
- [ ] Filed-figure tells [E4-30]: not run (no multi-year series of the new business exists).
- **Also recorded:** an auditor change (Deloitte, auditor since 2017, dismissed 2026-07-28; BPM LLP engaged); a late 10-Q (NT 10-Q,
  *"The Company requires additional time to review and confirm the accounting treatment for its Asset Sale"*); a director's sale of 9,200
  shares at $2.38 on 2026-08-25.
- **Converging [E4-52]:** the projection shortfall, the issuance, the stock-paid team, the timing of the ATM after the announcement and
  the unargued choice of a new business over a distribution all point one way, toward the listing's survival being the object. Treated as
  one system, as v4 requires, and still a prompt: the corpus's own warning that a fired flag is not a venality finding stands **[E5-38]**.

### STEP 3 - THE PRIMARY TEST [E2-01], balance sheet first
Stockholders' equity $397.0M, $316.8M, $185.3M, $101.7M, $35.9M at the year ends FY2021-25; $22.5M at 2026-06-30. Net loss on average
equity **-24.4%, -28.4%, -60.7%, -65.0%, -112.3%** (FY2021-25; `oe_out.txt`); the continuing company lost $18.9M in H1 2026 on $22.5M of
closing equity. **Every year fails, and the IPO's $397M of equity was consumed in four years.** The new management has no record of its own
here; the directors who oversaw the four years (the co-founder Brown; Dan Levitan, a managing member of Maveron's general partner; Boyce until 2026-09-30) remain on the board.

**The half-owner test [E2-26]:** the 10-Q separates continuing and discontinued lines at every level, which passes; the dividend estimate
and the dissolution language, above, are where the reporting told owners less than the positions reversed would want.

**The institutional imperative, scored [E2-30]:** [ ] (1) resists change (the opposite: two changes in a quarter) · [x] (2) funds soaked up
· [ ] (3) staff studies for the leader's craving (none filed) · [x] (4) peer behaviour imitated (a prompt, above).

**Capital allocation - the two buyback conditions [E5-08]:** no buyback. The allocation that matters is the choice between returning the
sale proceeds and funding a new business; **the corpus's first law applies [E5-24]** (*"what is smart at one price is dumb at another"*),
and no filing states the price, in expected return, at which the board judged the new business better than the cash in owners' hands.

**THE GUARDRAIL.**
- [x] Nothing in this Q3 is used to promote the name.
- [x] **The business requires a great manager [E4-23]**, recorded at Q2 as a moat defect.
- [x] **Is the manager the plan? [E2-35, E2-36]** Yes. There is no franchise with an *"excisable cancer"*; there is a new chief executive
  hired to build a business from one lease: the *"corporate Pygmalion"* case the corpus distinguishes and does not buy.

- **VERDICT (recorded, not governing): IN on the binary** (no disqualifier found), **with nine converging prompts**; a GATE case in which,
  had the file reached here, the capital-allocation reading (the owners' cash redirected without a stated return) would bind before price.

---
## Q4 - WILL IT SURVIVE? *(RECORDED, NOT GOVERNING: the file closed at Q1)*

### Owner earnings **[E2-23]** - from the filed cash-flow faces (`oe.py`, output `oe_out.txt`), $M
**A perimeter warning first, because it decides what these numbers mean.** Every annual year below is the **footwear business, sold on
2026-06-09**. The windows are shown because the framework requires the multi-year mean and because they are what the triage priced; **they
describe a business the share no longer buys.** The only figures of the business it does buy are H1 2026's continuing operations, at the end.

| FY | operating cash | stock comp | capex | D&A | OE, D&A end | OE, capex end |
|---|---:|---:|---:|---:|---:|---:|
| 2021 | -50.9 | 11.2 | 24.2 | 9.7 | -71.7 | -86.3 |
| 2022 | -90.6 | 19.9 | 31.4 | 14.7 | -125.1 | -141.8 |
| 2023 | -30.2 | 19.3 | 10.9 | 21.0 | -70.6 | -60.4 |
| 2024 | -63.9 | 11.5 | 4.1 | 12.4 | -87.7 | -79.4 |
| 2025 | -55.1 | 7.8 | 3.1 | 8.0 | -70.9 | -66.0 |

- **Five-year mean FY2021-25 (the default window [E2-42]): -$85.2M (D&A end) to -$86.8M (capex end).**
- **Three-year mean FY2023-25: -$76.4M (D&A end) to -$68.6M (capex end).**
- **Twelve months to 2026-06-30, whole company** (FY2025 less H1 2025 plus H1 2026, continuing and discontinued together, from the faces):
  operating cash **-$41.7M**, stock compensation **$7.7M** (the equity statements' $4,399 thousand and $4,380 thousand for the halves),
  capex **$1.8M** excluding the GPU purchase: **about -$51.2M at the capex end, -$54.0M if the $2.758M GPU purchase is counted**; the D&A end
  cannot be built, because H1 2026's footwear D&A sits inside a $22.8M aggregate of non-cash items in discontinued operations.
- **The business the share buys, H1 2026 continuing operations**: operating cash -$7.3M was flattered by working capital (**+$8.5M**:
  prepaid expenses released $7.3M, accrued liabilities rose $6.6M, of which employee-related liabilities $6.8M at June 30); before those
  movements and after stock pay, **-$18.2M for the half, about -$36M a year at that rate**. Maintenance capex for a GPU lessor is the whole
  cost of the fleet over its life ([E5-20]'s class, where the D&A end is invalid); with one lease there is no fleet to average.
- **Stock compensation subtracted in full [E5-06]**, at the charge. **The [E3-70] measure is larger**: H1 2026's grants carried about **$14.5M
  of grant-date value** (2,423,569 RSUs at $5.97) against a $2.4M continuing charge, so the charge-based figures above flatter the new
  business by up to about $12M for the half. SBC resolves for every year (no SBC-of-zero); no stock-settled item was found outside the SBC
  elements (the notes' interest may be paid in shares, and will appear as interest).
- **Is the range too wide to conclude? No [E4-25]**: every window and every (c) end is negative by tens of millions against a $27.2M market
  value. The distorted years are named: FY2022-23 (peak spending and a -$152.5M loss year), and H1 2026 (the sale, severance accruals, the
  pivot).

### Great, good, or gruesome? **[E4-20]**
- [ ] great · [ ] good · [x] **gruesome**: the footwear business *"both pays an inadequate interest rate and requires you to keep adding money
  at those disappointing returns"*, and the new one needs capital for every contract, funded at about 19.5%, to earn about 19% before
  overhead. v4's reading of the class (consumed cash is gruesome only where it fails to earn a reasonable return) is not met on any filed
  figure.

### Staying power **[E5-11]** - scored on the worst case [E2-55]
- (1) **A large and reliable stream of earnings: none.** One lease, about $1.0M a year of receipts, from one lessee with its own
  going-concern doubt.
- (2) **Massive liquid assets: modest.** About $34M of cash after the dividend, against a continuing burn of about $36M a year at the
  half-year's rate: **about one year**, before any new fleet is bought.
- (3) **No significant near-term cash requirements: fails in structure.** The notes (*"senior secured obligations"*, 12%, maturing 2028)
  carry a **125% redemption premium** on default or change of control and let the holders require redemption from *"25% of the gross proceeds of any Subsequent Placement and 100% of the gross proceeds of any
  asset transfer or sale"* (8-K of 2026-04-20); the leftover store leases carry $6.3M of liabilities; June's employee-related
  accruals are $6.8M. The plan itself is a standing cash requirement: *"We expect to fund our operations through debt or equity
  financings, as well as expected future operating cash flow."* (10-Q, liquidity). **This is the kindness of strangers [E5-39] written into the business model.**
- **Leverage, named and quantified [E4-16, E3-29]:** $8.25M face of secured convertible notes today; up to $91.75M more at the holders'
  option. **Coverage [E2-54]:** interest of about $1.0M a year cannot be met *"out of current cash flow net of ample capital
  expenditures"*; it is payable in shares, which is the same test failed in another currency.

### The specific way THIS business dies **[E2-27, E3-24, E4-40]**
- **The mechanism: dilution through a conversion price with no floor, before insolvency.** The notes convert at *"93% of the lowest volume
  weighted average price"* of the prior ten trading days (85% in default); the holder's profit is the discount, so conversion and sale are
  rational for it at any price; each conversion adds shares that press the price that sets the next conversion. The ATM (up to $98.1M) and
  the 3.5M plan shares add supply. **Survival shape #8, THE EQUITY IS THE REVENUE** (customers pay a small part of the costs, new
  shareholders the rest), **with #6, THE BORROWED BALANCE SHEET, as a feature** (a lessor funded by two-year secured notes against
  three-year leases to a lessee whose own plans include *"an additional $15,300,000 draw under the USD.AI protocol"*).
- **Quantified from filed figures:** at $2.30 the alternate conversion price is about $2.1, so the **$8.25M of notes alone convert into
  about 3.9M shares, a third of the count**; every further $10M drawn under the facility at that price is about 4.8M more (40%). Funding one
  year of the half-year's continuing burn (about $36M) through the ATM at $2.30 would take about 15.7M shares, **more than the whole
  current count**. Book equity, $22.5M at June 30, less the $3.6M dividend and a quarter at Q2's rate net of stock pay (about $10.8M), is
  about $8M, **about $0.70 a share at September 30 before any issuance** (arithmetic at a stated rate, not a forecast; the Q3 10-Q will show).
- **Exposure, not experience [E4-40]:** the fleet is one lease today; the exposure the plan creates is hardware bought with dear money,
  leased so far to one young, loss-making lessee, in a market the filer says may make it *"obsolete or less available more quickly than we expect"*.
- **Likelihood: [x] likely** that the owner of a share today owns a much smaller fraction of the company within the notes' two-year term;
  insolvency inside a year **a low-level possibility** while about $34M of cash remains and the ATM is open.
- **VERDICT (recorded, not governing): would be OUT** (gruesome; none of [E5-11]'s three strengths; [E2-54] failed).

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q1 is UNKNOWABLE; the file is closed. What follows is recorded, as the precedents do.

---
## Q5 - WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND? *(COMPUTATION — NOT A CLEARANCE)*

### COMPUTATION — NOT A CLEARANCE
*Headed as operator rule 3 requires. No entry language; no band; no ranking.*

**THE FLOOR FIRST [E4-28].** The honest pre-tax expectancy at this price cannot be stated as a positive number: owner earnings are negative
in every window, of the sold business and of the one the share buys. The name is not ranked; under the floor it would be quit on even if
Q1-Q4 had cleared.

**1. THE YIELD** (`oe_out.txt`), at US$2.30 (2026-09-18 close, aggregator flagged) x 11,809,193 = **$27.2M**:

| numerator | owner earnings | yield | points against the 5.34% sovereign |
|---|---:|---:|---:|
| five-year FY2021-25, D&A / capex end (the sold footwear business) | -$85.2M / -$86.8M | -313.7% / -319.6% | -319.0 / -324.9 |
| three-year FY2023-25, D&A / capex end (the sold footwear business) | -$76.4M / -$68.6M | -281.3% / -252.6% | -286.6 / -257.9 |
| twelve months to 2026-06-30, whole company, capex end, without / with the GPU purchase | -$51.2M / -$54.0M | -188.5% / -198.8% | -193.8 / -204.2 |
| **the business the share buys: H1 2026 continuing, before working capital, after stock pay, x2** | **about -$36.5M** | **about -134%** | **about -140** |

**The first three rows repeat the triage's mismatch (Step 0, reading (e)) and are shown only so a reader can see it**: they divide a sold
business's losses by the value of the company that sold it. The fourth row is the only one that describes what the price buys, and it is a
half-year annualised, not a multi-year mean.

**2. WHAT THE PRICE ALREADY ASSUMES.** The ~10% floor needs owner earnings of about **+$2.7M a year** on this cap, against a continuing
business consuming about $36M a year: a swing of about $39M a year, from a base of one lease earning about $0.4M a year of interest. Year-1
growth needed from a negative base is **not a number** (the MRVL rule, RESUME STATE item 3D). In words: the quote assumes that a company
with one customer and funding dearer than its lease yield becomes, within a few years, a profitable fleet operator, or that its cash is
worth more than its book in someone else's hands. **The corpus's base rate for sustained high growth among the best businesses is *"fewer
than 10 of the 200 most profitable companies"*** **[E4-35]**, and this is not among the profitable.

**3. WHAT YOU ARE PAID.** About **140 points under the sovereign** on the continuing business; more on every other row; below the floor by
more.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]:** no owner-earnings value above zero exists on any window. **The only positive anchor is the
balance sheet**: book equity $22.5M at 2026-06-30, **$1.91 a share**; less the $3.6M dividend and a quarter at Q2's loss rate net of stock
pay, **about $0.70 a share at 2026-09-30** before any issuance (arithmetic at a stated rate, not a forecast); and the fairness opinion's
liquidation range for the whole company, done before the pivot, was *"$0.2 million to $16.9 million"*. **So the value lies roughly between
nothing and about $0.70 to $1.90 a share, falling each quarter the plan spends; the price of $2.30 is above the whole range.** What bounds
the upside [E2-63]: no filed document states an owner-earnings level for the new business; the CEO's letter declines to (*"we will share
updates on key benchmarks"*).

**Bar used:** neither applies; there is nothing to apply a margin to and no conservative case above the price to screen. **Windage count:**
zero; the (c) band is displayed, not stacked.

- **VERDICT: not reached** (the file closed at Q1). Computation recorded: price above a range whose top is book value, and book is falling.

## Q6 - WHAT WOULD PROVE ME WRONG? *(recorded; reopening conditions in words, no band)*

**No alert band is armed and no PORTFOLIO row is added.** The file closed at Q1 without a finding about the business; a price alert would
presume a business the filings do not yet show (the QLYS ruling, 2026-09-07, applied as the HHH, RGTI and DJT runs applied it).

**The reopening conditions, pre-committed in words [E1-02]:** reopen Q1 only when **all** of the following appear in filed documents:
1. **A record exists**: at least two full fiscal years of the AI-infrastructure business in audited statements (the first possible is
   FY2027, with FY2026 a part-year).
2. **More than one customer**: several lessees or service customers, no one of them above half of revenue, with the filed contract terms.
3. **The contracts earn more than the money costs**: lease or service yields above the cost of the funding that bought the hardware, after
   overhead, i.e. operating income positive for a full year; and the convertible notes repaid or converted without new floorless paper.
4. **Owner earnings positive** for a full year (operating cash less stock pay at the larger of charge and grant value [E3-70] less the
   fleet's replacement), with no ATM sales in that year.
5. **The constant-change question answered in the record**: contracts renewed or re-leased on hardware a generation old at rates the filings
   show, which is the only evidence that could meet [E3-31] and [E4-04] rather than be argued past them. **On reopening, run the Q1 OUT case
   (recorded above) first.**

**Thesis-breaking signals that would turn a reopening into OUT at once:** a draw of the remaining $91.75M of notes on the same floorless
terms; a second change of business; the lessee's default; any restatement.

- **VERDICT (recorded): not reached.** Next dated evidence: the annual meeting of **2026-09-30** (the 3.5M plan shares and the conversions
  above 19.99%), and the **Q3 2026 10-Q** (due about mid-November 2026), the first full quarter of the new business, the post-cover share
  count, and any conversions, ATM sales or further dividend.

---
## SELF-AUDIT
- [x] Questions answered in order; the file stopped at Q1 (UNKNOWABLE) and Q2-Q6 are labelled recorded, not governing.
- [x] No question marked IN. The one IN written (Q3's binary, recorded) is worded as the absence of found disqualifiers [E5-17].
- [x] No UNRESEARCHED verdict. The unfiled items (the post-cover share count, conversions, the dividend's payment, the Q3 quarter) are named
      with the document that will carry them (the Q3 2026 10-Q) and none could change the Q1 verdict.
- [x] The UNKNOWABLE verdict states what cannot be known (how the new business makes money: no record of it exists, by the filer's own
      words) and answers the separating test (no document exists that would resolve it); the case for IN and for OUT are both recorded.
- [x] Step 0: the filing was read (10-Q Q2 2026 `0001437749-26-028446` whole; 10-K FY2025 `0001628280-26-022192` in part; the DEFM14A,
      the DEF 14A and the 8-Ks listed), and five figures were cross-checked against filed faces (FY2025 and FY2024 operating cash, stock
      pay, capex and D&A; H1 2026 continuing operating cash), all identical to companyfacts.
- [x] Owner earnings on multi-year means (five-year default, three-year, twelve months), both (c) ends shown where they can be built, (c)
      disclosed as a judgment, and **the perimeter stated: every annual year is a sold business**; the continuing half-year shown apart.
- [x] Competitor row filled (recorded): five filers, same metrics, latest filed periods, one figure checked to a face; the unsegmented and
      private rivals named as a class and the reason they are absent stated; Applied Digital's capex not resolved and said so.
- [x] Sovereign for the earnings currency (USD), from the issuing authority (US Treasury), dated 09/18/2026, struck by this run.
- [x] Value stated as a range (nothing to about $0.70-1.90 a share, from the balance sheet), not a point estimate.
- [x] One bar only, and neither applied; windage count zero.
- [x] Price dated (2026-09-18 close), aggregator flagged, corroborated at three filed dates (the 06-18 RSU grant value, the proxy's 05-07
      price, the 09-02 Form 4s).
- [x] Share classes summed only after the charter was read (identical except votes; one-for-one conversion); the DEF 14A record-date total
      matches the cover sum; post-cover changes named.
- [x] SBC resolved and complete; the [E3-70] grant-value measure computed from the RSU table; the notes' share-paid interest identified.
- [x] Deal read (ROKU lesson): the deal form was the registrant's own asset sale, closed 2026-06-09; no offer for BIRD; not a spread.
- [x] Every ledger id cited was checked against `principle_ledger.csv` (one row each; `ledger_check.py`, `ledger_out.txt`).
- [x] Run committed to git (template `4ae1654`, Step 0 `4effd47`, Q1 `2e565af`, Q2-Q4 `a6641a5`, Q5-Q6 with audit and register in the
      commit that carries this line; the fold in the fold commit).
- [x] No em dashes written by this run (the required heading and verbatim quotations keep theirs).
- **Quotation note (prime rule 1):** stripped inline-XBRL text reads *"$ 0.1 million"* and *"( 13,197,322 )"*; in running text the dollar
  sign is closed up to the number (*"$0.1 million"*), and nothing else in any quotation is altered; ellipses mark every cut.

### CORRECTIONS MADE BEFORE CLOSE (my own errors, caught before the commit of the section that carried them)
1. **A misquotation at Q1**: the draft put *"expected"* in quotation marks; the 10-Q says *"We expect our customers to purchase"*. Corrected
   to the exact sentence.
2. **A wrong multiple at Q1**: "overhead about fifteen times its annual lease income". The half-year's overhead runs at about $33M a year
   against about $1.0M of lease receipts: more than thirty times. Corrected.
3. **Two general-knowledge labels at Q2**: IREN as "a former bitcoin miner" and CoreWeave as "the largest pure-play" came from memory, not a
   filing. Removed and reworded ("the largest in the row").
4. **Two overstatements at Q2**: "no filer in the row earns positive owner cash" (QumulusAI's and Applied Digital's did not resolve) and
   "smallest by two to three orders of magnitude" (the lessee is about four times Smartbird's revenue). Both narrowed to what the row shows.
5. **Two bracketed edits inside quotations at Q3** (*"exclude[d]"*, *"agree[s]"*), which prime rule 1 does not allow. Replaced by the exact
   filed text.
6. **Two counts at Q3**: "twice the dividend" raised (it was $22.7M against $3.6M, about six times) and a "ten-page" chronology (eight).
7. **A misread obligation at Q4**: "must be redeemed with 100% of the gross proceeds" of an asset sale; the 8-K gives the holders the
   right to require it. Corrected with the exact clause.
8. **A quotation at Q4 attributed to [E4-20] that is v4's own wording**, not the ledger row's. Reworded without quotation marks.
9. **An unsourced label at Q4**: the lessee's funding source called a "crypto-lending protocol". No filing read says so; replaced with the
   lessee's own words (*"the USD.AI protocol"*). And "lessees" (plural) corrected to the one lessee.

### THE BRIEF'S DEFECTS (every brief in this queue has had at least one)
1. **The name and the business are out of date, and this is the one that matters.** "BIRD (Allbirds, Inc.)" has been **Smartbird, Inc.**
   since 2026-06-15; the Allbirds brand, trademarks, customer lists and inventory were sold to American Exchange Group on 2026-06-09. The
   brief's Q1 prompt (*"after its channel and store changes"*) and its Q2 prompt (*"brand, repeat purchase, pricing, direct-to-consumer
   data"*) both address a business the share no longer buys. Followed literally, the run would have closed a brand at Q2 that belongs to
   someone else. (The brief's own guard, *"do not let the Q2 argument substitute for Q1"*, is what caught it.)
2. **The skip-reason hypotheses missed the decisive reading.** (a) and (b) were right and (c) was right; (d) was refuted (no shell, one
   vintage per cash-flow fact); **the fifth, unlisted reading is the one that explains the row**: the triage's numerator was the losses of a
   business sold before the triage ran.
3. **The reverse-split belief was RIGHT** (1-for-20, effective 2024-09-04, 8-K `0001653909-24-000064`), and so was the implied dual-class
   belief (Class A and B, identical except votes). Recorded as verified, not as defects.
4. **"No screen row" was RIGHT** (confirmed: no BIRD or Allbirds row in any CSV).
5. **"A consumer-brand name recently public with a falling share price"**: public since November 2021, nearly five years; and the latest
   leg of the fall is the pivot's, not the brand's (the price rose from $2.49 to $16.99 on the day the AI plan was announced, 2026-04-15).
6. **The brief did not mention the convertible notes, the ATM or the special dividend**; the standing "Deals" instruction found the asset
   sale's proxy through `deal_note`, and the rest was found by reading the 8-Ks.
7. The ledger ids named in the brief ([E4-27], [E4-52], [E4-26], [E3-41], [E4-28], [E3-03], [E5-20]) were all verified present and used
   as the brief described them. The register count of 116 for SOUN is checked by counting at the fold.

### LIMITS OF THIS RUN
- **The watchlist pricing script is not on disk** (the HBB finding): which count the triage used is bounded (the correct count or the
  split-adjusted pre-IPO count; both trip the yield bound) but not read.
- **The post-cover share count is not filed**: the 2026-09-01 vesting, any ATM sales and any note conversions since 2026-08-10.
- **The dividend's payment is not confirmed by a filing**: the 10-Q and the 8-K of 2026-08-10 give an *"anticipated payment date"* of
  2026-08-20.
- **The lease's implicit rate is reconstructed** from Note 11's schedule, not stated by the filer; **QumulusAI's filings read do not name
  Smartbird**, so the lease is evidenced from the lessor's side only.
- The Q1 2026 10-Q and the FY2021-24 10-Ks were downloaded but their figures enter through companyfacts (single vintage), checked for
  FY2024-25 against the FY2025 face; no earnings-call transcript was read (the FY2025 call was cancelled).
- Kroll's IP-asset analysis in the DEFM14A was not read in full; the brand's value is taken from the bids in the chronology.
- Whether a going-concern paragraph is a "modification as to uncertainty" under Item 304 was not settled from a primary source.
- The competitor row uses companyfacts transcriptions of the peers' statements with one figure checked to a face; the hyperscalers are
  unsegmented and private GPU clouds file nothing.

## REGISTER
- Verdict: [ ] IN [ ] OUT (about the business) [ ] UNRESEARCHED (about my diligence) [x] **UNKNOWABLE (about my evidence), at Q1**
- **One line:** the share sold as BIRD is no longer Allbirds: on 2026-06-09 the footwear business, brand and inventory were sold to
  American Exchange Group for $40.7M, and the registrant, renamed Smartbird, Inc., owns about $34M of cash, $8.25M of floorless convertible
  notes and one $2.758M GPU lease to one lessee that reports its own going-concern doubt; by its own words it has *"no historical
  information relevant to that business"*, its plan was restated twice in four months, and its one contract earns about what its funding
  costs. **Q1 UNKNOWABLE, closed without prejudice**, the case for OUT on constant change [E3-31, E4-46] recorded and named as the first to
  run on any reopening. Recorded, not governing: Q2 would be OUT (the brand's own auction put the trademarks near the value of the shoe
  stock, and the brand is gone; Smartbird fails [E3-03] criterion 2 in its own words); Q3 IN on the binary with nine converging prompts
  (a proxy dividend of *"approximately $1.34"* paid at $0.31, +45% shares in a year, 20.5% of the count granted as RSUs in a half, the sale
  proceeds redirected to keep the listing); Q4 would be OUT (owner earnings -$85.2M to -$86.8M five-year for the sold business, about
  -$36M a year for the new one; shape #8 with #6 as a feature). Price US$2.30 x 11,809,193 = US$27.2M, headed COMPUTATION — NOT A
  CLEARANCE, above a value range whose top is a falling book value. **FAIL at Q1.**
- **If UNKNOWABLE:** what cannot be known is how Smartbird makes money: the record that would show it (several years of contracts,
  customers beyond one, returns net of funding and overhead, renewals across a hardware generation) does not exist in any document.

