# Company Run — Snowflake Inc. (SNOW) — 2026-09-18
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs. **This is a NEW NAME, not a
holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.**

Filled top to bottom. **Stop at the first verdict that is not IN.** Run unattended from scratch. No prior
run file for SNOW exists; the PLTR run of 2026-09-11 used Snowflake as a data-platform comparator, and every
SNOW figure below is recomputed from Snowflake's own filings. WAVE 5, the second of the seven "perimeter or
restatement above threshold" names. Research, scripts and downloaded filings are in
`Test Runs/_research 2026-09-18 SNOW/`.

*Dated note, 2026-09-18 ~18:10 EDT: **this is a RESUMED run.** The unattended session that wrote the header and
STEP 0 (commits `fda9b24`, `adabbbc`, 15:10-15:18 EDT) was killed after Step 0; it never wrote Q1. A fresh session
was handed the disk inventory at about 18:10 EDT and continues from Q1. Step 0 is not rewritten; anything found
wrong in it is corrected in a dated note beside it (operator rule 6). The research files the killed session fetched
after Step 0 and did not commit (companyfacts, submissions, three FY2026 10-K extracts, the `8k/` folder, four
Form 4s and two fetch scripts) are committed with this note and verified before any figure from them is used.*

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Asked aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0: THE SKIP REASON, THE RATE, THE PRICE, THE COUNT, THE PERIMETER, AND THE FILING

### The skip reason, tested on the filing rather than inherited
The wave 5 row is *"perimeter or restatement above threshold: read the filing first"*; the skipped-reason list
says *"revenue step or cross-accession restatement above threshold."* **A prompt to read, never a verdict.**

**Which code produced the label.** The wave 5 table was written at `a8bc84f` (2026-09-01 22:15). The watchlist
triage itself ran at `ce98258` (2026-09-01 20:53) *"through the same pipeline as the sweep"* (reading list,
WATCHLIST TRIAGE section). The watchlist harness was not committed (`ce98258` carries only the CSV, the reading
list, `floor_screen.py` and `tools/resume_ping.py`), so the guard ORDER is read from the sweep's
`Screens/new_candidates.py` at `ce98258` (identical at `a8bc84f`), and the guard FUNCTIONS from
`floor_screen.py` at `a8bc84f` (`floor_screen_a8bc84f.py` in the research folder). The order is:
(1) `share_count_shift` outside **0.75-1.50x** returns "perimeter"; (2) `scale_shift` **> 2.0** returns
"perimeter by revenue step"; (3) `filed_years < 5`; (4) `owner_earnings() == "CAPEX_UNRESOLVED"`.
**`restatement_shift` is not called anywhere in that pipeline** (grepped at both commits): it exists as a
function and never gates a name. Reproduction, on companyfacts cut to facts filed by 2026-09-01
(`triage_repro.py`, output `triage_repro_out.txt`):

| guard, in order | value | fires? | what it was reacting to, on the filings |
|---|---|---|---|
| 1. `share_count_shift` | **1.034x** | no (inside 0.75-1.50) | ordinary issuance net of buybacks; no split in the window (`split_factor_after` 1.0) |
| **2. `scale_shift`** | **2.0595x** | **YES, at the 2.0x line: THIS IS THE GUARD THAT RETURNED SNOW UNPRICED** | **FY2021 revenue $592.0M to FY2022 $1,219.3M**, the oldest pair in its six-year window (every later step is 1.29-1.69x). **Organic, on the face of the filing**: the FY2022 10-K cash-flow statement shows *"Cash paid for business combinations, net of cash acquired — ( 6,035 ) ( 6,314 )"* for FY2022, FY2021 and FY2020, i.e. **zero** in FY2022. Snowflake's first acquisition of size (Streamlit, $362.6M cash plus $438.9M of stock) closed in FY2023, the year AFTER the step. |
| 3. `filed_years` | 8 | no | |
| 4. `owner_earnings` | 5y D&A **-$527M**, 5y capex **-$450M** | no (priced, and negative) | the triage stopped at guard 2 and never reached this |
| (`restatement_shift`, not a guard) | (1.0, FY2020) | n/a | **a null**: only one revenue element carries data (`RevenueFromContractWithCustomerExcludingAssessedTax`, 18 annual observations; the other three `REV_TAGS` carry none), and every period end agrees across accessions |

**So the label was, for SNOW: a genuine revenue DOUBLING that was ORGANIC (the 2.0x line is a merger proxy, and
a 106% growth year trips it), with no perimeter event and no restatement.** Checked for a restatement on the
documents as well as in the tags: the FY2026 10-K cover leaves both error-correction boxes unticked (*"reflect the
correction of an error to previously issued financial statements. ☐"*); the filing index shows **no 10-K/A or
10-Q/A** in the company's history (`filings_list.txt`, `filings_list_old.txt`); and the FY2020-FY2026 revenue,
operating-cash and SBC figures read off the FY2022, FY2023 and FY2026 10-K faces agree with companyfacts to the
thousand. **The step leaves the window by itself**: when the FY2027 10-K is filed, FY2021-22 drops out of
`scale_shift`'s six years and the guard would pass at 1.69x. **The perimeter events that DO matter are newer than
any guard read and run the other way**: acquisitions paid substantially in stock (FY2023-FY2027, below), and
$2.3bn of convertible notes now deep in the money (below).

**What the current screen says behind the label (tagged data, a prompt only):** `owner_earnings()` prices SNOW and
returns **negative owner earnings at every end** (5y D&A -$527M, 5y capex -$471M, 3y D&A -$580M, 3y capex
-$488M), because stock compensation exceeds operating cash in every year. `working_capital_flag` fires on FY2022
*"ContractWithCustomerLiability moved 478% of 2022 OCF"* (deferred revenue +$526.2M against operating cash of
+$110.2M): taken up at Q4. SBC resolves for every year and the face line is *"Stock-based compensation, net of
amounts capitalized"*, so it is **not complete** on its own: the capitalised part is a separate supplemental line
(taken up at Q4).

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.29%** · **09/17/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority.** Struck by
  this run: `tools/sources.sovereign("USD")` returned `(5.29, '09/17/2026', 'US Treasury daily par yield curve')`
  on 2026-09-18 (`step0_out.txt`). Not inherited from the brief; 09/17 is still the newest row published, so it
  is the same figure the SMCI run struck. FRED was not used.
- **Earnings currency: USD.** FY2026 10-K Item 7A: *"The majority of our sales are currently denominated in U.S.
  dollars, although we also have sales in Euros and, to a lesser extent, in British pounds, Australian dollars,
  Canadian dollars, Brazilian reals, and Indian rupees."* Revenue by customer location FY2026: United States
  $3,524.0M of $4,683.9M (75.2%). No FX or ADR conversion applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$338.39, the close of 2026-09-17**, the last completed close. Source: Yahoo Finance daily chart via
  `sources._chart("SNOW", rng="1mo")` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`).
  Bar: open 334.00, high 344.66, low 328.77, close 338.39.
- **`tools/sources.price()` was NOT used for the struck price.** It returned `(332.835, '2026-09-18', 'USD')`,
  the intraday `regularMarketPrice` stamped with today's date, while its docstring says *"Latest close."* **The
  TOST, EQIX, DLR and SMCI defect reproduces on a fifth name.**
- Recent closes: 09-10 $329.72 · 09-11 $328.99 · 09-14 $332.35 · 09-15 $322.98 · 09-16 $331.02 · 09-17 $338.39.
  The Q2 release day moved the stock: 09-02 close $305.84, 09-03 open $377.24 and close $356.47.
- **Primary-filing cross-check of the aggregator, three Form 4s:** accession `0002127025-26-000007` (Jonathan
  Beaulier) reports tax withholding at **$332.35** on 2026-09-15, which is exactly Yahoo's 09-14 close, and an
  open-market sale on 2026-09-16 at a weighted **$336.124** (*"ranging from $335.888 to $336.140"*), inside
  Yahoo's 09-16 bar (low $317.45, high $338.00); `0001821737-26-000014` (Benoit Dageville) the same $332.35
  withholding price; `0001640147-26-000038` (Christian Kleinerman) withholding at **$337.18** on 2026-09-08,
  exactly Yahoo's 09-04 close, and a 10b5-1 sale on 09-09 at $335.72 inside that day's range ($331.00-$339.59).
  **The aggregator series is corroborated by primary documents.**
- **Split factor after the count's date: 1.0** (`sources.split_factor_after("SNOW", "2026-08-21")`). `close`
  used, never `adjclose`.

### The share count: from the cover, with the accession
- **352.8 million shares**, from the cover of the **Q2 FY2027 Form 10-Q** (quarter ended 2026-07-31, filed
  **2026-09-04**, accession **`0001640147-26-000037`**): *"As of August 21, 2026, there were 352.8 million shares
  of the registrant's common stock, par value of $0.0001 per share, outstanding."* One class of common stock;
  200,000 thousand preferred authorised, *"zero shares issued and outstanding"*.
- **The filer rounds its cover to the hundred thousand**, and no exact count exists on the cover. The balance
  sheet is in thousands: *"352,836 and 344,317 shares issued as of July 31, 2026 and January 31, 2026,
  respectively; 352,455 and 343,918 shares outstanding"*, with 381 thousand in treasury. **ERIC trap checked**:
  the cover says "outstanding"; the balance-sheet outstanding figure three weeks earlier is 352.455M, and the
  cover's 352.8M is consistent with three weeks of RSU vesting. **SPGI trap checked**: no exclusion clause.
- **`Screens/cover_shares.py SNOW` returned a broken figure: `1,640,147,000,000` shares.** Reading the same
  `R1.htm` by hand shows why: the row runs *"Entity Common Stock, Shares Outstanding 352.8 Entity Central Index
  Key 0001640147"*, the renderer header says *"shares in Millions"*, and the tool took the CIK that follows the
  count, scaled by a million. Tooling note at the audit; the count here is read off the document.

### The perimeter between the business and the common holder: stated, not blended
1. **Convertible senior notes, deep in the money.** 10-Q Note 10: $1.15bn of 0% notes due 2027-10-01 and $1.15bn
   due 2029-10-01, each at *"Initial Conversion Price $ 157.50"*, **7,302 thousand shares per series, 14.604M in
   total**; the company *"may choose to pay or deliver, as the case may be, cash, shares of our common stock or a
   combination of cash and shares of our common stock, at our election"*. Capped calls reduce dilution *"subject
   to a cap based on a cap price initially equal to $ 225.00 per share"*. **At $338.39 the notes' if-converted
   value is 14.604M x $338.39 = $4,941.9M against $2,300M of principal; the capped calls return at most 14.604M x
   ($225.00 - $157.50) = $985.8M; the notes' net claim on the equity is therefore about $3,956M, or about 11.7M
   shares at the struck price (+3.3%).** Treatment: shown as a perimeter-consistent cap beside the plain one,
   and the notes are then not also deducted as debt. The 10-Q says conversions of the 2027 Notes through July 31,
   2026 were *"not material"*.
2. **Acquisitions paid in stock, inside and after the window.** Cash paid for business combinations FY2022-26
   **$847.5M** (0; 362.6; 275.7; 30.3; 178.9) plus stock issued **$714.0M** (438.9 FY2023; 174.3 FY2024; 87.7
   FY2025; 13.1 FY2026); and in H1 FY2027 alone **$254.4M cash plus $420.6M of "Non-cash consideration for
   business combinations"** (goodwill $1,194.4M to $1,639.0M in six months). Taken up at Q3 and Q4.
3. **Cash and investments at 2026-07-31: $4,329.2M** (cash $1,707.2M, short-term $637.5M, long-term $1,984.5M);
   no bank debt; strategic equity investments carried in other assets.

### The market cap
- **$338.39 x 352.8M = US$119,384M ($119.4bn).** Split factor after 2026-08-21 = 1.0.
- **Perimeter-consistent, with the convertibles' net claim: US$123,340M** ($119,384M + $3,956M), the notes then
  not deducted as debt. Displayed side by side, not blended.

### LIVE-DEAL CHECK: run by this run, not inherited
- `sources.deal_filings("0001640147")` returned `([], [], '2026-03-20')` and `deal_note` an empty string: no
  DEFM14A, PREM14A, S-4, SC 14D9, SC TO-T or 425.
- The full EDGAR submissions index was read (`filings_list.txt`): every 8-K since the FY2026 10-K carries Items
  7.01, 2.02, 5.07 or 5.02; **no Item 1.01 since the 2024-09-23 convertible-note 8-K**, no SC TO, no SC 13D. **The
  quote is an owner-earnings price, not a spread.**

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2026 Form 10-K**, fiscal year ended 2026-01-31, filed **2026-03-20**, accession **`0001640147-26-000008`**
  (`10K_FY2026.txt`); auditor **PricewaterhouseCoopers LLP**, San Jose, report dated March 20, 2026, *"We have
  served as the Company's auditor since 2019."*
- **Q2 FY2027 Form 10-Q**, quarter ended 2026-07-31, filed **2026-09-04**, accession **`0001640147-26-000037`**.
- Also read: 10-Ks FY2025 (`0001640147-25-000052`), FY2024 (`0001640147-24-000101`), FY2023
  (`0001640147-23-000030`), FY2022 (`0001640147-22-000023`), FY2021 (`0001640147-21-000073`); the Q1 FY2027
  10-Q (`0001640147-26-000030`); the DEF 14A of 2026-05-18 (`0001640147-26-000019`); the 8-K EX-99.1 releases
  and Item 5.02 8-Ks named at Q3; and the Form 4s above.
- **Figures cross-checked against the filed statement** (FY2026 consolidated statement of cash flows):
  *"Net cash provided by operating activities 1,221,942 959,764 848,122"*, *"Stock-based compensation, net of
  amounts capitalized 1,599,547 1,479,314 1,168,015"*, *"Purchases of property and equipment ( 101,628 ) ( 46,279
  ) ( 35,086 )"* and revenue *"$ 4,683,946 | $ 3,626,396 | $ 2,806,489"* all match companyfacts exactly. The one
  that does not is capex before FY2026: `annual(CAPX_TAGS)` returns property and equipment only, while the face
  carries a second line, *"Capitalized software development costs — ( 29,433 ) ( 34,133 )"*, which
  `capital_acquired()` adds (Q4).

*Dated note, 2026-09-18 ~18:35 EDT, by the resuming session, beside Step 0 rather than editing it (operator rule 6):
**Step 0 was re-checked and no error was found** in the arithmetic this run relies on (acquisitions $847.5M cash and
$714.0M stock FY2022-26 against the filed cash-flow faces; the convertible net claim 14.604M x $338.39 less 14.604M x
$67.50 = $3,956M, about 11.7M shares; cap $119,384M). **Two newer figures now exist and change nothing**: the US
Treasury published **09/18/2026, 30 Yr 5.34%** (fetched directly; `tools/sources.sovereign()` still returned the
14:41 cached 09/17 row at 18:30, a tooling note at the audit), and SNOW **closed at $332.43 on 2026-09-18** (Yahoo
daily chart, aggregator, flagged). Every owner-earnings yield in this file is negative, so neither moves any
verdict or any sign; Step 0's pair (US$338.39, 5.29%, 09/17) remains the run's pair.*

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### The unit economics, in my own words, without management's language
Snowflake rents computers and disk from Amazon, Microsoft and Google, runs its own database software on them,
and sells the result to companies by the unit of use: so many seconds of a sized computer, so many terabytes
stored a month, so much data moved. A customer usually signs a one-to-four-year contract for a dollar amount of
use, is billed annually in advance, and draws the amount down as it runs queries; revenue is booked as the
units are used, not as the contract is signed. **Snowflake keeps the difference between what it charges for a
unit and what the cloud charges it for the same unit, and then spends almost all of that difference, and more,
on selling and building the product.**

FY2026 10-K (accession `0001640147-26-000008`), statement of operations, $M:

| line | FY2026 | per $100 of revenue | FY2025 | FY2024 |
|---|---:|---:|---:|---:|
| Revenue (product $4,472.3M, services $211.6M) | 4,683.9 | 100.0 | 3,626.4 | 2,806.5 |
| Cost of revenue (cloud bills, support staff, amortisation) | 1,537.8 | 32.8 | 1,214.7 | 898.6 |
| **Gross profit** | **3,146.1** | **67.2** | 2,411.7 | 1,907.9 |
| Sales and marketing | 2,062.1 | 44.0 | 1,672.1 | 1,391.7 |
| Research and development | 1,969.5 | 42.0 | 1,783.4 | 1,287.9 |
| General and administrative (incl. $108.7M office impairment) | 549.7 | 11.7 | 412.3 | 323.0 |
| **Operating loss** | **-1,435.2** | **-30.6** | -1,456.0 | -1,094.8 |
| *of which stock-based compensation, across the lines above* | *1,599.5* | *34.1* | *1,479.3* | *1,168.0* |

Read as a reseller of rented computing with software on top:
1. **The cloud bill is the main cost of the product.** *"Cost of product revenue consists primarily of (i)
   third-party cloud infrastructure expenses, including those related to graphics processing units (GPUs) and
   AI inference, incurred in connection with our customers' use of our platform"* (MD&A). FY2026 product gross
   margin **72%** (FY2020 62%, FY2021 65%, FY2022 70%, FY2023 72%, FY2024 74%, FY2025 71%; each year's 10-K).
2. **The margin moved on the cost side, and the 10-Ks say so.** FY2021: *"better discipline over discounting,
   higher volume-based discounts for our purchases of third-party cloud infrastructure"*; FY2023: *"increased
   cost efficiency as a result of cloud infrastructure processor improvements"*; FY2024: *"higher volume-based
   discounts for our purchases of third-party cloud infrastructure"*; FY2025, down to 71%: *"newly launched
   product capabilities and features that have not yet reached economies of scale."*
3. **The suppliers are paid under minimum commitments.** Note 11: non-cancelable purchase commitments of
   **$2,681.9M** beyond one year, including *"at least $ 1.0 billion between June 2023 and May 2028"* with one
   cloud and *"at least $ 530.0 million between November 2025 and October 2030"* with another; *"The Company is
   required to pay the difference if it fails to meet the minimum purchase commitment"*. Item 1A: *"a
   substantial majority of our business is run on the AWS public cloud."*
4. **Customers pay ahead, which is why cash exceeds profit.** *"Under capacity arrangements, from which a
   majority of our revenue is derived, we typically bill our customers annually in advance of their
   consumption"* (MD&A). Operating cash was **+$1,221.9M** in FY2026 against a net loss of **-$1,329.0M**; the
   gap is mostly stock compensation (non-cash, **$1,599.5M**) and the growth of prepaid billings (Q4).
5. **Before stock pay, the business earns about 3.5 cents on the dollar.** Operating loss plus stock
   compensation is **+$164.4M** on $4,683.9M of revenue in FY2026. The selling and building lines take **86 cents
   of every revenue dollar**, and **34 cents of every revenue dollar is paid to employees in stock.**
6. **Growth comes from existing customers using more.** *"The substantial majority of our revenue was derived
   from existing customers under capacity arrangements, which represented approximately 97% of our revenue"*;
   net revenue retention **125%** at 2026-01-31; 733 customers above $1M a year, **68%** of product revenue.

### The scarce input this business controls
**Not the computers: they are rented from three companies the 10-K names as its primary competitors** (*"We
currently offer our platform on the public clouds provided by AWS, Azure, and GCP, which are also some of our
primary competitors"*). What Snowflake controls is **the software and the position it creates inside a
customer**: the customer's data loaded into Snowflake's storage format, the pipelines, queries and applications
written against it, and the data-sharing links with other Snowflake customers. That is a switching cost, and
the 10-K itself now says the company is choosing to lower it: *"we have adopted open data formats like Apache
Iceberg tables to allow customers to use our platform to process data stored in external customer-controlled
environments outside of Snowflake ... there is less customer 'lock in' when our products are used in external
environments"* (Item 1A). Whether what remains is a position or only a lead is a relative claim, and it is Q2's.

### Will the fundamentals look broadly the same in ten years?
**The mechanism, probably yes**: rent the machines, sell metered use of software on them with a markup,
prepaid by contract. It has been the same mechanism in every 10-K year on disk (FY2020-FY2026), with product gross
margin inside 62-74%. **The product, certainly not**: the 10-K lists new product categories added in each of
the last several years (Snowpark 2021-22, Snowpark Container Services 2023, Snowflake Intelligence 2024-25,
Postgres 2025-26, observability by acquisition in February 2026), and says *"The markets in which we operate
are rapidly evolving and highly competitive."* **The margin structure, not knowable from the record**: the
company has never earned a GAAP operating profit (*"We have experienced net losses in each period since
inception"*), so no filed year shows what the business earns when it stops spending on growth.

**The honest limit, stated rather than smoothed.** [E3-31] asks for businesses *"relatively simple and stable
in character"*. How a dollar of revenue is made is simple and stable (a markup on rented computing, prepaid);
**what the customer is buying changes every year**, and that is where a forecast of cash would fail. The SMCI
and TOST runs carried that second question to Q2 ([E4-04], the moat that must be rebuilt) rather than closing
Q1 on it, and this run does the same, for the same reason: the money mechanism is writable in five minutes
**[E4-46]**, which is what Q1 asks.

- **VERDICT: [x] IN**
  *The unit economics are writable in plain words (metered resale of rented cloud computing with Snowflake's
  software on top, prepaid under multi-year contracts, at a 67% gross margin that is then more than spent on
  selling and development); the mechanism is recognisable across every filed year [E3-31]. The scarce input is
  a customer's installed data and workloads, which the company itself says open formats are loosening; whether
  that is a franchise is a relative claim, and it is Q2's.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

### WHAT IS BEING TESTED
Q1 named the scarce input as **the installed position**: a customer's data in Snowflake's format, the
workloads written against it, and sharing links to other Snowflake customers. The franchise claim is that
customers regard Snowflake as having **no close substitute** once installed, and [E3-03] says how that claim
shows itself: *"The existence of all three conditions will be demonstrated by a company's ability to regularly
price its product or service aggressively and thereby to earn high rates of return on capital."* (1991 letter;
the same sentence is [E3-43]'s demonstration clause.) Both halves are tested on Snowflake's own filings first
(`price_sweep.py`, `price_sweep_out.txt`: 23 documents, the FY2021-FY2026 10-Ks, both FY2027 10-Qs and fifteen
earnings releases), then against the row. **The prior on disk** is the PLTR run (2026-09-11), which used
Snowflake as a comparator for Palantir's question; its Snowflake figures are not used, and every SNOW number
below is rebuilt from SNOW's filings (`peers.py`, `peers_row.py`, `peers/peers_row_out.txt`).

### THE CASE FOR, AT FULL STRENGTH **[E4-26, E4-51]**
1. **Realised prices have risen, and the 10-Ks say so in three years.** FY2021: *"an increase in capacity sales
   prices of approximately 8% ... primarily as a result of better discipline over discounting"*; FY2022: *"an
   increase in capacity sales prices of approximately 4% ... primarily due to increased sales of higher-priced
   editions of our platform"*; FY2024: *"an increase in capacity consumption prices of approximately 3% ...
   primarily due to increased consumption of higher-priced editions of our platform and better discipline over
   discounting."* Discounts were withdrawn and customers moved up to dearer editions without the volume
   falling: that is pricing conduct, and it is recorded first.
2. **Customers keep spending more.** Net revenue retention **168% (FY2021), 178% (as first filed; 177% as restated in the FY2023 10-K), 158%, 131%,
   126%, 125% (FY2026), 126% at 2026-07-31**; *"approximately 97% of our revenue"* from existing customers under capacity
   contracts; 733 customers above $1M a year (FY2026) and 828 at 2026-07-31. Remaining performance obligations
   **$9,771.5M** at 2026-01-31, weighted-average contract term signed in FY2026 about 3.1 years.
3. **Growth is re-accelerating at scale.** Product revenue **+37%** in Q2 FY2027 (EX-99.1 of 2026-09-02,
   `0001640147-26-000033`: *"Q2 marks our third consecutive quarter of product revenue growth acceleration"*),
   full-year guidance raised to 36%.
4. **The legacy incumbent is shrinking and names Snowflake.** Teradata's revenue fell **-4.5% (2024) and -5.0%
   (2025)** (Teradata 10-K FY2025, `0001628280-26-012671`), and it lists *"AWS, Databricks, Google Cloud,
   Microsoft Azure, Snowflake, and more"* as its competitors.
5. **Growth needs almost no capital, because customers prepay it.** At 2026-01-31 deferred revenue was
   **$3,361.4M**; equity plus the convertible notes (**$4,203.9M**) was less than cash and investments
   (**$4,784.7M**), so the business's net invested capital was **negative** (FY2026 10-K balance sheet). Net
   property and equipment $248.6M on $4.7bn of revenue. [E2-44]'s second half (*"only minor additional
   investment of capital"*) passes on plant and working capital.

### THE THREE CONDITIONS **[E3-03]**
**(1) Needed or desired: IN.** $4.7bn of revenue, 13,328 customers, 790 of the Forbes Global 2000.

**(3) Not subject to price regulation: IN.** No regime sets Snowflake's prices; public-sector contracts carry
the usual price-reduction clauses (Item 1A), which are contract terms, not rate-setting. [E2-59] not engaged.

**(2) No close substitute: NOT SHOWN, and Snowflake's own 10-K says the substitute is getting closer, by its
own choice, in four places.**
1. **The company is lowering its own switching cost, and says so.** FY2026 10-K Item 1A: *"we have adopted open
   data formats like Apache Iceberg tables to allow customers to use our platform to process data stored in
   external customer-controlled environments outside of Snowflake ... These changes are driving increased
   competition, both because there is less customer 'lock in' when our products are used in external
   environments, and also because we are competing across more product categories"*; and *"Our support of open
   data formats may also reduce switching costs between us and our competitors."* The scarce input Q1 named is
   the thing the company itself says is being loosened.
2. **The suppliers are the competitors, and larger.** *"We currently offer our platform on the public clouds
   provided by AWS, Azure, and GCP, which are also some of our primary competitors. Currently, a substantial
   majority of our business is run on the AWS public cloud. There is risk that one or more of these public cloud
   providers could use its respective control of its public clouds to embed innovations or privileged
   interoperating capabilities in competing products, bundle competing products, provide us unfavorable
   pricing"*; and *"our costs and gross margins are significantly influenced by the prices we are able to
   negotiate with these public cloud providers, which in certain cases are also our competitors."*
3. **It competes on price, and against rivals who discount more.** *"We compete based on various factors,
   including price"*; *"we may not be able to ... offer as many discounts or free services as our
   competitors"*; results may fluctuate on *"changes in our pricing model, including in response to significant
   price discounts by our competitors"* (Item 1A). The Q2 FY2027 release's customer example is a price example:
   *"Sayari cut costs by more than half"*.
4. **Efficiency gains are passed to the customer by design.** Every 10-K FY2022-FY2026: *"New software releases
   or hardware improvements, like better storage compression, cloud infrastructure processor improvements, and
   compute optimization, may make our platform more efficient, enabling customers to consume fewer compute,
   storage, and data transfer resources to accomplish the same workloads ... To the extent these improvements
   do not result in an offsetting increase in new workloads, we may experience lower revenue."* The price per
   credit may rise; the price per unit of work falls whenever the platform improves. **[E3-62]**: *"All of the
   advantages from great improvements are going to flow through to the customers."*

**And the demonstration clause fails on its second half.** [E3-43] asks for *"high rates of return on
capital"*. Snowflake has *"experienced net losses in each period since inception"*; its operating margin was
**-39.0%, -40.2%, -30.6%** (FY2024-26) and, **before** stock compensation, **+2.6%, +0.6%, +3.5%**. Invested
capital is negative, so no ratio exists; what exists is an operating profit before stock pay of **$164.4M** on
**$4,683.9M** of revenue in the best year, and a loss after it. **[E3-46]**'s *"very high returns on capital
employed over time"* is a statement about what the business earns; eight filed years and $4.7bn of revenue in,
it has not earned it, and the price record in the case-for is +3% to +8% in three years out of six, by
discount discipline and edition mix, with no list-price increase found (below).

**The price record, swept rather than assumed** (the absence-claim rule, v4 section VI): across the 23 documents,
*"price increase"*, *"increase our prices"*, *"raise prices"* and *"pricing action"*: **no instance found**. The
FY2023, FY2025 and FY2026 10-Ks and both FY2027 10-Qs attribute product revenue growth only to *"increased
consumption of our platform by existing customers"*; the realised-price sentence appears only in FY2021, FY2022
and FY2024.

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4)*
**Who the filings say the competitors are.** Snowflake's 10-K names only *"AWS, Azure, and GCP"* and classes
(*"less-established public and private cloud companies"*, *"established vendors of legacy database solutions"*,
*"existing observability solution providers"*). Teradata names Snowflake and Databricks. MongoDB, Datadog, Elastic
and Palantir name neither (0 hits each for "Snowflake" in their latest 10-Ks); they are adjacent filers whose
products overlap Snowflake's newer categories (MongoDB: operational databases, which Snowflake's Postgres
entered in 2025-26; Datadog and Elastic: observability, which Snowflake entered by buying Observe in February
2026; Palantir: the PLTR run's data-platform comparator). **Taken: seven filers** (the three clouds, Teradata,
MongoDB, Datadog, Elastic) **plus Palantir**; latest three fiscal years each, from companyfacts cross-checked
to each filed income statement (`peers/*_10K_*.txt`: *"Total revenue | 2,463,797"* MongoDB, *"Total revenue |
1,663"* Teradata, *"Revenue | $ | 3,427,158"* Datadog, *"Total revenue | 1,739,331"* Elastic, *"Total revenue |
$ | 4,475,446"* Palantir, all matching).

**ROW A: THE DATA SOFTWARE FILERS** (same metrics, each filer's last three fiscal years, `peers/peers_row_out.txt`)

| company | years | revenue growth | gross margin | GAAP operating margin | operating margin before SBC | SBC / revenue | 10-K accession |
|---|---|---|---|---|---|---|---|
| **Snowflake** | FY2024-26 (Jan) | **35.9 / 29.2 / 29.2%** | **68.0 / 66.5 / 67.2%** | **-39.0 / -40.2 / -30.6%** | **2.6 / 0.6 / 3.5%** | **41.6 / 40.8 / 34.1%** | `0001640147-26-000008` |
| MongoDB | FY2024-26 (Jan) | 31.1 / 19.2 / 22.8% | 74.8 / 73.3 / 71.7% | -13.9 / -10.8 / -5.6% | 13.3 / 13.8 / 16.8% | 27.1 / 24.6 / 22.3% | `0001628280-26-016799` |
| Datadog | CY2023-25 | 27.1 / 26.1 / 27.7% | 80.7 / 80.8 / 80.0% | -1.6 / 2.0 / -1.3% | 21.1 / 23.3 / 20.6% | 22.7 / 21.2 / 21.9% | `0001628280-26-008819` |
| Elastic | FY2024-26 (Apr) | 18.6 / 17.0 / 17.3% | 74.0 / 74.4 / 76.1% | -10.3 / -3.7 / -1.9% | 8.6 / 13.7 / 15.2% | 18.9 / 17.4 / 17.2% | `0001707753-26-000018` |
| Palantir | CY2023-25 | 16.7 / 28.8 / 56.2% | 80.6 / 80.2 / 82.4% | 5.4 / 10.8 / 31.6% | 26.8 / 35.0 / 46.9% | 21.4 / 24.1 / 15.3% | `0001321655-26-000011` |
| Teradata (names Snowflake) | CY2023-25 | 2.1 / -4.5 / -5.0% | 60.8 / 60.5 / 59.4% | 10.1 / 11.9 / 12.3% | 17.0 / 18.7 / 19.1% | 6.9 / 6.8 / 6.7% | `0001628280-26-012671` |

**ROW B: THE THREE CLOUDS, which are Snowflake's suppliers AND its named primary competitors** (segment
operating margin; transcribed from the AMZN run's `_research 2026-09-13 AMZN/peers/competitor_row.md` Table A,
each figure there with its accession: Amazon 10-K `0001018724-26-000004`, Microsoft 10-K
`0001193125-26-323660`, Alphabet 10-K `0001652044-26-000018`)

| unit | prior year | latest year | latest growth |
|---|---:|---:|---:|
| Amazon, AWS (FY2025) | 37.0% | **35.4%** | +19.7% |
| Microsoft, Intelligent Cloud (FY2026, June) | 42.0% | **41.3%** | +29.7% |
| Alphabet, Google Cloud (FY2025) | 14.1% | **23.7%** | +35.8% |

**Not taken, and why, each tested on the document:**
- **Databricks** is the private competitor the brief named. Snowflake's filings never name it (0 hits in all
  23 documents). **It is an SEC filer of Form D only**: CIK `0001587468`, 17 Form D and 3 Form D/A, the latest two
  filed **2026-08-27** (`0001587468-26-000002`: an equity offering of **$5,000,000,000**, $4,999,997,255 sold,
  first sale 2026-08-12; `0001587468-26-000001`: $241.2M), each with revenue range *"Decline to Disclose"*. No
  rung of the evidence ladder gives its margins; **the one filed fact is that the named private rival raised
  $5.0bn of equity last month.** EDGAR full-text search returns 110 10-Ks mentioning "Databricks"; a count of
  mentions, not a row.
- **Confluent** is no longer a filer: Form **15-12G** filed 2026-03-27 (`0000950142-26-000892`).
- **The clouds' own data-warehouse products** (Redshift, Fabric/Synapse, BigQuery) have no product-level figure in
  any filing: the AMZN and PLTR runs each recorded a sweep of the Amazon, Microsoft and Alphabet 10-Ks with **no
  instance found**. Row B is whole segments, which include the compute Snowflake itself rents.
- **Oracle** reports no database-cloud segment; **Cloudera** is private.

**Peers: eight carried with numbers (three cloud segments, five software filers), three recorded as
unavailable (Databricks, Confluent, the clouds' product lines).** Buffett says eight; the industry has more
than eight, and the one the market treats as the closest private rival cannot be measured.

**What the row shows.**
- **Position: Snowflake has the lowest gross margin of the software filers except the shrinking legacy
  incumbent, and the lowest operating margin before stock pay of all six.** 67% against 72-82% for MongoDB,
  Elastic, Datadog and Palantir; 0.6-3.5% before SBC against 8.6-46.9%. **It pays the most stock to earn the
  least**: SBC 34-42% of revenue against 15-27% for the other growth filers.
- **Why the gross margin sits there: part of every Snowflake dollar is a cloud's revenue.** Cost of product
  revenue is *"primarily ... third-party cloud infrastructure expenses"*, rented from units earning 24-41%
  segment margins (Row B). The 10-Ks attribute the FY2021-FY2024 rise in product gross margin (62% to 74%) mainly
  to the cost side (*"higher volume-based discounts for our purchases of third-party cloud infrastructure"*,
  *"cloud infrastructure processor improvements"*), and its FY2025 fall to 71% to new products *"that have not yet
  reached economies of scale"*.
- **Direction: retention falling every year from 178% (FY2022) to 125-126%**, which the company forecasts will
  continue (*"We expect our net revenue retention rate to decrease over the long-term"*, MD&A). Growth is
  re-accelerating (+37% product revenue in Q2 FY2027) on AI workloads, which is recorded, and which is a new
  product category rather than the old position.
- **The row's limit [E3-61]**: it shows position, not conduct; it cannot show how Databricks or the clouds will
  price. **The gate does not close on that gap**: a Databricks margin above Snowflake's would not give Snowflake
  the pricing its own 10-K says it does not have, and one below would confirm the finding.

### THE OTHER Q2 TESTS
- **[E2-44] two-characteristic test.** (1) *"an ability to increase prices rather easily (even when product
  demand is flat and capacity is not fully utilized) without fear of significant loss of either market share or
  unit volume"*: **not shown**. Realised prices rose 3-8% in three years out of six by discounting less and
  selling dearer editions; the same filings say price is a competitive factor, rivals discount more, and every
  efficiency gain lowers the price of a workload. No price rise under flat demand exists to test, because demand
  has never been flat. (2) *"only minor additional investment of capital"*: **passes**, on customer prepayments
  (case-for item 5). The capital this business consumes is not on the balance sheet: it is **$1.6bn a year of
  stock paid to employees**, which Q4 subtracts in full [E5-06].
- **[E4-04] rapid change: ENGAGED, in the company's own words, and v4's scope test answers "replacement".**
  *"The markets in which we operate are rapidly evolving and highly competitive"*; *"We believe that the pace of
  innovation will continue to accelerate"*; and a new named threat in FY2026: *"Frontier AI model providers may
  seek to vertically integrate their offerings by expanding into the data storage and management layers and
  developing their own database solutions. In addition, companies may use AI to develop their own software,
  reducing their need to purchase third-party solutions."* The $1,969.5M of FY2026 R&D (42% of revenue) and a
  new product category each year (Q1) do not defend the 2014 data warehouse; they build the next category
  (AI agents, Postgres, observability), while the company opens the old one to competitors through Iceberg.
  [E5-23] licenses continuous defence; it does not turn an advantage the owner is deliberately opening to rivals
  into an enduring one.
- **[E4-36] which cause of extreme success: wave-riding.** The wave is the migration of enterprise data from
  on-premise warehouses to the public cloud, and the row shows it (Teradata shrinking; *"a focus on replacing
  legacy solutions and big data offerings"* is Snowflake's own stated growth strategy, Item 1). **[E3-51]**: a
  surfing run is not a moat; the advantage lives in the wave.
- **[E2-45] the attacker's test: the attackers exist, are larger, and one was funded last month.** The three
  clouds (segment margins 24-41%, Row B) are Snowflake's landlords; *"Many of our competitors have
  substantially greater brand recognition, customer relationships, and financial, technical, and other
  resources than we do"*; *"Some of our privately-held competitors also have greater operational flexibility"*;
  Databricks sold $5.0bn of equity in August 2026 (Form D).
- **[E2-58] the commodity end: not engaged at the product.** The software is differentiated. It is engaged at
  the input: the compute is the clouds' product, bought under minimum commitments ($2,681.9M beyond one year).
- **[E4-32] direction: narrowing.** Retention falling for four years and forecast by the company to keep
  falling; the lock-in being opened by the company's own format choice; the one rising margin was the
  suppliers' discount, not the customers' price.
- **[E4-55] units:** no unit series is filed (credits, compute hours or terabytes are not disclosed); dollar
  product revenue is the only series, the weaker one [E4-55] warns about, and the company itself says the dollars
  per workload fall with each efficiency gain.
- **[E3-33] untapped pricing power: REFUSED** under **[E5-28]**: claiming it is claiming *"a monopoly or a near
  monopoly"*; Snowflake names three larger competitors that are also its suppliers.
- **[E2-53] dominance: not available.** No filing gives a share; the company names larger competitors.
- **[E4-23] key-person dependence: no defect found.** The CEO changed on 2024-02-27 (8-K `0001640147-24-000033`:
  *"Frank Slootman retired as Chief Executive Officer ... and Sridhar Ramaswamy was appointed to succeed"*) and
  the CFO in September 2025 (8-K `0001640147-25-000181`); revenue growth continued through both.

### CLASS AND VERDICT
- Needed or desired **[x]** · no close substitute **[ ]** (not shown; the company says open formats reduce
  switching costs, it competes on price with rivals that discount more, and its suppliers are its largest
  competitors) · not price-regulated **[x]**
- **Class: NONE.** A fast-growing, well-liked product with real customer expansion and a real engineering lead,
  riding the migration of data to the cloud, reselling its competitors' computing, and earning no operating
  profit after paying its people. **Direction: narrowing** (retention 178% to 125%; switching costs reduced by
  the company's own choice).
- **The gate does not close on missing evidence.** Databricks is unmeasurable and the clouds' product lines are
  unsegmented; neither is what fails the gate. It fails on Snowflake's own sentences about lock-in, price and
  efficiency, its own margin record after eight filed years, and a row in which it earns the least before stock
  pay and pays the most stock.

**VERDICT: [ ] IN  [x] OUT**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
*OUT on the business: [E3-03] criterion (2) is not shown and is contradicted in the company's own words (open
formats *"may also reduce switching costs between us and our competitors"*; competition *"based on ...
price"*; efficiency gains that let customers *"consume fewer ... resources"*, [E3-62]); [E3-43]'s demonstration
clause fails on returns, [E3-46] (an operating loss in every year since inception; 0.6-3.5% before stock pay);
[E4-04] engaged in the company's own words, with frontier AI providers named as possible entrants into its
layer; the record is a surfing run on cloud migration [E3-51, E4-36]; the three largest competitors are also its
suppliers [E2-45]. Not a finding that Snowflake is badly run or technically weak: its product, customer
expansion and realised price discipline are recorded at full strength. **The file closes here.** Q3-Q6 below
are RECORDED, NOT GOVERNING, as at SMCI, TOST and the other Q2 closes in wave 5.*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the brief asked
> for the conduct record and the releases to be read, and because the queue asks every run for its price and
> flags. It decides nothing and cannot reopen Q2 [E2-37, E3-39].

### STEP 1 - THE WEIGHT CASE
- [x] **Daily execution [E3-38]: TICKED.** Q2 found the product rebuilt each year in a market the company
  calls *"rapidly evolving"*, priced against larger rivals at every renewal, with the company opening its own
  lock-in through Iceberg. The product decision (what to build, what to open, what to price) is re-made
  continuously; this is the have-to-be-smart-every-day case.
- [ ] **Control [E1-16]**: not ticked; a minority public holding.
- [ ] **Leverage [E3-29]**: not ticked. $2.3bn of 0% convertible notes against $4.3bn of cash and investments
  (2026-07-31); assets $8.7bn on equity $1.9bn at 2026-01-31, but the liabilities are mostly customer prepayments
  ($3.4bn of deferred revenue), not borrowing.

**Case declared: a BINARY GATE (daily execution). No price compensates [E5-35].**

### THE BINARY - honesty **[E5-16]**, each matter dated to when it became PUBLIC
| public | what | document |
|---|---|---|
| 2023-09-15 | an NLRB administrative law judge rules for a former employee who said he was fired for protected concerted activity (charge filed 2021-03-23); the company appeals; *"reasonably possible"* loss *"between zero and $ 25 million, plus interest"* | FY2026 10-K Note 11 |
| 2024-02-29 | securities class action (Exchange Act 10(b) and 20(a)) against the company, the former CEO and the former CFO, filed the day after the 2024-02-28 release and CEO change; five derivative suits follow; **dismissed 2026-02-17 with leave to amend**; third amended complaint filed 2026-04-14; motion to dismiss pending *"As of September 3, 2026"* | FY2026 10-K Note 11; Q2 FY2027 10-Q |
| 2024-06-13 onward | class actions alleging the company *"failed to take reasonable measures to secure systems that contained consumer data, thereby allowing threat actors to access and exfiltrate personally identifiable information"* from customer accounts; consolidated in a multidistrict litigation in Montana; **motions to dismiss denied 2025-10-28/29**; in discovery; no loss estimate. **No 8-K was filed on the incident** (filing index: no Item 1.05 or 8.01 between 2024-05-22 and 2024-08-21); the 10-K risk factors place responsibility for credentials on customers under a *"shared responsibility cybersecurity model"* | FY2026 10-K Note 11 and Item 1A; `filings_list.txt` |
| 2025-11-21 | copyright class action alleging works were used *"without authorization to train the Company's large language model"*; in discovery | Q2 FY2027 10-Q |

**No disqualifier found.** No SEC or DOJ order, no restatement (Step 0), no auditor change (PwC since 2019), no
material weakness (*"our internal control over financial reporting was effective as of January 31, 2026"*,
audited), and no filed finding of personal misconduct against any officer. The securities suit has been
dismissed once; the data-breach suits survive a motion to dismiss, which is a finding that the claims are
pleadable, not that they are true. [E5-22]: penalty size is not seriousness in either direction; no penalty
exists here. *IN on the binary is not a finding that the managers are honest [E5-17].*

### THE INCENTIVE READ **[E4-27]**
*"Never, ever, think about something else when you should be thinking about the power of incentives."*
- **What executive pay vests on** (DEF 14A of 2026-05-18, `0001640147-26-000019`): performance RSUs on *"three-year
  growth rate targets for product revenue, the core performance metric for the PRSU awards (70% weighting), and
  annual performance targets for non-GAAP operating margin (15% weighting) and non-GAAP adjusted free cash flow
  (15% weighting)"*; the FY2027 cash bonus pool on *"total revenue"*. **Both profit yardsticks exclude stock
  compensation**, the company's largest cost (34% of revenue).
- **The CEO's new award is on the share price** (8-K of 2026-07-16, `0001628280-26-048373`): 1,000,000 PSUs in five
  tranches at **$324, $375, $427, $479 and $531**, measured on a 90-day average close, *"designed to culminate in
  adding up to $100 billion of stockholder value"*. The stock closed **$338.39** on 2026-09-17, above the first
  tranche. A price yardstick, not a per-share-value yardstick; a prompt only [E5-38].

### STEP 2 - THE FLAGS. *Each is a prompt to READ, never a verdict.*
- [x] **EBITDA / adjusted-earnings promotion [E4-29], the CGNX companion rule applied: FIRES in the releases and in
  the pay plan.** Every release read (15, 2023-03 to 2026-09) guides only non-GAAP margins: the Q2 FY2027 release
  guides *"Non-GAAP operating margin 2 of 14.5%"* and *"Non-GAAP adjusted free cash flow margin 2 of 23.0%"*, and
  says a GAAP reconciliation *"is not available on a forward-looking basis without unreasonable effort"*. For the
  quarter it reported **GAAP operating margin -17.0% beside non-GAAP +15.3%** (*"Operating income (loss) |
  ($263.0) | (17.0 | %) | $237.0 | 15.3"*), a 32-point gap that is mostly stock pay. The same two non-GAAP
  measures are 30% of the executives' PRSU yardstick. **[E2-49]** asks whether the yardstick is pre-set and
  long-lived: it is (the same measures in every release read), which answers metric-switching, not the flag.
- [x] **Serial share issuance [E5-15]: FIRES, net of buybacks.** Stock compensation **$6,258M** over FY2019-26
  against cumulative operating cash of **$3,320M** (**189%**, `oe_out.txt`). The company spent **$5,125M** in
  FY2023-26 on repurchases ($3,398M) and on taxes to net-settle vesting awards ($1,727M), and the share count
  still rose: outstanding **333.9M** (2025-01-31) to **343.9M** (2026-01-31) to **352.5M** (2026-07-31);
  guided non-GAAP diluted shares **361M** (Q1 FY2024 guidance, 2023-03-01) to **382M** (Q3 FY2027 guidance).
- [x] **Trumpeted projections [E4-22], and the record [E3-48]: ticked as a guidance practice, with a clean
  record.** Quarterly and annual product-revenue guidance in every release since 2023 (**[E5-30]**: the practice
  itself is the corpus's concern). **Scored against outturn**: FY2024 guided **$2,600-2,650M**, delivered
  **$2,666.8M**; FY2025 guided **$3,300-3,430M**, delivered **$3,462.4M**; FY2026 guided **$4,325-4,446M**,
  delivered **$4,472.3M**; FY2027 raised from $5,660M to $5,840M to **$6,070M**. No full-year miss in the releases
  read; the guide is set low and beaten.
- [ ] **Weak accounting [E4-22]: not ticked.** Stock compensation is expensed; the FY2026 switch from
  capitalising platform software (ASC 350-40) to expensing it (ASC 985-20) moved cost INTO the income statement.
  Deferred commissions are capitalised and amortised over five years (MD&A); recorded, not flagged.
- [ ] **Unintelligible footnotes**: not ticked; the notes are legible and the MD&A states plainly that
  retention is expected to fall.
- [ ] **Filed-figure tells [E4-30]**: not applicable; the company has pre-tax losses and pays little cash tax;
  reported growth is not smooth (29% to 37% product growth, with a fall from 106% before it).
- **[E4-34] the auditor questions**: nothing on the record to answer them against; no auditor change,
  no restatement, clean ICFR opinions.
- **[E4-52] the flags converge?** Adjusted margins in the releases, the same adjusted margins in the pay plan,
  and share issuance the buyback cannot absorb point one way: the reported profit number that matters to
  management excludes the cost the owners bear. Read as one system, not a count.

### STEP 3 - THE PRIMARY TEST **[E2-01]**, scoped by **[E2-43]**
- **Return on average equity** (net loss attributable to Snowflake over average equity, filed balance sheets):
  **FY2024 -15.7%** (-$836.1M on $5,456.4M and $5,180.3M), **FY2025 -31.4%**, **FY2026 -54.1%**. Every year
  since inception is a loss. The denominator is shrinking because buybacks and net-settlement taxes exceed the
  stock credited to equity: equity **$5,456.4M (2023-01-31) to $1,924.1M (2026-01-31)**.
- **[E2-43] unleveraged net tangible assets**: operating income is negative, so the ratio is negative; net
  tangible assets are themselves negative once customer prepayments are netted (Q2 case-for item 5).

### CANDOR - THE HALF-OWNER TEST **[E2-26]**
**Candid in the 10-K; promotional in the release.** For: the 10-K says in plain words that lock-in is falling,
that retention will decline, that the clouds are competitors with pricing leverage, and it prints stock pay by
line and as a percentage of revenue. Against: the releases lead with product revenue and non-GAAP margins, guide
no GAAP figure, and headline an "adjusted" free cash flow; a half-owner would want the owner-earnings figure, and
no release gives the number after stock pay. The 2024 customer-account incident appears in the filings only as
litigation and risk-factor language; no filing read describes what happened.

### RATIONALITY IS CAPITAL ALLOCATION
- **Buybacks [E5-08, E5-24]**: **4.0M shares at $147.50 (FY2024, $591.7M); 14.8M at $130.87 (FY2025, $1.9bn,
  including 3.6M bought at $112.50 from the purchasers of the convertible notes); 4.9M at $177.37 (FY2026,
  $873.5M); 1.7M at $178.95 (H1 FY2027, $300.0M)** (10-K and 10-Q liquidity sections). Condition (1), ample
  funds: yes, $4.3bn of cash and investments. **Condition (2), a material discount to conservatively calculated
  intrinsic value: cannot be met on this run's numbers**, because owner earnings are negative on every
  construction (Q4). **CAPITAL ALLOCATION FLAG**, with the humility clause **[E4-13]**: this rests on our own
  valuation, and management knows the business better than we do. The buybacks have not reduced the count; they
  have partly offset issuance.
- **The convertible was used to buy stock.** $2.3bn of 0% notes (September 2024) funded $195.5M of capped calls
  and **$399.6M of repurchases from the note purchasers themselves** at $112.50. At $338.39 the notes now convert
  into about 11.7M net shares (Step 0).
- **The institutional imperative [E2-30]**: (2) projects and acquisitions soak up funds: **ticked as a prompt**:
  an acquisition in every year since FY2023 (Streamlit, then others; Crunchy Data $164.5M cash in June 2025;
  Observe $596.2M in February 2026, $286.2M cash and 1.5M shares; H1 FY2027 **$254.4M cash plus $420.6M
  non-cash**), each into a new product category. (1), (3), (4): not scored from the filings.

### THE GUARDRAIL
- [x] Nothing in this Q3 is used to promote the name; the file is closed at Q2 [E2-37, E2-38, E3-39].
- [x] Key-person dependence was considered at Q2 [E4-23] and not found.
- [x] No great-manager case is made [E2-35, E2-36].

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *Gate case (daily execution). No disqualifier found in the filed record: no enforcement, restatement,
  auditor change or control weakness; the open suits are pleadings. Flags live: [E4-29] in the releases and the
  pay yardstick; [E5-15] issuance the buybacks do not absorb; a buyback flag under [E5-08] with [E4-13]'s
  humility clause. IN never promotes [E5-17].*

---
## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). Written because the brief asked for the owner
> earnings rebuilt over every window, the deferred-revenue contribution shown both ways, and SBC tested for
> completeness; it decides nothing and cannot reopen Q2 [E2-37, E3-39].

### Owner earnings — the one number **[E2-23]**
Construction (CONVENTION, v4 section VI): operating cash flow, less stock compensation, less (c). Every figure
from the filed cash-flow faces: FY2019-21 from the FY2021 10-K, FY2021-23 from the FY2023 10-K, FY2024-26 from
the FY2026 10-K, the half-years from the Q2 FY2027 10-Q (`cf_faces.txt`, `oe.py`, `oe_out.txt`). No net-income
proxy. **A ten-year window does not exist on filed statements**: the first filed annual statements (FY2021
10-K) begin at FY2019, so eight years exist, of which FY2019-21 are pre-profit-scale years.

**SBC, tested for resolution and completeness.** The face line is *"Stock-based compensation, net of amounts
capitalized"*; it resolves in every year, and **it is not complete**: the capitalised part sits in a
supplemental line (*"Stock-based compensation included in capitalized software development costs"*: $23.6M,
$28.5M, $48.2M, $38.5M, zero in FY2022-26). **This run adds it back**, so the SBC subtracted is the whole charge
(the screen's -$527M and -$471M five-year ends differ from this run's by that amount, about $28M a year). In FY2026
capitalisation stopped (ASC 985-20, MD&A), so from FY2026 all development cost, stock included, is in operating
expense: a definition break of the TOST kind, and it lowers the capex end from FY2026 on without changing the
cash spent. **[E3-70]**: the grants are now almost wholly RSUs, whose grant-date value is the share price, so the
accounting charge is close to the market measure; the unvested pool is **$3.1bn** over 2.7 years (MD&A). **And
the cash test agrees**: FY2023-26 repurchases plus net-settlement taxes ($5,125M) were 98% of the whole SBC
charge over the same four years ($5,224M), and the count still rose (Q3). The accounting charge is not an
overstatement of the cost.

**What (c) is made of, asked before assuming it is plant.** FY2026 D&A **$220.4M** is **$110.1M amortisation of
acquired intangibles (50%)**, **$71.6M amortisation of capitalised software (32%)** and about **$38.7M of plant
depreciation (18%)** (the property-and-equipment and intangible-asset notes). Plant is small: net property and equipment $248.6M, capex $101.6M (2.2% of
revenue). **[E5-20] is not engaged**: the platform runs on rented cloud computing, which is in cost of revenue
and therefore already inside operating cash. The (c) band here is about software and acquisitions, not plant; the
two ends differ by about $57M a year over five years, so the band does not decide anything.

**The deferred-revenue line, shown both ways (the brief's instruction; the TOST interest-income precedent).**
Customers are billed annually in advance for capacity, so each year's growth in prepayments adds to operating
cash: **+$526.2M (FY2022), +$514.3M, +$528.0M, +$382.8M, +$755.2M (FY2026)**, a five-year mean of **$541.3M**,
against a five-year mean operating cash of $737.1M. **Is it float in the [E3-52] sense?** It is interest-free and
carries no covenant, but it is not a liability whose payment comes later: it is paid off by delivering the
service, mostly within a year (*"approximately 46%"* of RPO within 12 months; current deferred revenue $3,347.0M
of $3,361.4M), and the company itself says billing is moving toward it shrinking: *"we expect to see an increase
in capacity contracts providing for quarterly upfront billings and monthly in arrears billings"* (MD&A). **It is
a growth-dependent timing benefit, not a durable source of owner cash**; it reverses if billings stop growing or
shift to arrears. H1 FY2027 shows the seasonal reversal: deferred revenue **-$807.2M**.

| $M | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | TTM Jul-26 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| operating cash flow | -176.6 | -45.4 | 110.2 | 545.6 | 848.1 | 959.8 | 1,221.9 | 1,253.2 |
| of which deferred revenue | 223.0 | 312.9 | 526.2 | 514.3 | 528.0 | 382.8 | 755.2 | 271.9 |
| SBC, whole charge (face + capitalised) | 79.5 | 303.5 | 628.7 | 890.0 | 1,216.2 | 1,517.8 | 1,599.5 | 1,641.9 |
| capex + capitalised software (cash) | 22.9 | 40.3 | 29.0 | 49.1 | 69.2 | 75.7 | 101.6 | 57.9 |
| D&A | 3.5 | 9.8 | 21.5 | 63.5 | 119.9 | 182.5 | 220.4 | 253.0 |
| **OE, convention, capex end** | **-279** | **-389** | **-548** | **-394** | **-437** | **-634** | **-479** | **-447** |
| OE, convention, D&A end | -260 | -359 | -540 | -408 | -488 | -741 | -598 | -642 |
| *OE without the deferred-revenue increment, capex end* | -502 | -702 | -1,074 | -908 | -965 | -1,017 | -1,234 | -719 |
| *display: cash flow before SBC (= the company's "free cash flow")* | -200 | -86 | 81 | 497 | 779 | 884 | 1,120 | 1,195 |
| *display: acquisitions, cash plus stock* | 11 | 6 | 0 | 802 | 450 | 118 | 192 | n/a |

*(FY2019: operating cash -$144.0M, owner earnings -$171M at the capex end. The "free cash flow" row matches the
company's own reconciliation to the decimal ($1,120.3M, $884.1M, $778.9M), which is the cross-check of the
transcription.)*

**MORE THAN ONE WINDOW [E4-25, E4-38]:**

| window | convention, capex end | convention, D&A end | without the deferred-revenue increment | before SBC (display) |
|---|---:|---:|---:|---:|
| **five-year default [E2-42], FY2022-26** | **-$498M** | **-$555M** | -$1,040M to -$1,096M | +$672M |
| three-year, FY2024-26 | -$517M | -$609M | -$1,072M to -$1,164M | +$928M |
| seven-year, FY2020-26 | -$451M | -$485M | -$915M to -$948M | +$439M |
| TTM to 2026-07-31 | -$447M | -$642M | -$719M to -$914M | +$1,195M |

**The range, in dollars and a word: about -$0.45bn to -$0.64bn a year on the convention in every window, and
about -$0.7bn to -$1.2bn without the prepayment timing. NEGATIVE, on every window, at both (c) ends, in every
filed year FY2019 to TTM.** It is not wide in the [E4-25] sense: it does not span zero, so a conclusion can be
reached, and the conclusion is that after paying its people the business has not produced a dollar for owners in
any filed year. A positive figure appears only when stock compensation is left out. **[E4-41] favourable breaks
named**: the prepayment increment (above) and interest income of $190.6M in FY2026 on cash raised at the IPO and
from the notes, both inside operating cash; removing either makes every figure more negative.

### Great, good, or gruesome? **[E4-20, E4-43]**
- [ ] great · [ ] good · [x] **gruesome, on the filed record**
*"The worst sort of business is one that grows rapidly, requires significant capital to engender the growth, and
then earns little or no money."* The capital here is not plant: it is **stock paid to employees, $1.6bn a year**,
supplied by the owners through dilution and bought back with $5.1bn of the owners' cash in four years. [E5-40]:
cash-consuming businesses are unattractive *"unless the cash they consume gets to earn a reasonable return"*;
eight filed years show none after stock pay. **The case against the label, at full strength**: stock pay has fallen
from 41.6% of revenue (FY2024) to 34.1% (FY2026), and the company guides non-GAAP operating margin up to 14.5%;
if stock pay fell to the 15-22% of revenue its software peers carry (Q2 Row A), owner earnings would turn
positive. That is a forecast, not a record, and [E3-48] says to set it against the record.

### Staying power — score all three **[E5-11]**
- **(1) A large and reliable stream of earnings: NO, for owners.** Operating cash is large and has grown every year
  since FY2021, but it is smaller than the stock paid to produce it in every year.
- **(2) Massive liquid assets: YES.** Cash and investments **$4,329.2M** at 2026-07-31 (cash $1,707.2M,
  short-term $637.5M, long-term $1,984.5M); no bank debt.
- **(3) No significant near-term cash requirements: MOSTLY YES.** The **2027 notes ($1.15bn, due 2027-10-01)** are
  in the money and settle in *"cash, shares of our common stock or a combination ... at our election"*; the capped
  calls return up to $985.8M of value across both series. Cloud purchase commitments of **$2,681.9M** beyond one year
  (two with minimum spends: *"at least $ 1.0 billion between June 2023 and May 2028"* and *"at least $ 530.0
  million between November 2025 and October 2030"*) against a cloud bill that is most of a $1.26bn cost of product
  revenue. No covenanted debt.
- **Score: 2 of 3.** **Leverage [E4-16, E3-29]**: $2.3bn of 0% convertibles, no interest payable; **[E2-54]'s
  coverage test** is met trivially (no cash interest). **[E3-52] terms**: the largest liability is customer
  prepayment, due in service, not cash.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**
**The mechanism: the stock stops paying the staff.** Snowflake pays **34 cents of every revenue dollar in stock**
and has never covered that cost from operations. The arrangement works while the share price holds: employees
accept stock, and the buybacks that offset it are affordable. If growth slows (the company's own list: open
formats that let customers move compute elsewhere, larger rivals who are also its landlords, frontier AI
providers moving into the data layer), the price falls, the same stock grant buys less labour, and the company
must choose between more dilution, cash pay it has not been earning, or losing the engineers who are the
product. **Quantified from filed figures**: at FY2026 scale, replacing the $1,599.5M of stock pay with cash would
turn operating cash of $1,221.9M into about **-$378M**; the $4.3bn of liquid assets would cover about **eleven
years** of that deficit at the FY2026 rate, before the $1.15bn of 2027 notes if they were settled in cash. The
exposure [E4-40] is the stock-pay model itself, not any year's experience, because every filed year has been a
rising-price year for the model to run in.

- Survival shapes (`Screens/SURVIVAL SHAPES - index.md`): **#2 EARNS NOTHING FOR OWNERS AFTER PAYING ITS PEOPLE**
  (SBC 131% of FY2026 operating cash; 189% of all operating cash FY2019-26), with **#13 THE TENANT** as the
  structural reason the gross margin is capped (the compute is rented non-exclusively from three owners who rent
  it to every rival and are themselves the named primary competitors; the renewal terms are theirs) and **#11 THE
  PASS-THROUGH** in its efficiency form (each performance gain lets customers *"consume fewer"* resources).
  **No new shape is proposed.**
- **Likelihood: [ ] likely [ ] a real possibility [x] a low-level possibility** of insolvency, with $4.3bn of
  liquid assets and no cash-pay debt; **likely** that owners continue to earn nothing after stock pay unless stock
  pay falls sharply as a share of revenue, which is a forecast the record does not yet support.

- **VERDICT (RECORDED, NOT GOVERNING): [ ] IN  [x] OUT on the owner-earnings leg  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  *The business will very likely survive (staying power 2 of 3; $4.3bn liquid; no cash-interest debt). Owner
  earnings are negative on every window and both (c) ends (five-year -$498M to -$555M; about -$1.0bn to -$1.1bn
  without the prepayment timing), in every filed year, because stock compensation exceeds operating cash
  [E2-23, E5-06]; [E4-20] gruesome on the record, and v4 lets only the gruesome fail Q4 [E4-43]. Recorded only.*

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
*Q5 does not open: Q2 is OUT (and Q4, recorded, is OUT on the owner-earnings leg). The arithmetic below is
recorded because the queue asks every run for a price, and it carries no entry language. It is not a ranking and
it arms nothing.*

**The pair (Step 0):** price **US$338.39**, the **2026-09-17 close** (Yahoo daily chart, aggregator, flagged;
corroborated by three Form 4s) x **352.8M shares** (Q2 FY2027 10-Q cover, `0001640147-26-000037`) x split factor
**1.0** = **US$119,384M**; **perimeter-consistent with the convertibles' net claim, US$123,340M**, used as the
harder denominator, the notes then not deducted as debt. **Sovereign USD 30-year 5.29%**, US Treasury daily par
yield curve, **09/17/2026**. (`q5.py`, `q5_out.txt`.) Owner earnings are after interest income ($190.6M in
FY2026), and the cash is left in the cap; no adjustment is made for either, and removing the interest would make
every figure below more negative.

| construction | $M a year | yield on $123.3bn | vs 5.29% | perpetual growth needed to reach ~10% |
|---|---:|---:|---:|---:|
| **five-year default, convention, capex end** | **-498** | **-0.40%** | **-5.69 pts** | **refused: a negative base has no growth rate** |
| five-year, convention, D&A end | -555 | -0.45% | -5.74 pts | refused |
| three-year, capex end | -517 | -0.42% | -5.71 pts | refused |
| TTM to 2026-07-31, capex end | -447 | -0.36% | -5.65 pts | refused |
| five-year, without the prepayment increment | -1,040 | -0.84% | -6.13 pts | refused |
| *display only, not owner earnings:* TTM cash flow before stock pay (the company's own free cash flow) | +1,195 | 0.97% | -4.32 pts | 8.9% |
| *display only:* FY2027 guided "adjusted free cash flow" (23% margin on about $6,357M of revenue, derived from the $6,070M product guide) | +1,462 | 1.19% | -4.10 pts | 8.7% |

**1. THE YIELD.** Negative on every owner-earnings construction. **Even with stock compensation left out
entirely, and on the company's own guided adjusted figure, the yield is about 1.0-1.2%**, under a quarter of the
5.29% sovereign and about a tenth of the ~10% floor **[E4-28]**.

**2. WHAT THE PRICE ALREADY ASSUMES.** On owner earnings, no growth rate exists because the base is negative. On
the before-SBC display, about **9% a year of growth in perpetuity** to reach ~10%, and about 4% to match the bond.
**What the business has done**: revenue +29% in each of FY2025 and FY2026, product revenue +37% in Q2 FY2027;
owner earnings negative in every year. [E4-35]'s base rate (*"fewer than 10 of the 200 most profitable
companies"* sustain 15% growth for 20 years) and **[E4-44]**'s bound (value *"cannot over the long term grow
faster than its earnings do"*) bind, and here there are no earnings to grow.

**3. WHAT YOU ARE PAID.** About **-5.7 points** against the sovereign on the five-year default; **-4.3 points**
even before stock pay.

**Certainty is not priced in the rate [E3-42].** Sovereign used 5.29%, bare. No per-name premium.

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-01]**
Value per share = base / (0.10 - g), over 364.5M shares (352.8M plus the notes' ~11.7M net):

| base | g = 3% | g = 5% | g = 7% |
|---|---:|---:|---:|
| owner earnings, any window (negative) | no value computable | | |
| *display:* TTM before stock pay ($1,195M) | $47 | $66 | $109 |
| *display:* FY2027 guided adjusted FCF ($1,462M) | $57 | $80 | $134 |

**Value, in round numbers: nothing on owner earnings; roughly $50-130 a share only if stock compensation is
treated as costless and cash flow grows 3-7% a year forever.** **Current price: $338.39, above the whole range,
including the display that ignores the company's largest cost.**

**Which bar:** the screamer test [E4-01] only, because the file is closed and no margin is applied. **The price is
above the whole range: no.** Windage count: **ONE** (the prepayment increment shown at both ends rather than
chosen; growth rates displayed, not chosen).

- **VERDICT: none. Q5 did not open (Q2 OUT).** Had every gate been IN, the computation shows a business yield of
  **-0.4% on the five-year default** against a 5.29% sovereign and a ~10% floor [E4-28], and about 1% even with
  stock pay ignored. **FAIL on price as well, on every construction on disk.**

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

> **RECORDED, NOT GOVERNING.** Nothing is owned and nothing is armed. These are the conditions on which the file
> would be REOPENED at Q2 [E1-02]; a Q2 OUT is a finding about the business, so a price alert would be a category
> error (the QLYS ruling, 2026-09-07).

**What would reopen Q2 (each observable in a filing):**
1. **A GAAP operating profit that is not an accident.** Operating income positive after stock compensation for two
   consecutive fiscal years, with stock compensation below about 20% of revenue (the Row A peers' 15-22%); that is
   the return-on-capital half of [E3-43] beginning to show.
2. **A price record.** A 10-K that again reports realised capacity prices rising (as FY2021, FY2022 and FY2024 did)
   in a year of flat or falling retention, i.e. price holding without the consumption wave; or a list-price
   increase that survives a renewal cycle without the retention rate falling below 115%.
3. **Lock-in shown to survive open formats.** Net revenue retention stabilising at or above 120% for three years
   while the share of customers using Iceberg or external storage rises, which would show the position does not
   depend on holding the data.
4. **The landlords' terms.** A filed statement that product gross margin rose on price rather than on cloud
   discounts.

**Thesis-confirming (for the OUT):** retention below 120%; product gross margin falling as AI inference (GPU cost)
grows; the FY2027 10-K's first-year ASC 985-20 accounting pushing GAAP operating margin down; another year in which
buybacks and net-settlement taxes exceed operating cash while the count rises; a cloud provider or Databricks
named in a filing as winning a migration from Snowflake.

**Next dated documents:** the Q3 FY2027 10-Q and release (early December 2026: the $1,588-1,593M product-revenue
guide and the 15.5% non-GAAP margin guide against GAAP); the FY2027 10-K (March 2027: retention, the first full
year without capitalised software, stock compensation as a share of revenue); the ruling on the motion to dismiss
the third amended securities complaint; the 2027 notes' settlement election (by October 2027).

**Position size:** none. **VERDICT (RECORDED, NOT GOVERNING): not applicable; the file closed at Q2 and the
reopening conditions are recorded above.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, **Q2 OUT, the file closed**; Q3, Q4, Q5 and Q6
  recorded beneath explicit RECORDED, NOT GOVERNING banners, with Q5 headed COMPUTATION — NOT A CLEARANCE.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed income
  statement, MD&A and notes. Databricks and the clouds' product lines missing from the Q2 row are named as limits
  and are not what closes the gate.
- [x] No UNRESEARCHED or UNKNOWABLE verdict was returned in any governing or recorded section.
- [x] Step 0 (the killed session's): the filing was read with accession numbers and figures cross-checked; this
  session re-checked the acquisition, convertible and cap arithmetic against the faces and found them right, and
  records the 09-18 sovereign and close in a dated note without changing Step 0's pair.
- [x] Owner earnings on the five-year default, three-year, seven-year and TTM windows, both (c) ends, the
  deferred-revenue increment shown both ways, SBC made complete by adding back the capitalised part; (c)
  disclosed as a judgment [E2-23]; the ten-year window stated as not existing.
- [x] Competitor row filled from filings (three cloud segments via the AMZN run's accessioned table; Teradata,
  MongoDB, Datadog, Elastic and Palantir from their own latest 10-Ks, one revenue figure each checked to the face);
  its gaps stated (Databricks Form D only; Confluent deregistered; the clouds' products unsegmented).
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated 09/17/2026 (Step 0).
- [x] Value stated as a round-number range under a COMPUTATION — NOT A CLEARANCE heading.
- [x] One bar (the screamer test); windage count one.
- [x] Prices dated as closes, aggregator flagged, corroborated by Form 4s (Step 0).
- [x] Run committed to git after every gate, with a pathspec.
- [x] Every ledger id cited was looked up in `principle_ledger.csv` (`led.py`) before it was written.
- [x] No em dashes in anything this session wrote (the template's own headings and the required
  `COMPUTATION — NOT A CLEARANCE` heading carry them).
- [x] Never presented as proven to beat the market; nothing here claims it.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **Q1, corrected before commit**: the first draft said the mechanism had been the same *"for every filed year
   (FY2019-FY2026)"* with product gross margin inside 62-74%; the earliest product gross margin on disk is FY2020's
   62%, so the sentence now says FY2020-FY2026.
2. **Q2, corrected before commit**: net revenue retention for FY2022 is 178% as first filed and 177% as restated
   in the FY2023 10-K; both are now shown.
3. **Q4, corrected before commit**: a draft compared FY2023-26 buybacks and net-settlement taxes ($5,125M) with
   SBC over FY2024-26 ($4,334M) and said the cash "exceeded" the charge; the windows did not match. Over the same
   four years the cash was 98% of the charge ($5,224M), and the sentence now says so.
4. **A first draft of the peer script** read `sources.cik_for()` as a string (it returns a tuple) and
   `sources.annual()` as a dict (it returns a tuple); both crashed rather than returning wrong numbers, and were
   fixed before any figure was used.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN (and in the resume handoff)
1. **The brief's memory claims, tested.** IPO September 2020: consistent with the filings (FY2021 financing shows
   *"Proceeds from initial public offering and private placements"* of $4,242.3M; the S-1 was not re-read).
   Consumption model, capacity contracts, product revenue, NRR and RPO: **held**. The platform on AWS, Azure and
   GCP, which are also named competitors: **held**, and sharper (*"a substantial majority of our business is run
   on the AWS public cloud"*). **Databricks: the 10-K never names it**; it is a Form D filer that raised $5.0bn in
   August 2026. CEO change Slootman to Ramaswamy: **held**, effective 2024-02-27 (8-K `0001640147-24-000033`). The
   2024 incident: **held as litigation** (class actions from 2024-06-13, motions to dismiss denied October 2025);
   **no 8-K was filed**. Convertible notes of about $2.3bn with capped calls: **held**, September 2024, 0%, two
   $1.15bn series, conversion $157.50, cap $225.00; large buybacks: **held** ($3.7bn FY2024 to H1 FY2027).
   Acquisitions paid substantially in stock: **partly**: Streamlit (FY2023) was $438.9M of stock to $362.6M of
   cash; **Crunchy Data was $164.5M in cash**, not stock; Observe (February 2026) was about half and half; Neeva was
   not checked by name. Non-GAAP headlines: **held**, and they are also in the pay plan.
2. **The brief's list of skip-reason values was right, and the killed session's Step 0 answered it**: the guard
   that fired was `scale_shift` at 2.06x, organic.
3. **The resume handoff undercounted the `8k/` folder**: it said three files; there are **45** (every 8-K main
   document and EX-99.1 release from 2023-03 to 2026-09). Harmless; they were used.
4. **The brief said companyfacts, the probe and its output were committed with the first commit**; `companyfacts.json`
   was untracked until this session's first commit (`ae076aa`).
5. **The brief pointed at the PLTR run's Snowflake figures as unlabelled evidence**; they were not used, and this
   run's SNOW operating margin (-30.6% FY2026) and SBC/OCF (131%) agree with that run's table.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`tools/sources.sovereign()` serves a cached curve for up to 12 hours**: at about 18:30 EDT it returned
  `(5.29, '09/17/2026')` from a 14:41 cache while the Treasury had already published **09/18/2026: 5.34%**
  (fetched directly by this session). A run late in the day can record yesterday's row as the newest.
- **`sources._chart()` returns the `result` object, not the raw Yahoo envelope**; a caller expecting
  `['chart']['result']` crashes. Recorded because the price strike in every run goes through it.
- **`sources.cik_for()` returns a `(cik, name)` tuple and `annual()` a `(values, tags, unit)` tuple**; both are
  documented in their docstrings and both crash loudly when misread, which is the right failure.
- **`owner_earnings()` subtracts only the face SBC line** (*"net of amounts capitalized"*); at SNOW the capitalised
  part ($23.6-48.2M a year FY2022-25) is in a supplemental line, which is the TOST definition break on a second name.
- **`Screens/cover_shares.py SNOW` returned the CIK as the share count** (Step 0 recorded it).

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**When a company's cost is paid in its own stock, read the financing section before the operating section.**
Snowflake's operating cash is $1.2bn and rising, its "free cash flow" is positive, and its release guides a 23%
adjusted free-cash-flow margin; its financing section shows **$5.1bn of buybacks and net-settlement taxes over four years
(FY2023-26), spent to hold the share count, which still rose**. The owner's cost of the staff is on the financing line, and a
run that stops at operating cash will price a business that has never earned a dollar for its owners.

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** SNOW FAILS AT Q2 (OUT, on [E3-03] criterion (2) not shown and contradicted in its own 10-K: open
  formats *"may also reduce switching costs between us and our competitors"*, competition *"based on ... price"*
  against rivals that discount more, efficiency gains passed to customers [E3-62]; [E3-43]/[E3-46] no operating
  profit in any year since inception, 0.6-3.5% before stock pay, the lowest in a six-filer software row; [E4-04]
  engaged in its own words; the three clouds are its landlords and its named primary competitors [E2-45]; a
  surfing run on cloud migration [E3-51, E4-36]). Q1 IN; Q3 IN on the binary (recorded; gate case; [E4-29] fires
  in the releases and the pay plan, [E5-15] issuance the buybacks do not absorb, a buyback flag under [E5-08]);
  Q4 OUT on the owner-earnings leg (recorded; five-year owner earnings -$498M to -$555M, negative in every filed
  year, SBC 189% of all operating cash FY2019-26; survival itself not in doubt, $4.3bn liquid; shapes #2 with #13
  and #11); price $338.39 x 352.8M = $119.4bn ($123.3bn with the notes' net claim), headed COMPUTATION — NOT A
  CLEARANCE: yield -0.4% on the five-year default against 5.29%, about 1% even before stock pay; Q6 arms nothing.
- Work order: none. UNKNOWABLE: none.
